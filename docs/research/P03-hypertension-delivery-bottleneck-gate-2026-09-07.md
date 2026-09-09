# P03 exploration — hypertension delivery bottleneck gate

**Reviewed:** 2026-09-07  
**Status:** decision-bearing exploration candidate; requires independent Worker C verification before Worker D integration  
**Assignment:** Worker D cross-domain exploration while P07 and P06 decision products await verification

## Decision question

Should HumanityAI spend additional P03 compute comparing antihypertensive drugs or awareness/screening interventions in aggregate, or should it route first by the **care-delivery bottleneck**: medicine/device availability, standardized treatment protocol, task-sharing capacity, follow-up/retention, and patient financial burden?

## Short answer

**Route first by delivery bottleneck.** The core clinical intervention is already unusually mature: effective low-cost medicines exist, and community/team-based delivery can improve blood-pressure control. The larger decision uncertainty is whether a health system can repeatedly diagnose, initiate, titrate, supply, and retain patients in treatment at scale. Future P03 work should therefore compare delivery packages and binding constraints, not continue generic “does hypertension treatment work?” accumulation.

## Evidence that changes the routing decision

### 1. The global control gap is primarily a delivery problem, not absence of an effective treatment

WHO estimates that **1.4 billion adults aged 30–79 had hypertension in 2024**, while only about **320 million (23%) had it controlled**. About 600 million were unaware they had hypertension and roughly 630 million were diagnosed and treated. Two-thirds of adults with hypertension live in low- and middle-income countries.

Source: WHO, *Hypertension* fact sheet, 25 September 2025.  
https://www.who.int/news-room/fact-sheets/detail/hypertension

**Decision implication:** screening, treatment initiation, and durable control are separable cascade stages. A program that increases diagnosis without increasing treatment continuity may have little final-outcome value.

### 2. Medicine and equipment availability are first-order bottlenecks

WHO's 2025 global hypertension report identifies limited access to validated blood-pressure devices, lack of standardized protocols and trained primary-care teams, unreliable supply chains, costly medicines, inadequate financial protection, and weak information systems as major barriers. Only **7 of 25 low-income countries (28%)** reported general availability of all WHO-recommended hypertension medicines, versus 93% of high-income countries.

Source: WHO, *Uncontrolled high blood pressure puts over a billion people at risk*, 23 September 2025.  
https://www.who.int/news/item/23-09-2025-uncontrolled-high-blood-pressure-puts-over-a-billion-people-at-risk

**Decision implication:** HumanityAI should not rank screening or counseling programs without first checking whether patients can obtain reliable measurement, medicines, and follow-up.

### 3. Community/team-based delivery appears effective, but the useful unit is a delivery package

A 2024 systematic review and meta-analysis of 18 randomized or cluster-randomized LMIC studies found community-based strategies increased blood-pressure control overall (RR **1.48**, 95% CI 1.40–1.57; 12 studies reporting control). The interventions were heterogeneous and often multicomponent.

Source: *Community-Based Strategies to Improve Health-Related Outcomes in People Living With Hypertension in Low- and Middle-Income Countries: A Systematic Review and Meta-Analysis* (2024).  
https://pubmed.ncbi.nlm.nih.gov/38883258/

A broader implementation meta-analysis found the largest systolic-BP reductions with multilevel strategies that included team-based care and medication titration, while noting sparse LMIC evidence and possible publication bias.

Source: *Comparative Effectiveness of Implementation Strategies for Blood Pressure Control in Hypertensive Patients* (2018).  
https://pubmed.ncbi.nlm.nih.gov/29277852/

**Decision implication:** future comparisons should specify who can titrate medication, what protocol is used, whether medicines are in stock, how follow-up occurs, and whether patients remain in care.

### 4. Task-sharing may be economically attractive, but cost evidence is still heterogeneous

A 2026 systematic review of hypertension management by non-physician health-care workers in LMICs found seven economic studies across eight countries. Results generally favored cost-effectiveness, but designs, cadres, currencies/price adjustments, and outcome denominators varied widely; the authors explicitly call for more evidence on generalizability.

Source: *Cost-Effectiveness and Implementation Strategies for Hypertension Management Using Non-Physician Healthcare Workers in Low- and Middle-Income Countries: A Systematic Review* (2026).  
https://pubmed.ncbi.nlm.nih.gov/41836051/

**Decision implication:** do not create a portable global “cost per controlled patient” number. Country-level salary structure, drug procurement, visit frequency, scope-of-practice rules, and retention can dominate economics.

### 5. Adoption is constrained by workforce rules and implementation design, not only patient demand

A survey of hypertension team-based care in 17 LMIC countries/regions found common perceived barriers including inadequate training, regulatory issues, and resistance from patients and clinicians; treatment algorithms and adequate compensation were frequently identified as facilitators. Because this was a convenience-sample survey, it is implementation evidence rather than causal effectiveness evidence.

Source: *Landscape of team-based care to manage hypertension* (2023).  
https://pubmed.ncbi.nlm.nih.gov/37487684/

**Decision implication:** task-sharing recommendations should be conditional on legal scope of practice, training/supervision, compensation, and medication-titration authority.

## Proposed routing rule

Before spending another P03 slot on hypertension intervention ranking, require the candidate decision to specify:

1. **Cascade stage:** detection, treatment initiation, titration, medicine continuity, retention, or control.
2. **Delivery cadre:** physician, nurse, pharmacist, community health worker, or mixed team, including titration authority.
3. **Supply reliability:** validated BP devices and uninterrupted access to the protocol's medicines.
4. **Patient burden:** out-of-pocket drug costs, visit frequency, travel/time cost, and refill interval.
5. **Follow-up system:** registry, recall mechanism, adherence/retention measurement, and treatment intensification rules.
6. **Outcome denominator:** controlled patient at a defined threshold and horizon, not screenings completed or people contacted.

## START / MORE / LESS / STOP

**START:** one or two country-level comparisons of hypertension delivery packages where medicine prices/availability, cadre costs, treatment protocols, and retention/control data can be sourced on a common horizon.

**MORE:** evidence on stock-outs, refill duration, patient out-of-pocket burden, treatment intensification, loss to follow-up, cadre compensation, and actual controlled-patient yield.

**LESS:** generic reviews of antihypertensive efficacy, awareness campaigns, or screening volume where downstream treatment capacity is unspecified.

**STOP:** ranking programs by cost per person screened; assuming diagnosis equals treatment; treating community health workers as a single portable intervention; or importing a global cost-per-controlled-patient estimate across countries.

## Kill test

Do **not** allocate multiple new P03 slots to a global cost-effectiveness ranking of hypertension delivery models unless at least two candidate packages can be compared using a common control definition and horizon with source-grounded medication cost/availability, workforce cost, and retention assumptions.

If those inputs are unavailable, the higher-value next step is a **country-level care-cascade bottleneck diagnosis** rather than a synthetic global ranking.

## Decision delta for Worker D

This shifts the P03 question from **“Which hypertension intervention works best?”** to **“Which care-cascade bottleneck is limiting durable blood-pressure control in a specific system, and which delivery package relaxes it at acceptable cost?”**

That should redirect future slots away from mature clinical-efficacy questions and toward medicine access, task-sharing authority, retention, patient burden, and controlled-patient yield.

**Confidence:** high that hypertension treatment efficacy is not the main unresolved question; high that medicine/device availability and continuity are necessary gates; moderate-high that task-sharing is a promising delivery strategy; moderate on portability of cost-effectiveness estimates across health systems.

## Uncertainty and limitations

- The 2024 community-intervention meta-analysis pools heterogeneous multicomponent interventions; its summary RR is not a portable effect for any single delivery model.
- The 2026 economic review contains only seven studies and mixes study designs and economic denominators.
- The team-based-care barrier survey used convenience samples and should not be treated as prevalence estimates for all LMIC systems.
- WHO medicine-availability data are country-reported and describe general availability, not patient-level uninterrupted access.
- Blood-pressure control is an intermediate outcome; reductions in cardiovascular events depend on persistence, baseline risk, and treatment duration.

## Recommended next assignment

If Worker D allocates another P03 exploration slot, choose **one high-burden country with public hypertension cascade and medicine/procurement data** and identify the dominant leakage point from diagnosis to durable control. Compare no more than two delivery packages only if medication availability, workforce costs, follow-up intensity, and control at a common horizon can be sourced. Otherwise stop the comparison and document the missing decision inputs.
