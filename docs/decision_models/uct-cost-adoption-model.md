# Bounded UCT cost and adoption decision model

Date: 2026-09-07

## Assignment

Worker D's current portfolio assigns Operator A to build a bounded decision model for unconditional cash transfers (UCTs), using source-grounded ranges for transfer cost, administrative cost, outcome effects, duration, targeting/adoption constraints, and explicit stop conditions against invented precision.

This document is a **decision-support model for future HumanityAI analysis**. It is not a recommendation that any government, donor, or implementer launch a cash-transfer program, and it does not collapse multidimensional outcomes into one welfare score.

## Decision question

What can HumanityAI already say, with traceable evidence, about the cost and implementation envelope of UCTs in low- and middle-income settings—and what remains too context-dependent to support a scalar cost-effectiveness ranking?

## Evidence anchors

### Effectiveness anchor: Cochrane 2022

The current Cochrane systematic review includes 34 studies, 25 experimental and 9 non-experimental, with 1,140,385 participants and 50,095 households across Africa, the Americas, and South-East Asia. The 24 identified UCT programs included government programs and research experiments. Most studies had an overall high risk of bias, and the evidence was current to September 2021.

Source: Pega F, Pabayo R, Benny C, Lee E-Y, Lhachimi SK, Liu SY. *Unconditional cash transfers for reducing poverty and vulnerabilities: effect on use of health services and health outcomes in low- and middle-income countries*. Cochrane Database of Systematic Reviews 2022, Issue 3, CD011135. https://www.cochrane.org/evidence/CD011135_does-giving-money-people-low-and-middle-income-countries-without-conditions-attached-lead-better

### Delivery-cost and targeting anchor: World Bank 2024

A World Bank Social Protection & Jobs discussion paper on scaling social assistance where data are scarce reports that administrative costs for welfare-targeted cash transfer programs are commonly about 5–10% of total program cost, while cited program examples span below that range and above it. The same paper documents major implementation dependence on registries, identification, payment infrastructure, data quality, procurement, mobile access, and targeting method.

Source: Okamura Y, Ohlenburg T, Tesliuc E. *Scaling up social assistance where data is scarce: Opportunities and limits of novel data and AI*. World Bank Social Protection & Jobs Discussion Paper No. 2402, March 2024. https://documents1.worldbank.org/curated/en/099050724145524418/pdf/P171913-1f545ae0-ad05-4e97-b3db-7f9d6820d240.pdf

### Qualitative adoption anchor: Cochrane 2023

A Cochrane qualitative evidence synthesis covering conditional and unconditional cash-transfer experiences found that recipients often regarded transfers as useful, but also reported insufficient transfer size, access barriers, stigma or inappropriate eligibility processes, social tension where eligibility differed, and cases where cash alone was insufficient to change behavior without complementary support.

Source: Yoshino CA et al. *Experiences of conditional and unconditional cash transfers intended for improving health outcomes and health service use: a qualitative evidence synthesis*. Cochrane Database of Systematic Reviews 2023, Issue 3, CD013635. https://www.cochrane.org/CD013635/EPOC_experiences-and-perceptions-cash-transfers-health

### Implementation case anchor: rural Kenya

A large GiveDirectly experiment in rural Kenya delivered one-time transfers of about USD 1,000 to more than 10,500 poor households across 653 randomized villages. The study found large recipient consumption and asset effects, positive spillovers to non-recipients and firms, and minimal local price inflation in that setting. This is a useful implementation case, not a universal transfer-size benchmark.

Source: Egger D, Haushofer J, Miguel E, Niehaus P, Walker MW. *General Equilibrium Effects of Cash Transfers: Experimental Evidence from Kenya*. NBER Working Paper 26600 / published study. https://www.nber.org/papers/w26600

## Bounded parameter envelope

The table below deliberately separates **observed empirical ranges** from **model-ready anchors**. “Low/base/high” means a source-grounded sensitivity envelope, not a probability distribution and not three forecasts.

| Parameter | Low anchor | Base anchor | High anchor | Interpretation / caveat |
|---|---:|---:|---:|---|
| Administrative share of total program cost | 2% | 5–10% | 16.2% | World Bank 2024 cites 2–10% for last-resort ECA cash programs, about 5–10% as a normal-times cash-transfer benchmark, and program examples up to 16.2%. Program maturity, conditionality, geography, registry quality, payment systems, staffing, and bundled services materially change this share. |
| UCT cash value relative to annual GDP per capita | 1.3% | **No defensible universal base** | 81.9% | Cochrane reports this empirical span across included UCTs. The range is too wide to justify a universal midpoint. A model must use a program-specific transfer amount or transfer-to-income ratio rather than inventing a global “typical” UCT. |
| Illness risk ratio | 0.92 | 0.79 | 0.67 | Cochrane point estimate RR 0.79, 95% CI 0.67–0.92, 6 cluster RCTs; moderate-certainty evidence. Low/high are conservative/favorable CI anchors, not posterior percentiles. |
| Food-security risk ratio | 1.09 | 1.25 | 1.45 | Cochrane RR 1.25, 95% CI 1.09–1.45; low-certainty evidence and substantial heterogeneity (I²=85%). |
| Household dietary-diversity change | +0.18 | +0.59 | +1.01 food categories | Cochrane mean difference 0.59, 95% CI 0.18–1.01; low-certainty evidence and substantial heterogeneity (I²=79%). |
| Current school-attendance risk ratio | 1.04 | 1.06 | 1.09 | Cochrane RR 1.06, 95% CI 1.04–1.09; moderate-certainty evidence, assessed 12–24 months into intervention. |
| Extreme-poverty risk ratio | 0.97 | 0.92 | 0.87 | Cochrane RR 0.92, 95% CI 0.87–0.97; low-certainty evidence, assessed 12–36 months into intervention. |
| Evidence-bearing follow-up window | 12 months | 12–24 months | 36 months | Major Cochrane outcomes were assessed over roughly 12–36 months depending on outcome. This is an observation window, not proof that benefits persist for 36 months after transfers stop. |

### Why transfer size has no global base case

The most important negative result of this modeling exercise is that a universal transfer-size base case would be fabricated. Cochrane reports cash values ranging from 1.3% to 81.9% of annualized GDP per capita across included UCT programs. A rural-Kenya trial used transfers around USD 1,000, while another Kenya experiment studied USD 404 and USD 1,525 transfer arms. These are context-specific designs, not interchangeable points on a single global cost-effectiveness curve.

For any later country/program analysis, the model must therefore obtain at minimum:

1. transfer amount per eligible household/person;
2. number of transfers and payment schedule;
3. local income or consumption baseline;
4. administrative/delivery share;
5. expected coverage and exclusion/inclusion errors;
6. intended outcome family and follow-up horizon.

If these are unavailable, stop before computing a scalar return-on-cost estimate.

## Mechanical cost model

For a defined program only:

`total_program_cost = total_cash_delivered / (1 - administrative_share)`

Equivalently:

`administrative_cost = total_program_cost × administrative_share`

This identity is useful for sensitivity analysis because the World Bank provides plausible administrative-share anchors. It does **not** imply that administrative cost is the only non-transfer cost experienced by beneficiaries or society.

Illustrative arithmetic, using a hypothetical USD 100 of cash delivered:

| Administrative share assumption | Implied total program cost | Implied administrative cost |
|---:|---:|---:|
| 2% | USD 102.04 | USD 2.04 |
| 5% | USD 105.26 | USD 5.26 |
| 10% | USD 111.11 | USD 11.11 |
| 16.2% | USD 119.33 | USD 19.33 |

These rows are mathematical translations of source-grounded administrative-share assumptions, not estimates of any particular program.

## Adoption and implementation constraints

### 1. Registry and identification capacity

The World Bank reports that designing and implementing targeted transfers generally requires data to identify, locate, screen, and pay beneficiaries, alongside systems such as IDs, registries, management-information systems, and payment infrastructure. Countries with current, high-coverage registries were better positioned to scale emergency support quickly; “data desert” settings faced much larger targeting and registration problems.

**Decision implication:** a favorable effect estimate is not enough. If the intended population is poorly represented in administrative data, cost and exclusion risk should both be widened.

### 2. Targeting error is a first-order model input

The World Bank paper explicitly notes that no targeting approach is fully inclusive. In the STEP-KIN case, consultations identified concerns that poor people without phones could be missed and that geographic targeting could include better-off residents while excluding poor households elsewhere. The paper also reports that roughly 10% of beneficiaries in that program never withdrew their funds despite repeated contact attempts.

**Decision implication:** “budgeted transfer value” and “cash effectively accessed by intended recipients” are different quantities. Future models should include an access/realization factor when program-specific evidence exists.

### 3. Digital delivery lowers some costs but can shift exclusion risk

World Bank case evidence shows that mobile and digital systems can lower setup/transaction costs and speed delivery, but people lacking phones, IDs, accounts, connectivity, or sufficient digital literacy may be excluded. Cameroon implementation evidence similarly reports that missing IDs and inaccurate data delayed or prevented mobile-money delivery for some intended beneficiaries.

**Decision implication:** digital delivery should not automatically be coded as a pure efficiency improvement; the model should separately track administrative savings and access/exclusion risk.

### 4. Acceptability and adequacy matter

The 2023 Cochrane qualitative synthesis reports that recipients commonly viewed transfers as useful but sometimes too small relative to need; some faced barriers accessing programs, stigma or problematic eligibility processes, and social tension where some people received transfers and others did not.

**Decision implication:** transfer adequacy, eligibility legitimacy, communication, and grievance mechanisms are adoption variables, not side notes.

### 5. Cash is not a universal behavior-change technology

The same qualitative synthesis found that recipients sometimes viewed cash alone as insufficient to change behavior and believed complementary support was needed.

**Decision implication:** do not infer that because UCTs improve income-linked outcomes they will solve constraints caused primarily by missing services, information, discrimination, legal barriers, or supply shortages.

## Outcome interpretation

The model should keep outcomes separate rather than converting them to one ungrounded score:

- **Health:** illness incidence shows moderate-certainty improvement, but health-service use may change little or not at all; mortality evidence was absent in the review.
- **Food security:** favorable direction, but lower certainty and substantial heterogeneity.
- **Dietary diversity:** favorable mean change, with substantial heterogeneity.
- **School attendance:** moderate-certainty positive effect; this is attendance, not learning achievement.
- **Extreme poverty:** favorable low-certainty effect; definitions and baseline poverty matter.
- **Employment, livestock ownership, depression, parenting quality and child labour:** evidence remains uncertain in the Cochrane review.

A later cost-effectiveness model may translate an outcome into a common unit only when a defensible conversion source and explicit normative assumptions are supplied. Until then, HumanityAI should present a **cost-to-outcome vector**, not a single score.

## Decision matrix for the next analysis

| Situation | Recommended analytical action |
|---|---|
| Program has known transfer amount, duration, beneficiary count, and admin share | Run transparent low/base/high total-cost sensitivity and pair with outcome-specific effect ranges. |
| Transfer amount known but admin share unknown | Use 5–10% as a World Bank benchmark sensitivity band, with 2% and 16.2% as wider stress anchors; label these as external benchmarks, not program estimates. |
| Targeting/delivery system weak or unknown | Do not use a narrow cost range; explicitly model exclusion/access uncertainty or stop if no defensible assumption can be sourced. |
| Desired outcome is school attendance, illness, food security, dietary diversity, or extreme poverty | Cochrane provides quantitative effect anchors, subject to certainty and heterogeneity limitations. |
| Desired outcome is mortality, employment, livestock, depression, parenting quality, child labour, or long-run persistence | Do not fabricate effect sizes from the current canonical review; acquire additional evidence first. |
| Proposed comparison requires one scalar UCT “value” across multiple outcomes | Stop unless a transparent common-unit conversion and normative weighting scheme are explicitly justified and reviewable. |

## Stop / kill conditions

Stop quantitative ranking and return an uncertainty statement if any of these apply:

1. **No program-specific transfer amount or defensible transfer-intensity anchor.** The empirical UCT transfer-value span is too broad for a universal midpoint.
2. **Outcome not supported quantitatively by the current evidence base.** Do not substitute a nearby outcome.
3. **Administrative-cost benchmark is being mistaken for a program estimate.** A 5–10% benchmark must remain a sensitivity assumption unless local data exist.
4. **Targeting or digital-access constraints are likely material but unmeasured.** Do not present nominal coverage as effective coverage.
5. **Long-run persistence is required but only 12–36 month in-intervention follow-up is available.** Do not extrapolate indefinitely.
6. **Multiple outcomes are being collapsed into a scalar without explicit conversion and value assumptions.** Preserve the vector instead.
7. **The analysis treats confidence-interval endpoints as probabilities of low/base/high scenarios.** They are sensitivity anchors only.

## Decision delta

The UCT evidence is mature enough to support a **bounded, program-specific cost-and-outcome sensitivity model**, but **not** a universal UCT cost-effectiveness number.

The strongest reusable quantitative inputs now available are:

- administrative-cost stress range around a World Bank 5–10% normal-times benchmark;
- outcome-specific Cochrane point estimates and confidence intervals for illness, food security, dietary diversity, school attendance, and extreme poverty;
- a 12–36 month evidence-bearing observation window;
- explicit implementation constraints around registries, IDs, targeting, mobile access, beneficiary uptake, and program acceptability.

The missing variable with the greatest decision leverage is **program-specific transfer intensity and realized coverage**. That should be the next required input before HumanityAI attempts a cost-effectiveness comparison with another intervention.

## Confidence

**Moderate-high** that this model correctly bounds what can be computed from the cited evidence without invented precision.

Confidence is lower for transferring any administrative-cost or implementation benchmark across countries because delivery systems, program maturity, geography, targeting methods, payment rails, and bundled services vary materially.

## Controller-facing next action

Treat this as a Tier-2 decision product requiring independent Worker C verification before Worker D integration.

Recommended C checks:

1. verify every Cochrane effect estimate, confidence interval, certainty statement, and follow-up window;
2. verify the World Bank administrative-cost range and ensure examples are not presented as universal estimates;
3. challenge the interpretation of targeting, digital exclusion, and adoption constraints;
4. confirm that the arithmetic example is mechanically correct and clearly hypothetical;
5. confirm that no scalar cost-effectiveness ranking is implied.

If C returns PASS or a manageable QUALIFY verdict, D should integrate the model as the default UCT analysis template and require future UCT-vs-other-intervention comparisons to supply program-specific transfer amount, duration, administrative cost, effective coverage, and outcome choice before ranking.