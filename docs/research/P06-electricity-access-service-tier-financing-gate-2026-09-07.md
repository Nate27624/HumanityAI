# P06 exploration — electricity access service-tier and financing gate

**Reviewed:** 2026-09-07  
**Status:** decision-bearing exploration candidate; requires independent Worker C verification before Worker D integration  
**Assignment:** Worker D cross-domain exploration while P07 production is held pending review

## Decision question

When HumanityAI allocates additional P06 compute, should it continue asking whether decentralized/off-grid electrification is effective in aggregate, or should it first route by **required service tier, affordability, and financing architecture**?

## Short answer

**Route first by service tier and affordability.** Existing evidence is already strong enough to say that decentralized electricity can expand access and can improve some socioeconomic outcomes, but it is not strong enough to treat “off-grid electricity” as one portable intervention. The most decision-relevant bottleneck is whether the intended users can afford the level of service required and whether a project can finance that service without degrading quality, excluding poorer households, or relying on unsustainable subsidy assumptions.

## Evidence that changes the routing decision

### 1. The remaining access gap is concentrated where decentralized systems matter, but the gap is still large

The 2026 *Tracking SDG7* report from the IEA, World Bank, IRENA, UN DESA and WHO reports that **655 million people lacked electricity access in 2024**, with **563 million in sub-Saharan Africa**. The same report notes that solar home systems commonly provide partial Tier 1, Tier 1, or Tier 2 access, while mini-grids and grid electricity can support higher tiers. This is an empirical pattern, not a technology-to-tier taxonomy: the Multi-Tier Framework evaluates realized service attributes across capacity, availability, reliability, quality, affordability, legality, and safety, so future comparisons must measure the service actually delivered rather than infer tier from the technology label alone.

Source: IEA et al., *Tracking SDG7: The Energy Progress Report, 2026*, published 24 June 2026.  
https://www.iea.org/reports/tracking-sdg7-the-energy-progress-report-2026

**Decision implication:** a connection count is not a common outcome denominator. A low-tier household system and a higher-tier mini-grid/grid connection can be different products with different productive-use capacity. Future comparisons should not rank them by cost per “connection” without service normalization, and should not assign service tier solely from whether the pathway is SHS, mini-grid, or grid.

### 2. Off-grid solar has large least-cost reach, but household affordability is a binding adoption constraint

The World Bank/ESMAP 2024 *Off-Grid Solar Market Trends Report* estimates that off-grid solar would be the least-cost route for roughly **398 million people (41% of the approximately 1.03 billion people who need to be electrified between 2024 and 2030 to achieve universal access, accounting for population growth)**. This is not the denominator of people projected to remain unelectrified in 2030 under the current trajectory. The report also estimates that realizing this off-grid-solar potential requires roughly **$21 billion** of investment.

However, the same report finds that only **22% of households without electricity can afford a Tier 1 solar energy kit on PAYG** when affordability is defined as spending no more than 5% of household income. Another 27% could afford it only “at a stretch” using a 10% threshold. For Tier 2 PAYG products, only **1%** of households are classified as able to afford them under the 5% threshold.

Sources:  
- World Bank/ESMAP, *Off-Grid Solar Market Trends Report 2024*, published 8 October 2024.  
  https://www.esmap.org/Off-Grid_Solar_Market_Trends_Report_2024  
- Affordability chapter: https://mtr.esmap.org/chapter-03-affordability-of-OGS

**Decision implication:** “least-cost technology” does not imply “adoptable product.” The affordability constraint becomes more severe as the desired service tier rises.

### 3. Financing cost and subsidy design can move adoption materially, but no single financing lever closes the gap

The IEA's 2025 *Financing Electricity Access in Africa* analysis estimates that around **220 million people in sub-Saharan Africa (about 40% of those without access)** would be unable to afford its basic electricity bundle at prevailing income and subsidy levels, and around **400 million** would be unable to afford its higher “essential” bundle. It estimates an additional **$2–10 billion per year** would be needed to close the affordability gap, depending on service level.

The IEA further estimates that electricity-access projects face a cost of capital roughly three to four times that of grid projects in advanced economies. Reducing financing costs toward advanced-economy levels could reduce project costs by roughly **15–25%** and make basic service affordable to about **40 million additional people**. It also models supply-side grants covering 30% of mini-grid capital/operating expenditure and 50% for solar-home-system costs as materially improving affordability, while explicitly concluding that **demand-side support would still be necessary for the poorest households**.

Source: IEA, *Financing Electricity Access in Africa*, 2025, especially “Beyond new connections” and executive summary.  
https://www.iea.org/reports/financing-electricity-access-in-africa/beyond-new-connections

**Decision implication:** future P06 work should compare financing architectures, not just generation technologies. Cost of capital, developer subsidy, consumer subsidy, payment terms, and service tier are first-order variables.

### 4. Existing HumanityAI effectiveness evidence argues against using downstream welfare effects as a shortcut

HumanityAI record E0003 summarizes a 2025 Campbell systematic review of 47 rigorous evaluations of off-grid electrification in low- and middle-income countries. The review found reduced kerosene use and small positive average effects on income and women's decision-making, but no significant effects on school attendance or test scores, no statistically significant air-quality effect in the small available evidence base, sparse CO2 evidence, and substantial heterogeneity and risk of bias.

Source already represented canonically as E0003; underlying review: Campbell Collaboration, *Improving Energy Access, Climate and Socio-Economic Outcomes Through Off-Grid Electrification Technologies: A Systematic Review* (2025).

**Decision implication:** outcome evidence does not justify a generic “off-grid works” scalar. Service quality, use case, affordability and implementation remain necessary decision variables.

## Proposed routing rule

Before spending another P06 slot on technology-level effectiveness or cost-effectiveness, require the candidate decision to specify:

1. **Target service tier / use case** — lighting and phone charging, household appliances, productive use, public facility, or higher-reliability service, defined by realized service attributes rather than technology label.
2. **Population/location** — density, remoteness, fragility/conflict exposure, and proximity to existing grid infrastructure.
3. **Affordability threshold** — expected user payment burden and whether the analysis assumes 5%, 10%, or another explicit household-income threshold.
4. **Financing architecture** — commercial capital, concessional capital, developer grant, demand-side subsidy, PAYG financing, public provision, or combination.
5. **Outcome denominator** — cost per connection is insufficient unless service tier is comparable; prefer cost per user reaching a defined service level, plus persistence/reliability where available.
6. **Distributional/adoption risk** — whether the financing model selectively reaches households already able to pay while leaving the poorest behind.

## START / MORE / LESS / STOP

**START:** service-tier-normalized comparisons of solar home systems, mini-grids, and grid extension in one or two high-deficit country contexts where geospatial least-cost plans and financing data are public.

**MORE:** study-level extraction of realized tariffs/payment burden, connection uptake after subsidy offers, default/disconnection rates, reliability, productive-use adoption, and durability of access after project support ends.

**LESS:** global statements that one electrification modality is “most cost-effective” without specifying service tier, geography, financing cost, and affordability assumptions.

**STOP:** scalar rankings based on cost per connection alone; treating technology labels as fixed service-tier labels; assuming that least-cost supply automatically produces household adoption; or inferring broad welfare gains from connection counts.

## Kill test

Do **not** allocate multiple new P06 slots to a full cross-country modality ranking unless at least two candidate pathways can be compared on a common service tier and outcome horizon with source-grounded financing and affordability assumptions.

If those comparable inputs cannot be obtained, the higher-value next step is a **country-level binding-constraint case study** rather than a global ranking.

## Decision delta for Worker D

This shifts the P06 question from **“Which electricity-access technology works best?”** to **“For a required service level in a specific access context, which financing-and-technology package is affordable, adoptable, reliable and durable?”**

That change should redirect multiple future slots away from generic effectiveness accumulation and toward service-normalized, country-level decision models.

**Confidence:** high that service tier and affordability are necessary gates; moderate-high that financing architecture is a first-order tractability constraint; moderate on portability of the quantitative affordability/subsidy estimates outside the IEA/ESMAP modeled contexts.

## Uncertainty and limitations

- The ESMAP affordability estimates are modeled global estimates and depend on income data, product prices, PAYG terms, and the chosen 5%/10% affordability thresholds.
- The ESMAP 398 million / 41% figure uses the population requiring electrification between 2024 and 2030 to achieve universal access, including population growth; it must not be conflated with the separate current-trajectory projection for how many people would still lack access in 2030.
- The IEA financing results are scenario/model outputs for Africa, not causal estimates of what every subsidy or cheaper-capital program will achieve in practice.
- The $21 billion OGS investment requirement is a sector-level modeled requirement, not a portable unit cost and should not be divided into a universal cost-per-person estimate.
- Service tiers capture multidimensional realized electricity service and should not be inferred solely from grid, mini-grid, or SHS labels; they also do not fully represent productive-use value or household welfare.
- Technology choice is geography-sensitive. Grid extension, mini-grids, and stand-alone systems can be complements over time rather than permanent substitutes.

## Recommended next assignment

If Worker D allocates another P06 exploration slot, choose **one high-deficit country with a public least-cost electrification plan** and compare no more than two pathways at a common service tier, including tariff/payment burden, subsidy design, financing cost, uptake, reliability and persistence. Abandon the comparison if those common denominators cannot be sourced.
