<!-- Modified by Lexvia & Co.: manual adaptation of Impeccable 4.8.2;
automatic configuration, launcher context, and live setup removed. -->

# Capture product context

Run only when the user asks to initialize or capture durable product context.
`init` writes PRODUCT.md; it does not invent a visual world, create DESIGN.md,
configure tooling, or edit source code.

## Explore before asking

Find existing product documentation, the relevant app boundary in a monorepo, and any
applicable PRODUCT.md. Read confirmed facts before updating them. Inspect routes,
workflows, users/roles, real copy, capabilities, constraints, and available evidence.
Infer platform and framework from the project; do not assume a new stack or treat
mobile web as native. Reuse an established product record rather than creating a
competing authority in another folder.

Ask only about material gaps or contradictions the request and repository cannot
resolve. Keep questions focused: audience and job, purpose and success, product
mechanism, binding constraints, and real evidence. Do not turn this into a visual-style
interview. Confirm uncertain inferences; label open decisions instead of inventing facts.

## Write the requested record

For a new record, write PRODUCT.md at the consumer project root or the location the
user specifies. In a monorepo use the target app's established documentation boundary.
For an existing file, merge the requested updates and preserve unrelated sections.
Resolve any proposed replacement that would discard work before writing it. A request
to initialize does not authorize replacing an existing product definition wholesale.

Include the sections that have supported content:

- Platform and stack: the actual implementation and any explicit delivery constraints.
- Users: the people, context, and jobs the product serves.
- Purpose and success: what it enables and what good outcomes mean.
- Positioning: confirmed distinguishing mechanisms, not invented marketing claims.
- Workflows and terminology: the product's real tasks and language.
- Capabilities and constraints: supported functions and explicit limits.
- Brand commitments: existing identity constraints the user made binding.
- Evidence on hand: real content, assets, and proof, with useful repository pointers.
- Accessibility and inclusion: known needs and requirements.
- Open decisions: unresolved facts, explicitly marked.

Do not write aesthetic recipes, speculative customers, invented benchmarks, workflow
settings, hidden state, or engine sidecars. PRODUCT.md captures product truth, not
the current screen's mode or a future visual concept.

## Finish

Check the resulting document against the source facts and requested changes. Summarize
what was captured and what remains undecided. Leave DESIGN.md, source files, and project
configuration untouched. Recommend a relevant next command if helpful; do not start it.
