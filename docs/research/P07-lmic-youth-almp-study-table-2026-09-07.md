# P07 study-level LMIC youth ALMP comparison

Date: 2026-09-07  
Producer: Operator B (exploration)  
Status: Tier-2 decision-bearing research candidate; requires independent Worker C verification and Worker D integration.

## Assignment

Worker D directed Operator B to move beyond global youth-ALMP modality averages and extract a small study-level comparison of employment-services and entrepreneurship interventions in low- and middle-income settings. Required fields include cost definition, bundle components, provider capability, employer linkage, target population, duration, persistence, adoption constraints, and evidence quality. If the studies are not comparable enough for a scalar ranking, the correct output is insufficient comparability.

## Decision delta

**Do not build a youth-ALMP scalar ranking yet.** The study-level evidence changes the decision problem from “employment services versus entrepreneurship” to **which constraint is binding, for which target population, under which delivery architecture, and over what horizon?**

**START** using study archetypes and explicit constraint diagnosis before allocating more compute to pooled modality rankings.

**MORE** compute on service take-up, employer-side demand and willingness to interview/hire, persistent earnings/employment after treatment exit, true incremental delivery cost, and targeting/cream-skimming.

**LESS** compute on modality labels without program architecture.

**STOP** treating the roughly $230 versus $730 global descriptive median-cost contrast as portable enough to imply that employment services dominate entrepreneurship in LMICs.

Confidence: **high** that scalar comparability is currently insufficient; **moderate-high** that binding-constraint diagnosis should determine the next study cells; **moderate** on the exact portability of the individual studies below.

## Small study-level table

| Study / context | Modality and bundle | Target population | Provider / required capability | Employer linkage | Cost definition available | Outcome and persistence | Adoption / external-validity constraint | Evidence quality |
|---|---|---|---|---|---|---|---|---|
| **Groh et al. 2015, Jordan NOW 2.0** | Employment services: psychometric testing plus intensive manual matching of screened graduates to firms | 1,354 recent university/community-college graduates around Amman; 1,011 assigned to matching treatment | Specialized screening, psychometric assessment, employer outreach, rapid candidate filtering and repeated follow-up | **Direct and intensive**; staff solicited vacancies and sent firms selected candidate CVs | Approx. **$204,800 total implementation** including $28,800 assessment design/validation, $146,000 enrollment/testing/matching, and about $30,000 firm listing; authors estimate **$22,755 per directly matched job lasting >1 month** ($19,556 excluding setup) | More than 1,000 matches generated only **9 jobs lasting >1 month**; ITT employment and salary effects were small and statistically insignificant. Endline was about five months after matching ended | Funnel loss occurred on both sides: only 134 of 2,454 contacted firms had openings they wanted help filling, firms declined to interview candidates in 55% of matches, candidates declined 28% of match opportunities, and 30/54 offers were rejected. Formal matching was solving a weakly binding constraint for this educated group | Randomized experiment; unusually strong implementation/cost documentation; narrow educated-urban target |
| **Balavac-Orlic et al. 2024, Bosnia and Herzegovina** | Employment services: counseling/profiling versus counseling plus active matching by a private provider paid for placements | Registered jobseekers; especially relevant subgroup under 30 and lower-educated workers | Private employment-service provider with counselor discretion and employer relationships | **Direct**; specific introductions/referrals plus general CV forwarding | Study describes matching as costly to provider, but the source reviewed in this pass does **not expose a standardized per-participant program cost suitable for cross-study comparison** | Matching increased formal employment about **5.8 pp** at 3–6 months and **4.1 pp** at 21–24 months in the administrative-data specification; under-30 effects were larger (about 9.3 pp short-run, 7.8 pp medium-run) | Only about 23% of treated jobseekers received specific matching; counselor employability ratings predicted who received intensive matching, creating a **cream-skimming / targeting** concern. Long-term unemployed did not benefit significantly | Random assignment between service intensities; strong administrative follow-up; cost field incomplete for current comparison |
| **Benin Youth Employment Project, World Bank impact evaluation / completion documentation** | Entrepreneurship support: business + socio-emotional skills training, cash grant, full bundle, and control in separate randomized arms | Unemployed/underemployed youth; program deliberately included women and vulnerable/self-employed participants | Government program plus training delivery capable of business and socio-emotional instruction; beneficiaries often already had a trade/apprenticeship background | **No direct employer linkage**; intervention targets self-employment/productive activity | Completion analysis reports about **$1,050 per capita for training** and **$629 for the cash-grant component**. Grant arm allowed up to roughly $400 nominal grant value; cost figure includes more than transfer face value | Training improved business practices and skills; completion documentation reports monthly earnings increases of about **$16 for women and $29 for men** and describes effects as sustained in the available follow-up. Short-term profit results were less clear | Existing trade-specific skills may be an important complement; effects should not be generalized to youth without viable self-employment opportunities or local product demand | Multi-arm randomized impact evaluation; cost data available; treatment bundle differs fundamentally from matching services |
| **Blattman, Fiala & Martinez 2020, Uganda Youth Opportunities Program** | Entrepreneurship capital: group-based unconditional grants intended for vocational training, tools and materials for skilled self-employment | Young adults aged roughly 16–35 who self-organized into groups and submitted business/training proposals | Government transfer administration; groups themselves selected activities, budgeting and training; low ongoing provider intensity | **No employer linkage**; self-employment pathway | About **$400 per person** (reported average around $382 in contemporary summaries), roughly one year of youth income at the time; transfer itself is the dominant program resource | At four years grants raised work about **17%** and earnings about **38%**; by **nine years employment, earnings and consumption had converged** with controls, though durable assets and skilled occupational choice remained higher | Requires motivated groups able to propose and organize skilled-trade investments. Long-run convergence means a short-horizon earnings comparison would materially overstate persistent advantage | Randomized allocation among approved groups; nine-year follow-up provides unusually strong persistence evidence |

## What this table changes

### 1. Employment services are not one treatment

Jordan and Bosnia point in opposite directions without contradicting one another. Jordan's highly intensive matching system generated almost no durable direct placements among educated graduates because the funnel lost opportunities on both sides: few contacted firms had suitable openings they wanted help filling, firms often declined to interview matched candidates, and workers also rejected interviews/offers or quit. Bosnia's private-provider matching improved formal employment, particularly for younger and lower-educated jobseekers, but provider incentives also produced targeting/cream-skimming risk.

The decision variable is therefore not “matching works.” It is closer to:

> **Are information/referral frictions actually binding for the target group, are enough suitable vacancies available, are employers willing to interview and hire referred candidates, are workers willing to accept the available job attributes, and can a provider create additional matches without selecting only easy-to-place clients?**

Jordan is a strong **STOP** signal for scaling elaborate matching where employer demand/selection, reservation-job attributes, or worker preferences dominate search frictions.

Bosnia is a **MORE** signal for direct-referral models aimed at younger/lower-skill jobseekers, conditional on obtaining program cost and guarding against cream-skimming.

### 2. Entrepreneurship effects can be real but horizon-sensitive

Benin shows that a higher-cost training/capital package can raise earnings and business capabilities where beneficiaries have trades and self-employment is a plausible margin. Uganda shows why persistence must be coded explicitly: a roughly $400 grant produced large four-year earnings gains but no nine-year employment/earnings/consumption gap as controls caught up.

Thus “entrepreneurship has larger LMIC effects” is not enough for allocation. The relevant question is whether the objective values **accelerated income and capital formation**, **persistent lifetime earnings**, or **structural occupational change**. Those lead to different conclusions from the same Uganda study.

### 3. Current cost fields are not denominator-compatible

The four rows use materially different denominators:

- Jordan reports total implementation cost and cost per directly matched durable job;
- Bosnia currently lacks a comparable exposed unit-cost figure in the reviewed source;
- Benin reports per-capita component cost for training and grants;
- Uganda is dominated by a direct transfer per recipient.

These cannot be converted honestly into one cost-effectiveness ranking without additional extraction and a common outcome/time horizon. In particular, Jordan's cost-per-placement denominator is not comparable to Benin/Uganda cost-per-assigned-participant.

## Binding-constraint routing rule

For future P07 compute, route a candidate intervention according to the diagnosed constraint:

1. **Search/referral friction + enough suitable vacancies + employers willing to interview/hire referred candidates + workers willing to accept available job attributes** -> explore direct employment matching.
2. **Search friction but provider incentives favor easy cases** -> require targeting safeguards and subgroup effects before scaling.
3. **Capital constraint + viable self-employment demand + participants have/obtain productive skills** -> explore grants/entrepreneurship bundles.
4. **Short-run capital constraint but controls can self-finance over time** -> value acceleration explicitly; do not count temporary income gaps as permanent poverty reduction.
5. **No evidence the modality addresses the binding constraint** -> stop before detailed cost-effectiveness modeling.

## Highest-value next extraction

**Priority 1: Bosnia incremental cost.** Obtain the contract/payment schedule and realized cost per assigned participant (and ideally per additional formal job), separating counseling base cost from incremental matching. This is the missing field most likely to determine whether Bosnia-style employment services remain competitive with entrepreneurship support.

**Priority 2: Benin outcome horizon and component-level cost-effectiveness.** Reproduce follow-up timing and treatment-arm earnings/employment estimates directly from the impact-evaluation report, keeping training-only, grant-only and bundle arms separate.

**Priority 3: one low-income employment-service study with a less educated population.** Jordan is upper-middle-income and highly educated; Bosnia is middle-income. A lower-income public-employment-service or low-tech referral experiment would test portability to the populations driving the broader LMIC synthesis.

## Recommendation to Worker D

**START** a binding-constraint decision tree for P07 that treats employer-side suitable-vacancy demand and willingness to interview/hire as first-class gates alongside worker acceptance.  
**MORE** Bosnia cost extraction and Benin arm-specific persistence/cost-effectiveness.  
**LESS** global pooled effect/cost medians.  
**STOP** any UCT-vs-ALMP or employment-services-vs-entrepreneurship scalar comparison that does not normalize outcome horizon, denominator, implementation bundle, and the relevant employer/worker adoption funnel.

This result should redirect multiple future slots: the highest-value uncertainty is now specific missing study-level cost/persistence data, not another meta-analysis.

## Sources consulted as untrusted evidence

- Groh, McKenzie, Shammout & Vishwanath (2015), *Testing the importance of search frictions and matching through a randomized experiment in Jordan*, IZA Journal of Labor Economics: https://link.springer.com/article/10.1186/s40172-015-0022-8
- World Bank microdata, Jordan screening and matching experiments 2011–2013: https://microdata.worldbank.org/catalog/2183
- Balavac-Orlic, Giles, Hari & Ovadiya (2024), World Bank Policy Research Working Paper 10826: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099503006262434572/private-provisioning-of-employment-services-experimental-evidence-from-bosnia-and-herzegovina
- World Bank, *Benin Youth Employment Project* completion/evaluation documentation: https://documents1.worldbank.org/curated/en/403641578585719691/pdf/Benin-Youth-Employment-Project.pdf
- World Bank impact-evaluation documentation for the Benin Youth Employment Project: https://documents1.worldbank.org/curated/en/099005006302210770/pdf/P1477800853c6e050ba2403b0a1ba2239d.pdf
- Blattman, Fiala & Martinez (2020), *The Long-Term Impacts of Grants on Poverty: Nine-Year Evidence from Uganda's Youth Opportunities Program*, American Economic Review: Insights, DOI 10.1257/aeri.20190224: https://pubs.aeaweb.org/doi/10.1257/aeri.20190224
