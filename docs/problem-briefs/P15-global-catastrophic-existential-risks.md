# P15 — Global catastrophic and existential risks

## Why this problem matters

P15 covers low-frequency, potentially extreme events that could cause harm across countries, generations, or global systems. The category includes nuclear catastrophe, severe pandemics, extreme climate outcomes, dangerous emerging technologies, asteroid impacts, systemic infrastructure collapse, and other hazards whose probability, severity, and tractability differ substantially. These risks should not be collapsed into a single convenience score merely because they share a catastrophic tail.

## Current baseline

Canonical indicator [`I0016`](../../data/indicators.json) records SIPRI's estimate that **9,745 nuclear warheads were in global military stockpiles in January 2026**. SIPRI estimated 12,187 warheads in total inventories across nine nuclear-armed states, with about 4,012 stockpiled warheads deployed with operational forces.

The canonical record deliberately uses the military-stockpile count as an inventory baseline. It is **not** an estimate of the annual probability of nuclear war, expected fatalities, escalation risk, command-and-control resilience, or existential risk. Warheads differ in yield, delivery systems, readiness, survivability, and strategic role, and SIPRI describes these open-source figures as approximate estimates subject to revision.

Source: Stockholm International Peace Research Institute, *SIPRI Yearbook 2026* (2026).

## Existing reusable infrastructure

Canonical resource [`RSC0005`](../../data/resources.json), the **Humanitarian Data Exchange (HDX)** maintained by the UN OCHA Centre for Humanitarian Data, is relevant to crisis-context and humanitarian-response data across multiple problem areas including P15.

HDX is useful discovery infrastructure, not an early-warning guarantee or a measure of catastrophe preparedness. Its datasets vary in timeliness, methodology, geography, licensing, and sensitivity, and some are restricted. HumanityAI should reuse such infrastructure where appropriate while separately evaluating whether a dataset is fit for a specific risk-analysis task.

## Decision-useful distinctions

P15 analysis should keep at least these questions separate:

1. **Hazard:** What physical, biological, technological, or institutional process could cause extreme harm?
2. **Probability:** How likely is the event within a defined time horizon, and how uncertain is that estimate?
3. **Exposure:** Which populations, systems, ecosystems, or future generations could be affected?
4. **Vulnerability:** How severe would consequences be given current preparedness, infrastructure, institutions, and recovery capacity?
5. **Prevention:** Which actions reduce the chance that the event occurs?
6. **Mitigation:** Which actions reduce harm if prevention fails?
7. **Resilience and recovery:** Which systems preserve essential capabilities and shorten recovery after disruption?
8. **Rights and power:** Could risk-reduction measures themselves create coercion, surveillance, secrecy, arms races, or concentrated authority?

A large hazard inventory does not directly imply high annual catastrophe probability, and a low-probability event can still merit attention when consequences are extreme.

## What current evidence does not establish

Current HumanityAI records do not yet establish:

- a defensible cross-risk comparison of nuclear, pandemic, extreme-climate, asteroid, infrastructure, biotechnology, or advanced-technology catastrophic risks;
- an authoritative annual probability of nuclear war or a conversion from warhead counts to expected catastrophe;
- complementary non-nuclear P15 baseline indicators with comparable definitions;
- causal effectiveness or cost-effectiveness of nuclear-risk reduction, pandemic preparedness, biosecurity, civil defense, infrastructure resilience, asteroid defense, or other catastrophic-risk interventions;
- how prevention, mitigation, resilience, and recovery portfolios interact across hazards;
- HumanityAI's comparative advantage in implementing any particular catastrophic-risk intervention.

## High-value next evidence

- Add complementary non-nuclear baselines where strong authoritative measurement exists, while keeping unlike hazards non-additive.
- Add systematic reviews, historical evaluations, natural experiments, or other strong evidence on preparedness and risk-reduction interventions, with special attention to null findings and implementation failures.
- Separate stockpiles, capabilities, near misses, warning indicators, modeled probabilities, and realized outcomes rather than blending them into one risk estimate.
- Add short- and medium-horizon preregistered forecasts only where authoritative resolution criteria can be frozen in advance.
- Map existing monitoring, early-warning, preparedness, and resilience infrastructure before proposing new systems.
- Examine interventions for second-order effects such as arms-race incentives, secrecy, centralized emergency power, dual-use proliferation, or displacement of risk into less visible channels.

## Rights and governance cautions

Catastrophic-risk policy can create unusually strong arguments for centralized authority, secrecy, surveillance, restriction, or emergency powers. Those measures may sometimes be proposed for legitimate safety reasons, but HumanityAI should not treat aggregate risk reduction as sufficient justification by itself. Due process, proportionality, accountability, reversibility, pluralism, and distribution of burdens remain part of the evaluation.

## What this brief does not establish

This brief does not claim that nuclear inventory size is a direct probability measure, that P15 risks are commensurable, that the most dramatic hazard is automatically the highest-priority one, or that a specific prevention or preparedness intervention should be adopted. It summarizes current canonical records and identifies evidence needed for better risk decisions.
