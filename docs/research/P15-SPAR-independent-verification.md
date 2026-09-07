# Independent verification: P15 WHO SPAR candidate

Checked 2026-09-07 against WHO primary-source pages, independently of the candidate write-up.

## Record checked

Candidate in `docs/research/P15-pandemic-preparedness-baseline-candidate.md`: **global average IHR core-capacity score 63% in 2025, based on reports from 196 of 197 States Parties.**

## Result

**REPRODUCED, with a versioning qualification.**

WHO's current International Health Regulations monitoring-framework page directly reports for 2025:

- 99% report submission;
- 196 of 197 States Parties submitted SPAR data;
- 63% global average of overall capacity scores from the 196 reporting States Parties;
- the second-edition SPAR has 15 capacities and 35 indicators.

Primary source: https://www.who.int/data/gho/data/themes/international-health-regulations-%282005%29-monitoring-framework

WHO's indicator metadata independently defines SDG indicator 3.d.1 as the **average of 15 IHR core-capacity scores**, expressed as the percentage of attributes of those capacities attained at a point in time.

Definition source: https://data.who.int/indicators/i/9A84EA5/FDBB8E8

WHO's SPAR methodology page confirms that this is an annual **self-assessment** by States Parties and describes the 35 indicators across 15 capacities.

Methodology source: https://www.who.int/emergencies/operations/international-health-regulations-monitoring-evaluation-framework/states-parties-self-assessment-annual-reporting

## Independent qualification discovered

WHO surfaces are not perfectly synchronized. The SPH analytics portal, updated 2026-09-05, currently displays a **64% global average** and describes 196 reporting States Parties, while the main WHO GHO monitoring-framework page explicitly labels **63% for 2025** and **64% for 2024**. The SPH portal also labels its report series `2010-2024`, making its 64% figure consistent with the 2024 value rather than contradictory evidence for 2025.

SPH portal: https://extranet.who.int/sph/spar/analytics

This means the candidate's 63% value is reproducible, but any machine-readable promotion should cite the year-specific GHO monitoring-framework page and preserve the `2025` reference period. Consumers should not treat an unlabeled/latest SPH dashboard value as interchangeable across vintages.

## Interpretation check

The candidate correctly avoids treating 63% as a pandemic probability, mortality estimate, intervention effect, or direct catastrophic-risk measure. WHO describes SPAR as capacity/preparedness measurement, and the self-reporting design creates a material limitation. Aggregation can also conceal country- and capacity-specific bottlenecks.

## Recommendation

Promote the candidate only as a **preparedness-capacity baseline** for P15, with the existing self-assessment and aggregation limitations. Add a versioning note that WHO dashboard surfaces may expose different reporting vintages; the cited 2025 GHO page should remain the authority for the 63% headline.
