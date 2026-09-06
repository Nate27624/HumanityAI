# Contributing

HumanityAI should be useful to researchers, engineers, policymakers, nonprofits, students, domain experts, and AI systems.

## Good contributions

- Add a credible source or dataset.
- Correct an inaccurate claim.
- Add an existing project or organization.
- Document evidence for or against an intervention.
- Identify an unresolved question.
- Improve the machine-readable schema.
- Build an agent, crawler, evaluator, or visualization.
- Propose a small experiment that could reduce an important uncertainty.
- Critique the project's assumptions or prioritization methods.
- Independently reproduce or challenge an existing quantitative claim.

## Evidence standard

Whenever practical, separate:

- **Fact** — directly supported by a source.
- **Estimate** — derived from data or a model.
- **Hypothesis** — plausible but unresolved explanation.
- **Value judgment** — depends on normative assumptions.
- **Proposal** — suggested action.
- **Unknown** — important uncertainty.

Disagreement is not repository damage. Preserve credible competing views.

## AI-generated contributions

AI-generated contributions are welcome and may be fully agent-operated, but they must be traceable and reviewable.

If you want to donate agent compute, read [`AGENTS.md`](AGENTS.md) and the machine-readable task queue at [`agent/tasks.json`](agent/tasks.json). External agents should normally contribute through forks/branches and pull requests, not direct writes to `main`.

Every external-agent pull request should record:

- HumanityAI task ID, or a reason the work was unscheduled;
- model/agent system when known;
- whether a human reviewed the work before submission;
- sources considered;
- important contradictory or qualifying evidence;
- key uncertainty;
- tests/evaluations run;
- expected benefit and plausible failure modes;
- reversibility and files changed.

Use the repository pull-request template. The task queue supports both exclusive and parallel work; agents should check linked issues and open PRs before starting substantial work to reduce duplicated compute.

## Agent contribution principle

External agent compute is donated analysis, not delegated authority. A pull request is a proposal. Maintainers, CI, independent audits, and human governance remain responsible for what becomes part of HumanityAI.

Contributors should optimize for improving the shared model, not winning ideological arguments, maximizing commit count, or making the project appear more active.