# Search-discovery baseline — 2026-09-17

## Assignment

Worker D allocated Operator B to analyze where likely qualified users search and identify the highest-value reversible repository-level discoverability gap, without starting Tier-2 production or performing outreach.

## Method

This is a small directional probe, not evidence of traffic, demand, or user behavior. On 2026-09-17, public web search was probed with four query families that approximate ways a qualified researcher, funder, program evaluator, or AI-research practitioner might describe the repository's function:

1. `"evidence-based intervention prioritization" AI global development open source`
2. `"global development decision support" AI evidence open source`
3. `"auditable AI research" evidence synthesis global problems`
4. `"HumanityAI" global problems evidence interventions`

The probe records whether HumanityAI itself surfaced and what competing meanings or adjacent tools occupied the result set. Search ranking is dynamic and personalized; this baseline should therefore be treated as a reproducible qualitative check, not a stable rank measurement.

## Observation

HumanityAI did not surface in the returned results for these descriptive query families during this probe. The exact-name query was especially ambiguous: other unrelated projects and initiatives already use `HumanityAI` / `Humanity AI` language. The descriptive queries instead surfaced adjacent work in intervention prioritization, auditable AI, evidence synthesis, and public-interest AI.

This changes the discoverability diagnosis. The immediate problem is not simply that the repository lacks more occurrences of generic keywords. It is that the project has little demonstrated association with the *functional phrases* a qualified user is likely to search, while its short brand name is not uniquely identifying on the public web.

## Highest-VOI gap

**Functional-category association is a higher-value gap than brand repetition.**

The repository already contains accurate phrases such as `evidence-grounded decision support`, `intervention prioritization`, `cost-effectiveness evidence`, `auditable AI research`, and `machine-readable evidence synthesis` in prominent entry points. It also has GitHub topics spanning evidence synthesis, global problems, open science, reproducible research, and public-interest technology. Adding more synonyms without measuring indexing would risk keyword stuffing and has low expected information value.

The next useful question is therefore whether public search/indexing systems actually associate the repository with those existing functional terms. That can be tested without outreach by repeating a small fixed query panel after entry-point changes and recording presence/absence, result context, and date.

## Decision delta

- **START:** maintain a tiny fixed descriptive-query panel for periodic presence/absence checks after meaningful public-entry-point changes.
- **MORE:** optimize for accurate functional-category language (`evidence-grounded decision support`, intervention prioritization, evidence synthesis, auditable decision products) and direct paths to a concrete example.
- **LESS:** optimize for the bare `HumanityAI` brand term; it is ambiguous and currently competes with unrelated entities.
- **STOP:** adding broad keywords merely because they are adjacent to the mission, or interpreting repository metadata changes as traction before search presence or qualified use is observed.

## Recommendation to Worker D

Treat public indexing/presence as the next discoverability measurement layer. PR #168 already targets first-minute routing inside the repository, so Operator B should not duplicate that work. After #168 resolves, prefer one of two paths:

1. If descriptive-query presence remains absent after indexing time, improve one existing high-authority entry point around a *specific functional category* rather than adding more generic mission prose.
2. If descriptive-query presence appears, shift measurement toward whether search arrivals can reach the concrete DP0001 example in one step; do not infer successful external use from search presence alone.

A repository rename, external outreach, paid promotion, or claims of traction are not implied by this analysis and remain outside this assignment.

## Confidence and blockers

**Confidence: moderate** that bare-brand discovery is structurally noisy and that functional-category discovery is the more useful optimization target; **low** confidence about any specific ranking because this is a single search snapshot.

**Blockers:** no external analytics or qualified-user behavior data are available, and direct user outreach is human-review gated. Search-engine indexing latency also makes before/after attribution weak unless query wording and observation dates are preserved.

## Fixed-panel recheck — 2026-09-18

A second public-search snapshot repeated the same four query strings after the repository entry-point work had been integrated. This remains a presence/absence probe only; it does not measure impressions, clicks, qualified visits, or traction.

| Fixed query | HumanityAI repository surfaced? | Returned context |
| --- | --- | --- |
| `"evidence-based intervention prioritization" AI global development open source` | No | No HumanityAI repository result observed in the returned set. |
| `"global development decision support" AI evidence open source` | No | No HumanityAI repository result observed in the returned set. |
| `"auditable AI research" evidence synthesis global problems` | No | Results included adjacent auditable-AI/research material, but not the HumanityAI repository. |
| `"HumanityAI" global problems evidence interventions` | No | Results were dominated by unrelated projects using HumanityAI / Humanity AI branding, including the philanthropic Humanity AI initiative; the repository did not surface. |

### Recheck decision delta

The first post-change snapshot does **not** provide evidence that the repository has acquired descriptive-query presence. It also does not establish that the entry-point changes failed: indexing latency, search-system variability, and the very small panel prevent that inference.

- **START:** preserve the fixed panel and recheck after a longer indexing interval rather than changing query wording.
- **MORE:** treat the exact-name collision as a persistent discovery constraint and prioritize functional-category association when future discoverability work is justified.
- **LESS:** spend near-term slots adding synonyms or more repository copy before another measurement point.
- **STOP:** interpreting absence in this snapshot as zero demand, or interpreting any future appearance as traction without downstream visit/use evidence.

**Confidence:** high in the recorded presence/absence for this specific returned snapshot; low in causal attribution to recent repository changes and low in extrapolating to other users, engines, times, or geographies.

**Recommendation to Worker D:** keep new discoverability copy held. The highest-value next observation is another fixed-panel recheck after materially more indexing time. If absence persists across spaced measurements, revisit whether repository-level copy is actually the binding constraint before allocating more production.