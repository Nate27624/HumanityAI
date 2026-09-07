# P03 — Health and preventable suffering

**Status:** early synthesis, reviewed 2026-09-07  
**Problem definition:** preventable illness, disability, premature death, mental distress, gaps in effective care, and health-system constraints that reduce people's ability to live lives they value.

This brief synthesizes current HumanityAI records plus a small set of recent systematic reviews that expose important evidence gaps. It is not a priority ranking, a medical recommendation, or a claim that health can be represented by one metric.

## What the current evidence says

### Essential-service coverage remains incomplete at global scale

HumanityAI indicator [`I0002`](../../data/indicators.json) records the World Health Organization estimate that **about 4.6 billion people were not fully covered by essential health services in 2023**. This is a service-coverage measure, not a direct count of preventable deaths, untreated diagnoses, low-quality care, or people who cannot afford care.

Source: World Health Organization, *Universal health coverage (UHC)* (updated 5 December 2025): https://www.who.int/news-room/fact-sheets/detail/universal-health-coverage-%28uhc%29

The baseline therefore supports a broad access problem while leaving several distinct dimensions unresolved: service quality, financial protection, geographic access, workforce capacity, preventable disease burden, mental health, and whether available services actually improve outcomes.

### Cash transfers can improve some health-related determinants without improving every health-service outcome

HumanityAI evidence record [`E0001`](../../data/evidence.json) summarizes a 2022 Cochrane review of unconditional cash transfers in low- and middle-income countries. The review found benefits for several welfare outcomes, including food security and dietary diversity, but little or no effect on a summary measure of health-service use.

That distinction matters for P03: an intervention can improve material determinants of health without reliably increasing measured healthcare use, and healthcare use itself is an intermediate outcome rather than proof of improved health.

Source: Cochrane, *Unconditional cash transfers for reducing poverty and vulnerabilities: effect on use of health services and health outcomes in low- and middle-income countries* (29 March 2022): https://www.cochrane.org/evidence/CD011135_does-giving-money-people-low-and-middle-income-countries-without-conditions-attached-lead-better

### Embedding financial services in healthcare has not yet demonstrated robust health or financial effects

HumanityAI evidence record [`E0002`](../../data/evidence.json) summarizes a 2024 Campbell systematic review of medical-financial partnerships in the United States. Only four studies met inclusion criteria; financial effects were generally small and statistically non-significant, while one study found improvements in appointment attendance and vaccination adherence.

The appropriate conclusion is **insufficient evidence**, not that financial stress is irrelevant to health or that these partnerships cannot work. The current evaluations are too few, small, heterogeneous, and methodologically limited to support a general effectiveness claim.

Source: Campbell Collaboration, *Medical-financial partnerships for improving financial and medical outcomes for lower-income Americans: A systematic review* (November 2024): https://www.campbellcollaboration.org/review/medical-financial-partnerships-for-improving-financial-and-medical-outcomes-for-lower-income-americans-a-systematic-review/

### More diagnosis is not automatically better health

HumanityAI evidence record [`E0007`](../../data/evidence.json) summarizes and independently reproduces the 2019 Cochrane review of broad general health checks for adults not selected for a specific disease or risk factor. Across large randomized evidence, general checks had little or no effect on all-cause or cancer mortality and probably little or no effect on cardiovascular mortality, even though some diagnoses increased.

This is a useful guardrail for the wider project: **diagnostic activity, screening volume, app engagement, appointment counts, or service adoption should not be substituted for final health outcomes without evidence linking them.** The result does not apply to symptom-driven care, disease-specific screening, or targeted prevention for high-risk groups.

Source: Cochrane, *General health checks for reducing illness and mortality* (30 January 2019): https://www.cochrane.org/evidence/CD009009_general-health-checks-reducing-illness-and-mortality

## Additional intervention evidence worth integrating

The following recent systematic reviews are not yet canonical HumanityAI evidence records. They are included as source-grounded context and should be independently checked before machine-readable integration.

### Smartphone weight-management apps: widespread plausibility, limited demonstrated long-term benefit

A 2024 Cochrane review included **18 randomized studies with 2,703 participants** evaluating integrated smartphone apps for adolescents and adults with overweight or obesity. Compared with no or minimal intervention, the review found little or no difference in BMI at 12 months and little or no difference in body weight at 12 or 24 months; quality of life, well-being, and dietary-behaviour measures also showed little or no difference at longer follow-up. Evidence for some shorter-term BMI effects was very uncertain.

The evidence was especially sparse for adolescents, low- and middle-income countries, and people from different socioeconomic and cultural backgrounds. Thirty-four additional studies were ongoing when the review searched through 2 October 2023.

This is a high-value negative/qualifying result because digital availability, low marginal distribution cost, downloads, or engagement do not establish clinically meaningful benefit. It also does not establish that all digital health tools are ineffective: app design, population, comparator, intensity, and integration with human support vary substantially.

Source: Cochrane, *Mobile health (m-health) smartphone interventions for adolescents and adults with overweight or obesity* (20 February 2024): https://www.cochrane.org/evidence/CD013591_smartphone-apps-people-overweight-or-obesity

### Mental-health promotion in humanitarian crises: urgent need, scant randomized evidence

A 2024 Cochrane review included **13 randomized controlled trials with 7,917 participants** evaluating psychosocial interventions intended to promote positive mental health among people living in low- and middle-income countries affected by humanitarian crises. Nine trials involved children or adolescents and four involved adults.

For children and adolescents, the review found no clear difference in mental well-being or prosocial behaviour at the end of treatment, with low or very-low certainty. One small trial suggested improved functioning, but the evidence was very uncertain. Among adults, three trials suggested a slight improvement in mental well-being at treatment end, but evidence was low-certainty and the effect may not persist at follow-up. The review concluded that randomized evidence remains scant and inconclusive.

This is not evidence that psychosocial support is unimportant in crises. It shows a large gap between humanitarian need, plausible mechanisms, programme delivery, and confidently measured positive-mental-health outcomes. Studies also excluded participants enrolled because of a diagnosed mental disorder, so the finding should not be generalized to treatment of PTSD, depression, anxiety, or other diagnosed conditions.

Source: Cochrane, *Psychological and social interventions for the promotion of mental health in people living in low- and middle-income countries affected by humanitarian crises* (21 May 2024): https://www.cochrane.org/evidence/CD014300_do-psychological-and-social-interventions-promote-improved-mental-health-people-living-low-and

### Lay first-aid training: educational gains are better established than real-world health outcomes

A 2025 Cochrane review identified **36 studies with 15,657 participants** who had no formal healthcare education. First-aid training probably improved knowledge, skills, and self-efficacy in the short term. However, the review found **no studies measuring effects on the health outcomes of people receiving first aid or the quality of first aid delivered in real emergencies**, and only one study addressed real-world helping behaviour with insufficient data for a conclusion.

This is another example of an intermediate-outcome gap: successful training can improve measured capability without establishing how often people act, how well they perform under real conditions, or whether recipients experience better health outcomes. Only two studies were conducted in a low-income country, further limiting global transferability.

Source: Cochrane, *First aid training for laypeople* (12 August 2025; searches through 16 December 2024): https://www.cochrane.org/evidence/CD015538_first-aid-training-laypeople-effective

## What is not yet established

Current HumanityAI records do **not** establish:

- a single defensible scalar measure of preventable suffering, healthcare access, care quality, mental health, disability, and financial protection;
- which health-system bottleneck has the highest marginal global value to address;
- that increased healthcare use, diagnosis, training performance, app engagement, or programme adoption implies improved health outcomes;
- which intervention families are most cost-effective after accounting for implementation capacity, opportunity cost, and distribution;
- whether effects measured in high-income health systems transfer to low-resource, conflict-affected, rural, or institutionally different settings;
- the comparative value of prevention, treatment, social determinants, public-health infrastructure, and health-system strengthening across contexts;
- HumanityAI's comparative advantage in implementing, funding, recommending, or advocating any health intervention.

## High-value next evidence

1. **Complementary global baselines.** Add final-outcome measures such as avoidable mortality or healthy-life loss alongside service coverage, while explicitly handling overlap and model uncertainty.
2. **Financial protection.** Add authoritative catastrophic or impoverishing health-expenditure measures rather than treating service coverage as affordability.
3. **Care quality.** Identify a defensible global measure of effective coverage or quality; nominal access and effective care are not interchangeable.
4. **Mental health.** Add burden and treatment-gap baselines plus intervention syntheses that distinguish promotion, prevention, and treatment.
5. **Intervention integration.** Independently verify the three recent Cochrane reviews above before canonicalizing them in `data/evidence.json`.
6. **Cost-effectiveness.** Where credible comparative estimates exist, preserve resource requirements and uncertainty rather than ranking interventions by effect direction alone.
7. **Distribution and rights.** Record who gains access, who bears costs, consent and stigma concerns, disability inclusion, rural access, sex/gender differences, and effects on groups underserved by current systems.
8. **Outcome hierarchy.** Prefer morbidity, mortality, functioning, quality of life, and validated well-being outcomes over proxies when the research question is health improvement.

## Rights and distribution cautions

Health interventions can expand freedom by reducing pain, disability, premature mortality, uncertainty, and financial risk. They can also impose burdens through coercive treatment, privacy loss, stigma, unequal access, medical debt, surveillance, discrimination, or opportunity costs from low-value care.

P03 analysis should therefore preserve informed consent, patient autonomy, disability rights, privacy, cultural differences, and distributional effects alongside aggregate health outcomes. A population-average benefit does not make every implementation acceptable, and a null average effect does not rule out important subgroup benefits or harms.

## Current HumanityAI records used

- Problem taxonomy: [`PROBLEM_MAP.md`](../../PROBLEM_MAP.md)
- Baseline indicator: [`I0002`](../../data/indicators.json)
- Intervention evidence: [`E0001`](../../data/evidence.json), [`E0002`](../../data/evidence.json), [`E0007`](../../data/evidence.json)

The external sources remain the evidentiary authority. This brief is HumanityAI-authored synthesis and should be revised when stronger, newer, contradictory, or more distribution-sensitive evidence is added.
