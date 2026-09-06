# Failure Recovery and Autonomous Reliability

HumanityAI should assume that web sources fail, APIs rate-limit, connectors lose permission, models make mistakes, partial writes occur, CI breaks, and scheduled runs are occasionally skipped. Reliability comes from detecting and recovering from failure, not assuming it will not happen.

## Core rules

### 1. Fail closed on consequential writes
If required context, source verification, repository state, or permissions cannot be confirmed, do not make a consequential change. Record the blocked task and continue with safe work when possible.

### 2. Reads before writes
Before updating an existing file, fetch the current version and SHA immediately before writing. Never overwrite an unseen newer state.

### 3. Prefer atomic, reversible changes
Keep changes small enough to understand and revert. Large architectural changes belong on branches/PRs. Avoid coupling unrelated changes into one write.

### 4. Retry transient failures once, then degrade gracefully
For temporary web/API/GitHub failures:

1. retry once when safe;
2. try an authoritative alternative source or independent read path if appropriate;
3. do not invent missing data;
4. record the failure and next retry target;
5. continue another useful safe task if one exists.

Repeated retries should not consume an entire run.

### 5. Never treat tool failure as evidence
A source failing to load does not mean a claim is false. A search returning no result does not prove nonexistence.

### 6. Idempotence
Recurring tasks should be safe to run twice. Before creating issues, files, claims, or entries, check whether equivalent work already exists.

### 7. Checkpoint persistent state
Each successful autonomous run should update persistent state with:

- run timestamp;
- task chosen;
- completion status;
- changes made;
- sources checked;
- evaluation result;
- failures encountered;
- retry-needed items;
- best next action.

A later run should be able to resume without relying on conversational memory.

### 8. Heartbeat
Maintain a machine-readable last-successful-run timestamp. Independent audits should flag a stale hourly maintainer heartbeat, repeated no-op failures, or repeated inability to access the repository.

### 9. CI before confidence
When code/schema changes are made, use deterministic validation/CI when available. A model saying code "looks correct" is not a substitute for tests.

### 10. Do not merge around failing validation
If validation fails because of the proposed change, fix or revert it. Do not weaken tests merely to obtain a green result unless the test itself is demonstrably wrong and the rationale is recorded.

### 11. Corruption recovery
If machine-readable state becomes malformed:

- preserve the broken version in git history;
- restore the most recent valid state;
- diagnose the cause;
- add a regression test where feasible.

### 12. Source resilience
Important claims should avoid dependence on a single fragile URL when strong alternatives exist. Preserve identifiers such as DOI, dataset ID, publication title, organization, and access date where applicable.

### 13. Permission isolation
Autonomous agents may operate only on the explicitly authorized HumanityAI repository. Permission ambiguity must never cause fallback writes to another repository or account.

### 14. Escalation threshold
Human attention is for failures that autonomous recovery cannot responsibly resolve, including:

- persistent repository/permission failure;
- repeated scheduled-run failure or stale heartbeat;
- security or credential concern;
- constitutional/value conflict;
- serious factual/reputational incident;
- inability to determine whether a consequential change is safe.

Routine transient failures should be logged and recovered automatically.

## Run status model

Use explicit statuses such as:

- `success`
- `partial_success`
- `no_change_needed`
- `blocked_transient`
- `blocked_permission`
- `blocked_governance`
- `failed_validation`
- `reverted`

Do not record a run as successful merely because it produced output.

## Failure budget

The system should periodically measure:

- successful runs / expected runs;
- runs with meaningful improvements;
- transient tool failures;
- persistent failures;
- failed/reverted writes;
- CI regression rate;
- duplicate-work rate;
- stale-heartbeat incidents;
- time from detected failure to recovery.

Reliability metrics are diagnostics, not the mission. They exist so the project can remain operational long enough to pursue the mission.

## Scheduled-task recovery

Because an external scheduler may skip or fail a run, no single scheduled execution should be mission-critical. Each future run must inspect repository state and recover unfinished high-value work from the prior state. Daily and weekly audit layers should independently detect whether the hourly process appears stale or unhealthy.
