# 选题记录格式

仅在维护选题库、比较同一事件后续进展或构建自动化时读取。

```text
id: 稳定 URL 或主题 + 日期
title: 选题标题
tier: A | B | C | D
category: legislation | visa | skilled | state-nomination | student | employer | citizenship | industry | explainer
jurisdiction: federal | NSW | VIC | QLD | WA | SA | TAS | ACT | NT | national
published_or_updated_at: 日期；未知则 null
effective_at: 生效/截止日期；未知则 null
fact_hook: 可发布的已核验事实
content_angles: 可解释角度列表
audience_relevance: 中国大陆 | 香港 | 台湾 | 马来西亚 | 新加坡 | 越南 | 泛亚洲参考 | 通用
wording_note: 必须保留的限定语
primary_url: 官方或原始来源 URL
supporting_urls: 补充核验 URL 列表
status: effective | announced | proposed | reported | inspiration | rejected
```

`reported` 和 `inspiration` 不能写成已生效规则；`rejected` 不得进入交付结果。
