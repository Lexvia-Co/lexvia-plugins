---
name: australia-migration-watch
description: Monitor material Australian immigration-policy changes from official sources and produce verified Chinese alerts and branded weekly PDF reports. Use for visa, skilled migration, state nomination, occupation, fee, English, and processing-rule updates; not for personal eligibility advice.
---

# Australian Migration Policy Watch

Verify public Australian migration-policy changes. Produce Chinese reader-facing output only when the task prompt requests it. Report facts only; never assess an individual's eligibility, prospects, or application strategy.

## Sources, state, and scope

- Read [official sources](references/sources.md) before monitoring. Only Australian federal, state, territory, legislative, or directly linked official materials prove a policy change.
- For monitoring runs, follow [operations](references/operations.md). For weekly reports and PDFs, follow [weekly-report](references/weekly-report.md). Codex Scheduled controls when a run occurs; this skill defines only the workflow and output rules.
- Do not retain passports, visa numbers, ImmiAccount details, finances, or application documents.
- Monitor material changes to allocations, program openings or closures, occupation lists and assessing authorities, visa eligibility and conditions, fees, English rules, state nomination, processing priorities, legislation, and transition arrangements.

## Verification

For every candidate change, confirm the official title and URL, publication/update date, effective date or deadline, affected cohort, and a reliable before/after difference. Use one of: effective, announced-not-effective, proposed, or unverified. Do not infer a difference from a page redesign, ordinary processing-time movement, commentary, or an inaccessible source.

State nomination and a federal visa grant are separate outcomes. If a prior rule cannot be verified, say so rather than claiming a comparison.

## Monitoring baseline

On the first scheduled run, set the monitoring baseline to that run's Sydney timestamp and record the current official-source state without sending alerts or treating earlier publications as new changes. On later runs, use the official page's displayed publication or update date to identify candidates: only items dated after the baseline are eligible for a new-change alert or report entry. An item published before the baseline remains baseline context, even if it is first discovered later or takes effect after monitoring begins.

## Outputs

### Material-change alert

Alert only for high-impact changes, or medium-impact changes with a deadline. Do not repeat an alert unless the rule, effective date, transition arrangement, or official version materially changes.

```markdown
⚠️ [Visa/state/policy]: rule update

- Status: effective / effective YYYY-MM-DD / proposed / unverified
- Published: YYYY-MM-DD; effective/deadline: YYYY-MM-DD or not stated
- Affected: visa, occupation, state program, or cohort
- Change: verified difference from the prior rule
- Check: official condition, evidence, or deadline to confirm

[Official source](URL)
```

### Weekly PDF

Include only verified changes first seen, updated, or effective in the reporting period. If none exists, produce the PDF with a clear no-verified-material-change statement. Do not fill it with old news.

Use `references/logo template.docx` as the fixed company template. Store PDFs and state in the user's local project directory, never in the plugin directory. Render and inspect every page for the logo, localized text, page numbers, links, and overflow.

Append the requested-language disclaimer: this is public policy information, not migration or legal advice; readers must rely on the official source and their own circumstances.
