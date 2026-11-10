<!-- Modified by Lexvia & Co.: manual adaptation of Impeccable 4.8.2;
engine sidecars, automatic initialization, and agent handoffs removed. -->

# Document the implemented design system

Run only when the user asks to capture or update the design system. Record the system
that exists in DESIGN.md, not an identity you would prefer to invent. Tokens are the
authority for values; prose explains their use.

## 1. Inspect the system

Find the consumer project root and applicable DESIGN.md files. In a monorepo, identify
the target app's documentation boundary and inherited rules. Read existing documentation,
tokens, theme configuration, global styles, and representative shared components.

Extract actual values from CSS custom properties, Tailwind configuration, CSS-in-JS
themes, token files, platform resources, and component variants. Sample rendered styles
when tools are available to detect drift. Separate normative tokens from isolated
hardcoded values and component exceptions. Preserve the project's semantic names.

Capture colors and contrast roles; type families, weights, scales, and measure; spacing
and container roles; shapes and radii; elevation; motion and focus treatment; responsive
breakpoints; important component variants and states. Every asserted value needs an
observed source. Do not infer a whole palette from one screenshot or claim extraction
from a browser that did not run.

## 2. Decide the write boundary

For an existing DESIGN.md, merge the requested corrections while retaining unrelated
material. Show and resolve conflicting rules or a replacement that would discard work;
honor any replacement already explicitly authorized. Do not silently replace its format
or token system. A missing PRODUCT.md does not block documenting an implemented design.

If the project has no implementation or tokens, explain that there is no implemented
system to extract. Offer a provisional direction document only if that is what the
user wants; do not present new design decisions as observations. Use [new-work](new-work.md)
for an explicitly requested design exploration, without starting an implementation.

## 3. Write DESIGN.md

Use the existing format when one exists. For a new document, the following order keeps
the system easy to scan; omit sections that are irrelevant or unsupported:

1. Overview: identity, intended use, source authority, and unresolved drift.
2. Colors: semantic roles, exact values, themes, and contrast constraints.
3. Typography: families, role scales, weights, leading, tracking, and fallback/loading behavior.
4. Layout: containers, grid, spacing, breakpoints, density, and reflow.
5. Elevation & Depth: shadows, tonal steps, overlays, and their purpose.
6. Shapes: radii, borders, and consistent form language.
7. Components: variants, states, accessibility, and pointers to the real implementations.
8. Do's and Don'ts: specific observed conventions and known exceptions.

Optional YAML frontmatter may contain source-backed `name`, `description`, `colors`,
`typography`, `rounded`, `spacing`, and `components` values. Quote CSS values. Keep one
canonical value for each role; do not introduce a parallel token layer or claim external
schema validation. Document motion, focus, and other rules in prose when no existing
schema has a suitable field.

## 4. Verify and finish

Cross-check documented tokens against source and rendered evidence where available.
Distinguish current implementation, intended rules, and unresolved drift. Check the diff
for unrelated deletions and contradictory values. Report what was documented, what
evidence was checked, and any gaps. Write only the requested document; no configuration,
sidecars, source migrations, reports, or automatic follow-on work.
