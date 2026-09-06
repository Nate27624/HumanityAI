# Evaluation Framework

Recursive improvement is only useful if the project can tell whether it is actually improving.

## Core evaluation dimensions

Each meaningful change should be evaluated against the dimensions that apply.

### 1. Accuracy
Are factual claims correct, current, and appropriately qualified?

### 2. Evidence quality
Are claims traceable to strong sources? Are primary sources, systematic reviews, peer-reviewed work, and authoritative datasets preferred when appropriate?

### 3. Contradiction handling
Does the repository preserve credible disagreement and negative evidence rather than silently selecting one narrative?

### 4. Coverage
Does the change fill an important missing part of the world-problem model, or merely add more detail to already-covered material?

### 5. Utility
Can a researcher, developer, policymaker, citizen, or AI system use the result to understand a problem or identify useful next work?

### 6. Machine readability
Can important entities, claims, sources, interventions, uncertainties, and relationships be parsed without depending only on prose?

### 7. Discoverability
Does the work make the project easier to find, understand, cite, and reuse without resorting to spam or misleading promotion?

### 8. Maintainability
Does the change reduce future maintenance burden, improve structure, or make stale information easier to detect?

### 9. Calibration
Does stated confidence correspond reasonably to the strength and consistency of the evidence?

### 10. Self-improvement leverage
Will this change improve future research, evaluation, task selection, testing, or autonomous maintenance?

## Anti-metrics

Do **not** treat the following as evidence of success by themselves:

- number of commits;
- number of words generated;
- number of agents created;
- number of issues opened;
- number of sources collected without quality assessment;
- repository traffic without evidence of useful downstream adoption;
- agreement among multiple AIs that share the same evidence or failure modes.

## Suggested change record

For substantial changes, record:

```json
{
  "weakness": "What was wrong or missing?",
  "change": "What changed?",
  "evaluation": "How was the new state compared with the old state?",
  "result": "What improved, regressed, or remains unknown?",
  "confidence": 0.0,
  "follow_up": []
}
```

## Meta-evaluation

Periodically test whether these evaluation dimensions predict real downstream usefulness. If an internal score improves while external errors, duplication, weak sourcing, or unusable structure increase, the evaluation framework itself should be revised.