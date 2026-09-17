# HumanityAI examples

Start here if you want to see what HumanityAI produces before reading the repository architecture.

## Find the useful layer quickly

| If you want to... | Start here |
| --- | --- |
| See a concrete AI-assisted decision-support output | [`DP0001`](../products/decision_products/DP0001-zambia-catchup-caregiver-messaging.md) |
| Audit the research behind that decision | [`P05 parent attendance-information exposure test`](../docs/research/P05-parent-attendance-information-exposure-test-2026-09-11.md) |
| Inspect machine-readable evidence and provenance | [`data/`](../data/) |
| Understand how uncertainty and competing evidence are evaluated | [`EVALUATION.md`](../EVALUATION.md) |
| Contribute research or coding with an AI agent | [`AGENTS.md`](../AGENTS.md) and [`agent/tasks.json`](../agent/tasks.json) |

HumanityAI is currently most useful to researchers, implementers, analysts, and AI-agent operators who want **auditable evidence synthesis and intervention decision support** rather than an opaque recommendation. The repository is an early public prototype, not a validated decision service.

## Decision-support example

### Zambia Catch Up: caregiver attendance-information messaging

[`DP0001`](../products/decision_products/DP0001-zambia-catchup-caregiver-messaging.md) is the current concrete decision-product prototype. It asks whether a Zambia education implementer already considering or operating Catch Up should add caregiver attendance-information messaging next.

The current answer is **CANNOT DECIDE** until a small operational sample establishes whether relevant exposure states can be reconstructed, caregivers have an actionable information gap and can reliably receive/understand messages, and the incremental implementation cost is acceptable. If those gates pass, the product routes to a bounded **TEST**, not immediate scale.

This example is useful because it shows the intended HumanityAI workflow rather than only describing it:

- turn research into an explicit present-tense decision route;
- distinguish evidence from assumptions and missing observations;
- expose portability and denominator limits instead of forcing incomparable cost-effectiveness estimates;
- state kill conditions and what evidence would change the recommendation;
- keep provenance inspectable through the linked research synthesis.

For the underlying evidence trail, see [`P05 parent attendance-information exposure test`](../docs/research/P05-parent-attendance-information-exposure-test-2026-09-11.md).

## What to inspect next

- [`products/decision_products/`](../products/decision_products/) — decision-facing outputs.
- [`docs/research/`](../docs/research/) — research syntheses supporting decisions.
- [`data/`](../data/) — machine-readable evidence, indicators, resources, and forecasts.
- [`EVALUATION.md`](../EVALUATION.md) — how changes are evaluated.
- [`AGENTS.md`](../AGENTS.md) — how external research/coding agents can contribute safely.

HumanityAI does not yet claim demonstrated improvement in external users' decisions. These examples are public, auditable prototypes intended to make the project's current capabilities and limitations easy to inspect.