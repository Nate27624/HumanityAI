# Worker B independent verification: sport-health delivery contrast

Date: 2026-09-07
Task: AT0003 (parallel intervention-effectiveness evidence)
Problem: P05
Checked artifact: `research/worker-c-sport-health-contrast-2026-09-07.md`

## Verification result

**Reproduced with qualifications.** The 2025 Cochrane review (Hodder et al., CD012170) supports the core Worker C characterization that interventions delivered through sporting organisations probably produce a modest increase in moderate-to-vigorous physical activity, while evidence for several other health behaviours is weaker, null, or very uncertain.

Primary source checked:
https://www.cochrane.org/evidence/CD012170_do-programmes-offered-through-sporting-organisations-promote-healthy-behaviour-and-improve-peoples

Cochrane reports 20 included studies with 8,179 participants. Sporting-organisation interventions probably increased moderate-to-vigorous physical activity by about 7.4 minutes/day (SMD 0.36, 95% CI 0.22 to 0.49; 4 trials, 1,213 participants; moderate-certainty evidence). They may make little or no difference to sedentary behaviour (MD -15.18 minutes/day, 95% CI -30.82 to 0.47; 2 trials, 1,047 participants; low-certainty evidence) and may increase fruit and vegetable consumption (SMD 0.50, 95% CI 0.35 to 0.65; 5 trials, 1,402 participants; low-certainty evidence). Evidence was very uncertain for sugary-drink and alcohol consumption, while tobacco-use and unintended-adverse-consequence findings were equivocal in the few reporting trials.

## Important qualifications

- All 20 included studies were conducted in high-income countries.
- Most studies targeted adult sporting-organisation members or supporters, and 11 studies included only males; much of the evidence for key outcomes came from men with health-related risk factors and male football supporters.
- Certainty ranged from moderate to very low. Many RCT outcome assessments were at high risk of bias, often because outcomes were self-reported.
- The review explicitly emphasizes heterogeneity across interventions, participants, and sporting organisations.
- The 7.4-minute/day estimate is a modest behavioural effect, not evidence of large downstream health impact, cost-effectiveness, or broad benefit across settings.

## Relationship to E0005

This evidence does **not** overturn or directly contradict E0005. E0005 concerns participation in organised leisure-time sport among at-risk youth and broad developmental/risk outcomes. CD012170 evaluates health-promotion interventions implemented through sporting organisations, mostly among adults in high-income settings.

The Worker C ontology warning therefore survives independent review: HumanityAI should not infer from insufficient evidence for organised-sport participation as a youth-development intervention that interventions delivered through sporting organisations lack demonstrated effects. These are different intervention constructs, populations, and outcomes.

## Decision value

The useful update is construct separation rather than a generic conclusion that "sport works." If HumanityAI later promotes this evidence into `data/evidence.json`, the record should retain the delivery-channel distinction and population limits rather than attaching the result to sport participation broadly.

No machine-readable evidence change is made in this verification pass because the source supports a narrow, qualified intervention claim and the existing research note already captures the principal conclusion. The next promotion step should remain a separate reviewable decision.