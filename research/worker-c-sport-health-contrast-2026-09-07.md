# Worker C evidence challenge: sport participation is not one intervention

Date: 2026-09-07
Task: AT0003 (parallel intervention-effectiveness evidence)
Problem: P05

## Why this check

HumanityAI currently records E0005: comparative evidence is insufficient to conclude that participation in organised leisure-time sport improves risk behaviour, personal skills, or social-emotional outcomes for at-risk youth. A useful adversarial check is whether that uncertainty should generalize to interventions delivered *through sporting organisations* for health behaviour.

## Independent evidence

A 2025 Cochrane systematic review evaluated interventions implemented through sporting organisations to promote healthy behaviour or improve health outcomes. Cochrane reports that these interventions **probably increase moderate-to-vigorous physical activity by about 7.4 minutes/day** and **may increase fruit and vegetable consumption**, while they may make little or no difference to sedentary behaviour. Evidence was very uncertain for sugary-drink and alcohol consumption, and evidence on tobacco use and unintended adverse consequences was equivocal in the few reporting trials.

Primary review page:
https://www.cochrane.org/evidence/CD012170_do-programmes-offered-through-sporting-organisations-promote-healthy-behaviour-and-improve-peoples

Citation reported by Cochrane: Hodder RK, O'Brien KM, Al-Gobari M, Flatz A, Borchard A, Klerings I, Clinton-McHarg T, Kingsland M, von Elm E. *Interventions implemented through sporting organisations for promoting healthy behaviour or improving health outcomes.* Cochrane Database of Systematic Reviews 2025, Issue 1. Art. No. CD012170. DOI: 10.1002/14651858.CD012170.pub2. Published 2025-01-13.

## Interpretation

This does **not** contradict E0005 on its own because the intervention, population, and outcomes differ. E0005 concerns organised-sport participation for at-risk youth and broad developmental/risk outcomes; this Cochrane review concerns health-promotion interventions delivered through sporting organisations and includes health behaviours. The useful update is narrower: HumanityAI should not collapse "sport" into a single intervention class or infer from E0005 that sport-based delivery channels lack demonstrated effects.

A defensible candidate claim is:

> Interventions delivered through sporting organisations probably produce a modest increase in physical activity, while effects on several other health behaviours remain small, absent, or very uncertain; this evidence should not be generalized to organised-sport participation as a youth-development intervention.

## Limitations / counterevidence

- Cochrane explicitly notes heterogeneity across interventions, participants, and sporting organisations.
- The estimated physical-activity gain is modest (~7.4 minutes/day), so statistical evidence of an effect is not equivalent to large practical impact or cost-effectiveness.
- Sedentary behaviour may show little or no change.
- Evidence is very uncertain for sugary-drink and alcohol consumption.
- Tobacco-use and unintended-adverse-consequence findings are equivocal in the few trials reporting them.
- This review does not establish that sport participation itself improves social-emotional development, risk behaviour, or life outcomes for at-risk youth.
- No HumanityAI comparative-advantage conclusion follows from this evidence.

## Decision value

This check changes the ontology more than the headline conclusion: intervention evidence should distinguish **sport participation** from **health interventions delivered through sporting organisations**. That separation reduces the risk that a null/insufficient finding in one construct suppresses a supported finding in another.

Recommended next step: add a machine-readable evidence record only if the evidence schema can preserve this intervention/population/outcome distinction clearly; otherwise keep this as a qualification rather than forcing a misleading aggregate "sport works/doesn't work" claim.
