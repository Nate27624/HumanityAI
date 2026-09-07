# Per-role heartbeat compatibility artifacts

HumanityAI's repository heartbeat files are retained for compatibility and historical diagnostics. **Scheduler metadata is the authoritative liveness source during the protected-main migration.** A stale repository heartbeat is not, by itself, evidence that a scheduled worker failed.

The current scheduled architecture is:

- Independent Audit — approximately `:11` hourly
- Adaptive Worker A — approximately `:23` hourly
- Adaptive Worker B — approximately `:35` hourly
- Adaptive Worker C — approximately `:47` hourly
- Adaptive Worker D — approximately `:59` hourly

The four JSON files in this directory predate the five-slot adaptive architecture and remain compatibility artifacts:

- `audit.json` — historical audit heartbeat
- `primary.json` — historical primary-worker heartbeat
- `frontier.json` — historical frontier-worker heartbeat
- `secondary.json` — historical secondary-worker heartbeat

Worker D intentionally has no fifth repository heartbeat. **Do not create one.**

## Migration rules

1. Use scheduler metadata, not repository heartbeat freshness, to determine whether Audit or Workers A/B/C/D are alive.
2. Do not create heartbeat-only pull requests merely to refresh timestamps.
3. Do not treat inability to update a compatibility heartbeat as worker failure.
4. Never create a fifth heartbeat and never rewrite another slot's compatibility artifact.
5. If a future design restores repository-persisted liveness as an authoritative signal, it must be compatible with protected `main`, avoid heartbeat-only churn, and be adopted through the normal reviewed change process.
6. Historical timestamps and notes in the JSON files may describe earlier scheduler layouts or security state. They are evidence about past runs, not authoritative statements about current scheduler or repository configuration.

`agent/state.json` is likewise a project-history and summary artifact; it should not override current scheduler metadata for liveness decisions.
