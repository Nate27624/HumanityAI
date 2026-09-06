# Impact and Prioritization Model — v0.1

HumanityAI should not assume that improving its knowledge base automatically means improving humanity. The project needs an explicit process for deciding which problems, uncertainties, interventions, and tools deserve attention.

This file is a starting framework, not a final moral formula.

## Objective

Prioritize work that has a strong evidence-based chance of expanding human capability, liberty, safety, health, opportunity, understanding, and peaceful cooperation while respecting equivalent freedoms and avoiding unjustified concentration of power.

## Do not collapse everything into one permanent score

A single scalar objective can hide value conflicts and false precision. Keep the underlying dimensions visible and preserve uncertainty.

For candidate work, estimate the following separately when possible:

### 1. Scale
How many people or future people could be materially affected, and how large could the effect be?

### 2. Severity / capability constraint
How strongly does the problem restrict basic safety, health, agency, rights, opportunity, knowledge, or peaceful coexistence?

### 3. Tractability
Given currently available technology, institutions, resources, and legal authority, how plausible is meaningful progress?

### 4. Neglectedness
Is high-quality effort already abundant, or are important research/action gaps underserved?

### 5. Evidence strength
How strong, current, diverse, and causally relevant is the evidence that the proposed action would help?

### 6. Rights and coercion risk
Could the intervention expand aggregate outcomes while reducing fundamental freedoms, consent, privacy, pluralism, or minority protections?

### 7. Distributional effects
Who gains? Who loses? Are benefits concentrated among people already well served while burdens fall on vulnerable groups?

### 8. Reversibility
If the project is wrong, can the action be cheaply stopped or reversed?

### 9. Information value
Would a small experiment or research effort substantially reduce uncertainty for future high-impact decisions?

### 10. Systemic / second-order effects
Could the intervention alter incentives, institutions, power concentration, trust, environmental stability, conflict risk, or other problems outside its immediate target?

### 11. Comparative advantage
Is HumanityAI unusually capable of contributing, or would another organization likely use the same resources better?

### 12. Opportunity cost
What promising work will not happen if this task is chosen?

## Priority records

When prioritizing major research or interventions, preserve the vector rather than only a score:

```json
{
  "candidate_id": "...",
  "scale": {"estimate": null, "confidence": null},
  "severity": {"estimate": null, "confidence": null},
  "tractability": {"estimate": null, "confidence": null},
  "neglectedness": {"estimate": null, "confidence": null},
  "evidence_strength": {"estimate": null, "confidence": null},
  "rights_risk": {"estimate": null, "confidence": null},
  "distributional_notes": [],
  "reversibility": {"estimate": null, "confidence": null},
  "information_value": {"estimate": null, "confidence": null},
  "systemic_effects": [],
  "comparative_advantage": {"estimate": null, "confidence": null},
  "opportunity_costs": [],
  "major_uncertainties": [],
  "value_assumptions": [],
  "decision": null
}
```

## Research versus action

Early HumanityAI should usually prefer **high-information, reversible research and tooling** over direct high-impact intervention. A strong research result may reveal that another existing organization should execute the intervention instead.

The project should not confuse "we identified a high-impact action" with "we should personally execute it."

## Counterfactual impact

Ask:

> What changes because HumanityAI exists that probably would not have happened otherwise?

Linking to excellent existing work, exposing an overlooked contradiction, improving coordination, producing a reusable dataset, or identifying a decisive experiment may have more counterfactual value than creating a new organization or duplicating an intervention.

## Prediction and calibration

For consequential forecasts, record predictions before outcomes are known. Later compare predicted and observed outcomes.

The project should maintain calibration statistics where feasible:

- predicted intervention effects versus measured effects;
- predicted research usefulness versus actual downstream use;
- predicted source reliability versus later corrections;
- predicted task value versus retrospective audit assessments.

A project that cannot learn when its impact predictions are wrong cannot responsibly claim recursive improvement toward maximum human benefit.

## Real-world feedback ladder

Evidence should progressively move beyond internal AI judgments:

1. Internal consistency and deterministic tests.
2. Independent model critique.
3. Reproduction against authoritative sources/data.
4. Domain-expert or public criticism.
5. Retrospective validation against later data.
6. Small reversible real-world experiments where appropriate and authorized.
7. Replication across settings.
8. Measured downstream outcomes.

Confidence should increase only as evidence moves up this ladder.

## Anti-Goodhart rule

No internal metric—including a future "capability score"—should become the mission itself. If optimizing a metric produces outcomes inconsistent with the project's constitutional principles or observable human benefit, revise or discard the metric.
