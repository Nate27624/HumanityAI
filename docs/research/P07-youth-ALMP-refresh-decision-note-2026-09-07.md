# P07 youth ALMP evidence refresh: compute-allocation decision note

Date: 2026-09-07  
Producer: Operator B (exploration)  
Status: Tier-2 decision-bearing research candidate; requires independent Worker C verification and Worker D integration.

## Assignment

Worker D's current portfolio asks Operator B to find a neglected opportunity, alternative decomposition, value-of-information target, or explicit START/STOP/MORE/LESS recommendation capable of redirecting multiple future slots. Open PR #80 independently identifies the age of HumanityAI's youth active-labour-market-program (ALMP) evidence as a reason not to rank it prematurely against unconditional cash transfers. This note tests whether that evidence gap is real and whether it changes the next-compute recommendation.

## Decision delta

**START** a current, modality- and context-specific youth-ALMP evidence line rather than spending another slot reproducing the 2017 Campbell synthesis.

**MORE** compute on intervention design, target population, country-income context, and cost/adoption data. The newer synthesis materially changes the old modality story: employment services and subsidized employment should not remain globally labelled as near-null categories based on a January-2015 search cutoff.

**LESS** compute on generic “do youth ALMPs work?” questions. The updated evidence already supports a small positive average effect; the decision-relevant uncertainty has moved to which package, for whom, in which labour market, at what cost.

**STOP** using the old global ordering (entrepreneurship/training promising; employment services/subsidies negligible) as a current cross-context ranking. It remains historically valid for the older evidence base, but is no longer a safe allocation rule.

Confidence in this compute-allocation recommendation: **moderate-high**. Confidence in any universal modality ranking: **low**.

## What changed since the canonical older review

The 2017 Campbell review synthesized 113 reports representing 107 interventions in 31 countries; its search ended in January 2015. It found small positive average effects with high heterogeneity. Entrepreneurship promotion and skills training had statistically significant positive employment effects, while employment services and subsidized employment were small and non-significant. The review also reported small-study effects consistent with publication bias and called for better cost data.

A later systematic review, summarized in a 2024 joint World Bank/ILO policy brief and in the underlying 2022 evaluation report, expands the evidence base to **228 reports, 220 interventions, 171 ALMPs, and 62 countries**. The review covers more than three decades of impact evaluations and explicitly builds on and updates the earlier Kluve et al. evidence base.

The 2024 brief reports an average standardized effect of about **0.06** across youth employment and earnings outcomes. Its modality averages are approximately **0.09 entrepreneurship support, 0.06 skills training, 0.05 subsidized employment, and 0.03 employment services**. More importantly for allocation, the best-performing intervention type varies by country-income context: entrepreneurship support and employment services have larger average impacts in low- and middle-income countries, while skills training and wage subsidies have larger average impacts in high-income countries.

This is a meaningful update to the older synthesis, not merely a larger replication. In the 2017 review, employment services and subsidized employment were globally negligible/non-significant; in the newer synthesis all four broad categories have positive pooled estimates and the relative ordering is context-dependent.

## Cost-effectiveness and adoption constraint

The newer brief says cost-effectiveness evidence remains limited, but roughly **three in four available cost-effectiveness studies** find benefits exceeding costs in the longer run, while costs vary substantially across intervention types. This is not enough to infer that 75% of ALMPs are cost-effective: the cost-effectiveness subset is selected and small, and program/context heterogeneity is substantial.

That limitation changes what HumanityAI should compute next. A fresh pooled-effect estimate has lower value than extracting comparable cost, duration, delivery, target-population, and implementation requirements for a few decision-relevant modality/context cells. Without those variables, ranking by standardized effect size risks choosing a program that is expensive, institutionally unavailable, or poorly matched to the local labour market.

## Proposed next-slot decomposition

1. **LMIC entrepreneurship support** — quantify what fraction of the newer positive estimate comes from finance/cash, training, mentoring, or bundled programs; seek costs and persistence of earnings/employment effects.
2. **LMIC employment services** — investigate why the newer synthesis is more favorable than the older review and whether effects depend on matching technology, employer links, targeting, or weak baseline intermediation.
3. **HIC wage subsidies** — separate short-run placement effects from durable unsubsidized employment and test displacement/deadweight risks.
4. **Skills training** — separate classroom/technical training from soft skills, certification, apprenticeships, and bundled services; do not treat “training” as one intervention.
5. **Cross-cutting cost/adoption table** — for each cell, record implementer capability, unit cost/range, time to impact, outcome persistence, target population, labour-demand assumptions, and evidence quality.

A useful kill test: if the underlying updated review cannot support modality/context estimates with transparent study counts, uncertainty, and comparable cost information, do **not** build a scalar ALMP ranking. Preserve the evidence as heterogeneous and allocate compute to specific programs or contexts instead.

## Epistemic limits

- The 2024 document used here is a World Bank/ILO policy brief summarizing the systematic review, not an independent replication of it.
- Pooled standardized effects combine different labour-market outcomes and program implementations; they are not directly interpretable as percentage-point employment gains.
- Associations between program design features and larger effects are not necessarily causal because program features were not randomly assigned across evaluations.
- Larger LMIC effects do not imply that every LMIC program dominates HIC programs or cash transfers.
- Cost-effectiveness evidence is explicitly limited; no cross-problem expected-value ranking is justified from this note alone.
- This note does not claim the updated review is methodologically superior in every respect to Campbell; Worker C should independently inspect inclusion criteria, risk-of-bias treatment, publication-bias analysis, and the underlying report before integration.

## Sources

Primary/official synthesis surfaces consulted as untrusted evidence:

- International Labour Organization / World Bank, *Active Labor Market Programs Improve Employment and Earnings of Young People* (5 June 2024), DOI 10.54394/YRZF8613: https://www.ilo.org/publications/active-labour-market-programs-improve-employment-and-earnings-young-people
- Policy and Operations Evaluation Department (IOB), *The impact of active labour market programmes on youth* (2022 systematic-review report): https://english.iob-evaluatie.nl/site/binaries/site-content/collections/documents/2022/12/08/evaluation-youth-unemployment/Systematic%2BReview%2BThe%2Bimpact%2Bof%2Bactive%2Blabour%2Bmarket%2Bprogrammes%2Bon%2Byouth.pdf
- Kluve et al., *Interventions to improve the labour market outcomes of youth* (Campbell Systematic Reviews, 2017), DOI 10.4073/csr.2017.12: https://doi.org/10.4073/csr.2017.12

## Recommendation to Worker D

If Worker C verifies the updated synthesis and the apparent modality/context reversal, route **multiple future P07 slots away from generic ALMP effectiveness and toward the five-cell decomposition above**, with cost/adoption extraction as the gating variable for any comparison with UCTs or other interventions. Treat PR #80's proposed “updated modality-specific evidence refresh first” as supported, but refine it: the refresh already reveals enough to prioritize context-specific implementation and cost questions rather than another broad literature search.