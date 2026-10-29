---
name: rednote-picture
description: Create a polished branded LEXVIA social-media image from Chinese or bilingual Australian legal copy, including copy just produced by the `rednote-content` skill. Use when a user asks to turn supplied or newly drafted legal social copy into a finished visual; do not use for copywriting, legal analysis, translation, or text-only editing.
---

# Rednote Picture

When the user pastes standalone article copy, a headline with supporting points, or a legal social post, treat it as a request to make the visual unless they explicitly ask for analysis, rewriting, translation, or another text-only task. **Directly generate the finished image in the same turn.** Do not merely provide a prompt, design plan, or a `SKILL.md` explanation. Use the image-generation tool and return the result.

If the user gives only a title or a short fragment, create a title-led editorial visual. Do not ask for a layout approval, dimensions, or a brand confirmation unless an essential source asset is required. Default to a portrait 3:4 social-media composition.

## Required behavior

1. Extract the article’s title, central legal distinction, supporting points, and any supplied caveat.
2. Silently repair only obvious formatting noise such as broken numbering or accidental line breaks. Do not change legal meaning or invent advice.
3. Choose one topic-specific visual metaphor, then call the image generator. Do not ask the user to approve a prompt unless a missing input materially blocks the work.
4. Inspect the generated image. If brand spelling, critical Chinese text, crop, or an unwanted element is materially wrong, make one focused correction and re-check.
5. Return the selected image inline. If the generation environment supplies a local output file, also place it in the active workspace under a descriptive filename and link it in the final response.
6. Every finished image must display the official LEXVIA logo from `assets/brand/lexvia-logo.png`. Verify that the complete logo is visible, legible, proportionate, and undistorted before delivery.

## Style reference library

`example/` is the canonical LEXVIA visual-reference library. Before generating every image, inspect **all** images in that folder and include them as visual references in the image-generation request. Use the library to infer the shared visual system, rather than selecting one image as a topic template.

## Brand colour system

`assets/brand/lexvia-logo.png` is the canonical LEXVIA logo asset. Treat it as the authoritative source for the brand colour system, not as a decorative image.

- Before every generation, include the logo asset as a visual reference in addition to all images in `example/`, and instruct the generator to place the complete official logo on the artwork.
- Sample and preserve the logo's primary red faithfully as `LEXVIA_RED`; do not substitute a generic crimson, burgundy, orange-red, or bright scarlet.
- Every finished image must contain a clearly visible, intentional use of `LEXVIA_RED`, such as a headline field, rule, editorial panel, seal, accent shape, or controlled lighting detail.
- Use a restrained brand palette: `LEXVIA_RED`, white or warm off-white, charcoal/near-black, plus at most one muted topic-specific supporting colour.
- Topic-led colours may support the story, but must not overpower or replace the brand red. Avoid dominant blue, green, purple, or unrelated gradient treatments unless they are visibly subordinated to `LEXVIA_RED`.
- Place the official logo as an integrated signature element with calm breathing room; do not substitute, recreate, crop, recolour, stretch, or replace it with typed brand text.

When the user supplies an actual image associated with the post, treat it as the primary visual direction for that post. First infer its subject type, framing, sense of place, energy, text density, and palette; use `example/` to retain LEXVIA's brand finish. Do not copy the supplied image exactly unless the user asks for an edit or close reproduction.

- Preserve the shared house language at the level of tone rather than a template: calm, polished, premium Australian legal-advisory editorial design; clear Chinese typography; deliberate material and photographic choices; and a strong sense of order.
- Preserve the information design principles: an obvious title-led hierarchy, concise explanatory text, generous whitespace, and readable grouping. Use rules, panels, cards, annotations, icons, or lists only when they clarify that particular story.
- Use `example/` to learn the shared level of polish, editorial pacing, typography, image treatment, whitespace, and information hierarchy. The examples are not the source of the palette: the logo asset defines the fixed LEXVIA brand palette, while the supporting topic colour is selected afresh for the specific story.
- `LEXVIA_RED` is the company's mandatory brand anchor. Use it in a deliberate, topic-appropriate form rather than a fixed red footer, red information band, or predominantly red image.
- Treat only elements repeated across the library as house rules. Vary the specific hero image, topic metaphor, layout, and information modules to fit the supplied legal content.
- Do **not** copy or closely imitate any individual reference's exact composition, person, photograph, headline, icon sequence, hand-drawn annotation, or policy subject. The references define visual language, not reusable post templates.
- When new approved posts are added to `example/`, they automatically become part of the shared reference set. Do not remove, rename, or overwrite reference images unless the user asks.

## Visual mode selection

Choose the visual mode that best conveys the story before deciding the layout. Do not default every post to a legal still life or an information graphic.

- **Regional migration-policy news** (state nomination, regional visas, state programs): use a geographic news-cover approach. Lead with a real or credible editorial scene tied to the relevant place—landscape, recognisable local environment, architecture, or policy setting—and use restrained location cues such as a pin, a highlighted Australia outline, or a short region label when helpful.
- **Policy announcements involving an institution or public figure:** use a policy-news approach, such as a briefing environment, institutional architecture, lectern, or appropriate news-photo treatment.
- **Transactions, property, contracts, and disputes:** use a legal-editorial approach, such as documents, material details, architecture, or carefully selected objects and people.

The main image should establish where the event matters and why it matters before the text explains the rule.

## Visual identity

Create a premium Australian legal-advisory editorial image in a portrait social-media format. Match the shared visual language in `example/` at the level of quality and tone: confident, calm, highly legible, editorial, and materially connected to the legal topic. Do not turn the reference library into a fixed layout, palette, or footer treatment.

- Choose visual material and one muted supporting colour that communicate the legal subject clearly. The logo asset defines the fixed LEXVIA brand palette; determine only the supporting colour from the story, subject, setting, and desired emotional register. For region-led news, derive that supporting colour from the place itself where appropriate.
- Use `LEXVIA_RED` in every image as a visible brand anchor. It may appear as a headline emphasis, underline, seal, shape, glow, editorial colour field, or controlled hero-image detail. Keep its scale proportionate to the concept: do not default to a red footer or information band, and do not require an overwhelmingly red image. If an exact brand colour value is recorded with the official logo asset, use it faithfully.
- Within each image, commit to a disciplined palette with strong contrast for readable Chinese type. Avoid green plants/foliage unless they serve the subject.
- Lead with the visual that carries the strongest sense of the event. For regional migration, visa, or state-policy news, prefer a real location or credible news-photography-style scene. Use a contract spread, title certificate, dossier, letter/envelope, ribboned transfer path, key, seal, or other abstract legal object only when a place, people, or relevant environment cannot tell the story as well.
- Use refined, high-contrast Chinese headline typography with a clear hierarchy. Set one large title, one concise takeaway or quote, then only the supporting information that can be read comfortably on a phone.
- For a distinction or comparison, express it physically and editorially: paired documents, a split composition, a ribbon/trajectory, a central balancing object, or a contained comparison panel. Do not default to bar charts, icons, or card grids.
- Every image must display the complete official LEXVIA logo asset. Give it calm breathing room in a deliberate signature area; its position, ground, and treatment must follow the composition rather than a repeated footer formula. Preserve its original aspect ratio, complete lock-up, and brand colours.
- Keep backgrounds and props intentional: books, fountain pens, seals, keys, paper texture, brass objects, architectural models, real landscapes, and softly out-of-focus interiors are welcome when relevant. Plants are optional accents only, never the default motif.
- Do not use Sydney landmarks, Australian flags, government crests, or portraits as generic decoration. When a location is itself the story, prefer the relevant region's landscape, environment, architecture, or map cue over generic national imagery.
- Avoid cartoon aesthetics, stock real-estate advertising scenes, generic icon grids, QR codes, watermarks, extra logos, or unconnected decorative objects.

### Reference quality bar

The target is the visual language established by `example/`: a polished Chinese legal-advisory carousel cover with precise typography, generous negative space, carefully edited information, and a memorable scene or legal metaphor. Vary the palette, brightness, composition, material treatment, hero image, information structure, and logo placement from post to post. Preserve the reference library's premium editorial finish—not its individual layouts, repeated visual ingredients, or colour schemes.

## Let the legal idea drive the image

Do not turn every numbered article into cards. Prefer one coherent visual narrative. For news-style covers, preserve the main scene and compress the message into a headline, one key conclusion, and at most one short qualifier or callout. Use a lower informational panel or a compact numbered list only when the source genuinely has multiple actionable points and the layout can keep each point legible.

For example:

- Transaction terms: documents, contract margins, settlement paper, signature, keys.
- Land restrictions: site plans, boundary lines, setbacks, surveying marks.
- Title searches: a magnifier revealing registry details while unknown questions fade outside it.
- Family funds: a transfer path separating a gift declaration from a loan agreement.
- Immigration policy: a speech dossier or policy lines branching from the news event.

Use short labels, margin notes, callouts, document annotations, trajectories, or a comparison only when they clarify the main legal point. Use cards or a list only when that is genuinely the clearest option.

## Text standards

- Keep the title, central takeaway, and legal caution highly legible and inside safe margins.
- Use only the minimum on-image text needed to communicate the point: normally a title, one key distinction, and an optional short caution. Do not attempt to reproduce a long article verbatim.
- Use Simplified Chinese for visible content by default. A short, accurate official program name, visa subclass, or institution name may remain in English when it materially helps recognition and is part of the supplied source, for example `NT Graduate / NT Resident` or `MigrationNT`.
- Do not mechanically translate or print an English legal term beside its Chinese equivalent. Convert the underlying idea into plain, accurate Chinese that an everyday reader can grasp (for example, use “登记业主” rather than `registered proprietor`, and “登记在产权上的限制或权益” where that explains the point better than a string of English terms). Keep specialist English out of decorative document props, labels, seals, books, and background scenery as well.
- Preserve supplied source/caveat wording where present. If none is supplied, use a small general-information disclaimer only if legal-brand context has already made it expected.
- Use concise visible copy when the supplied article is long; do not introduce new legal claims.

## Delivery

State briefly that the image is complete. Include an inline preview and a clickable workspace file link. Do not return a design description instead of the image.
