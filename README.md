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

```text
HumanityAI/
├── README.md
├── PRINCIPLES.md
├── PROBLEM_MAP.md
├── CONTRIBUTING.md
├── AI_OPERATIONS.md
├── EVALUATION.md
├── ROADMAP.md
├── CITATION.cff
├── schema/
│   └── evidence.schema.json
├── data/
│   ├── problems.json
│   └── evidence.json
└── agent/
    ├── CHARTER.md
    └── state.json
```

Future versions should add structured registries for organizations, interventions, projects, datasets, experiments, open questions, evaluations, and autonomous run history.

## Contributing and criticism

Criticism is part of the architecture, not an attack on it. Corrections, contrary evidence, alternative causal models, better datasets, competing normative assumptions, and improved evaluation methods are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Status

**v0.1 — autonomous bootstrap**

The goal is not to claim we already have the correct model of civilization. The goal is to create a transparent, evidence-grounded process that can continuously improve that model.