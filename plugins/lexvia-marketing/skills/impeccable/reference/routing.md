<!-- Modified by Lexvia & Co.: manual routing for Impeccable 4.8.2;
engine signals, automatic scans, live variants, and storage lookups removed. -->

# Choose an Impeccable playbook

For a workflow question, answer it directly using the relevant references. Advice does
not authorize an audit, edit, initialization, or document write.

For a bare Impeccable invocation, inspect only enough existing project context to make
useful suggestions, then present a small menu:

- Unsure what to make: `shape` returns a scoped UX/UI brief without code.
- Existing surface: `critique` reviews design and usability; `audit` checks technical quality.
- Ready for a final pass: `polish` fixes scoped defects while keeping the design.
- Want a new identity or surface: describe the goal and use the general design workflow.
- Want durable context: `init` records product facts; `document` records an implemented system.

Make one recommendation based on actual evidence, then wait for a selection. Missing
PRODUCT.md or DESIGN.md alone is not a blocker and does not trigger a writing workflow.
Follow an explicit supported request without showing this menu again.

For `live`, `generate`, `hooks`, `doctor`, pin/unpin, engine management, or deprecated
aliases, explain that this manual package does not support that command. Point to the
[upstream project](https://github.com/pbakaus/impeccable#readme) for the full toolset if
useful; do not install it, configure it, run a substitute command, or claim the feature ran.

The command table in SKILL.md is the complete supported interface. `$impeccable audit`
is a conversational invocation, not a shell command. No other skill or engine is required.
