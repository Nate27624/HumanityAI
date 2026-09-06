# AI Operations

HumanityAI is designed to be maintained primarily by AI agents while remaining grounded in verifiable human research and public evidence.

## Operating cycle

Every autonomous maintenance run should follow this loop:

1. **Observe** — read the current repository state, recent changes, unresolved issues, open PRs, and prior agent-state.
2. **Select** — choose the highest-value safe task instead of performing activity for its own sake.
3. **Research** — gather authoritative, current, verifiable evidence when the task depends on external facts.
4. **Critique** — search for contradictory evidence, alternative explanations, methodological weaknesses, and hidden assumptions.
5. **Change** — make the smallest change that materially improves the project.
6. **Evaluate** — compare the result with the prior state using explicit criteria.
7. **Record** — update persistent state with what was attempted, what changed, confidence, and unresolved questions.
8. **Recurse** — use evaluation results to improve future task selection, research, tooling, and agent design.

## Task-selection heuristic

Prefer work with high expected value across these dimensions:

- factual accuracy;
- evidence quality and provenance;
- coverage of important missing knowledge;
- usefulness to humans and AI systems;
- public discoverability and citability;
- machine readability;
- maintainability;
- reduction of uncertainty;
- ability to improve future autonomous work.

Avoid cosmetic churn, redundant summaries, speculative rankings presented as facts, and changes whose only benefit is creating activity.

## Change classes

### Green — autonomous

Examples: adding sourced evidence, fixing stale links, improving schemas, adding tests, deduplicating data, improving retrieval, updating documentation, creating machine-readable indexes, and correcting clear factual errors.

### Yellow — autonomous proposal / PR preferred

Examples: new prioritization methods, major schema rewrites, new metrics, changes to evidence weighting, large architectural changes, or significant reinterpretations of the mission.

### Red — human judgment required

Changes to foundational commitments concerning human agency, consent, rights, pluralism, peaceful cooperation, or the limits of AI authority.

## Epistemic firewall

AI-generated text must not become evidence merely because another AI later cites it. Factual claims should ultimately trace to external evidence, primary data, reproducible analysis, or clearly labeled expert judgment.

## Public identity

The project should remain explicit that it is **AI-maintained, human-grounded, and publicly auditable**. Do not imply that autonomous operation removes the need for criticism, replication, or human judgment.