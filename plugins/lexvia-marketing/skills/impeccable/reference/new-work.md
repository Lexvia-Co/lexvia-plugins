<!-- Modified by Lexvia & Co.: manual adaptation of Impeccable 4.8.2; engine
selection, phase gates, telemetry, agent handoffs, and persistence removed. -->

# New visual work

Use for a new surface or an explicitly requested redesign. A missing DESIGN.md is not
permission to replace an existing identity. Do not run initialization or write context
files automatically. Discovery and direction are part of this task, not engine setup.

## 1. Decide what is already true

Inspect the requested target, real product content, applicable documentation, visual
assets, tokens, components, and representative rendered screens. Determine the platform,
surface mode, audience, primary task, and success condition. Record factual uncertainty
without inventing prices, endorsements, users, capabilities, or proof.

Choose the amount of invention from the request:

- **Extend a surface:** reuse its identity, patterns, and interaction model. Invent only
  what the new content or task needs.
- **Add a whole surface inside an established world:** preserve palette, type, component
  character, and navigation; design its own information hierarchy and task sequence.
- **Create or replace a visual world:** the request authorizes a new identity or a
  replacement. Preserve product truth, function, accessibility, and platform affordances.

Do not split an explicit redesign into timid polish, or smuggle a redesign into a fix.
If the request and incumbent evidence conflict, resolve the material conflict first.

## 2. Resolve the brief

Answer from the request and repository before asking: who arrives, why, what they need
to understand or do, the content and evidence available, what must remain untouched,
and the framework/platform constraints. Ask only for gaps that would materially change
the result. Existing project conventions answer routine implementation choices.

Use the surface modes in SKILL.md. Operate and Read favor familiar task paths,
scanability, and consistency; see [operate](operate.md), [mode-operate](mode-operate.md),
and [mode-read](mode-read.md). Persuade earns attention through a product-specific story
and proof. Experience lets the actual work lead rather than decorating around it.

## 3. Choose a concrete direction

Honor a direction already pinned by the user. Otherwise develop a few distinct
approaches only when a real visual or structural choice remains open. Each must state
the product-specific idea, composition, type/color roles, content sequence, primary
action, and implementation consequence. Do not offer mood labels as finished directions.

Select the approach best supported by the brief and available assets when the user has
delegated design choices. Ask for a choice when alternatives imply a material scope,
identity, or product change. Do not reopen settled decisions or require a visual-options
round for routine work. `shape` returns its brief at this point and stops before edits.

For the chosen approach, keep a short working contract in this conversation:

- the one idea that belongs to this product;
- visual authority: what is preserved and what is replaced;
- the first viewport's concrete hierarchy and primary action;
- content sequence and important interaction/state changes;
- responsive behavior, actual assets, and the finish criteria.

This is task context, not a mandatory project file. Do not create hidden configuration,
surface briefs, phase state, seed records, or documentation as a side effect.

## 4. Build the whole requested surface

Read [craft-floor](craft-floor.md) just before editing. Use existing semantic tokens and
components where they remain authoritative. Build the complete content, behavior, and
reachable states: loading, empty, error, success, disabled, long content, and permissions
where relevant. Author representative demonstration data only when appropriate and label
it wherever a visitor could mistake it for factual proof.

Use real product assets or available image tools when the brief needs imagery. Keep a
generated concept image distinct from a real customer, product photograph, or testimonial.
An image reference is not an implementation; reproduce its hierarchy with semantic,
responsive elements. Never fabricate an unavailable asset or quietly replace essential
imagery with decorative chrome. Follow the active image tool's instructions for assets;
this playbook does not provide image generation or an API fallback.

Implement directly using the available project tools. There is no engine-generated
composition, build-phase state, mandatory screenshot comparison service, or agent handoff.
If the task needs a comp or design choice before code, use the available tools and the
user's requested approval boundary rather than inventing a new workflow gate.

## 5. Inspect, correct, and finish

Inspect the rendered surface at representative shipping sizes in a batched pass. Test
the main action and reachable states, keyboard focus, content overflow, zoom, supported
themes, and reduced motion where applicable. On native apps use the platform references
and actual simulator/emulator/device evidence, not a web screenshot.

Step back from implementation and review the result against the request and working
contract in the current session. Identify material mismatches, fix them together, and
verify the changed paths again. Stop repetitive checks once the relevant evidence is
sound. If rendering or hardware is unavailable, report the source-only evidence and
the untested behavior; do not claim a visual or performance pass.

Review the diff for accidental churn. Return the result, design decisions that matter,
checks performed, and any unresolved gaps. Existing PRODUCT.md and DESIGN.md stay intact
unless the user explicitly requested their creation or update; suggest `document` when
a durable record would be useful, without running it automatically.
