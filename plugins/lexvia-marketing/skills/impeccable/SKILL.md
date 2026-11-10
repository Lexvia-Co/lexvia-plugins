---
name: impeccable
description: >-
  Use only when the user explicitly selects Impeccable for frontend design, redesign,
  shaping, critique, audit, polish, or another named Impeccable command. An independent
  alternative to design-taste-frontend and ui-ux-pro-max, covering web and native UI,
  hierarchy, typography, color, motion, UX copy, accessibility, responsive layout,
  and documenting design systems. This is Lexvia's manual playbook adaptation;
  it does not include the upstream engine, detector, hooks, or live variants.
metadata:
  upstream_version: "4.8.2"
---

<!-- Modified by Lexvia & Co.: manual, explicitly invoked adaptation of Impeccable
4.8.2, commit ec229b48547f24685ffb22aa51c462c5ae27908c. See README.md and LICENSE. -->

# Impeccable — manual design playbooks

Use this workflow when the user explicitly chooses Impeccable. Ordinary design requests
continue through Marketing's existing Taste/Pro Max workflow. Do not invoke Taste's draw,
its inspector, or Pro Max's design-system generator as part of an Impeccable run unless
the user explicitly asks to combine them. This is an independent alternative, not a new
default or a claim to run the full upstream toolset.

Build with a clear point of view, preserve product truth, and verify the rendered result.
The brief and existing brand commitments win over aesthetic preferences in any reference,
including rules described as bans. Refinement preserves identity, behavior, factual copy,
and everything outside scope. Redesign replaces only the visual world the user asked
to replace; it preserves product truth, function, and platform conventions.

## Load context directly

1. Resolve the target, consumer project root, framework, and platform from the request
   and repository. All reference paths are relative to this loaded skill directory,
   including when it lives in a plugin cache or a path containing spaces. Resolve them
   from `SKILL.md`, never the consumer project's working directory. Read references
   on demand; do not load the whole library.
2. Read existing product documentation and any applicable `PRODUCT.md` and `DESIGN.md`.
   In a monorepo, inspect the root and target app's applicable documents rather than
   inventing a competing authority. Inspect tokens, shared components, routes, real
   copy, assets, and representative rendered UI. A missing context file does not make
   an existing interface greenfield and does not block a narrow fix.
3. Use the supplied brief and repository evidence first. Ask only for material gaps
   that cannot be inferred. Do not run `init` or write project documentation merely
   because a file is missing. `init` and `document` run only when requested.
4. Load the selected playbook below. On native projects load [iOS](reference/ios.md),
   [Android](reference/android.md), or both for an adaptive native app. Mobile web
   remains web; browser screenshots cannot prove native behavior.
5. Immediately before a UI edit, read [craft-floor](reference/craft-floor.md).
   Planning and report-only work do not need that step.

There is no launcher or bootstrap step. Do not download an engine, install dependencies,
enable hooks, register agents, create shortcuts, or change the host's configuration.
Use available code-reading, editing, browser, and project-check tools directly.

## Choose the surface mode

- **Persuade:** a landing page, campaign, or pricing surface helps someone decide and act.
  Give it a product-specific story, real proof, and an obvious action.
- **Operate:** an app, dashboard, editor, form, or settings surface helps someone finish
  a task. Scanability, feedback, consistency, and familiar affordances lead.
- **Read:** documentation, articles, and help support understanding. Structure, measure,
  navigation, and sustained readability lead.
- **Experience:** portfolios, galleries, and showcases put the work itself first.

Choose from the surface, not the product category. A tool's landing page is Persuade;
its workspace is Operate. See [Operate depth](reference/operate.md),
[Operate concepts](reference/mode-operate.md), and [Read concepts](reference/mode-read.md).
Keep the mode in the current task brief; do not persist project configuration.

## Commands

These are conversational subcommands of `$impeccable`, not shell commands or separately
registered skills. For example: “Use Impeccable to polish the settings form” or
`$impeccable audit the checkout page`.

| Command | Purpose | Playbook |
|---|---|---|
| General design / redesign | Establish or extend the requested visual world | [new-work](reference/new-work.md) |
| `shape` | Plan UX/UI and return a brief without code | [shape](reference/shape.md) |
| `init` | Capture confirmed product context in PRODUCT.md | [init](reference/init.md) |
| `document` | Capture the implemented design system in DESIGN.md | [document](reference/document.md) |
| `extract` | Reuse tokens and components | [extract](reference/extract.md) |
| `critique` | Review design and usability; report only | [critique](reference/critique.md) |
| `audit` | Review technical quality; report only | [audit](reference/audit.md) · [native](reference/audit.native.md) |
| `polish` | Finish a scoped interface without redesigning it | [polish](reference/polish.md) |
| `bolder` | Amplify the existing identity | [bolder](reference/bolder.md) |
| `quieter` | Reduce overstimulation | [quieter](reference/quieter.md) |
| `distill` | Simplify without losing the essential job | [distill](reference/distill.md) |
| `harden` | Handle errors, localization, and edge cases | [harden](reference/harden.md) |
| `onboard` | Improve first-run and empty-state flows | [onboard](reference/onboard.md) |
| `animate` | Add purposeful, accessible motion | [animate](reference/animate.md) |
| `colorize` | Improve semantic and expressive color | [colorize](reference/colorize.md) |
| `typeset` | Improve type roles, measure, and hierarchy | [typeset](reference/typeset.md) |
| `layout` | Improve grouping, spacing, and responsive structure | [layout](reference/layout.md) |
| `delight` | Add appropriate personality | [delight](reference/delight.md) |
| `overdrive` | Explore an ambitious interface enhancement | [overdrive](reference/overdrive.md) |
| `clarify` | Improve labels, instructions, and recovery copy | [clarify](reference/clarify.md) |
| `adapt` | Adapt to devices and contexts | [adapt](reference/adapt.md) · [native](reference/adapt.native.md) |
| `optimize` | Improve measured UI performance | [optimize](reference/optimize.md) |

- Bare `$impeccable` or a workflow question: use [routing](reference/routing.md).
  Present relevant choices; do not automatically audit, initialize, or edit.
- Explicit or clearly implied supported command: run only its requested scope. A next
  command suggested by a playbook is a recommendation, not authorization to start it.
- General design request naming Impeccable: use new-work. Do not route a focused fix
  through a full redesign or an initialization interview.
- `live`, `generate`, `hooks`, `doctor`, pin/unpin, engine management, and deprecated
  command aliases are not supported in this package. Say so and link to the
  [full upstream installation](https://github.com/pbakaus/impeccable#readme) if useful.
  Do not install anything or silently approximate a live variant feature.

## Evidence and review boundaries

This package uses manual review in the current session. For critique, finish the design
assessment first, then inspect implementation and interaction evidence as a separate pass.
Do not require delegation or represent those passes as isolated agents.

Use rendered screenshots and actual interactions at representative sizes when tools are
available, then batch fixes before verifying again. Use source evidence if a surface cannot
run, but label the result source-only; do not claim rendered, keyboard, touch, contrast, or
native-device verification that did not happen. Distinguish viewport emulation from real
touch/hardware tests. Ordinary project tests are evidence for what they actually check.

Lead audit and critique reports with: **Method: manual playbook review**. Name the target,
evidence, supported sizes/platforms tested, and limitations. The upstream deterministic
detector is not included and did not run; no overlay, engine score, or automatic conformance
verdict exists. Mark untestable dimensions unverified rather than awarding a clean score.
Heuristic scores are manual estimates of observed evidence, never certification.

Audit and critique do not edit source, fix issues, write reports, or change project state.
Return findings in chat. Save a report only when requested, at the requested location (or
an ordinary project documentation path if the user delegates the location), preserving
existing files. Do not create engine sidecars, hidden state, or automatic report storage.

`init` and `document` authorize their named documents, not project configuration or broad
source changes. Read existing files, merge only in-scope updates, and preserve unrelated
content. Ask only when an unresolved contradiction or replacement would discard work.
Other commands must not create PRODUCT.md or DESIGN.md as a side effect.

Finish with the outcome, verification evidence, and material limitations. For changes,
review the source diff for accidental churn and unrelated edits. Report what remains open
instead of treating an untested path as complete.
