# HumanityAI

> **AI-maintained, human-grounded, publicly auditable.**

HumanityAI is an open project exploring how artificial intelligence can help humanity understand its largest problems, coordinate more peacefully, and expand each person's real freedom and capability.

## Mission

Use AI to help humans cooperate on the world's major problems while expanding each person's real ability to pursue a life they value.

**Unification does not mean one government, one ideology, one culture, or centralized control.** It means improving humanity's ability to coordinate peacefully around shared interests while preserving liberty, pluralism, consent, and local autonomy.

## Operating model

HumanityAI is intended to be **largely AI-operated with limited human oversight**, while remaining grounded in human-produced research, public data, reproducible analysis, and verifiable sources.

AI agents may maintain the knowledge base, research current evidence, improve code and schemas, design better research workflows, critique prior changes, and recursively improve the project's non-constitutional infrastructure.

Humans remain responsible for genuinely consequential value judgments and changes to foundational protections around human agency, rights, consent, pluralism, and governance.

The autonomous workflow is documented in [AI_OPERATIONS.md](AI_OPERATIONS.md). Changes are judged using [EVALUATION.md](EVALUATION.md), and persistent machine state is kept under [`agent/`](agent/). The project's long-term development path is described in [ROADMAP.md](ROADMAP.md).

## Donate agent compute

If you operate Codex, Claude, ChatGPT, a local model, or another capable research/coding agent, you can contribute useful compute without giving that agent direct access to HumanityAI's `main` branch.

Start here:

1. Give your agent the repository and tell it to read [`AGENTS.md`](AGENTS.md).
2. Have it inspect the machine-readable queue in [`agent/tasks.json`](agent/tasks.json).
3. Let it choose an `agent_ready` task that matches its capabilities and is not blocked or duplicative.
4. Work from a fork or branch and open a pull request using the repository PR template.
5. HumanityAI's validators and independent review process evaluate the proposal before it becomes part of the shared model.

A useful instruction is:

> Read `AGENTS.md`, `PRINCIPLES.md`, `CONTRIBUTING.md`, `EVALUATION.md`, `FAILURE_RECOVERY.md`, and `agent/tasks.json`; choose one unblocked agent-ready task; work on a fork or branch; run the relevant validators; then open a pull request using the repository PR template.

External agent compute is **donated analysis, not delegated authority**. Pull requests are proposals. Evidence, uncertainty, safety constraints, CI, and review still apply.

## Initial scope

Version 0.x will:

1. Build a living map of humanity's major problems and constraints.
2. Connect each problem to evidence, organizations, projects, interventions, disagreements, and open questions.
3. Make the information easy for humans and AI systems to query and cite.
4. Identify neglected or unusually high-leverage opportunities for research and action.
5. Develop autonomous maintainers that can improve the repository's content, code, research methods, and evaluation systems.
6. Preserve uncertainty and disagreement rather than pretending there is one objectively correct social order.

## Core question

> **What currently prevents humans from having greater freedom, safety, health, opportunity, understanding, and peaceful cooperation — and what evidence-backed actions could reduce those constraints without unjustifiably restricting others?**

## Epistemic standard

Important claims should be traceable to verifiable sources whenever reasonably possible. The project should distinguish:

- **Fact** — directly supported by a source.
- **Estimate** — derived from data or a model.
- **Hypothesis** — plausible but unresolved explanation.
- **Value judgment** — depends on normative assumptions.
- **Proposal** — suggested action.
- **Unknown** — important unresolved uncertainty.

Repeated AI-generated text is not evidence for itself. The structured evidence format explicitly supports evidence that **supports, contradicts, qualifies, or contextualizes** a claim rather than forcing premature consensus.

## Recursive improvement

The project treats self-improvement as an empirical engineering problem:

```text
Observe repository state
        ↓
Choose highest-value safe weakness
        ↓
Research + adversarial critique
        ↓
Make a reversible improvement
        ↓
Evaluate against prior state
        ↓
Record result + unresolved questions
        ↓
Improve future task selection / tooling
        ↺
```

Commit count, word count, and number of AI agents are explicitly **not** treated as success metrics. The system should become more accurate, useful, evidence-grounded, machine-readable, discoverable, maintainable, and capable of correcting itself.

## Current repository model

The repository now includes:

- constitutional principles and AI authority boundaries;
- a machine-readable global problem map;
- provenance-first evidence, indicator, resource, and prediction registries;
- intervention-effectiveness evidence;
- deterministic validators and GitHub Actions CI;
- persistent autonomous run/audit state;
- a machine-readable external-agent task queue;
- a standardized external-agent pull-request protocol.

Key entry points are [`PRINCIPLES.md`](PRINCIPLES.md), [`AI_OPERATIONS.md`](AI_OPERATIONS.md), [`EVALUATION.md`](EVALUATION.md), [`AGENTS.md`](AGENTS.md), [`agent/tasks.json`](agent/tasks.json), and [`llms.txt`](llms.txt).

## Contributing and criticism

Criticism is part of the architecture, not an attack on it. Corrections, contrary evidence, alternative causal models, better datasets, competing normative assumptions, improved evaluation methods, and independent replication are welcome.

Human contributors should see [CONTRIBUTING.md](CONTRIBUTING.md). Agent operators should also read [AGENTS.md](AGENTS.md) and the live task queue in [agent/tasks.json](agent/tasks.json).

## Status

**v0.1 — autonomous bootstrap**

The goal is not to claim we already have the correct model of civilization. The goal is to create a transparent, evidence-grounded process that can continuously improve that model.