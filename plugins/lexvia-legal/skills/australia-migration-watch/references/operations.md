# Monitoring Operations

Use this file for monitoring runs and periodic reports. One-off policy questions do not need persistent state. The Codex task controls whether and when this workflow runs; this file does not prescribe a cadence.

## Run sequence

1. Read `records/monitoring-state.json` in the user's project directory. If it does not exist, set the baseline to the current Sydney timestamp, record the current official-source state, and send no alerts.
2. Check relevant federal sources, state and territory nomination sources, then assessing-authority and English-rule sources.
3. Compare official publication/update dates, prior verified facts, and sent alerts. Only items with an official displayed date after the baseline are candidates for new-change reporting. A changed timestamp or layout is not evidence of a rule change.
4. Verify, classify, and report eligible changes. Items published before the baseline are context only, including when first discovered later or when their effective date falls after monitoring begins. Record source failures; never treat a failed fetch as no change.

## State requirements

The state file is the single baseline and deduplication record for that user and project. Different users must not share it. Store the baseline timestamp, official URLs, displayed publication/update dates, verified summaries, access failures, and alert IDs; never store personal application data.

Use a stable alert ID based on the topic, visa/state, and effective date. Preserve history when an item is revised; add a new status instead of overwriting the prior alert.

## Limits

- A before/after claim needs both an official current source and reliable prior evidence. Otherwise say the new rule is confirmed but the prior version is not verified.
- Treat consultation papers, budgets, and media as proposed or leads until an implementing official source exists.
- Explain state and federal rules separately when their scopes differ.
- After three consecutive failed checks of a core source, disclose the limitation in the next eligible report.
- Use `Australia/Sydney` for all timestamps. Keep publication and effective dates separate.
- `records/` is per-user runtime data and must not be committed with the skill.
