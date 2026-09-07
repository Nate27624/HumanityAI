# P15 pandemic-preparedness baseline candidate

## Why this fills a real measurement gap

HumanityAI's existing P15 baseline (`I0016`) measures one catastrophic-risk dimension: the estimated number of nuclear warheads in global military stockpiles. That is useful for nuclear-risk orientation, but P15 explicitly covers multiple catastrophic and existential risk classes. A complementary pandemic-preparedness measure changes the diagnostic picture by measuring a major non-nuclear resilience dimension rather than adding another nuclear inventory statistic.

The strongest conservative candidate I found is the World Health Organization's International Health Regulations (IHR) States Parties Self-assessment Annual Reporting (SPAR) aggregate.

## Candidate headline

**Global average IHR core-capacity score: 63% in 2025, based on reports from 196 of 197 States Parties.**

Primary source: WHO Global Health Observatory / IHR monitoring framework, *International Health Regulations (2005) States Parties Self-assessment Annual Report*.

Source URL: https://www.who.int/data/gho/data/themes/international-health-regulations-%282005%29-monitoring-framework

WHO reports that 196 of 197 States Parties submitted SPAR data for 2025 and that the average overall capacity score across reporting States Parties was 63%. SPAR's second edition covers 15 core capacities and 35 indicators.

A related WHO indicator definition identifies this measure as the **average of 15 IHR core-capacity scores** (SDG indicator 3.d.1) and defines it as the percentage of attributes of those capacities attained at a point in time.

Indicator-definition URL: https://data.who.int/indicators/i/9A84EA5/FDBB8E8

## Direct versus derived status

The proposed 63% value is **directly reported by WHO** as the global average of overall 2025 SPAR scores. HumanityAI would not calculate or impute it.

The interpretation that this is a pandemic/health-emergency preparedness baseline is supported by the IHR framework and SDG 3.d.1, but the value is not a direct estimate of pandemic probability, expected mortality, or existential risk.

## Why it is decision-useful

This measure is complementary to `I0016` in three ways:

1. It covers a **non-nuclear catastrophic-risk pathway**.
2. It measures **preparedness capacity rather than hazard inventory**.
3. It exposes a potentially actionable gap: the average reporting State Party has not attained all assessed IHR capacity attributes, even though reporting coverage is nearly universal.

That distinction matters for future resource allocation. A nuclear-warhead count points toward arms-control, escalation, command-and-control, and geopolitical interventions; an IHR preparedness-capacity measure points toward surveillance, laboratories, emergency coordination, risk communication, workforce, financing, and cross-border health-security capacity.

## Important limitations

- **Self-assessment bias:** SPAR is completed by States Parties themselves. It should not be treated as an independently audited measure of actual emergency performance.
- **Capacity is not outcome:** A 63% preparedness score does not imply a 37% probability of failure, nor does it translate directly into deaths prevented, pandemic probability, or catastrophic-risk reduction.
- **Equal-weight aggregation can hide bottlenecks:** An overall average across capacities and countries may conceal severe weaknesses in specific functions or jurisdictions that dominate real-world risk.
- **Cross-country comparability is imperfect:** Countries differ in institutions, resources, interpretation, and implementation quality even when reporting against a standardized tool.
- **Preparedness can be threat-specific:** IHR capacities cover broad health-emergency readiness and are not a complete measure of preparedness for every biological catastrophe, engineered pathogen, or high-consequence respiratory pandemic.
- **Directionality is subtle:** Higher capacity scores are generally desirable, but institutional capacity can still fail under extreme stress; this is not evidence that any specific preparedness intervention is effective.
- **Not a complete P15 measure:** This should sit alongside, not replace, nuclear, biological, technological, environmental, or other tail-risk indicators.

## Contradictory / qualifying evidence

WHO's own 2024 reporting showed a global average SPAR capacity score of 64%, versus 63% in 2025. That one-point decline argues against narrating preparedness as automatically improving year over year. It may reflect genuine deterioration, reporting composition, scoring changes, or normal measurement noise; a one-year change this small should not be overinterpreted.

WHO's 2024–2025 results reporting also notes that performance was stronger in preparedness than in detection and emergency response, and reports operational disruptions in surveillance in many countries during 2025. This is a useful warning that self-reported capacity and operational resilience under funding or crisis pressure are distinct constructs.

## Recommendation

**Candidate is suitable for addition to `data/indicators.json` after ordinary schema/ID integration.** It is materially complementary to the existing nuclear baseline, uses a primary WHO source, has near-universal reporting coverage, and has a precise definition.

Suggested framing if promoted to a machine-readable indicator:

- problem: `P15` (optionally also `P03`, if multi-tagging is judged useful)
- name: `Global average International Health Regulations core-capacity score`
- value: `63`
- unit: `percent of assessed capacity attributes`
- value type: `estimate` or `observed summary` depending on current schema convention
- reference period: `2025`
- geography: `196 of 197 IHR States Parties`
- source publisher: `World Health Organization`

It should be explicitly labeled a **preparedness-capacity baseline**, not a direct measure of global catastrophic risk or intervention effectiveness.