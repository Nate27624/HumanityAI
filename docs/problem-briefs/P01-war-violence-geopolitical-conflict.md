# P01 — War, violence, and geopolitical conflict

**Status:** early synthesis, reviewed 2026-09-07  
**Problem definition:** armed conflict, organized violence, geopolitical escalation, civilian harm, forced displacement, and the institutions and interventions that may prevent, limit, or end violence.

This brief summarizes current HumanityAI records. It is not a conflict ranking, a prediction of where war will occur next, or a recommendation for a particular military, diplomatic, humanitarian, or peacebuilding intervention.

## What the current evidence says

### Armed conflict remains geographically widespread

Indicator [`I0005`](../../data/indicators.json) records SIPRI's 2026 assessment that **49 states had active armed conflicts in 2025**. SIPRI reports that most conflicts remained internal while interstate armed conflicts increased relative to 2024.

This is a useful breadth measure, but it is not a measure of total violence. A state count gives the same unit weight to very different conflicts and does not directly capture battle deaths, civilian deaths, duration, territorial extent, escalation risk, or the number of people exposed.

Source: Stockholm International Peace Research Institute, *SIPRI Yearbook 2026 — Global trends in armed conflict*: https://www.sipri.org/yearbook/2026/02

### Forced displacement shows one major human consequence, but it overlaps several problem domains

Indicator [`I0006`](../../data/indicators.json) records UNHCR's estimate of **117.8 million forcibly displaced people worldwide at the end of 2025**, down from 123.2 million at the end of 2024.

The record is relevant to P01 because conflict and violence are major causes of displacement, but it also belongs to P04 and P08. Forced displacement includes heterogeneous causes and legal categories, so it should not be treated as a direct conflict-fatality measure or added mechanically to other affected-population counts.

A decline in the global stock of displaced people is also not automatically evidence that underlying conflicts improved: returns can occur under difficult conditions, and stock changes depend on new displacement, returns, resettlement, demographic changes, and classification.

Source: UNHCR, *Global Trends 2025* (11 June 2026): https://www.unhcr.org/global-trends

### HumanityAI already has useful conflict-data infrastructure to build on

Resource [`RSC0001`](../../data/resources.json), the **Uppsala Conflict Data Program (UCDP) Dataset Download Center**, provides structured historical and current data on organized violence, including armed conflict, battle-related deaths, non-state conflict, one-sided violence, and georeferenced events. Its machine-readable datasets and API can support reproducible trend analysis rather than relying only on prose summaries.

Resource [`RSC0005`](../../data/resources.json), the **Humanitarian Data Exchange (HDX)**, provides a broader humanitarian discovery layer containing crisis-context, affected-population, needs, and response datasets from many organizations.

Neither resource is itself evidence that a peacebuilding or humanitarian intervention works. UCDP's value is measurement; HDX's value is discovery and interoperability. Dataset presence, organizational activity, or response volume must not be confused with improved outcomes.

## What is not yet established

Current canonical HumanityAI records do **not** yet establish:

- a multidimensional global P01 baseline covering conflict incidence, intensity, civilian harm, duration, recurrence, and escalation risk;
- a canonical intervention-effectiveness record for mediation, ceasefires, peacekeeping, sanctions, deterrence, arms control, post-conflict stabilization, reconciliation, violence interruption, or other conflict-reduction approaches;
- which conflict-prevention interventions work best across different conflict types and stages;
- comparative cost-effectiveness of diplomatic, humanitarian, institutional, security, or development approaches to reducing violence;
- whether an intervention that reduces one measured form of violence shifts harm elsewhere, delays violence, increases repression, or changes who bears the risk;
- HumanityAI's comparative advantage in implementing, funding, advocating, or coordinating any conflict-related intervention.

This is therefore a **measurement-first P01 evidence base**. HumanityAI can currently describe important dimensions of the problem and identify strong data infrastructure, but it should not imply that it has already identified a best solution.

## High-value next evidence

The strongest next work should broaden measurement and then add rigorous intervention evidence rather than another near-duplicate conflict count:

1. **Conflict intensity and human harm.** Add a transparent global measure of battle-related deaths and/or civilian deaths with explicit coding definitions, uncertainty, and treatment of missing data.
2. **Conflict duration and recurrence.** Distinguish persistent conflicts, new onsets, recurrences, negotiated endings, and temporary pauses; a state-count baseline cannot show whether violence is becoming harder to end.
3. **Civilian exposure and distribution.** Measure who bears harms, including children, displaced people, minorities, aid workers, and populations facing one-sided violence, without double-counting overlapping groups.
4. **Intervention effectiveness.** Search systematic reviews, meta-analyses, natural experiments, and other strong causal evidence on mediation, peacekeeping, ceasefire design, violence-prevention programs, post-conflict institution building, and related approaches. Preserve null, adverse, and heterogeneous findings.
5. **Escalation and spillovers.** Separate local reductions in violence from interstate escalation, regional spillovers, proxy involvement, arms-race dynamics, or displacement to neighboring areas.
6. **Implementation fidelity.** Distinguish adoption or deployment of a peace agreement, mission, sanction, monitoring mechanism, or institution from whether it is implemented, complied with, legitimate, durable, and rights-respecting.
7. **Forecasting and calibration.** Add preregistered, resolvable forecasts about conflict onset, continuation, or de-escalation only where resolution criteria and authoritative outcome sources can be frozen in advance.

## Rights and distribution cautions

P01 interventions can create severe tradeoffs even when aggregate violence falls. A ceasefire may freeze coercive territorial control; deterrence may reduce one risk while increasing escalation risk; sanctions may pressure leaders while imposing civilian costs; surveillance or emergency powers may suppress violence while weakening liberty; stabilization can protect some groups while excluding others.

HumanityAI should therefore keep civilian protection, consent, due process, minority rights, displacement, coercion, escalation risk, and distribution of benefits and burdens visible as separate dimensions. Lower measured violence is important, but it is not sufficient evidence that a policy is just, durable, or welfare-improving for everyone affected.

## Current HumanityAI records used

- Problem taxonomy: [`PROBLEM_MAP.md`](../../PROBLEM_MAP.md)
- Active-conflict baseline: [`I0005`](../../data/indicators.json)
- Forced-displacement baseline: [`I0006`](../../data/indicators.json)
- Conflict-data resource: [`RSC0001`](../../data/resources.json)
- Humanitarian-data resource: [`RSC0005`](../../data/resources.json)

The external sources remain the evidentiary authority. This brief is HumanityAI-authored synthesis and should be revised as stronger, contradictory, more granular, or intervention-specific evidence is added.
