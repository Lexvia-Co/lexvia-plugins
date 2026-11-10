# lexvia-plugins

Lexvia & Co. official plugin repository.

The marketplace contains Legal, Marketing, and Development (`lexvia-testing`) plugins.

## Interface design in Marketing

Marketing includes `design-taste-frontend` for art direction and `ui-ux-pro-max` for
searchable UX, accessibility, interaction, responsive layout, charts, and framework guidance.
Taste leads visual direction when both are used. Pro Max also supports a standalone workflow
when explicitly requested.

Example requests:

- “Build a landing page for our migration practice using Taste for art direction and UI UX Pro Max
  for accessibility and Next.js implementation guidance.”
- “Use UI UX Pro Max to fix keyboard focus and form validation in this React app. Keep the existing design.”
- “Use UI UX Pro Max alone to design a new analytics dashboard.”

Pro Max's search tool requires Python 3 and uses only the standard library, with no network
access or package installation. It runs from the installed skill directory. Saving a design
system is optional and targets the consumer project, preserving existing files unless an
overwrite is explicitly authorized.

See the [skill README](plugins/lexvia-marketing/skills/ui-ux-pro-max/README.md) for
the pinned upstream source, local adaptations, and verification commands.

## Impeccable as an alternative

Marketing also includes an explicitly selected, manual adaptation of Impeccable 4.8.2.
It provides design, critique, audit, refinement, and documentation playbooks using the
agent's available tools. The Taste/Pro Max workflow remains the default.

Example requests:

- “Use Impeccable to redesign this landing page.”
- “$impeccable audit the checkout form. Report findings without changing files.”
- “$impeccable polish the settings screen. Preserve its design and copy.”

Audit and critique return reports in chat. Product/design documents and saved reports
are written only when requested. This adaptation includes no engine, deterministic
detector, downloads, hooks, live variants, or agent registrations.

See the [Impeccable README](plugins/lexvia-marketing/skills/impeccable/README.md)
for the supported commands, source, license notices, and verification scenarios.
