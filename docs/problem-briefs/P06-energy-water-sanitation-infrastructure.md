# P06 — Energy, water, sanitation, and essential infrastructure

## Why this problem matters

Essential infrastructure expands or constrains practical human capability. Electricity, clean cooking, water, sanitation, transport, communications, and related systems affect health, education, economic opportunity, safety, time use, and the ability to participate in modern institutions. HumanityAI should therefore treat infrastructure as a multidimensional enabling condition rather than as a single access score.

## Current baseline

Canonical indicator [`I0003`](../../data/indicators.json) records the International Energy Agency's 2025 estimate that **about 730 million people lack access to electricity** worldwide. This is an access-threshold measure, not a complete measure of energy services: it does not capture reliability, affordability, generation quality, outage frequency, or whether available power is sufficient for productive use.

Canonical indicator [`I0004`](../../data/indicators.json) records the IEA's estimate that **about 2.0 billion people lack access to clean cooking**. This is materially larger than the electricity-access gap, but the two populations overlap and must not be added together. Clean-cooking access also does not directly measure exposure intensity, household fuel stacking, affordability, reliability, or resulting morbidity.

Source for both indicators: International Energy Agency, *World Energy Outlook 2025 — Achieving access for all*.

These two records are useful energy-access baselines, but they do not yet provide adequate canonical coverage of the water, sanitation, transport, or broader infrastructure dimensions named in P06.

## What current intervention evidence says

### Off-grid electrification — some socioeconomic gains, but broad spillover claims are not established

Canonical evidence [`E0003`](../../data/evidence.json) summarizes a 2025 Campbell systematic review of 47 rigorous impact evaluations of off-grid electrification in low- and middle-income countries. The review found reduced kerosene consumption and small positive effects on income and women's decision-making. It also found a possible increase in study time.

The same review substantially qualifies broader claims. School attendance and test scores did not show significant effects, five mostly high-risk-of-bias studies examining air quality did not show a statistically significant effect, and only one included study assessed CO2 emissions. The apparent study-time benefit may also be inflated by publication bias.

This means that supplying off-grid electricity should not be treated as evidence that education, health, climate, or economic outcomes automatically improve. Effects depend on technology, service quality, local institutions, complementary assets, baseline conditions, affordability, and how households and firms can actually use the electricity.

Source: Campbell Collaboration, *Improving Energy Access, Climate and Socio-Economic Outcomes Through Off-Grid Electrification Technologies: A Systematic Review* (2025).

## Existing infrastructure HumanityAI should reuse

- [`RSC0005`](../../data/resources.json), the **Humanitarian Data Exchange (HDX)**, provides a large cross-sector discovery and API layer for crisis-context, affected-population, needs, and response datasets, including infrastructure-relevant humanitarian data. Dataset presence does not establish that a dataset is current, authoritative, complete, or suitable for a particular causal claim.
- [`RSC0003`](../../data/resources.json), the **Open Referral Human Services Data Specification (HSDS)**, provides an interoperability standard for describing services, locations, and provider organizations. It can reduce duplicated service-directory infrastructure, but a standardized listing does not establish service availability, capacity, quality, eligibility, or effectiveness.

These are reusable information infrastructures, not evidence that a particular energy, water, sanitation, or service-delivery intervention works.

## Decision-useful distinctions

A useful infrastructure analysis should keep at least six questions separate:

1. **Is nominal access available?** Household connection or technology ownership answers only this threshold question.
2. **Is the service reliable and usable?** Outages, intermittency, pressure, contamination, maintenance, latency, travel time, and service quality can make nominal access misleading.
3. **Is the service affordable?** Infrastructure can exist physically while remaining economically inaccessible or creating harmful expenditure burdens.
4. **Does access change final outcomes?** More connections, devices, pipes, roads, or service listings are intermediate outputs; health, income, learning, safety, time use, and autonomy require separate evidence.
5. **Who gains and who bears costs?** Location, gender, disability, tenancy, income, displacement status, land rights, environmental burdens, and political power can strongly affect distribution.
6. **What complementary systems are required?** Productive electricity use, safe water, sanitation, transport, and digital services often depend on maintenance capacity, institutions, finance, skills, supply chains, and other infrastructure.

## Major evidence gaps

Current HumanityAI P06 coverage is still narrow. High-value next steps include:

- adding authoritative global baselines for safely managed drinking water and sanitation, while preserving the distinction between access and service quality;
- adding measures of electricity reliability, affordability, and sufficient energy use rather than treating connection status as complete access;
- evaluating clean-cooking interventions on sustained adoption, exposure, health outcomes, affordability, and fuel stacking rather than technology distribution alone;
- adding strong intervention evidence for water, sanitation, and hygiene, including null or heterogeneous results and implementation dependence;
- comparing centralized grid expansion, distributed energy, reliability improvements, clean-cooking approaches, and other infrastructure interventions using cost and outcome evidence where comparable;
- mapping infrastructure burdens by rurality, income, gender, disability, conflict exposure, and informal-settlement status;
- adding evidence on maintenance, institutional capacity, and long-run service continuity, since installed infrastructure is not equivalent to functioning infrastructure.

## What this brief does not establish

This brief does **not** rank infrastructure against other HumanityAI problem categories, recommend a specific technology or provider, imply that electricity access automatically improves all downstream outcomes, or treat listed datasets and standards as proof of intervention effectiveness. It summarizes current canonical records, makes the present evidence limits explicit, and identifies where additional evidence would most improve P06 decision usefulness.