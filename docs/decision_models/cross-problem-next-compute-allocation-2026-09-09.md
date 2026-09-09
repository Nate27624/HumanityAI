# Cross-problem next-compute allocation gate — P03 / P06 / P07

**Date:** 2026-09-09  
**Producer:** Operator A  
**Controller assignment:** current `agent/portfolio.json` rank-1 workstream: convert canonical P03 hypertension, P06 electricity-access, and bounded P07 ALMP routing gates into a concrete cross-problem allocation decision.

## Decision question

Given one small block of additional HumanityAI producer compute, which of the now-canonical P03, P06, and P07 lines is most likely to produce a **decision-changing comparison** rather than another evidence artifact?

This is a ranking of **next research/decision-readiness**, not a ranking of social importance or intervention cost-effectiveness across health, electricity, and employment. Outcomes and units are not commensurable, so this note deliberately does not collapse them into one scalar score.

## Recommendation

For the **next three producer opportunities** touching these lines:

1. **Allocate one bounded slot to P03 Bangladesh hypertension delivery.** It has the strongest combination of an existing routing gate, a concrete delivery package, a published cost denominator, measurable control/retention outcomes, and plausible within-country implementation heterogeneity.
2. **Allocate one bounded slot to P06 Nigeria electricity access, but make it a data-recovery / comparability test.** The program scale, financing architecture, geospatial planning, and technology deployment are well documented, but the decision gate still lacks sufficiently comparable public household payment burden, persistence/default/disconnection, and service-quality data. The slot should stop if those denominators cannot be recovered.
3. **Do not pre-allocate the third slot to P07. Hold it contingent.** Give it to whichever of P03 or P06 first produces a comparable decision model; otherwise use it on another controller-approved concrete allocation question such as the conditional Zambia package question. P07 Benin has already delivered the key bounded training-vs-cash diagnostic; more P07 accumulation is low marginal value until a named current program/package decision needs it.

**Decision delta:** move the portfolio from three parallel domain evidence streams to a two-stage process: first test whether a country case has enough cost/adoption/outcome comparability to support a decision; only then spend additional compute on estimation or ranking.

**Confidence:** high that P03 Bangladesh is presently the most decision-ready of these three; moderate-high that Nigeria deserves one bounded data-recovery slot; high that generic additional P07 evidence should remain paused absent a named downstream decision.

## Why P03 Bangladesh is first

The canonical P03 gate says hypertension work should route by care-cascade bottleneck, medicine/device availability, task-sharing authority, follow-up/retention, patient burden, and controlled-patient yield rather than generic treatment efficacy.

Bangladesh has unusually decision-ready inputs:

- A published HEARTS costing analysis estimates the annual hypertension-control package at **US$3.2 million** across the modeled catchment, **US$2.8 per capita**, or **US$8.9 per eligible patient**. Medicines account for **43%** of cost and provider time **38%**. The study identifies physician capacity as a scale-up constraint and explicitly points to task sharing as important for expansion.
- The canonical P03 work already identifies Bangladesh as a plausible within-country follow-up case because implementation reporting exposes treatment-control and missed-visit/follow-up variables rather than only screening counts.
- The useful next comparison can therefore use a common outcome concept — controlled hypertension at a defined horizon — while checking medicine continuity, follow-up intensity, treatment intensification, cadre/task sharing, and patient burden.

Primary cost source: Husain et al. (2022), *Cost of primary care approaches for hypertension management and risk-based cardiovascular disease prevention in Bangladesh: a HEARTS costing tool application*.  
https://pubmed.ncbi.nlm.nih.gov/35760540/

A newer four-country HEARTS investment-case analysis also indicates that Bangladesh-scale hypertension control remains a live budget-allocation problem, but its modeled long-run national estimates should be treated as scenario evidence rather than substituted for the local cost-and-delivery comparison.  
https://pubmed.ncbi.nlm.nih.gov/41370862/

### P03 next-slot test

Use one producer slot to identify **2–4 Bangladesh implementation areas or delivery configurations** with sufficiently comparable definitions/horizons to test whether variation in control or retention plausibly tracks:

- medicine continuity / stock availability;
- follow-up and overdue-patient recall;
- treatment intensification;
- physician versus nurse/community-health-worker task sharing;
- patient visit/refill burden;
- per-eligible-patient or per-controlled-patient program cost when source-grounded.

### P03 stop rule

Stop before constructing a ranking if the candidate areas do not share a defensible control definition/horizon or if program-cost and delivery-intensity data cannot be aligned. In that case, record which missing input has the highest value of information rather than inventing a synthetic cost-per-controlled-patient number.

## Why P06 Nigeria is second — and only as a bounded comparability test

The canonical P06 gate says electricity-access comparisons must normalize for realized service tier/use case, affordability, financing architecture, adoption, reliability, and persistence rather than rank technologies by connection count.

Nigeria has strong program/resource readiness:

- The World Bank's DARES program is financed by a **US$750 million IDA credit** and is intended to leverage **more than US$1 billion of private capital**, with a target of **more than 17.5 million people** receiving new or improved electricity access through distributed renewable energy.
- The predecessor Nigeria Electrification Project supported **125 mini-grids**, sales of **more than one million solar home systems**, and access for **more than 5.5 million people**; the program also used geospatial analysis, portfolio preparation, cost benchmarking, technical standards, and private-developer mechanisms.
- This makes Nigeria a strong setting for comparing financing-and-service packages — but public program summaries still do not establish a common household affordability, reliability, persistence, or default/disconnection denominator across mini-grid and standalone-solar pathways.

Primary program sources:  
- World Bank, *Nigeria to Expand Access to Clean Energy for 17.5 Million People* (2023): https://www.worldbank.org/en/news/press-release/2023/12/15/nigeria-to-expand-access-to-clean-energy-for-17-5-million-people  
- World Bank/ESMAP, *Expanding Nigeria’s mini grid market* (2025 page describing 2018–2024 NEP implementation): https://www.worldbank.org/en/news/feature/2025/03/07/expanding-nigeria-s-mini-grid-market

### P06 next-slot test

Use one producer slot only to determine whether at least two Nigerian access pathways can be compared on a common service/use-case basis with public source-grounded data for most of the following:

- realized household/business service level or reliable proxy;
- tariff/payment burden and subsidy/payment terms;
- financing mechanism and capital support;
- uptake after offer/connection availability;
- reliability/outage or service-continuity measure;
- persistence, default/disconnection, or sustained-use measure;
- implementation cost or results-based-financing payment basis.

### P06 stop rule

If tariff/payment burden plus persistence/default/reliability cannot be recovered for at least two comparable pathways, **do not** spend subsequent slots estimating a modality ranking. Report the missing denominator and keep Nigeria as a resource/implementation map rather than a cost-effectiveness comparison.

## Why P07 should pause

The newly integrated Benin evidence already answers the bounded question that justified the last P07 producer work:

- training-only, cash-only, training+cash, and control were separately randomized;
- long follow-up provides persistence information;
- component costs are available;
- training-only shows sustained business/earnings gains in this specific setting while grant-only lacks primary business/earnings effects;
- gender heterogeneity, attrition, implementation design, and non-portability prevent a global training-vs-capital ranking.

That is enough to change routing. Additional generic ALMP evidence now has low marginal decision value unless a **named current allocation** is specified.

Benin does have a newer Youth Inclusion / Azôli scale-up: the World Bank approved **US$41.3 million** in additional financing in June 2025, with plans to support roughly **60,500 vulnerable young people** plus **1,000 youth** in poultry value chains; the existing project had already reached more than **48,000 youth**, including wage-employment placements and self-employment support. But that program mixes wage employment, technical training, value-chain integration, and self-employment support and is not the same treatment architecture as the older PEJ experiment. The PEJ training-vs-cash result therefore cannot be used directly to rank Azôli package components.

Source: World Bank, *Benin: More than 60,000 Vulnerable Youth Integrated into Agri-Food Value Chains and Wage Jobs* (25 June 2025).  
https://www.worldbank.org/en/news/press-release/2025/06/25/benin-more-than-60-000-vulnerable-youth-integrated-into-agri-food-value-chains-and-wage-jobs

### P07 reopen condition

Reopen producer work only when D can name a decision such as:

- whether a current Benin youth-employment package should fund more technical/business training versus another component;
- whether a specific target population should receive a training, capital, placement, or combined package;
- whether a second comparable study is needed to test portability of the canonical Benin diagnostic.

Require a target population, package definition, measurable outcome horizon, and cost/adoption denominator before another Tier-2 P07 product.

## Cross-problem readiness matrix

| Line | Named downstream decision | Cost anchor | Adoption / implementation observability | Outcome comparability | Main missing input | Next action |
|---|---|---|---|---|---|---|
| **P03 Bangladesh hypertension** | Which delivery configuration best relaxes the control/retention bottleneck? | Strong local package cost anchor; medication/provider shares available | Relatively strong; task sharing, follow-up, medicine continuity, control are observable in program data | Potentially strong if common BP-control horizon is recoverable | Comparable area-level delivery intensity and patient-burden data | **One bounded comparison slot now** |
| **P06 Nigeria electricity** | Which financing + service package is affordable, adopted, reliable, and persistent at a common service level? | Strong program/financing totals and cost-benchmarking infrastructure, but weak portable household denominator | Moderate; deployment and financing architecture visible, household affordability/persistence less so | Not yet established across pathways | Tariff/payment burden + reliability + default/disconnection/persistence on common basis | **One bounded data-recovery slot now; stop if failed** |
| **P07 Benin ALMP** | No current package-allocation decision specified | Strong older experimental component costs | Strong for older PEJ trial; weaker relevance to current mixed Azôli architecture | Strong within old trial, weak transport to current package | A named current decision and comparable package/outcome denominator | **Pause producer work** |

## Portfolio rule produced by this synthesis

Before allocating a second producer slot to any of these three lines, require the first slot to return one of two states:

1. **decision_ready** — at least two alternatives share a defensible outcome horizon plus source-grounded cost/adoption inputs sufficient for a bounded comparison; or
2. **missing_decision_input** — name the specific unavailable variable and why further synthesis would not resolve it.

Do not reward a line for generating more papers or records. Reward it for crossing from an evidence gate into a measurable comparison that can change a downstream allocation.

## Value-of-information trigger for the held third slot

After the P03 and P06 bounded tests:

- If **P03 becomes decision_ready**, allocate the held slot to estimating the Bangladesh delivery comparison or independently reproducing its key denominator.
- Else if **P06 becomes decision_ready**, allocate the held slot to the Nigeria service/financing comparison.
- Else leave both lines at `missing_decision_input` and allocate the slot to another controller-approved decision question rather than forcing a cross-domain rank.

P07 receives the held slot only if a named current package decision appears and the old Benin evidence is genuinely decision-relevant to it.

## What this note does not claim

- It does not claim hypertension control has higher social value than electricity access or youth employment.
- It does not compare dollars across fundamentally different outcomes.
- It does not claim the Bangladesh HEARTS cost estimate is portable nationally or internationally.
- It does not divide Nigeria project finance by beneficiary targets to invent a cost-per-connection or cost-per-person figure.
- It does not treat the older Benin PEJ experiment as an evaluation of the current Azôli package.
- It does not authorize real-world spending, advocacy, implementation, or contact with any program.

## Recommended controller action

For the immediate P03/P06/P07 portfolio, set producer sequencing to:

**P03 Bangladesh bounded comparison test -> P06 Nigeria comparability/data-recovery test -> contingent third slot based on decision-readiness.**

Keep generic P07 accumulation paused. If neither country case crosses its comparability gate, treat that as useful information and redirect compute instead of manufacturing a scalar cross-problem ranking.
