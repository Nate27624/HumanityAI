# Bounded UCT cost and adoption decision model

Date: 2026-09-07

## Assignment

Worker D's current portfolio assigns Operator A to build a bounded decision model for unconditional cash transfers (UCTs), using source-grounded ranges for transfer cost, administrative cost, outcome effects, duration, targeting/adoption constraints, and explicit stop conditions against invented precision.

This is a **decision-support model**, not a recommendation that a government, donor, or implementer launch a cash-transfer program. It deliberately keeps multidimensional outcomes separate rather than collapsing them into one welfare score.

## Decision question

What can HumanityAI already say, with traceable evidence, about the cost and implementation envelope of UCTs in low- and middle-income settings, and what remains too context-dependent to support a scalar cost-effectiveness ranking?

## Evidence anchors

### Effectiveness: Cochrane 2022

The Cochrane review includes 34 studies (25 experimental and 9 non-experimental), 1,140,385 participants, and 50,095 households across Africa, the Americas, and South-East Asia. The 24 UCT programs included government programs and research experiments. Most studies had an overall high risk of bias, and the evidence search was current to September 2021.

Source: Pega F, Pabayo R, Benny C, Lee E-Y, Lhachimi SK, Liu SY. *Unconditional cash transfers for reducing poverty and vulnerabilities: effect on use of health services and health outcomes in low- and middle-income countries*. Cochrane Database of Systematic Reviews 2022, Issue 3, CD011135. https://www.cochrane.org/evidence/CD011135_does-giving-money-people-low-and-middle-income-countries-without-conditions-attached-lead-better

### Administrative cost and delivery: World Bank 2024

A World Bank Social Protection & Jobs discussion paper reports that administrative costs for welfare-targeted cash transfer programs in normal times are commonly about 5–10% of total program cost. It cites 2–10% for last-resort cash transfers in Eastern Europe and Central Asia, 0.4–5.5% across Burkina Faso, Chad, and Niger, 7.7% for the first phase of Tanzania's Productive Safety Net, about 11% for Jamaica PATH in 2018, 5.7% for DRC STEP-KIN, and about 10% for Togo Novissi Model 2. The same paper documents major dependence on registries, identification, payment infrastructure, data quality, procurement, mobile access, and targeting method.

Source: Okamura Y, Ohlenburg T, Tesliuc E. *Scaling up social assistance where data is scarce: Opportunities and limits of novel data and AI*. World Bank Social Protection & Jobs Discussion Paper No. 2402, March 2024. https://documents1.worldbank.org/curated/en/099050724145524418/pdf/P171913-1f545ae0-ad05-4e97-b3db-7f9d6820d240.pdf

### Wider administrative-cost stress case: World Bank guidance / ECA evidence

World Bank cash-transfer guidance reproduces program examples with administrative-cost shares ranging from about 2.2% for Armenia's Family Benefit Program to 16.2% for Bulgaria's last-resort social assistance program, while emphasizing that maturity, generosity, targeting, scale, and bundled services affect interpretation. The 16.2% figure is therefore retained only as a **wide external stress anchor**, not as a normal-times estimate and not as a claim from the 2024 paper above.

Source: World Bank, *Social Assistance Cash Transfers: What Matters Guidance Note* (program examples drawing on Grosh et al. and ECA administrative-cost evidence). The underlying ECA evidence is also reported in Tesliuc et al., *Income Support for the Poorest: A Review of Experience in Eastern Europe and Central Asia*.

### Adoption and acceptability: Cochrane 2023

A Cochrane qualitative evidence synthesis of conditional and unconditional transfer experiences found that recipients often regarded transfers as useful, but also reported inadequate transfer size, access barriers, stigma or inappropriate eligibility processes, social tension where eligibility differed, and cases in which cash alone was insufficient to change behavior without complementary support.

Source: Yoshino CA et al. *Experiences of conditional and unconditional cash transfers intended for improving health outcomes and health service use: a qualitative evidence synthesis*. Cochrane Database of Systematic Reviews 2023, Issue 3, CD013635. https://www.cochrane.org/evidence/CD013635_experiences-and-perceptions-cash-transfers-health

## Bounded parameter envelope

“Low/base/high” below means **sensitivity anchors**, not a probability distribution or three forecasts.

| Parameter | Low anchor | Base anchor | High anchor | Interpretation / caveat |
|---|---:|---:|---:|---|
| Administrative share of total program cost | 2% | 5–10% | 16.2% | 5–10% is the World Bank 2024 normal-times benchmark. The 2% and 16.2% values are wider external stress anchors from ECA program evidence; do not treat them as a typical global interval. |
| UCT cash value relative to annual GDP per capita | 1.3% | **No defensible universal base** | 81.9% | Cochrane's empirical span across included UCTs is far too wide for a universal midpoint. Use a program-specific transfer amount or transfer-to-income ratio. |
| Illness risk ratio | 0.92 | 0.79 | 0.67 | Cochrane RR 0.79, 95% CI 0.67–0.92; 6 cluster RCTs, moderate-certainty evidence. Endpoints are sensitivity anchors, not scenario probabilities. |
| Food-security risk ratio | 1.09 | 1.25 | 1.45 | Cochrane RR 1.25, 95% CI 1.09–1.45; low-certainty evidence, I²=85%. |
| Household dietary-diversity change | +0.18 | +0.59 | +1.01 food categories | Cochrane mean difference 0.59, 95% CI 0.18–1.01; low-certainty evidence, I²=79%. |
| Current school-attendance risk ratio | 1.04 | 1.06 | 1.09 | Cochrane RR 1.06, 95% CI 1.04–1.09; moderate-certainty evidence, assessed 12–24 months into intervention. |
| Extreme-poverty risk ratio | 0.97 | 0.92 | 0.87 | Cochrane RR 0.92, 95% CI 0.87–0.97; low-certainty evidence, assessed 12–36 months into intervention. |
| Evidence-bearing follow-up window | 12 months | 12–24 months | 36 months | Outcome-specific observations span roughly 12–36 months. This is not proof of persistence for 36 months after transfers stop. |

## Why transfer size has no global base case

Cochrane reports UCT cash values ranging from **1.3% to 81.9% of annualized GDP per capita** across included programs. That empirical range is itself a stop signal against inventing a universal “typical transfer.”

For any later country/program model, obtain at minimum:

1. transfer amount per eligible household or person;
2. number of transfers and payment schedule;
3. local income/consumption baseline or another defensible intensity denominator;
4. administrative/delivery share;
5. expected coverage plus inclusion/exclusion or access failure where measurable;
6. intended outcome family and follow-up horizon.

If these are unavailable, stop before computing a scalar return-on-cost estimate.

## Mechanical cost model

For a defined program only:

`total_program_cost = total_cash_delivered / (1 - administrative_share)`

and

`administrative_cost = total_program_cost × administrative_share`

Illustrative arithmetic for a hypothetical USD 100 of cash actually delivered:

| Administrative share assumption | Implied total program cost | Implied administrative cost |
|---:|---:|---:|
| 2% | USD 102.04 | USD 2.04 |
| 5% | USD 105.26 | USD 5.26 |
| 10% | USD 111.11 | USD 11.11 |
| 16.2% | USD 119.33 | USD 19.33 |

These are mathematical translations of sensitivity assumptions, not estimates for a particular program.

## Adoption and implementation constraints

### Registry and identification capacity

The World Bank reports that targeted transfers generally require data and systems to identify, locate, screen, and pay beneficiaries. Countries with current, high-coverage registries can scale more rapidly; data-scarce settings face larger targeting and registration burdens.

**Decision implication:** if the intended population is poorly represented in administrative systems, widen both cost and exclusion uncertainty.

### Targeting and realized access

In the DRC STEP-KIN case, program consultations raised concerns that poor people without phones could be missed and that geographic targeting could include better-off residents while excluding poor households elsewhere. The World Bank also reports that around 10% of beneficiaries never withdrew their funds despite repeated contact attempts.

**Decision implication:** nominal budgeted coverage and cash actually accessed by intended recipients are different quantities. Use a program-specific realization/access factor when credible evidence exists.

### Digital delivery can trade cost for exclusion

The World Bank cases show that digital/mobile delivery can speed deployment and reduce some transaction/setup costs, while people lacking phones, IDs, accounts, connectivity, or digital literacy can be excluded.

**Decision implication:** model administrative efficiency and access/exclusion separately rather than treating digitization as an unqualified benefit.

### Adequacy, legitimacy, and social acceptance

Cochrane's qualitative synthesis found that recipients often considered transfers useful but sometimes too small relative to need, and reported access barriers, stigma, problematic eligibility processes, and tension when some community members received transfers and others did not.

**Decision implication:** adequacy, eligibility legitimacy, communication, and grievance processes are adoption variables rather than side notes.

### Cash is not a universal behavior-change technology

Recipients in the qualitative synthesis sometimes regarded cash alone as insufficient to change behavior and identified needs for other forms of support.

**Decision implication:** do not infer that income support will solve constraints primarily caused by absent services, information, discrimination, legal barriers, or supply shortages.

## Outcome interpretation

Keep the outcome vector separate:

- **Illness:** moderate-certainty favorable effect; mortality was not measured.
- **Health-service use:** may change little or not at all.
- **Food security:** favorable direction, low certainty, substantial heterogeneity.
- **Dietary diversity:** favorable mean change, low certainty, substantial heterogeneity.
- **School attendance:** moderate-certainty positive effect; attendance is not learning.
- **Extreme poverty:** favorable low-certainty effect; baseline definitions matter.
- **Employment, livestock ownership, depression, parenting quality, child labour:** current Cochrane evidence remains uncertain.

A later model should translate these into a common unit only if a defensible conversion source and explicit normative assumptions are supplied. Until then, report a **cost-to-outcome vector**, not one score.

## Decision matrix

| Situation | Recommended analytical action |
|---|---|
| Transfer amount, duration, beneficiary count, admin share known | Run transparent total-cost sensitivity paired with outcome-specific effect ranges. |
| Transfer amount known, admin share unknown | Use 5–10% as the main World Bank benchmark sensitivity band; use 2% and 16.2% only as wider external stress cases and label provenance. |
| Targeting/delivery system weak or unknown | Widen or explicitly model access/exclusion uncertainty; stop if no defensible assumption can be sourced. |
| Outcome is illness, food security, dietary diversity, school attendance, or extreme poverty | Cochrane provides quantitative anchors, subject to certainty and heterogeneity limits. |
| Outcome is mortality, employment, livestock, depression, parenting quality, child labour, or long-run persistence | Acquire additional evidence before assigning an effect size. |
| Comparison requires one scalar UCT “value” across outcomes | Stop unless common-unit conversion and normative weighting are explicit, sourced where factual, and reviewable. |

## Stop / kill conditions

Stop quantitative ranking and return an uncertainty statement when:

1. there is no program-specific transfer amount or defensible intensity anchor;
2. the desired outcome is not quantitatively supported by the evidence being used;
3. an administrative-cost benchmark is being presented as a program estimate;
4. material targeting/digital-access constraints are unmeasured;
5. long-run persistence is required but only limited in-intervention follow-up is available;
6. multiple outcomes are collapsed without explicit conversion/value assumptions;
7. confidence-interval endpoints are being interpreted as probabilities of low/base/high scenarios.

## Decision delta

The evidence supports a **bounded, program-specific UCT cost-and-outcome sensitivity model**, but not a universal UCT cost-effectiveness number.

Reusable inputs now include:

- a World Bank **5–10%** normal-times administrative-cost benchmark, with wider externally sourced stress cases;
- quantitative Cochrane outcome anchors for illness, food security, dietary diversity, school attendance, and extreme poverty;
- an outcome-specific roughly **12–36 month** evidence-bearing window;
- explicit implementation constraints around registries, IDs, targeting, mobile access, beneficiary uptake, adequacy, and acceptability.

The highest-leverage missing inputs before comparison with another intervention are **program-specific transfer intensity and realized coverage/access**.

## Confidence

**Moderate-high** that this model correctly bounds what can be computed without invented precision.

Confidence is lower for portability of any administrative-cost or delivery assumption across countries because systems, program maturity, geography, targeting, payment rails, conditionality, and bundled services vary materially.

## Controller-facing next action

Treat this as a Tier-2 decision product requiring independent Worker C verification before Worker D integration.

Recommended C checks:

1. verify every Cochrane effect estimate, confidence interval, certainty statement, and follow-up window;
2. verify the 5–10% World Bank normal-times administrative-cost benchmark and independently trace the wider 2%/16.2% ECA stress anchors;
3. challenge the targeting, digital-exclusion, adequacy, and adoption interpretations;
4. confirm the hypothetical arithmetic;
5. confirm that no scalar cost-effectiveness ranking is implied.

If C returns PASS or a manageable QUALIFY verdict, D should integrate this as the default UCT analysis template and require future UCT-vs-other-intervention comparisons to supply program-specific transfer amount, duration, administrative cost, effective coverage/access, and outcome choice before ranking.