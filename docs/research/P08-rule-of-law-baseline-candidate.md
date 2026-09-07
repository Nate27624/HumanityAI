# P08 complementary baseline candidate: 2025 rule-of-law decline

## Why this fills a real gap

HumanityAI's P08 baseline currently includes regime classification and forced-displacement context, but those do not directly measure whether laws, institutions, checks on power, rights protections, regulatory enforcement, and justice systems function in practice. A complementary rule-of-law measure adds a distinct institutional-quality dimension rather than another democracy/autocracy count.

## Candidate headline

**68% of countries and jurisdictions covered by the World Justice Project Rule of Law Index experienced a decline in their overall rule-of-law score from 2024 to 2025.** The 2025 Index covers 143 countries and jurisdictions representing about 95% of the world's population. WJP reports that 32% improved and 68% declined; the mean overall score change across the covered countries was approximately -0.5%.

This is a **country-share trend indicator**, not a population share and not a claim that 68% of people experienced the same deterioration.

## Primary sources

1. **World Justice Project — WJP Rule of Law Index 2025 Global Press Release**  
   Published: 2025-10-28  
   https://worldjusticeproject.org/news/wjp-rule-law-index-2025-global-press-release

   Directly reports that 68% of covered countries declined in rule of law in 2025, up from 57% in 2024; describes coverage of 143 countries/jurisdictions and roughly 95% of the world's population; and reports more than 215,000 household surveys and 4,100 legal-practitioner/expert surveys.

2. **World Justice Project — Rule of Law Index 2025 report**  
   https://worldjusticeproject.org/rule-of-law-index/downloads/WJPIndex2025.pdf

   The report's scores-and-rankings section reports 68% declining versus 32% improving from 2024 to 2025 and an average overall score decline of about 0.5%.

3. **World Justice Project — 2025 Index Methodology**  
   https://worldjusticeproject.org/rule-of-law-index/downloads/Index-Methodology-2025.pdf

   The methodology states that the Index uses more than 550 variables from assessments of over 215,000 households and 4,100 legal practitioners/experts across 143 countries and jurisdictions. It aggregates eight factors and 44 sub-factors, drawing on a General Population Poll and Qualified Respondents' Questionnaires.

Sources accessed 2026-09-07.

## What the Index measures

The overall WJP score aggregates eight dimensions:

- Constraints on Government Powers
- Absence of Corruption
- Open Government
- Fundamental Rights
- Order and Security
- Regulatory Enforcement
- Civil Justice
- Criminal Justice

Scores range from 0 to 1, with higher values representing stronger adherence to WJP's rule-of-law framework. The index combines experience- and perception-based survey questions from households with assessments from in-country legal practitioners and experts.

## Important 2025 context

The deterioration was not confined to one subcomponent. WJP reports that indicators related to independent oversight, legislative and judicial checks on executive power, freedom of expression, freedom of assembly/association, civic participation, and civil justice declined in majorities of covered countries. This supports interpreting the headline as a broad institutional trend, while still avoiding the claim that every dimension declined in every country.

The 2025 result also reverses the apparent moderation seen in 2024: WJP reported 57% of countries declining in 2024, versus 68% in 2025. That year-to-year change is useful context but should not be overinterpreted as a precise causal effect of any single political or economic driver.

## Proposed machine-readable interpretation

If independently verified and promoted, a defensible indicator would look conceptually like:

- **problem_ids:** `P08`
- **name:** Countries/jurisdictions with declining overall rule-of-law score
- **value:** `68`
- **unit:** `percent of covered countries/jurisdictions`
- **value_type:** `observed_from_index`
- **reference_period:** `2024 to 2025`
- **geography:** `143 countries and jurisdictions; ~95% of world population represented by coverage`
- **source:** World Justice Project, Rule of Law Index 2025

Do not encode this as "68% of the world" or "68% of people".

## Limitations and interpretation guardrails

1. **Country share is not population share.** Every covered country/jurisdiction contributes one improving/declining classification regardless of population size.
2. **Coverage is broad but not universal.** WJP states that the 143 covered jurisdictions represent about 95% of the world's population; uncovered places can differ systematically.
3. **The index is a measurement framework, not ground truth.** WJP operationalizes a contested multidimensional concept using its own definitions, survey instruments, weighting, and aggregation choices.
4. **Perceptions and experiences are both inputs.** Some survey responses measure lived experience while others measure perceptions; these may be affected by information environments and expectations as well as institutional performance.
5. **Composite scores can hide offsetting movement.** An overall decline may combine worsening in some factors with improvement in others. HumanityAI should preserve factor-level context where relevant instead of treating the overall score as a complete description of institutional quality.
6. **Annual changes can be small.** The average overall score decline was about 0.5%; a large share of countries moving downward does not imply uniformly large deterioration.
7. **Comparability can be affected by survey and coverage changes.** The methodology has evolved toward nationally representative population polling, and Qatar entered the Index in 2025. Longitudinal interpretation should use WJP's own comparable annual series rather than naively recomputing across incompatible vintages.
8. **This is not intervention evidence.** The indicator describes institutional conditions and change; it does not show which governance reforms improve rule of law, whether they are cost-effective, or whether HumanityAI has comparative advantage in advocating them.

## Contradictory / qualifying evidence

The 2024 WJP release had reported that the global rule-of-law recession appeared to be slowing: 57% of countries declined, a smaller share than in prior years, and some criminal-justice and corruption measures improved. The 2025 result therefore should not be narrated as a simple monotonic collapse. The latest year shows renewed broad deterioration after a period in which the decline had moderated.

Alternative governance datasets use different concepts and coding strategies. V-Dem, Worldwide Governance Indicators, Freedom House, and other frameworks can disagree about specific countries and dimensions. That disagreement is a reason to retain multiple complementary P08 indicators rather than to merge them into a single governance score.

## Recommendation

**Promote after independent reproduction.** The 68% headline is directly reported in primary WJP material, measures a P08 dimension not captured by regime labels, has broad global coverage, and carries clear limitations. A second worker should independently confirm the 68% / 143-jurisdiction / coverage claims and check whether the final canonical indicator schema prefers `estimate` or `observed` terminology before insertion into `data/indicators.json`.
