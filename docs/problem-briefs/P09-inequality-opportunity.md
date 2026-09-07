# P09 — Inequality and unequal access to opportunity

## Why this problem matters

Inequality is not one quantity. Income dispersion, wealth concentration, unequal access to education and healthcare, geographic opportunity, discrimination, political power, exposure to risk, and intergenerational mobility can move differently and have different causes and remedies. HumanityAI therefore treats inequality as a family of distributional questions rather than a single score to minimize.

## Current baseline

Canonical indicator [`I0011`](../../data/indicators.json) records the World Bank's classification of **52 countries as having high within-country inequality in 2022**, using a Gini index above 40 and each country's most recent available household survey.

This is useful but narrow. The threshold is a policy indicator rather than a natural dividing line; survey concepts and vintages differ; 51 countries' 2022 classifications relied on household surveys more than five years old; and a country count gives the same weight to countries of very different population sizes. Most importantly, an income-or-consumption Gini does not directly measure wealth, political power, discrimination, social mobility, health, education, or access to technology.

Source: World Bank, *Inside the World Bank’s new inequality indicator: The number of countries with high inequality* (2024), using the Poverty and Inequality Platform.

## What current intervention evidence says

HumanityAI currently has **no canonical intervention-effectiveness record specific to P09**. Some evidence records in neighboring categories concern poverty, employment, education, or health, but positive average effects in those domains should not automatically be interpreted as reductions in inequality. Distribution depends on who receives an intervention, baseline conditions, take-up, financing, indirect effects, and who bears costs.

Accordingly, this brief does not infer that a policy reduces inequality merely because it raises average income, increases service access, or benefits a disadvantaged subgroup. Distributional claims require explicit distributional evidence.

## Existing infrastructure HumanityAI should reuse

- [`RSC0004`](../../data/resources.json), the **World Bank Poverty and Inequality Platform**, provides internationally comparable poverty and inequality data, including Gini and income-share measures. HumanityAI should reuse this infrastructure rather than recreate a global household-distribution database.
- [`RSC0002`](../../data/resources.json), **OpenFisca**, is an open-source rules-as-code engine for tax and benefit systems. It can support static distributional and eligibility simulations where jurisdictional rules are maintained, but those simulations do not themselves establish behavioral responses, incidence, long-run growth effects, or welfare changes.
- Other canonical records across poverty, health, education, housing, work, rights, and technology can provide inputs to opportunity analysis, but cross-domain differences should not be mechanically collapsed into a convenience composite.

These resources support measurement and simulation; they are not evidence that a particular redistributive policy is effective or desirable.

## Decision-useful distinctions

A useful inequality analysis should keep at least six questions separate:

1. **Inequality of what?** Income, consumption, wealth, opportunity, health, education, rights, time, security, political influence, and access to technology are distinct distributions.
2. **Between whom?** Global, between-country, within-country, regional, demographic, class, gender, disability, race/ethnicity, and intergenerational comparisons answer different questions.
3. **Level versus mobility:** A society can have substantial outcome inequality while allowing high mobility, or lower measured inequality with persistent barriers to movement and opportunity.
4. **Average gains versus distribution:** An intervention can improve mean outcomes while widening gaps, or reduce gaps because higher-burden groups gain more. Both effects should be reported.
5. **Absolute versus relative deprivation:** Reducing extreme deprivation can be valuable even if a relative inequality metric changes little; conversely, strong average growth can coexist with exclusion or concentration of gains.
6. **Rights and process:** Distributional outcomes do not erase questions about consent, discrimination, administrative burden, property rights, political capture, or whether people retain meaningful agency.

## Major evidence gaps

High-value next work includes:

- adding a global wealth-concentration baseline from a defensible source and explicitly separating it from household income/consumption inequality;
- adding opportunity or intergenerational-mobility measures where cross-country comparability is strong enough to justify headline use;
- documenting distributional effects of interventions already present in HumanityAI rather than reporting only average treatment effects;
- synthesizing strong evidence on tax-benefit reforms, early-childhood interventions, education access, labor-market policies, and other mechanisms that plausibly affect opportunity, including behavioral and general-equilibrium limitations;
- measuring administrative burden, exclusion error, discrimination, and unequal take-up where they change who actually benefits;
- independently reproducing the World Bank high-inequality country count and testing sensitivity to Gini threshold, survey vintage, population weighting, and income-versus-consumption concepts.

## What this brief does not establish

This brief does **not** claim that all inequality is harmful, identify one optimal distribution, rank countries by a single normative score, or recommend a particular redistribution policy. It also does not treat the count of 52 high-inequality countries as a complete measure of global inequality. It summarizes HumanityAI's current canonical baseline, identifies reusable measurement infrastructure, and makes the lack of P09-specific causal intervention evidence explicit.