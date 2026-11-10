# Impeccable for Lexvia Marketing

A manual adaptation of Impeccable's design playbooks, selected explicitly with
`$impeccable` or a request naming Impeccable. Marketing's Taste/Pro Max integration
remains the default. The skill metadata disables implicit invocation.

## Source and notices

- Upstream: [pbakaus/impeccable](https://github.com/pbakaus/impeccable).
- Version: 4.8.2; pinned commit
  [`ec229b48547f24685ffb22aa51c462c5ae27908c`](https://github.com/pbakaus/impeccable/tree/ec229b48547f24685ffb22aa51c462c5ae27908c).
- Instruction and reference source: `.agents/skills/impeccable/` at that commit,
  the generated Codex package. No upstream build step is needed for this import.
- Copyright 2025 Paul Bakaus. The complete upstream Apache-2.0 [LICENSE](LICENSE)
  and third-party [NOTICE.md](NOTICE.md) are retained unchanged.
- The platform guides derive from ehmo's MIT-licensed platform-design-skills.
  Its [MIT notice](third-party/platform-design-skills-LICENSE) is included;
  fetched license blob: `14fac913ccf80234b1848540089a3bbcb6e5283d`.

Modified upstream files carry prominent Lexvia modification notices. This is a derivative
playbook package, not a full installation of Impeccable or a claim to run its engine.

## Included interface

General design/redesign plus: shape, init, document, extract, critique, audit, polish,
bolder, quieter, distill, harden, onboard, animate, colorize, typeset, layout, delight,
overdrive, clarify, adapt, and optimize. These are conversational subcommands of one
skill, not shell commands or standalone registered commands.

Web and native guidance are included. Actual native verification still requires an
available simulator, emulator, or device; a web screenshot does not verify a native app.

`live`, `generate`, `hooks`, `doctor`, pin/unpin, engine management, and deprecated aliases
are unsupported. Ask for the [full upstream toolset](https://github.com/pbakaus/impeccable#readme)
when those features are needed; this package never installs it automatically.

## Local adaptations

- `SKILL.md` and `agents/openai.yaml` provide explicit-only routing and direct context
  inspection. Reference links resolve from the installed skill, including cache paths
  containing spaces. No host-specific project-relative script paths remain.
- `new-work`, `init`, `document`, and `routing` use manual workflows without engine
  selection, build gates, telemetry, configuration, sidecars, or automatic setup.
- `critique` retains upstream's cognitive-load, Nielsen heuristic, and persona reference
  material, with a manual design pass followed by an implementation/evidence pass in
  the current session. It does not require or register agents.
- `audit` and its native variant, `polish`, `layout`, and `typeset` use direct inspection
  and available project/browser checks. Reports disclose absent evidence and the fact
  that the upstream detector did not run. Manual scores are not conformance certification.
- `colorize` drops live variant parameters; `bolder` and the Operate/Read mode references
  drop engine direction-selection assumptions. `craft-floor` preserves explicit user
  constraints and existing identity over aesthetic preferences.
- Other included references retain the pinned upstream text. Interpret follow-on
  command suggestions as recommendations; do not start them without a matching request.

No runtime dependencies are added. Excluded: launchers, binaries, checksums, font catalogs,
browser bundles, hooks, live/variant playbooks, agent configurations, installers, duplicate
platform packages, and upstream development tooling.

Audit/critique are report-only and return findings in chat. Saving reports requires a
request. `init` and `document` write only their requested product/design documents and
preserve unrelated existing content. Other commands do not create those files as a
side effect. No hidden state is created.

## Verification and updates

The [evaluation cases](evals/evals.json) describe routing, read-only review, scoped polish,
unsupported commands, and document preservation. Run them with this skill loaded when
testing behavior in a host. Static policy/link checks do not prove host discovery or
model routing.

For a package check, parse the skill frontmatter and `agents/openai.yaml` as YAML and
the plugin manifest as JSON; verify the explicit-invocation boolean, unique skill names,
all relative reference links, license notices, and the supported command table. Check that
the instructions contain no engine/launcher invocations or named upstream agent handoffs.
Also check a copy under a path containing spaces.

For behavior verification, use a temporary UI fixture with a missing label, suppressed
focus outline, and fixed-width overflow. Audit must identify evidence without changing
the fixture or creating reports/configuration. A subsequent requested polish should fix
the defects while preserving the page's identity, content, and behavior. Inspect a mobile,
intermediate, and wide viewport, verify keyboard focus and the action, and disclose checks
that did not run. Keep fixture artifacts outside this plugin.

Before accepting an update:

1. Choose a reviewed upstream commit; retrieve the generated Codex package at that pin.
2. Compare the references and licenses. Reapply the adaptations listed above and mark
   modified files. Keep unsupported features out of the routing table and reference links.
3. Recheck explicit-only routing and state-writing boundaries across every included guide.
4. Run package checks, the evaluation scenarios, and the existing Pro Max validator/test
   suite. Document installed-host discovery separately from manual or static checks.
5. Update this pin and Marketing's version. Publishing and installation remain separate actions.
