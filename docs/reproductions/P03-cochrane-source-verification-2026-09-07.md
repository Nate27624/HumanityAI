# P03 Cochrane intervention source verification — 2026-09-07

**Scope:** independent source-fidelity check of three recent Cochrane reviews surfaced in the P03 health/problem brief. This note verifies what the cited reviews actually report; it does **not** by itself promote them into canonical `data/evidence.json`, establish cost-effectiveness, or recommend implementation.

**Task context:** AT0003 / P03 intervention-effectiveness evidence, with deliberate attention to null, mixed, intermediate-outcome, and external-validity findings.

## Result summary

| Review | Verification result | Main decision-useful conclusion |
| --- | --- | --- |
| Smartphone apps for overweight/obesity (2024) | **Verified / qualified** | Long-term clinically meaningful benefit is not clearly demonstrated; several medium/long-term outcomes show little or no difference, and certainty/generalizability are limited. |
| Psychosocial mental-health promotion in humanitarian crises (2024) | **Verified / qualified** | Randomized evidence for positive mental-health promotion remains scant and inconclusive, especially for children/adolescents and for outcomes beyond short-term adult well-being. |
| Lay first-aid training (2025) | **Verified / qualified** | Training probably improves short-term knowledge, skills, and self-efficacy, but recipient health outcomes and real-world first-aid quality were not evaluated in the included evidence. |

The central claims in `docs/problem-briefs/P03-health-preventable-suffering.md` are faithful to these source pages. The strongest cross-cutting lesson is an **outcome-hierarchy warning**: adoption, engagement, training performance, or measured capability can improve without evidence yet showing durable final health outcomes.

## 1. Smartphone weight-management apps

**Source:** Cochrane, *Mobile health (m-health) smartphone interventions for adolescents and adults with overweight or obesity*, published 20 February 2024.  
https://www.cochrane.org/evidence/CD013591_smartphone-apps-people-overweight-or-obesity

**Review design checked:** randomized controlled trials; search date 2 October 2023; follow-up at least three months; integrated smartphone apps using at least two behaviour-change techniques.

**Reproduced facts:**

- 18 studies with 2,703 participants were included; 16 studies involved adults and two involved adolescents.
- 34 additional studies were ongoing at the time of the review.
- For adults versus no/minimal intervention, 12-month BMI change showed little to no difference in the reported study, while 12-month body-weight change may show little to no difference and 24-month body-weight change probably shows little to no difference.
- Quality of life, well-being, and dietary-behaviour outcomes at longer follow-up generally showed little to no difference.
- The review concludes that available evidence does not demonstrate a clear benefit and that effects are generally minor and mostly not clinically significant.

**Important qualification:** the evidence does not support a blanket claim that all mobile/digital health tools are ineffective. Apps differed in features and components; adolescent evidence was sparse; and evidence was scarce in low- and middle-income countries and across socioeconomic/cultural groups.

**Status:** `verified / qualified`.

## 2. Mental-health promotion in humanitarian crises

**Source:** Cochrane, *Psychological and social interventions for the promotion of mental health in people living in low- and middle-income countries affected by humanitarian crises*, published 21 May 2024.  
https://www.cochrane.org/evidence/CD014300_do-psychological-and-social-interventions-promote-improved-mental-health-people-living-low-and

**Review design checked:** randomized controlled trials comparing psychosocial interventions with inactive/control conditions; studies enrolling participants because of a diagnosed mental disorder or positive screening threshold were excluded. Evidence was searched through January 2023.

**Reproduced facts:**

- 13 RCTs with 7,917 participants were included: nine in children/adolescents and four in adults.
- For children/adolescents, there was no clear difference in mental well-being or prosocial behaviour at endpoint; certainty was low or very low.
- One small child/adolescent trial suggested improved functioning, but the evidence was very uncertain.
- In adults, the source reports encouraging evidence of a slight improvement in mental well-being, but evidence was limited and did not cover other positive mental-health dimensions well.
- The authors conclude that randomized evidence is scant and inconclusive and is insufficient for firm practice or policy implications.

**Important qualification:** this review addresses **promotion of positive mental health**, not treatment effectiveness for PTSD, depression, anxiety, or other diagnosed disorders. It should not be generalized to therapeutic interventions for clinically selected populations.

**Status:** `verified / qualified`.

## 3. Lay first-aid training

**Source:** Cochrane, *First aid training for laypeople*, published 12 August 2025; latest search 16 December 2024.  
https://www.cochrane.org/evidence/CD015538_first-aid-training-laypeople-effective

**Review design checked:** physical-health first-aid training for people without formal healthcare education, compared with other training or no training.

**Reproduced facts:**

- 36 studies with 15,657 participants were included; 17 involved adults and 19 involved children/adolescents.
- Only two studies were conducted in a low-income country (Nigeria), limiting transferability to low-resource settings.
- No included study provided evidence on health outcomes of people receiving first aid or on the quality of first aid delivered in real-life emergencies.
- One study with 3,070 people examined helping behaviour but did not provide enough data to determine an effect.
- In the short term, training probably improves first-aid knowledge (8 studies, 3,515 participants), skills (12 studies, 3,063 participants), and self-efficacy (2 studies, 285 participants).
- Evidence on willingness to help was uncertain.

**Important qualification:** educational gains are meaningful outcomes, but they are not substitutes for evidence that trainees act in real emergencies, provide higher-quality care, or improve recipient health outcomes.

**Status:** `verified / qualified`.

## Cross-review implications for HumanityAI

1. **Prefer final outcomes when the decision question is health improvement.** Intermediate outcomes such as engagement, knowledge, skills, diagnoses, or service use can be useful but should not be silently upgraded into morbidity/mortality/quality-of-life claims.
2. **Preserve null and uncertain evidence.** High plausibility or widespread adoption is not equivalent to demonstrated effectiveness.
3. **Keep population and setting boundaries explicit.** Sparse adolescent, low-income-country, humanitarian-setting, or culturally diverse evidence constrains transferability.
4. **Do not infer cost-effectiveness.** None of these source checks establishes that the intervention is a good use of marginal resources relative to alternatives.
5. **Do not infer HumanityAI comparative advantage.** Verification improves the evidence map; it does not imply HumanityAI should implement or advocate these interventions.

## Integration recommendation

These three reviews are strong candidates for canonical P03 evidence records because each adds a distinct, decision-useful negative or qualifying finding and has now received an independent source-fidelity check. Before machine-readable integration, the integrating worker should re-read the live `data/evidence.json`, select non-colliding IDs, preserve the source-specific certainty language, and run all relevant validators. No current canonical record should be overwritten merely to force these findings into the registry.

**Checked:** 2026-09-07  
**Produced by:** HumanityAI Adaptive Worker A; external Cochrane sources remain the evidentiary authority.