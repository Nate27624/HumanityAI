# Operator A decision product: UCT vs youth active-labour-market evidence

Date: 2026-09-07

## Assignment

Under the current Worker D portfolio plan, identify a direct-progress comparison that changes prioritization rather than adding another baseline. This note compares the **marginal value of the next HumanityAI compute spent on unconditional cash transfers (UCTs)** versus **youth active-labour-market programmes (ALMPs)** using current canonical evidence `E0001` and `E0006`.

This is a compute-allocation decision, **not** a recommendation that governments or funders implement either intervention.

## Current evidence state

### Unconditional cash transfers — `E0001`

Current canonical evidence is comparatively decision-ready on broad effectiveness direction. The 2022 Cochrane review synthesized 34 studies with 1,140,385 participants in low- and middle-income countries. HumanityAI records probable/maybe improvements across several welfare outcomes, including food security, dietary diversity, school attendance, and the probability of not being extremely poor, while a summary measure of health-service use may change little or not at all.

The important unresolved decision variables are downstream of basic efficacy: transfer size and duration, administrative cost, delivery constraints, targeting versus universality, displacement or equilibrium effects, durability, and comparable cost-effectiveness across outcomes. The review also reports high overall risk of bias in most included studies, so quantitative expected-value work must carry wide uncertainty rather than treating the positive direction as a precise effect size.

### Youth active-labour-market programmes — `E0006`

Current canonical evidence is less decision-ready at the intervention-class level but more discriminating across programme types. The Campbell review covers 107 interventions in 31 countries and finds small positive average employment and earnings effects with substantial heterogeneity. Skills training and entrepreneurship promotion show significant average gains, while employment services and subsidized employment have negligible or statistically insignificant average effects; business-performance effects are not statistically significant.

The major constraint is evidence vintage and heterogeneity. Searches were current only through January 2015, programme designs differ substantially, and cost data were limited. A single expected-value estimate for “youth ALMPs” would therefore be misleading. The next useful work would need to split the class by modality and refresh the evidence before attempting cost-effectiveness comparison.

## Decision delta

**Allocate the next direct-progress quantitative analysis to UCT cost-effectiveness / adoption constraints before attempting a cross-intervention ranking with youth ALMPs.**

Rationale:

1. `E0001` already establishes a reasonably strong directional effectiveness case across multiple welfare outcomes, so additional generic UCT effectiveness review has lower marginal value than translating existing evidence into costs, implementation assumptions, and expected-value ranges.
2. `E0006` shows that the ALMP umbrella is too heterogeneous for a defensible scalar comparison. A new quantitative ranking should not combine skills training, entrepreneurship promotion, employment services, and subsidized employment as though they are one intervention.
3. The ALMP evidence search is materially older than the UCT review and the canonical record explicitly identifies limited cost data. The highest-value ALMP work is therefore an **evidence refresh by modality**, not immediate cost-effectiveness ranking.
4. A premature UCT-vs-ALMP score would mix different populations, outcome families, follow-up periods, programme designs, and evidentiary vintages. HumanityAI should reject that false comparability until common decision variables are made explicit.

## Recommended controller allocation

### MORE

- **Operator A:** build a bounded UCT decision model using source-grounded ranges for transfer cost, administrative cost, outcome effects, duration, and adoption/implementation constraints. Keep outcomes multidimensional unless a transparent common unit is genuinely available.
- **Operator B:** search for a current systematic review / meta-analysis of youth ALMPs that separates skills training, entrepreneurship, employment services, and subsidized employment, with special attention to costs, heterogeneity, and longer-run effects.

### LESS

- Generic “does UCT work?” evidence accumulation unless it materially changes `E0001`.
- Generic “do youth employment programmes work?” summaries that do not split programme modality.

### STOP / kill conditions

- Do **not** publish a single UCT-vs-ALMP priority score if costs or outcomes are not comparable.
- Do **not** infer that statistically significant average effects imply attractive cost-effectiveness.
- Do **not** treat a null average for employment services/subsidized employment as proof that every programme in those classes is ineffective.
- Stop the UCT decision-model attempt if available cost/effect inputs cannot support at least transparent low/base/high ranges without invented precision; record the unresolved variables instead.

## Confidence and unresolved uncertainty

**Confidence in compute-allocation recommendation: moderate-high.** The recommendation depends mainly on the maturity difference between the two canonical evidence records, not on an unsupported claim that UCTs are socially superior to ALMPs.

The strongest uncertainty is whether newer youth-ALMP evidence materially changes the 2017 Campbell conclusions. That uncertainty is itself the reason to route ALMP compute toward evidence refresh before comparative expected-value scoring.

## Controller-facing next action

Treat this as a Tier-2 decision product. Independent Worker C should verify that the comparison faithfully represents `E0001` and `E0006`, especially the UCT risk-of-bias limitation, the ALMP modality split, the 2015 search cutoff, and the limited-cost-data statement. If C returns PASS or a manageable QUALIFY verdict, Worker D can integrate this recommendation into the next portfolio allocation: A -> UCT cost/adoption model; B -> updated modality-specific youth-ALMP evidence search.
