# P04 — Housing and human habitat

## Why this problem matters

Housing is simultaneously shelter, a major household cost, a source of physical and environmental exposure, a platform for access to work and services, and a determinant of practical security and autonomy. HumanityAI therefore treats housing as multidimensional: adequacy, affordability, tenure security, crowding, location, infrastructure, accessibility, and exposure to hazards cannot be reduced to one global score without losing important distinctions.

## Current baseline

Canonical indicator [`I0007`](../../data/indicators.json) records UN-Habitat's 2026 global estimate that **up to 3.4 billion people lack access to secure, safe, and adequate housing**. The estimate includes more than 1 billion people living in informal settlements and slums.

The phrase **“up to”** matters. This is a broad global estimate spanning overlapping forms of housing inadequacy rather than a census of one precisely defined condition. Tenure insecurity, overcrowding, affordability problems, informality, environmental hazards, and inadequate services can overlap within the same household, so the figure should not be added to homelessness, displacement, or slum-population counts.

Source: UN-Habitat, *World Cities Report 2026: The Global Housing Crisis — Pathways to Action*.

A related cross-cutting baseline, [`I0006`](../../data/indicators.json), records UNHCR's estimate of **117.8 million forcibly displaced people at the end of 2025**. Displacement is not equivalent to housing inadequacy, and many displaced people are counted within other vulnerability measures, but it identifies a population for whom shelter, tenure, location, rights, and return or resettlement options can be unusually consequential.

Source: UNHCR, *Global Trends 2025*.

## What current intervention evidence says

HumanityAI currently has **no canonical P04 intervention-effectiveness record**. That absence is decision-relevant. A large housing burden does not by itself establish which interventions—housing supply reform, rental assistance, social housing, homelessness programs, upgrading informal settlements, tenure formalization, housing-first models, infrastructure investment, or relocation support—produce the best outcomes in particular settings.

Until comparative evidence is added, this brief deliberately does not infer effectiveness from program existence, construction volume, units funded, people enrolled, or policy adoption.

## Existing infrastructure HumanityAI should reuse

- [`RSC0003`](../../data/resources.json), the **Open Referral Human Services Data Specification**, provides a machine-readable standard for describing health, human, and social services. It can help interoperably represent housing and shelter services, but it does not guarantee that service listings are current, complete, high-quality, or available to a particular person.
- [`RSC0005`](../../data/resources.json), the **Humanitarian Data Exchange**, provides crisis and humanitarian datasets that can support context-specific analysis of displacement, shelter needs, hazards, and response activity. Dataset presence does not establish authority or intervention effectiveness.
- [`RSC0002`](../../data/resources.json), **OpenFisca**, can model tax-and-benefit rules where housing allowances, benefits, or eligibility systems are represented. Such simulations describe rules and distributional mechanics; they do not by themselves establish behavioral, supply-side, health, or long-run causal effects.

These resources are reusable infrastructure, not evidence that a housing policy works.

## Decision-useful distinctions

A useful housing analysis should keep at least six questions separate:

1. **Adequacy:** Is housing physically safe, uncrowded, accessible, and connected to essential services?
2. **Affordability:** What share of resources is required for housing, and what necessities are crowded out by housing costs?
3. **Security and rights:** Can people remain in their homes without arbitrary eviction, coercion, discrimination, or unsafe tenure arrangements?
4. **Location and opportunity:** Does housing provide practical access to work, education, healthcare, social networks, transit, and environmental quality?
5. **Intervention effects:** Does a policy improve final outcomes rather than merely increase units, spending, enrollment, permits, or administrative activity?
6. **Distribution and spillovers:** Who gains, who is displaced or excluded, and how do supply responses, land values, neighborhood change, and public costs alter the overall effect?

## Major evidence gaps

High-value next work includes:

- adding complementary global baselines for homelessness, severe housing-cost burden, overcrowding, tenure insecurity, and housing-service deficits while explicitly handling overlap;
- synthesizing strong causal evidence on homelessness and housing-stability interventions, including null and heterogeneous findings;
- separating demand-side assistance from supply-side and land-use interventions rather than treating “housing policy” as one intervention class;
- adding evidence on informal-settlement upgrading, tenure reform, climate resilience, and infrastructure quality in lower-income settings;
- measuring outcomes beyond housing status, including health, safety, earnings, schooling, mobility, community ties, autonomy, and displacement;
- adding credible cost and cost-effectiveness evidence where comparable.

## What this brief does not establish

This brief does **not** rank housing against other HumanityAI problem categories, recommend a specific housing policy, claim that the 3.4 billion estimate represents unique non-overlapping people across every housing deficit, or infer effectiveness from the existence of a service, platform, benefit, or housing program. It summarizes current canonical records and makes the intervention-evidence gap explicit.