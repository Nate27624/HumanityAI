# P11 research note — household energy-demand interventions

**Reviewed:** 2026-09-07  
**Status:** candidate evidence for independent review; not yet a canonical `data/evidence.json` record

## Why this matters

The new P11 problem brief correctly emphasizes that adoption or technological plausibility is not the same as demonstrated climate outcomes. A recent living systematic review provides unusually broad experimental and quasi-experimental evidence on a different mitigation lever: behavioral, informational, and monetary interventions intended to reduce household energy consumption.

## Main finding

Khanna et al. (2025), a living systematic review and network meta-analysis, screened more than 109,000 potentially relevant records and identified 213 relevant studies. Meta-analysis used 192 studies covering 40 countries and approximately 6.53 million households. Across behavioral, information, and monetary interventions, the authors estimate an overall effect of Cohen's d = 0.22, falling to 0.13 after adjustment for possible small-study effects. They translate the pooled effect to roughly a **4–6% reduction in household energy consumption**.

The review reports that monetary incentives have the largest average effect, followed by some behavioral/motivational and information interventions, and that some combinations outperform individual approaches.

Primary source: Tarun M. Khanna et al., *Behavioral, Information, and Monetary Interventions to Reduce Energy Consumption in Households: A Living Systematic Review and Network Meta-Analysis*, Campbell Systematic Reviews (published online 4 November 2025), DOI: https://doi.org/10.1002/cl2.70070

## Qualification / contrary evidence

This is useful evidence **against both overclaiming and dismissing demand-side behavior programs**:

- The pooled effect is positive but small-to-moderate; these interventions are not evidence for a stand-alone solution to P11.
- Adjustment for possible small-study effects materially reduces the standardized estimate from 0.22 to 0.13. Selection/publication effects therefore matter to interpretation.
- The review explicitly reports methodological weaknesses and varying study quality across the evidence base.
- Intervention categories are heterogeneous. Monetary incentives, feedback, social comparison, motivation, and information should not be treated as one interchangeable policy.
- Energy-consumption reduction is an intermediate outcome for climate mitigation. The review does not establish a uniform greenhouse-gas reduction because emissions consequences depend on energy source, timing, rebound, and context.
- Average effects across 40 countries do not establish equal effectiveness, distributional impact, durability, or cost-effectiveness in a particular jurisdiction.

A related economics review on energy efficiency in developing countries warns that rebound can make realized energy savings smaller than engineering projections and that rebound size varies substantially by context. This is not a direct contradiction of the Khanna review—the interventions and estimands differ—but it reinforces the need to keep observed consumption, projected savings, welfare gains, and emissions outcomes distinct.

Context source: Kenneth Gillingham, Amelia Keyes, and Karen Palmer, *The Economics of Energy Efficiency in Developing Countries*, Review of Environmental Economics and Policy 15(2), 2021, DOI: https://doi.org/10.1086/715606

## Proposed canonical interpretation

If later integrated into `data/evidence.json`, the defensible claim is approximately:

> Across a large international experimental and quasi-experimental evidence base, behavioral, informational, and monetary household interventions reduce energy consumption on average, but the effect is modest and smaller after adjustment for possible small-study bias; effectiveness varies by intervention type and this evidence alone does not establish emissions reductions, durability, distributional effects, or cost-effectiveness.

Suggested status: `mixed` rather than simply `supported`, because the positive pooled effect coexists with material small-study adjustment, methodological weaknesses, and unresolved translation from energy use to climate outcomes.

## Decision relevance

This evidence changes the P11 action space modestly: household demand interventions appear empirically real enough to remain in the portfolio, but their likely role is **complementary**, not a substitute for structural decarbonization or adaptation. A future prioritization exercise should compare marginal cost per durable unit of energy/emissions reduction against technology, pricing, infrastructure, and regulatory alternatives rather than ranking interventions by statistical significance alone.

## Falsifiable next checks

1. Verify whether effect persistence differs materially between short and long follow-up periods in the review's supplementary results.
2. Extract intervention-specific effect estimates and uncertainty before comparing monetary versus non-monetary approaches.
3. Look for direct emissions outcomes or credible energy-to-emissions mappings rather than assuming a fixed conversion.
4. Search for cost-effectiveness evidence and distributional effects, especially for monetary incentives.
5. Revisit this living review after its next update; its design is explicitly intended to incorporate newer studies.