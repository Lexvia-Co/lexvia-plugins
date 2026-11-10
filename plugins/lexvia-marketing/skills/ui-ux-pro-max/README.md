# UI UX Pro Max for Lexvia Marketing

Local, searchable design guidance packaged for the existing Codex Marketing plugin.
Taste leads visual direction when both skills are used; Pro Max supplies targeted UX,
accessibility, interaction, responsive-layout, chart, and detected-stack guidance. Explicit
standalone requests can use Pro Max's design-system generator.

## Source and adaptations

- Upstream: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).
- Pinned commit: [`4f2dbb67e64969a9a30ab00742f2d55d66ddec2b`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/4f2dbb67e64969a9a30ab00742f2d55d66ddec2b).
- `data/` and runtime/validator scripts come from `src/ui-ux-pro-max/`.
- `SKILL.md` and `references/` come from `.claude/skills/ui-ux-pro-max/`.
- Upstream MIT copyright and permission are preserved in [LICENSE](LICENSE).
  Dataset source and font-license metadata are retained in `data/`.

Runtime scripts and datasets are unchanged. Local instruction changes replace Claude-specific
paths with quoted absolute paths resolved from the loaded skill, select a Python 3 interpreter,
make persistence opt-in with an explicit consumer-project destination, and define Taste's
complementary role. Existing project tokens and design decisions take precedence.

Portable upstream runtime/data tests are included. The script-path and IME
reference tests check this installed layout. Upstream catalog-refresh, catalog-summary
generation, and relevance-evaluator tests are omitted because their repository-level
maintenance tools and their fixtures are not shipped here. Installers, CLI/platform copies, templates, the
website, and unrelated upstream skills are also excluded.

## Running and verifying

Requires Python 3 with only the standard library. Prefer `python3`; `python` or `py -3` may be
used after checking that they select Python 3. Node.js is optional for one upstream test that
executes a JavaScript IME example. Do not install dependencies automatically.

Replace `<skill>` below with the absolute directory containing this README, keeping quotes:

```bash
python3 "<skill>/scripts/search.py" "error summary validation" --domain ux
python3 "<skill>/scripts/search.py" "chip badge overflow nowrap" --stack html-tailwind
python3 "<skill>/scripts/search.py" "internal analytics dashboard" --design-system --json
python3 "<skill>/scripts/validate_data.py"
python3 -m unittest discover -s "<skill>/scripts/tests" -v
```

Searches do not write design files. To save a standalone design system, add `--persist`
and `--output-dir "<absolute-consumer-project-root>"`. Existing master and page files are
preserved unless `--force` is explicitly authorized. Never target the installed plugin.

## Updating the pinned import

1. Select and record a reviewed upstream commit. Download that exact archive, not a floating branch.
2. Compare its canonical scripts/data and packaged references with this import. Copy the complete
   data directory, including provenance and license metadata; retain the upstream license notice.
3. Reapply the documented instruction adaptations. Review added dependencies, options, tests,
   and dataset contracts; keep repository-maintenance tooling outside this runtime package.
4. Run the validator and test suite above, including relocation and persistence smoke tests.
   Review the three routing scenarios in the marketplace README against both skill instructions.
5. Update this pin and Marketing's plugin version. Publish only through a separately authorized release.
