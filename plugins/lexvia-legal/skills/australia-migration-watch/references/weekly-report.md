# Weekly Reports and PDFs

Use this file when a user asks for a weekly report or a weekly PDF, including when a Codex Scheduled task invokes the skill.

## Per-user state

Create the following automatically in the user's local project directory on first use. Do not show it to the user or require manual edits.

```text
records/
├── monitoring-state.json
└── weekly-report-state.json
```

These files record the monitoring start time, reported item IDs, report versions, and run results. They are local runtime data and are never committed with the plugin.

## Period and timing

- Use `Australia/Sydney`, including daylight saving time.
- A full reporting week is Monday 00:00:00 through Sunday 23:59:59.
- If monitoring starts mid-week, the first report begins at the actual start time and ends that Sunday at 23:59:59. Do not present pre-start information as monitored during that period.
- All later reports use full calendar weeks.
- The Codex task prompt determines when to run and which completed reporting period to generate. If it does not specify a period, use the most recently completed calendar week.

## Content and PDF

- Include only official, verified items with a displayed publication or update date after the monitoring baseline and within the reporting period. Pre-baseline publications remain context only, even if their effective date falls within the reporting period.
- Repeat an item only for a material rule, effective-date, transition, or official-version change.
- Put inaccessible or unverified items under an observations section; do not present them as confirmed.
- Produce a PDF even if there is no verified material change.
- Use `references/logo template.docx` and write the PDF to `outputs/weekly/` in the user's project directory. Create that directory if needed.
- Name reports `australia_migration_policy_weekly_YYYY-MM-DD_to_YYYY-MM-DD_v{version}.pdf`.
- Save the reporting range, item IDs, path, version, and visual-review outcome in the weekly state file.

## Codex Scheduled tasks

Codex Scheduled sets the cadence and calls `$australia-migration-watch`. The saved task prompt must state whether the run is a monitoring check or a weekly PDF run, the reporting period when needed, and whether to notify only for eligible immediate alerts. Use the local project directory rather than a separate worktree so the user's state persists across runs.
