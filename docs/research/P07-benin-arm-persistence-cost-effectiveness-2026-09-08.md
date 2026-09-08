# P07 Benin youth self-employment arms: persistence and cost-effectiveness bounds

Date: 2026-09-08  
Producer: Operator A  
Controller fallback assignment: after the bounded Bosnia cost search, extract Benin arm-specific persistence/cost-effectiveness without reopening global ALMP modality ranking.

## Decision delta

Benin's Youth Employment Project impact evaluation provides a substantially stronger within-study comparison than the canonical P07 routing note previously had: the randomized design separately identifies **training only**, **cash grant only**, **training + cash**, and control, follows outcomes for roughly **45 months after training / 38 months after grant**, and reports component-level per-capita delivery costs.

The decision-relevant result is not "training beats grants globally." It is narrower: **for this low-education, underemployed Benin sample and this specific delivery architecture, the training-only arm is the only arm with clear sustained gains in business performance and earnings at the longest follow-up, while grant-only has no primary business/earnings effect and adding the grant generally attenuates the training-only business-performance signal.** This makes human-capital/management constraints a more plausible binding constraint than start-up capital for the average participant in this study, while preserving important gender, welfare, implementation-quality, and portability caveats.

The report also provides an explicit implementation-cost anchor: **training cost about US$1,050 per beneficiary; the cash-grant component cost about US$629 per beneficiary.** The PDF text renders the latter as `US$ 629` followed by footnote marker `4`, which can appear in extracted text as `6294`; it is not a US$6,294 grant. The report's own back-of-the-envelope calculation says the training cost is recouped through the estimated earnings increment after about **36 months for men** and **64 months for women**, with the women's calculation requiring the assumption that the last observed earnings impact persists beyond follow-up.

**Routing implication for P07:** preserve Benin as evidence that constraint diagnosis and time horizon matter. For similar target populations, compare skill/management support against capital support only when delivery quality, participant baseline technical skills, gender constraints, cost accounting, and persistence are sufficiently comparable. Do not turn these Benin arm estimates into a portable global modality ranking.

Confidence: **high** on the within-study direction and reported component costs; **moderate-high** on the binding-constraint interpretation for this study population; **low** on portability to different entrepreneurship programs, populations, grant sizes, training quality, or macroeconomic settings.

## Primary source

Bossuroy, Thomas; Vaillant, Julia. 2022. *Final evaluation report of Benin's Youth Employment project*. World Bank / Government of Benin.

- Report: https://documents1.worldbank.org/curated/en/099005006302210770/pdf/P1477800853c6e050ba2403b0a1ba2239d.pdf
- World Bank microdata study description: https://microdata.worldbank.org/catalog/4044/study-description
- AEA RCT registry identified by the report: https://doi.org/10.1257/rct.232716

The report describes a randomized sample of 3,444 participants, with four equally sized groups: training + cash, training only, cash only, and pure control. The intervention targeted underemployed youth ages 18-35 with low education in 15 communes.

## Arm definitions

- **T1 — training + cash:** life/socioemotional skills + ILO Start and Improve Your Business training + follow-up coaching/home visits + unconditional start-up grant.
- **T2 — training only:** the same training/coaching package, no cash grant.
- **T3 — cash only:** unconditional grant, no training.
- **Control:** neither component.

The grant was designed as approximately US$400 at delivery. The later cost accounting is higher than the face value because component cost includes implementation and allocated project costs rather than only the transfer amount.

## Persistence / outcome horizon

Table 3 in the report gives the clean timing anchor:

- follow-up 1: ~15 months after training / ~8 months after grant;
- follow-up 2: ~27 months after training / ~20 months after grant;
- follow-up 3: ~45 months after training / ~38 months after grant.

A later sentence in the results section reverses the 38/45 labels. Because Table 3 explicitly maps timing to intervention sequence and is internally consistent with the program chronology, this note uses **45 months after training / 38 months after grant** and records the prose inconsistency rather than silently harmonizing it.

At the longest follow-up, the report states:

- training only had strong positive and significant impacts on business-performance measures for both women and men;
- training-only monthly earnings increased by roughly **US$16 for women** and **US$29 for men**;
- grant only had no effect on revenues, profits, or earnings for either women or men;
- training + grant effects were generally smaller than training only on business performance, with especially clear attenuation/null effects for women;
- grant recipients did show welfare/asset effects in some dimensions, so null business-performance effects must not be rewritten as "the grant produced no benefit";
- women receiving training + grant created paid jobs even though their own business profits did not improve, showing that owner earnings and employment spillovers are distinct outcomes.

## Cost accounting and what can safely be compared

The report states that it ran a component cost analysis and reports:

- **training: US$1,050 per beneficiary**;
- **cash-grant component: US$629 per beneficiary**.

Its footnote says component costs include prorated general project management, sensitization/communication, enrollment and lottery costs, monitoring/supervision, training design/trainer preparation/delivery, grant amounts, and payment fees.

The report then performs a simple earnings-payback calculation for **training only**:

- men: cost recouped after about **36 months**;
- women: cost recouped after about **64 months**, assuming the last observed earnings effect persists beyond the final follow-up.

### Do not over-derive a combined-arm unit cost

The report does not present a single explicit per-beneficiary cost for T1 in the same passage. Although T1 receives both components, simply adding US$1,050 + US$629 could be misleading if shared/prorated implementation items overlap or if assignment-specific delivery differs. Until an accounting table explicitly confirms additivity, keep the T1 unit cost **unresolved rather than derived**.

### Do not call payback a full cost-effectiveness estimate

The 36/64-month figures are a simple undiscounted earnings-payback calculation, not a social benefit-cost ratio. They do not monetize business spillovers, paid jobs created, assets, welfare, taxes, opportunity cost of participant time, general equilibrium effects, displacement, or fiscal financing costs. The women's figure extrapolates beyond observed follow-up.

## Why the training-only result may not transport

Several mechanisms in the report make this a delivery-specific result rather than a modality constant:

1. **High take-up and local delivery.** Around 99% attended at least one training session, with sessions decentralized to reduce travel barriers.
2. **Substantial socioemotional content.** The package was not generic business training; it included life skills, personal initiative, financial literacy, business modules, individual counseling, and follow-up visits.
3. **Gender-informed participation supports.** Transport, meals, local delivery, and childcare accommodation were built into implementation.
4. **Baseline technical skills.** The report notes that many participants had prior technical training/apprenticeship, potentially making management and socioemotional skills unusually complementary to existing productive skills.
5. **Grant capture/redistribution and investment quality.** The report discusses intra-household transfers and suboptimal investment as plausible mechanisms behind weak grant effects, particularly for women.
6. **Outcome heterogeneity.** Grant arms can improve assets/expenditures or job creation even when owner profits/earnings do not rise.

## Current P07 decision rule

- **START:** use Benin as a within-study binding-constraint comparison where capital and skills were experimentally separated.
- **MORE:** comparable studies with explicit arm costs, long follow-up, implementation/take-up data, and outcomes separated by participant earnings, profits, job creation, and welfare.
- **LESS:** short-horizon conclusions that miss slowly emerging human-capital returns.
- **STOP:** treating cash-transfer face value as total program cost, converting the Benin result into a universal training-vs-capital ranking, or constructing a scalar cross-study ranking without common cost/outcome horizons.

## Recommended next action for Worker D

This closes the specific Benin persistence/cost gap identified after PR #87 well enough to update P07 routing, subject to independent Worker C verification. If C confirms the report extraction and denominator handling, D can integrate this note and reduce further P07 producer compute unless a concrete downstream decision requires a comparable second study or a verified T1 combined-arm unit cost.
