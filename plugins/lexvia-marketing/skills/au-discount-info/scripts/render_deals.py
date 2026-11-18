#!/usr/bin/env python3
"""Render a sourced Australian discount report into portrait PNGs."""

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


COLUMNS = "ID Brand Range Discount Conditions Where How Starts Ends Phase Status Sources".split()
WIDTH, HEIGHT = 1440, 1920
MARGIN, CONTENT_BOTTOM = 60, 1810
INK, PAPER, WHITE = "#181919", "#F3F0E8", "#FFFFFF"
YELLOW, RED, GRAY, RULE = "#FFD447", "#B72820", "#545850", "#E4E1D9"
STATUS_COLORS = {"live": "#167146", "announced": "#2459A5"}
MAIN_X, SHOP_X = 91, 860
MAIN_WIDTH, SHOP_WIDTH = 720, 482


@dataclass(frozen=True)
class Deal:
    id: str
    brand: str
    range: str
    discount: str
    conditions: str
    where: str
    how: str
    starts: str
    ends: str
    phase: str
    status: str
    sources: str

    def sort_key(self):
        deadline = self.ends if self.status == "live" else self.starts
        return (self.status != "live", endpoint(deadline) or date.max, self.brand.casefold())


@dataclass
class Report:
    title: str
    checked: str
    milestones: list[tuple[date, str]]
    categories: dict[str, list[Deal]]


def endpoint(value):
    if value == "—":
        return None
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?: .+)?", value):
        raise ValueError(f"Use YYYY-MM-DD with optional source time, or —. Found {value!r}.")
    return date.fromisoformat(value[:10])


def read_report(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, re.M)
    checked = re.search(r"^<!-- checked: (.+?) -->$", text, re.M)
    if not title or not checked or endpoint(checked[1]) is None:
        raise ValueError("Add an H1 title and a dated <!-- checked: ... --> comment.")
    milestones = sorted(
        (date.fromisoformat(day), label)
        for day, label in re.findall(r"^<!-- milestone: (\d{4}-\d{2}-\d{2}) \| (.+?) -->$", text, re.M)
    )
    categories, seen = {}, set()
    category = ""
    in_table = False
    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            category = line[3:].strip()
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip()[1:-1])]
        if cells == COLUMNS:
            if not category:
                raise ValueError(f"Line {number} needs an H2 category heading.")
            in_table = True
            continue
        if not in_table or all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if len(cells) != len(COLUMNS) or not all(cells):
            raise ValueError(f"Line {number} needs {len(COLUMNS)} nonempty offer cells.")
        deal = Deal(*cells)
        if deal.id in seen or deal.status not in STATUS_COLORS or not re.search(r"\]\(https?://", deal.sources):
            raise ValueError(f"Line {number} needs a unique ID, a valid status and a Markdown source link.")
        start, end = endpoint(deal.starts), endpoint(deal.ends)
        if start and end and start > end:
            raise ValueError(f"{deal.id} ends before it starts.")
        seen.add(deal.id)
        categories.setdefault(category, []).append(deal)
    return Report(title[1], checked[1], milestones, categories)


def find_font(custom, language):
    if custom:
        return custom
    candidates = [
        Path.home() / "Library/Fonts/NotoSansSC-Variable.ttf",
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/System/Library/Fonts/STHeiti Medium.ttc"),
        Path("/Library/Fonts/Arial Unicode.ttf"),
    ]
    if language == "en":
        candidates.append(Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    for path in candidates:
        if path.is_file():
            return path
    raise ValueError("Supply a sans-serif font with --font. Chinese text needs a CJK font.")


@dataclass(frozen=True)
class Style:
    size: int
    color: str = INK
    bold: bool = False

    @property
    def leading(self):
        return round(self.size * 1.32)


def plain(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[\^[^\]]+\]|\[[Dd]?\d+(?:[,， ]+\d+)*\]|【[Dd]?\d+(?:[,， ]+\d+)*】", "", text)
    text = text.replace("`", "").replace("**", "")
    text = re.sub(r"\*(\S[^*]*?)\*", r"\1", text)
    return re.sub(
        r"(?P<unit>(?<![A-Za-z])(?:mm|cm|m|km|in|ft|yd|mi)[²³])|"
        r"[*＊†‡⁰¹²³⁴⁵⁶⁷⁸⁹]+(?=$|[\s,.，。、:：;；!?！？)）])",
        r"\g<unit>",
        text,
    ).strip()


# Keep research phrasing out of the cards while preserving the shopping instructions.
SHOPPER_COPY = (
    ("。活动公告已核实，结账页面未能独立读取", "。"),
    ("结账确认自动折扣", "结账时看看折扣有没有生效"),
    ("核验会员资格", "出示会员信息"),
    ("核实赠品库存", "问问还有没有赠品"),
    ("同一订单下单前核实交期", "下单前问一下什么时候能送到"),
    ("5G 须核查地址与覆盖", "先看看这个地址有没有 5G 覆盖"),
    ("验证教育身份", "确认你的学生或教师身份"),
    ("带星号优惠，具体排除及库存以该店为准", "到店问问哪些商品参加、还有没有货"),
    ("三家已查营地的指定住宿", "三家营地的指定住宿"),
    ("此口径来自 DFO Perth，适用商品以门店标价和细则为准", "到店看哪些商品有优惠、活动价是多少"),
    ("指定 SKU", "指定款式"),
    ("折幅", "折扣"),
)


def shopping_copy(text):
    for source, replacement in SHOPPER_COPY:
        text = text.replace(source, replacement)
    return text


class Layout:
    def __init__(self, font_path, language):
        self.font_path = str(font_path)
        self.chinese = language == "zh"

    def label(self, chinese, english):
        return chinese if self.chinese else english

    @lru_cache(maxsize=48)
    def font(self, size, bold):
        index = 2 if self.chinese and Path(self.font_path).name == "NotoSansCJK-Regular.ttc" else 0
        font = ImageFont.truetype(self.font_path, size, index=index)
        try:
            axes = font.get_variation_axes()
            values = [axis["default"] for axis in axes]
            for i, axis in enumerate(axes):
                if axis["name"] == b"Weight":
                    values[i] = max(axis["minimum"], min(axis["maximum"], 710 if bold else 435))
            font.set_variation_by_axes(values)
        except (OSError, AttributeError):
            pass
        return font

    def width(self, value, style):
        return self.font(style.size, style.bold).getlength(value)

    def wrap(self, value, width, style):
        tokens = re.findall(r"[A-Za-z0-9À-ž$%+.,&'’/():#_-]+|\s+|.", plain(value))
        return self.wrap_tokens(tokens, width, style)

    def wrap_tokens(self, tokens, width, style):
        lines, line = [], ""
        for token in tokens:
            if self.width(line + token, style) <= width:
                line += token if line else token.lstrip()
                continue
            if line.strip():
                lines.append(line.rstrip())
            line = ""
            for char in token.lstrip():
                if self.width(line + char, style) > width:
                    lines.append(line)
                    line = ""
                line += char
        if line.strip():
            lines.append(line.rstrip())
        return lines

    def cell(self, width, *parts):
        return [(line, style) for value, style in parts for line in self.wrap(value, width, style)]

    def write(self, draw, x, y, lines):
        for value, style in lines:
            draw.text((x, y), value, font=self.font(style.size, style.bold), fill=style.color,
                      anchor="lt")
            y += style.leading

    def day_label(self, day, year):
        if self.chinese:
            year_label = f"{day.year}年" if day.year != year else ""
            return f"{year_label}{day.month}月{day.day}日"
        label = f"{day.day} {day:%b}"
        return label if day.year == year else f"{label} {day.year}"

    def short_date(self, value, year):
        return self.day_label(endpoint(value), year) + value[10:]


def total_height(lines):
    return sum(style.leading for _, style in lines)


def paginate(rows, available, balance=False):
    pages, page, used = [], [], 0
    for row in rows:
        height = row[0]
        if height > available:
            raise ValueError("An image row exceeds the page height. Shorten that row's copy.")
        if used + height > available:
            pages.append(page)
            page, used = [], 0
        page.append(row)
        used += height
    pages.append(page)
    if balance:
        # Move trailing rows into the next page to avoid a sparse last page.
        for left, right in reversed(list(zip(pages, pages[1:]))):
            left_height = sum(row[0] for row in left)
            right_height = sum(row[0] for row in right)
            while len(left) > 1:
                height = left[-1][0]
                if left_height - right_height <= height or right_height + height > available:
                    break
                right.insert(0, left.pop())
                left_height -= height
                right_height += height
    return pages


def calendar_rows(layout, report):
    checked_day = endpoint(report.checked)
    entries = defaultdict(lambda: {"milestones": [], "starts": {}, "ends": {}})
    for day, label in report.milestones:
        entries[day]["milestones"].append(label)
    for deals in report.categories.values():
        for deal in deals:
            for key in ("starts", "ends"):
                day = endpoint(getattr(deal, key))
                if day and day >= checked_day:
                    brand = plain(deal.brand)
                    entries[day][key].setdefault(brand.casefold(), brand)
    rows = []
    for day, entry in sorted(entries.items()):
        stamp = layout.cell(216, (layout.day_label(day, checked_day.year), Style(42, bold=True)))
        lines = layout.cell(984, (" · ".join(entry["milestones"]), Style(42, RED, True)))
        for key, label in (("starts", layout.label("开卖", "Starts")), ("ends", layout.label("截止", "Ends"))):
            if entry[key]:
                names = sorted(entry[key].values(), key=str.casefold)
                separator = layout.label("、", ", ")
                tokens = [f"{label}   ", *(name + separator for name in names[:-1]), names[-1]]
                style = Style(38)
                lines.extend((line, style) for line in layout.wrap_tokens(tokens, 984, style))
        # Keep dense dates legible and repeat the date when its entries span cards.
        for offset in range(0, len(lines), 10):
            block = lines[offset:offset + 10]
            height = max(total_height(stamp), total_height(block)) + 34
            rows.append((height, stamp, block))
    return rows


def sale_date_lines(layout, value, year, label, missing):
    style = Style(36)
    if value == "—":
        return [(missing, style)]
    day = layout.day_label(endpoint(value), year)
    tokens = [f"{label}  {day}", value[10:]]
    return [(line, style) for line in layout.wrap_tokens(tokens, SHOP_WIDTH, style)]


def category_rows(layout, report, deals):
    year = endpoint(report.checked).year
    for deal in sorted(deals, key=Deal.sort_key):
        status = layout.label("已经开始", "On now") if deal.status == "live" else layout.label("即将开卖", "Coming up")
        starts = sale_date_lines(layout, deal.starts, year, layout.label("开卖", "Starts"),
                                 layout.label("开卖日没写", "Start date not listed"))
        ends = sale_date_lines(layout, deal.ends, year, layout.label("截止", "Ends"),
                               layout.label("截止日没写", "End date not listed"))
        phase = "" if deal.phase in ("黑五", "Black Friday", "—") else deal.phase
        main = layout.cell(
            MAIN_WIDTH,
            (deal.brand, Style(53, bold=True)),
            (deal.discount, Style(53, RED, True)),
            (shopping_copy(deal.range), Style(39, bold=True)),
            (shopping_copy(deal.conditions), Style(38, GRAY)),
        )
        shopping = layout.cell(SHOP_WIDTH, (status, Style(37, STATUS_COLORS[deal.status], True)),
                               (phase, Style(34, GRAY)))
        shopping.extend(starts)
        shopping.extend(ends)
        shopping.extend(layout.cell(SHOP_WIDTH, (shopping_copy(deal.where), Style(38, bold=True)),
                                    (shopping_copy(deal.how), Style(38))))
        height = max(total_height(main), total_height(shopping)) + 66
        yield (height, deal.status, main, shopping)


def frame(layout, report, title, label, subtitle, page, page_count, header_bottom):
    image = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, WIDTH, header_bottom), fill=INK)
    tag = Style(31, INK, True)
    draw.rounded_rectangle((MARGIN, 47, MARGIN + layout.width(label, tag) + 34, 104), 10, fill=YELLOW)
    layout.write(draw, MARGIN + 17, 59, [(label, tag)])
    page_text = layout.label(f"第 {page} 页，共 {page_count} 页", f"Page {page} of {page_count}")
    page_style = Style(30, YELLOW, True)
    layout.write(draw, WIDTH - MARGIN - layout.width(page_text, page_style), 56, [(page_text, page_style)])
    title = plain(title)
    size = 80
    while size > 46 and layout.width(title, Style(size, WHITE, True)) > WIDTH - 2 * MARGIN:
        size -= 4
    layout.write(draw, MARGIN, 126, layout.cell(WIDTH - 2 * MARGIN, (title, Style(size, WHITE, True))))
    layout.write(draw, MARGIN, header_bottom - 48, layout.cell(WIDTH - 2 * MARGIN, (subtitle, Style(31, YELLOW))))
    draw.line((MARGIN, 1834, WIDTH - MARGIN, 1834), fill=RULE, width=3)
    footer_style = Style(30, GRAY)
    footer = layout.label("价格均为澳元", "Prices in AUD")
    layout.write(draw, MARGIN, 1854, [(footer, footer_style)])
    updated = layout.short_date(report.checked, endpoint(report.checked).year)
    stamp = layout.label("更新于 ", "Updated ") + updated
    layout.write(draw, WIDTH - MARGIN - layout.width(stamp, footer_style), 1854, [(stamp, footer_style)])
    return image, draw


def deal_counts(layout, live, upcoming):
    labels = []
    if live:
        labels.append(layout.label(f"{live} 个优惠已经开始", f"{live} on now"))
    if upcoming:
        labels.append(layout.label(f"{upcoming} 个优惠快开卖", f"{upcoming} coming up"))
    return "    ·    ".join(labels)


def draw_directory(layout, draw, y, index):
    entries = [(page, layout.cell(478, (title, Style(34)))) for page, title in index]
    rows = [entries[i:i + 2] for i in range(0, len(entries), 2)]
    heights = [max(total_height(lines) for _, lines in row) + 3 for row in rows]
    bottom = y + 70 + sum(heights)
    if not index or bottom > CONTENT_BOTTOM:
        return
    draw.rounded_rectangle((MARGIN, y, WIDTH - MARGIN, bottom), 14, fill=WHITE)
    layout.write(draw, 83, y + 16, [(layout.label("按品类找", "Find your category"), Style(35, bold=True))])
    top = y + 66
    for row, height in zip(rows, heights):
        for column, (page, lines) in enumerate(row):
            x = 83 + 644 * column
            page_text = layout.label(f"第 {page} 页", f"Page {page}")
            layout.write(draw, x, top, [(page_text, Style(29, RED, True))])
            layout.write(draw, x + 133, top, lines)
        top += height


def render(layout, report, output):
    timeline_header, timeline_top = 342, 422
    category_header, category_top = 278, 312
    calendar = paginate(calendar_rows(layout, report), CONTENT_BOTTOM - timeline_top)
    sections = [(name, paginate(category_rows(layout, report, deals), CONTENT_BOTTOM - category_top, balance=True))
                for name, deals in report.categories.items()]
    total = len(calendar) + sum(len(pages) for _, pages in sections)
    deals = [deal for group in report.categories.values() for deal in group]
    live = sum(deal.status == "live" for deal in deals)
    label = layout.label("什么时候买", "When to shop")
    subtitle = deal_counts(layout, live, len(deals) - live)

    output.mkdir(parents=True, exist_ok=True)
    if any(re.fullmatch(r"\d+-(?:timeline|category)\.png", path.name) for path in output.iterdir()):
        raise ValueError("Choose a fresh image output folder for this run.")
    number = 0
    index = []
    next_page = len(calendar) + 1
    for title, pages in sections:
        index.append((next_page, title))
        next_page += len(pages)

    for rows in calendar:
        number += 1
        image, draw = frame(layout, report, report.title, label, subtitle, number, total, timeline_header)
        year = endpoint(report.checked).year
        highlights = "   ·   ".join(f"{layout.day_label(day, year)} {plain(name)}" for day, name in report.milestones)
        highlight_style = Style(29, WHITE, True)
        x = WIDTH - MARGIN - layout.width(highlights, highlight_style)
        if highlights and x >= MARGIN + layout.width(subtitle, Style(31, YELLOW)) + 32:
            layout.write(draw, x, timeline_header - 48, [(highlights, highlight_style)])
        if index:
            note = layout.label("想看几点开卖、怎么买？往后翻到对应品类。", "Flip to each category for sale times and how to buy.")
            layout.write(draw, MARGIN, timeline_header + 23, [(note, Style(32, GRAY))])
        y = timeline_top
        for height, stamp, lines in rows:
            draw.rounded_rectangle((MARGIN, y, WIDTH - MARGIN, y + height - 14), 20, fill=WHITE)
            layout.write(draw, 91, y + 17, stamp)
            layout.write(draw, 343, y + 18, lines)
            y += height
        if not rows:
            layout.write(draw, MARGIN, y + 14, [(layout.label("还没有开卖或截止日期", "No sale dates yet"), Style(43, bold=True))])
            y += 84
        if number == len(calendar):
            draw_directory(layout, draw, y + 24, index)
        image.save(output / f"{number:02d}-timeline.png", optimize=True)

    for title, pages in sections:
        label = layout.label("按品类逛", "Deals by category")
        for rows in pages:
            number += 1
            running = sum(status == "live" for _, status, _, _ in rows)
            subtitle = deal_counts(layout, running, len(rows) - running)
            image, draw = frame(layout, report, title, label, subtitle, number, total, category_header)
            y = category_top
            padding = min(58, (CONTENT_BOTTOM - y - sum(row[0] for row in rows)) // len(rows))
            for height, status, main, shopping in rows:
                height += padding
                draw.rounded_rectangle((MARGIN, y, WIDTH - MARGIN, y + height - 16), 20, fill=WHITE)
                draw.rounded_rectangle((MARGIN, y + 12, MARGIN + 9, y + height - 29), 4, fill=STATUS_COLORS[status])
                top = y + 24 + padding // 2
                divider = SHOP_X - 26
                draw.line((divider, top, divider, y + height - 40), fill=RULE, width=2)
                layout.write(draw, MAIN_X, top, main)
                layout.write(draw, SHOP_X, top, shopping)
                y += height
            image.save(output / f"{number:02d}-category.png", optimize=True)
    return total, len(deals)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--language", choices=("zh", "en"), default="zh")
    parser.add_argument("--font", type=Path)
    args = parser.parse_args()
    try:
        report = read_report(args.report)
        layout = Layout(find_font(args.font, args.language), args.language)
        pages, deals = render(layout, report, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(f"Rendered {pages} PNGs from {deals} offers.")


if __name__ == "__main__":
    main()
