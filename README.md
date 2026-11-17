# Plugin Marketplace

A collection of reusable agent skills for legal research and documents, marketing
and design, and development. Skills are grouped into three plugins: Legal,
Marketing, and Development.

## Marketplace structure

```text
.agents/plugins/marketplace.json   Marketplace index and plugin sources
plugins/
  <plugin>/
    .codex-plugin/plugin.json      Plugin metadata and skill directory
    skills/
      <skill>/
        SKILL.md                  Purpose, invocation rules, and workflow
        agents/                   Optional agent metadata and invocation policy
        references/               Optional supporting guides
        scripts/                  Optional helper tools
        assets/                   Optional templates and media
    examples/                     Examples, where supplied
```

The marketplace index lists the plugins, and each plugin manifest points to its
skills. A skill's invocation name comes from the `name` field in `SKILL.md`; it can
differ from its folder name. Supporting files vary by skill.

## How to use

1. Enable the relevant plugin in your agent.
2. Select a skill in the skill picker, or explicitly request it by name, such as
   “Use $humanizer to edit the following paragraph.”
3. Supply the inputs mentioned below, plus your audience, desired output, and any
   constraints. For file-based work, attach the files or identify their workspace
   location.

`humanizer` and `pdf` appear in multiple plugins; choose the intended plugin's
version when selecting them. Available tools and dependencies vary by workflow;
each `SKILL.md` contains the detailed requirements.

## Legal skills

| Skill | Overview | Example request / inputs |
| --- | --- | --- |
| `australia-migration-watch` | Verify Australian migration-policy changes and produce Chinese alerts or weekly PDF reports. | “Use $australia-migration-watch for this week's verified policy changes.” |
| `australian-minimum-pay` | Research statutory minimum pay, award coverage, and classifications. | “Use $australian-minimum-pay for a Sydney retail assistant.” Include duties and employer industry if known. |
| `fill-form` | Fill a draft PDF from document evidence, with citations and a gaps report. | “Use $fill-form with this blank PDF and evidence folder.” Identify the intended subject. |
| `humanizer` | Make prose sound natural while preserving its meaning and facts. | “Use Legal's humanizer to edit this explanation.” Supply the draft. |
| `market-salary-test` | Research Australian market salaries and recommend a sourced base-salary range and target. | “Use $market-salary-test for a Melbourne software engineer with five years' experience.” |
| `org-chart` | Create an organization chart in a Word document from reporting relationships. | “Use $org-chart with this reporting hierarchy.” Supply roles and any labels to include. |
| `pdf` | Read, create, extract, merge, split, OCR, and fill PDFs. | “Use Legal's pdf skill to extract tables from these PDFs.” |

Minimum-pay research and market-salary benchmarking are separate workflows.
`fill-form` prepares drafts; it does not sign or submit forms.

## Marketing skills

### Content and documents

| Skill | Overview | Example request / inputs |
| --- | --- | --- |
| `marketing-ideas` | Generate marketing ideas, channel strategies, and growth experiments. | “Use $marketing-ideas for a budgeting app with a small launch budget.” |
| `ai-image-creator` | Develop image prompts, visual concepts, and social-content asset plans. | “Use $ai-image-creator to plan three product-launch visuals.” Supply the product and target platform. |
| `humanizer` | Edit AI-sounding prose while preserving facts and the writer's voice. | “Use Marketing's humanizer to revise this landing-page copy.” |
| `meeting-minutes` | Turn transcript text into concise Chinese meeting-minutes PDFs with decisions and actions. | “Use $meeting-minutes on this transcript.” Paste the text or attach a UTF-8 `.txt` file. |
| `pdf` | Create and process PDF documents, including extraction, OCR, and page operations. | “Use Marketing's pdf skill to merge these documents.” |
| `rednote-content` | Research and write Simplified Chinese legal educational copy for Rednote. | “Use $rednote-content to explain NSW rental bonds to renters.” Explicitly name this skill. |
| `rednote-picture` | Turn supplied Chinese or bilingual legal copy into a finished social-media image. | “Use $rednote-picture for the following post.” Supply the copy or headline and supporting points. |
| `rednote-post` | Coordinate copywriting, image generation, humanizing, and alignment checks; deliver a post, image, and Word document. | “Use $rednote-post and $rednote-content to create a rental-bond post with a matching cover.” |

`rednote-content` requires an explicit user request naming it, including when used
within a complete post workflow. Use `rednote-picture` for image-only requests and
`humanizer` for rewriting. These skills create deliverables rather than publishing
posts.

### Interface design

| Skill | Overview | Example request / inputs |
| --- | --- | --- |
| `design-taste-frontend` | Develop visual direction and implement web pages or app screens with screenshot review. | “Use $design-taste-frontend to redesign this portfolio.” Supply the project or page. |
| `ui-ux-pro-max` | Provide searchable UX, accessibility, layout, chart, and framework guidance. | “Use $ui-ux-pro-max to improve keyboard focus in this React form.” |
| `impeccable` | Apply explicitly selected design, critique, audit, and refinement playbooks. | “Use $impeccable to audit this checkout.” Specify whether to report findings or make changes. |

Taste leads art direction when paired with Pro Max. Pro Max can also handle focused
UX fixes or an explicitly requested standalone design workflow. Impeccable is an
explicitly selected alternative. The Taste skill lives in `taste-skill/`.

### Posters and motion

| Skill | Overview | Example request / inputs |
| --- | --- | --- |
| `morandi-cinematic-poster-zeejay` | Turn a supplied photograph into a restrained cinematic poster using typography. | “Use $morandi-cinematic-poster-zeejay on this travel photo.” |
| `scene-distillation-zine-v1-3` | Reinterpret a photo as a minimal illustrated zine poster without retaining photographic material. | “Use $scene-distillation-zine-v1-3 to make an illustrated poster from this photo.” |
| `scenes-gathered-zine-v1-3` | Combine retained photography, simplified illustration, and a torn-paper edge. | “Use $scenes-gathered-zine-v1-3 to make a paper-collage poster from this photo.” |
| `scenes-gathered-zine-live-flow-v1-0` | Create a poster and paper-tear Live Photo ZIP, with an optional macOS importer handoff. | “Use $scenes-gathered-zine-live-flow-v1-0 on this photo, ZIP only.” |
| `video-shotcraft` | Create cinematic product videos using shot recipes, templates, screenshots, motion, and audio. | “Use $video-shotcraft to make a 20-second product promo from this project using the template.” |

The Live Photo workflow also bundles `scenes-gathered-zine-v1-9` under
`references/static-poster-v1-9/`. It preserves photographic regions and blends them
with simplified illustration. For a static-only result, request that bundled
module and supply a photo; no animation is needed.

## Development skills

| Skill | Overview | Example request / inputs |
| --- | --- | --- |
| `mcp-builder` | Build MCP servers that expose APIs and services through agent tools. | “Use $mcp-builder to expose this API through a TypeScript MCP server.” Supply API documentation and required operations. |
| `australia-immigration-news` | Verify Australian immigration, study, and work news for Chinese topic banks or weekly digests. | “Use $australia-immigration-news to create this week's topic bank.” |
| `humanizer` | Rewrite prose naturally without changing supported meaning or facts. | “Use Development's humanizer to edit this technical introduction.” |
| `pdf` | Read and manipulate PDFs, including extraction, merging, OCR, and forms. | “Use Development's pdf skill to make this scanned PDF searchable.” |

The news skill lives in `news-aggregator/` and supports public-news research and
content planning. Use `australia-migration-watch` for official policy-change alerts.
