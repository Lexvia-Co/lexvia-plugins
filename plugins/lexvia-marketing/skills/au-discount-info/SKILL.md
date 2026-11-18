---
name: au-discount-info
description: Find and verify current and upcoming Australian deals year-round across all sectors and brands. Use for nationwide or local discounts, everyday specials, clearance, member offers, promo codes, cashback, and named sale events. Show portrait PNG calendars and category cards in chat and deliver all pages in one ZIP.
---

# Australian Discount Information

## Set the coverage

- For a general request, use the run date in Sydney to look for offers that are live or have a confirmed upcoming start. Search for everyday specials, weekly catalogue deals, recurring offers, clearance, member or introductory pricing, promo codes, cashback, and seasonal sales. Apply any event, geography, brand, or product filters the user gives. Include verified event dates and distinct access phases when relevant to the request.
- Cover all sectors and brands selling to customers in Australia. Search Australian and international brands with Australian eligibility, large chains, independent businesses, marketplaces, brand stores, shopping centres and outlets, and local service providers. Search major cities and regional locations across all states and territories, as well as Australian online offers. Use the categories below as starting points and expand them as evidence warrants.
- Run multiple source passes for fashion and footwear, sports and outdoors, beauty and personal care, health and wellness, electronics and telco, home and appliances, jewellery and accessories, baby and toys, food and groceries, pets, automotive and trade, travel and accommodation, experiences, and software and subscriptions. Include other consumer and business services when relevant. Check sector and regional gaps before finishing and record what the run actually covered. Describe the result as a dated collection of discoverable, verified offers.

## Verify and record

1. Browse current Australian offer pages, weekly catalogues, product pages, membership and rebate terms, and official store or centre listings. Use news, deal sites, or forums to discover leads, then open the seller's or promoter's current Australian evidence. Check the year and eligibility region when stated. Include standing and recurring offers when an official source confirms the saving and how to redeem it.
2. Use one row per distinct offer, with the brand and seller when they differ. Keep variants in one row only if the terms, dates, and buying method can be expressed clearly together. Split online, outlet, in-store, early-access, and later phases when the terms differ. De-duplicate identical offers listed in several sources. Link directly to the purchase or booking page and the official terms, product listing, or local store offer that verifies the details.
3. Capture the exact eligible product range or service, the discount or advertised sale price in AUD, the comparison basis when listed, minimum spend, codes, eligibility, exclusions and stock limits, redemption steps, eligible locations and channels, and any published start and end. Keep percentages, price reductions, gift cards, points, and cashback distinct. Put recurring windows, such as a weekday lunch special, in `Conditions`. State booking, travel, or claim dates separately from the redemption window. Preserve the source's time and time zone. Use `—` for an unlisted endpoint, including offers that run until stocks last without a stated date. Flag other unclear material terms and retain qualifiers such as “up to,” “selected,” and “first four months.”
4. Record the Sydney verification timestamp. Use `live` for open offers and recurring offers whose published schedule is in force. Use `announced` for a future start with a verified offer and purchase conditions. Check agreement between official terms and the sale or product page before publication. Put expired offers, teaser pages without a confirmed discount, conflicting claims, and third-party-only leads in the report's watchlist or exclusions, with the reason and source. Exclude those leads from offer counts and cards. Recheck prices, availability, eligibility, and dates on each refresh.

## Prepare the internal deal record

- Save a UTF-8 `au-discounts-YYYY-MM-DD.md` in a temporary run folder outside the skill. Include the request scope, snapshot time, every verified offer gathered, relevant watchlist items, search coverage and gaps, and purchase and evidence links. Include a campaign window when relevant. Use the user's preferred language. Default to Simplified Chinese when following the supplied screenshots, with official brand names and coupon codes as written.
- Use an H1 title, a `checked` comment with the actual Sydney timestamp, and H2 headings for product or service categories. Add `<!-- milestone: YYYY-MM-DD | Event name -->` only for relevant verified campaign dates. Localize the cell contents and category titles while keeping the table schema, unique offer IDs, and `live` or `announced` status values. Use ISO dates with source-stated times and zones where available, or `—`. Use `Phase` for a seller's event or access label, or a neutral label such as “Everyday offer” when none is published. Keep cells on one line and escape literal pipes as `\|`.

```markdown
# 澳洲优惠速览 · YYYY-MM-DD
<!-- checked: YYYY-MM-DD HH:MM TZ -->

## 家居与家电

| ID | Brand | Range | Discount | Conditions | Where | How | Starts | Ends | Phase | Status | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

## Render the pictures from the report

1. Inspect `examples/IMG_3001.JPG` for the cover, calendar and directory, `examples/IMG_3002.JPG` and `examples/IMG_3003.JPG` for category comparison rows, `examples/IMG_3004.JPG` for chronological grouping, and `examples/IMG_3005.JPG` for tall, readable cards. Apply the portrait proportions, high-contrast header, clear visual hierarchy, and discount and status accents. Base the image content on the current report. Omit the screenshots' watermarks and logos.
2. Render the temporary report with `scripts/render_deals.py` using Python 3.10 or later, Pillow and a CJK-capable font when using Chinese. Pass a fresh image directory for each render. Use `--language en` for English labels and `--font` to supply a local font if needed. Use an available deterministic typesetting tool if the helper's dependencies are unavailable. Keep the Markdown as the source of truth.

```bash
python3 scripts/render_deals.py /path/to/au-discounts-YYYY-MM-DD.md /path/to/run/images
```

3. Show published start dates and deadlines from the snapshot date onward. List each brand once per date under each heading for starts or ends. Give every distinct offer its own entry on its category page. Sort open offers by their closing date and upcoming offers by their opening date. Keep offers with missing dates on their category pages and label those dates in plain language.
4. Write PNG labels in everyday shopping language. Use phrases such as “什么时候买”, “现在就能买”, “即将开卖”, and “更新于 11 月 18 日”, or “When to shop”, “On now”, “Coming up”, and “Updated 18 Nov”. Use this tone throughout the images, including when the calendar has no dates. Keep offer IDs, citations, and footnote markers in the internal Markdown. Leave editorial labels such as “verified”, “已核实”, and “核验” off the images.
5. Make the brand and discount the easiest things to spot. Give the product range, key conditions, locations, dates, and buying steps enough room to wrap. Add pages when needed to keep text readable at phone size. Compare the finished PNGs with the Markdown for prices, codes, eligibility, locations, and dates. Check for missing glyphs, clipped text, and stray reference markers.

## Deliver the PNGs in chat

- Display each finished PNG inline in page order. Use the chat's image attachment or inline image display. Keep the temporary Markdown as internal working material.
- Create and link `au-deals-YYYY-MM-DD.zip` with every finished PNG at full resolution. Verify that the ZIP opens and contains every numbered page exactly once. Include only the final PNGs in the ZIP.
