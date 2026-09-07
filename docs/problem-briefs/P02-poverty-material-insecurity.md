# P02 — Poverty and material insecurity

## Why this problem matters

Material insecurity is broader than any one poverty threshold. It includes inadequate income or consumption, unstable access to food and essentials, exposure to shocks, inability to absorb emergencies, and limited practical access to services and opportunities. HumanityAI therefore treats monetary poverty as an important baseline dimension rather than a complete measure of deprivation or human capability.

## Current baseline

Canonical indicator [`I0001`](../../data/indicators.json) records the World Bank's March 2026 estimate that **847 million people lived below the $3.00/day international extreme-poverty line in 2024**. The same source nowcasts a global extreme-poverty rate of 10.0% for 2026.

This figure should be interpreted carefully. It is an estimate rather than a census; the international line uses 2021 purchasing-power parities for global comparison; and national poverty lines are generally more appropriate for country-level policy. Monetary poverty also omits dimensions such as housing quality, health, security, disability, unpaid care burdens, access to infrastructure, and resilience to shocks.

Source: World Bank, *March 2026 global poverty update from the World Bank: New data and updated poverty numbers*.

## What current intervention evidence says

### Unconditional cash transfers — promising across several outcomes, but not universally positive

Canonical evidence [`E0001`](../../data/evidence.json) summarizes a 2022 Cochrane systematic review of unconditional cash transfers in low- and middle-income countries. Across 34 studies and more than 1.1 million participants, transfers probably or may improve several welfare outcomes, including food security, dietary diversity, school attendance, and the likelihood of not being extremely poor.

The same review is an important warning against collapsing intervention evidence into a simple “works” label. Effects differ by outcome and context, most included studies had high overall risk of bias, and a summary measure of health-service use may change little or not at all. Evidence comparing unconditional with conditional transfers was also very uncertain. This record does not establish that every cash-transfer design is effective, that transfers are always cost-effective, or that HumanityAI has a comparative advantage in implementing them.

Source: Cochrane, *Unconditional cash transfers for reducing poverty and vulnerabilities: effect on use of health services and health outcomes in low- and middle-income countries* (2022).

### Medical-financial partnerships — insufficient evidence for robust outcome claims

Canonical evidence [`E0002`](../../data/evidence.json) covers a 2024 Campbell systematic review of medical-financial partnerships for lower-income people in U.S. healthcare settings. Only four studies met the review criteria. Financial effects were generally small and non-significant, while one study reported improvements in appointment attendance and vaccination adherence.

The useful conclusion is uncertainty rather than failure. The evidence base is small, methodologically weak, and concentrated in pediatric healthcare settings, with heterogeneous services such as tax preparation, financial coaching, and counseling. Current evidence is therefore insufficient to conclude that this intervention class reliably improves financial or health outcomes.

Source: Campbell Collaboration, *Medical-financial partnerships for improving financial and medical outcomes for lower-income Americans: A systematic review* (2024).

## Existing infrastructure HumanityAI should reuse

- [`RSC0004`](../../data/resources.json), the **World Bank Poverty and Inequality Platform**, provides internationally comparable poverty and inequality data and an API. HumanityAI should generally reuse this statistical infrastructure instead of constructing a parallel global poverty dataset.
- [`RSC0002`](../../data/resources.json), **OpenFisca**, provides an open-source rules-as-code engine for tax and benefit systems. It may support eligibility, distributional, and reform simulations, but simulation accuracy depends on jurisdiction-specific rules and does not itself establish behavioral or long-run causal effects.
- [`RSC0005`](../../data/resources.json), the **Humanitarian Data Exchange**, provides a large discovery and API layer for crisis-specific humanitarian data. Dataset presence on HDX does not by itself establish quality, authority, or intervention effectiveness.

These resources are infrastructure, not evidence that a particular anti-poverty policy works.

## Decision-useful distinctions

A useful poverty analysis should keep at least five questions separate:

1. **How many people face deprivation, and by which definition?** Extreme-poverty headcounts answer only one part of this.
2. **Which interventions change final welfare outcomes?** Program existence, eligibility, enrollment, or money distributed are not enough.
3. **For whom and under what conditions do effects differ?** Transfer design, baseline services, household composition, local prices, administrative burden, and shock exposure can materially change outcomes.
4. **What is the cost-effectiveness and opportunity cost?** Positive effects do not imply that an intervention is the best use of marginal resources.
5. **How are rights, dignity, autonomy, and distribution affected?** Administrative surveillance, conditionality, exclusion error, stigma, accessibility, and control over resources can matter even when average monetary outcomes improve.

## Major evidence gaps

Current HumanityAI coverage is still thin. High-value next steps include:

- adding complementary baselines for food insecurity, vulnerability to shocks, multidimensional deprivation, and severe material hardship without double-counting overlapping populations;
- comparing intervention classes such as cash transfers, social insurance, benefits-access simplification, housing or utility support, and livelihood interventions using strong causal evidence;
- adding cost and cost-effectiveness evidence where credible and comparable;
- preserving heterogeneous effects by gender, disability, household structure, geography, conflict exposure, and baseline income rather than relying only on global averages;
- independently reproducing the World Bank poverty estimate and documenting sensitivity to poverty-line and PPP choices.

## What this brief does not establish

This brief does **not** rank poverty against other HumanityAI problem categories, recommend a specific policy, imply that cash transfers solve all forms of material insecurity, or claim that any listed platform or organization is effective merely because it exists. It summarizes current canonical records and exposes the next decisions that require stronger evidence.