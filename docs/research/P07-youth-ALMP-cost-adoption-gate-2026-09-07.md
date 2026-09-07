# P07 youth ALMP cost/adoption gate: exploration note

Date: 2026-09-07  
Producer: Operator B (exploration)  
Status: Tier-2 decision-bearing research candidate; requires independent Worker C verification and Worker D integration.

## Assignment

Worker D's current portfolio directs Operator B to explore context-specific youth active-labour-market-programme (ALMP) implementation and cost questions, emphasizing modality-by-income-context, persistence, target population, implementer capability, and value-of-information. The controller explicitly says not to build a universal modality ranking from pooled subgroup estimates.

## Decision delta

The next useful ALMP comparison should be gated by **implementation-adjusted cost and institutional fit**, not by pooled standardized effect size alone.

**START** a small context-specific cost/adoption table for concrete ALMP cells before attempting any cross-intervention ranking.

**MORE** compute on realized per-participant cost, delivery intensity/duration, implementer type, employer linkages, certification, participant vulnerability, and whether benefits persist after program exit.

**LESS** compute on global modality averages that omit cost and delivery constraints.

**STOP** treating a larger pooled effect estimate as a sufficient reason to prefer one ALMP modality over another.

Confidence: **high** that cost/adoption is the current decision bottleneck; **moderate** that the headline median-cost differences are portable enough to guide exploration; **low** for any scalar global cost-effectiveness ranking.

## Why cost can overturn an effect-size-only ranking

The 2024 ILO/World Bank policy brief reports very different median program costs per beneficiary (2020 USD):

| Broad modality | Reported median cost per beneficiary | Decision implication |
|---|---:|---|
| Employment services | about **$230** | Low unit cost makes modest effects potentially competitive if delivery infrastructure exists and placement quality persists. |
| Skills training | about **$730** | Roughly three times the employment-services median; design/intensity and certification become important adoption variables. |
| Entrepreneurship support | about **$730** | Similar median to training, but bundle composition (finance, training, mentoring) and informal-market conditions matter. |
| Wage subsidies / public works | about **$1,700** | Much higher median cost; durable unsubsidized employment, displacement and deadweight become critical before ranking. |

The same brief reports median costs of about **$3,200 in high-income countries, $418 in middle-income countries, and $490 in low-income countries**. These are descriptive medians across heterogeneous programs, not standardized prices for interchangeable interventions.

This creates a simple decision warning: the newer synthesis's broad pooled effect estimates cannot be compared on effect size alone when nominal unit costs differ by several-fold and the interventions solve different barriers.

## Cost-effectiveness evidence is selected, not a 75% success rate

The policy brief states that nearly three out of four evaluations with cost-effectiveness analysis find benefits exceeding costs over the longer run, but also says rigorous cost-effectiveness evidence remains limited and concentrated in skills training.

Worker C's independent reading of the underlying review further identified that only a minority of reports contain cost-benefit analysis and that those analyses are heavily concentrated in skills training. Therefore:

- do **not** infer that roughly 75% of youth ALMPs are cost-effective;
- do **not** compare modalities using the selected cost-benefit subset as if it were representative;
- use the subset to motivate study-level extraction and standardization, not to produce a global scalar ranking.

## Adoption and implementer capability are part of the treatment

The 2024 ILO/World Bank brief associates better outcomes with several design/implementation features: soft-skills training, certification, multi-component programs, local/regional rather than national delivery, and public/non-public partnerships in low- and middle-income countries. The 2026 ILO/World Bank technical-report page likewise emphasizes program design, implementation partnerships, certification, and cost-effectiveness as policy-relevant dimensions.

These are not proven causal levers merely because they correlate with stronger evaluated programs. They are, however, strong reasons to treat implementer capability and delivery architecture as gating variables. A jurisdiction that lacks credible training providers, employer relationships, placement infrastructure, or the ability to verify skills may not reproduce the evaluated program even if the modality label is the same.

## Context-specific exploration cells

### 1. LMIC employment services

Why explore: headline unit cost is low and the updated evidence base is more favorable to employment services in lower-income settings than the old 2015-cutoff global ordering.

Key adoption questions:
- Is there a functioning public or contracted employment-service network?
- Are vacancies observable enough for formal matching to improve on informal hiring channels?
- Do providers have employer relationships and credible screening/counselling capacity?
- Are measured gains durable job matches or short-lived placements?

High-value evidence target: a study-level set of LMIC employment-service evaluations with program cost, placement mechanism, employer linkage, target population, follow-up length, and unsubsidized employment/earnings outcomes.

### 2. LMIC entrepreneurship support

Why explore: newer syntheses report comparatively larger average impacts in LMICs, but the modality covers materially different bundles.

Key adoption questions:
- Is the intervention primarily cash/grant/credit, business training, mentoring, or a bundle?
- Are local product markets deep enough to absorb additional microenterprise activity?
- Are profits/earnings persistent after grants or coaching end?
- Does implementation require screening, mentoring capacity, financial infrastructure, or follow-up support unavailable at scale?

High-value evidence target: separate finance-only, training-only, and bundled programs before comparing costs or effects.

### 3. HIC wage subsidies

Why explore: comparatively larger average effects are reported in high-income settings, but the median broad-category cost is high and short-run placement can overstate durable value.

Key adoption questions:
- What share of subsidized jobs would have been created anyway (deadweight)?
- Are unsubsidized workers displaced?
- Does employment persist after the subsidy ends?
- Is targeting administratively feasible enough to avoid paying for low-additionality hires?

High-value evidence target: post-subsidy outcomes plus displacement/deadweight estimates, not placement at program completion alone.

### 4. Skills training

Why explore: the evidence base and cost-benefit literature are relatively large, but "training" is too broad for direct comparison.

Key adoption questions:
- Is training classroom, technical, apprenticeship, on-the-job, soft-skills, certification, or bundled?
- Is curriculum linked to local employer demand?
- Can providers deliver the evaluated intensity and quality?
- Does certification credibly signal skills to employers?

High-value evidence target: compare programs only after coding provider type, duration/intensity, certification, employer linkage, target group, and follow-up horizon.

## Proposed minimum decision table

Before Worker D permits a quantitative youth-ALMP ranking, each candidate cell should contain at least:

1. country/income context and target population;
2. modality plus bundle components;
3. implementer/provider type and required capabilities;
4. nominal and inflation-year-adjusted cost per participant, with included cost categories stated;
5. duration/intensity and time to outcome;
6. employment and earnings outcomes separately;
7. follow-up after program exit;
8. evidence design/quality and publication-bias sensitivity;
9. adoption constraints (coverage, take-up, employer demand, provider capacity);
10. externalities/risks relevant to the modality (for example displacement/deadweight for subsidies).

If these fields cannot be populated for a candidate, the correct output is **insufficient comparability**, not a forced ranking.

## Value-of-information

The highest-value next extraction is likely **LMIC employment services versus LMIC entrepreneurship support**, because the 2024 brief's descriptive median cost gap is large (about $230 vs $730 per participant) while the updated synthesis suggests both can be relevant in LMICs. A modest effect from a much cheaper intervention could dominate on cost per durable outcome, but only if matching infrastructure and employer linkages are real and effects persist. Conversely, entrepreneurship may remain preferable where formal intermediation is weak and self-employment is the feasible margin.

This is a sharper question than "which modality has the largest pooled SMD?" and could redirect several future compute slots.

## Kill tests

Do not build a scalar ALMP ranking if any of the following remain true:

- costs are not defined consistently across programs;
- follow-up horizons differ enough that persistence cannot be compared;
- pooled outcomes combine employment and earnings without a defensible common unit;
- modality estimates are being treated as causal design effects despite publication-bias and composition concerns;
- adoption/implementer requirements differ materially and are not modeled;
- subsidy displacement/deadweight or entrepreneurship market-saturation risks are ignored where material.

## Sources

Primary/official sources consulted as untrusted evidence:

- ILO / World Bank, *Active Labor Market Programs Improve Employment and Earnings of Young People* (5 June 2024), DOI 10.54394/YRZF8613: https://www.ilo.org/publications/active-labour-market-programs-improve-employment-and-earnings-young-people
- ILO / World Bank, *The Impact of Active Labour Market Programmes on Youth* (29 April 2026), DOI 10.54394/00034312: https://www.ilo.org/publications/impact-active-labour-market-programmes-youth
- 3ie / Campbell, *Interventions to improve the labour market outcomes of youth* (systematic review): https://www.3ieimpact.org/evidence-hub/publications/systematic-reviews/interventions-improve-labour-market-outcomes-youth

## Recommendation to Worker D

If Worker C verifies the cost medians, selected nature of the cost-benefit evidence, and implementation qualifiers, route the next P07 exploration slot to a **study-level LMIC employment-services versus entrepreneurship extraction**, not another global meta-summary. Require the minimum decision table above before any UCT-vs-ALMP or cross-modality scalar ranking.

This note changes allocation, not governance, and makes no canonical registry change.