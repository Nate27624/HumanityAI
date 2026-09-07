# P11 research note — household energy-demand interventions

**Reviewed:** 2026-09-07  
**Status:** candidate evidence for independent review; not yet a canonical `data/evidence.json` record

## Why this matters

P11 needs intervention evidence, not merely climate-risk baselines or inventories of plausible solutions. A 2025 living systematic review and network meta-analysis provides a broad international evidence base on behavioral, informational, and monetary interventions intended to reduce household energy consumption.

## Main finding

Khanna et al. (2025) identified 213 relevant studies and meta-analyzed 192 studies comprising 663 effect sizes from 40 countries and 6,528,923 households. The pooled average effect was Cohen's d = 0.22 (95% CI 0.18–0.26). After PEESE adjustment for potential small-study/publication bias, the estimate fell to d = 0.13 (95% CI 0.09–0.17).

For observations that directly reported percentage energy changes, the authors estimated an average reduction of 6.6%, falling to 4.6% after the publication-bias adjustment. Their practical summary is therefore roughly a **4–6% reduction in household energy consumption on average**, with monetary incentives producing the largest average effect and some combinations outperforming single interventions.

Primary source: Tarun M. Khanna et al., *Behavioral, Information, and Monetary Interventions to Reduce Energy Consumption in Households: A Living Systematic Review and Network Meta-Analysis*, Campbell Systematic Reviews 21(4), e70070 (first published 4 November 2025). DOI: https://doi.org/10.1002/cl2.70070

## Qualification and negative evidence

The evidence is useful precisely because it argues against both overclaiming and dismissing demand-side programs:

- The average effect is positive, but modest; it does not establish a stand-alone solution to climate mitigation.
- The reduction from d = 0.22 to d = 0.13 after small-study-bias adjustment is material and should remain visible in any downstream claim.
- Study quality varies, and the review reports methodological weaknesses. In its risk-of-bias sensitivity analysis, higher-risk studies tended to show larger effects than lower-risk studies.
- The evidence base mixes experimental and quasi-experimental designs and therefore should not be summarized as one uniform causal estimate.
- Intervention categories are heterogeneous. Monetary incentives, feedback, social comparison, motivation and information are not interchangeable treatments.
- Energy consumption is an intermediate outcome. A decrease in household energy use is not automatically an equal decrease in greenhouse-gas emissions because emissions depend on the energy source, timing and system context.
- The review does not establish cost-effectiveness, welfare effects or equitable distribution of benefits and burdens across jurisdictions.
- Persistence remains uncertain. The review explicitly notes that few studies conduct follow-up measurement, even though follow-up duration is coded when available.
- Network comparisons are limited by a largely star-shaped evidence network: many studies compare an intervention with control rather than directly comparing competing interventions.

## Proposed canonical interpretation

If later integrated into `data/evidence.json`, a defensible claim would be:

> Across a large international evidence base, behavioral, informational and monetary household interventions are associated with lower household energy consumption on average, but estimated effects are modest and materially smaller after adjustment for possible small-study bias. Effects differ by intervention type, study quality and context, and the evidence alone does not establish durable emissions reductions, cost-effectiveness, distributional effects or one uniform causal effect across the full evidence base.

Suggested status: `mixed` rather than simply `supported`. The positive pooled result is credible enough to change the action space, but the bias adjustment, study-quality gradient, heterogeneous designs, sparse follow-up evidence and incomplete translation from energy use to climate outcomes materially qualify it.

## Decision relevance

Household demand interventions appear worth retaining as **complementary** mitigation options. The evidence does not support treating them as substitutes for structural decarbonization or adaptation. Future prioritization should compare marginal cost per durable unit of energy or emissions reduction against pricing, technology, infrastructure and regulatory alternatives rather than rank interventions by statistical significance alone.

## Falsifiable next checks

1. Extract intervention-specific estimates and uncertainty before claiming monetary approaches outperform non-monetary approaches in a decision context.
2. Test whether effects differ materially by study risk of bias and follow-up duration.
3. Look for direct emissions outcomes or credible energy-to-emissions mappings rather than assuming a fixed conversion.
4. Search for cost-effectiveness and distributional evidence, especially for monetary incentives.
5. Revisit the living review after its next update and record whether the pooled estimate or bias adjustment changes materially.