# Per-role heartbeats

These files are the canonical liveness records for HumanityAI's recurring autonomous roles.

Each scheduled role owns exactly one file:

- `primary.json` — primary research/self-improvement loop (~:26 hourly)
- `frontier.json` — frontier/possibility rotation (~:41 hourly)
- `secondary.json` — complementary second pass (~:56 hourly)
- `audit.json` — independent audit/watchdog (~:11 hourly)

## Rules

1. A role may update only its own heartbeat file.
2. Read the current file immediately before writing so concurrent repository activity is not overwritten.
3. Update `last_attempt_at` on every run that can access the repository.
4. Update `last_success_at` only when that role's run is genuinely successful or `no_change_needed`; blocked/partial/failed runs do not advance it.
5. Record the real run status; never fabricate a heartbeat to hide a missed scheduler execution.
6. `consecutive_non_success` increments for partial/blocked/failed runs and resets to zero on success/no-change-needed.
7. The independent audit should treat one missed/late run as tolerable scheduler jitter. Repeated unexplained staleness across roughly two expected windows is actionable; persistent staleness or a security-relevant failure should trigger the configured human-review email path.
8. `agent/state.json` remains a useful project summary, but it is **not** the canonical source for per-role liveness once these files are populated.

The initial files intentionally contain null timestamps. Scheduled roles must establish their own first authoritative heartbeat; bootstrap code must not pretend a role ran merely because a scheduler was configured.
