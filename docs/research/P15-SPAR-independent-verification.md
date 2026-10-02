# Independent verification: P15 WHO SPAR candidate

Checked 2026-09-07 against WHO primary-source pages, independently of the candidate write-up.

## Record checked

Candidate in `docs/research/P15-pandemic-preparedness-baseline-candidate.md`: **global average IHR core-capacity score 63% in 2025, based on reports from 196 of 197 States Parties.**

## Result

**PARTIALLY REPRODUCED, with a material same-year reporting-count discrepancy and a separate versioning qualification.**

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

## Same-year WHO discrepancy discovered by independent audit

A separate first-party WHO source does **not** reproduce the 2025 reporting count. WHO Director-General report A79/7, dated 4 May 2026 and covering 1 January–31 December 2025, states that **97% of States Parties (191 of 197) submitted SPAR reports for 2025** and points readers to e-SPAR for current data.

Source: https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_7-en.pdf

That conflicts with the current GHO page's **99% / 196 of 197** reporting figure for 2025. Both are WHO sources. The available evidence here does not establish why they differ; possibilities such as extraction timing or later data finalization must remain hypotheses unless separately sourced. The contradiction therefore belongs in the record rather than being normalized away.

Importantly, A79/7 does not overturn the current GHO page's directly reported **63% global average capacity score**. The score claim is reproduced from the current year-specific GHO page; the associated 196-of-197 coverage claim is disputed by another same-year WHO publication.

## Separate reporting-vintage qualification

WHO surfaces are also not perfectly synchronized across reporting vintages. The SPH analytics portal, updated 2026-09-05, currently displays a **64% global average** and describes 196 reporting States Parties, while the main WHO GHO monitoring-framework page explicitly labels **63% for 2025** and **64% for 2024**. The SPH portal labels its report series `2010-2024`, making its 64% figure consistent with the 2024 value rather than contradictory evidence for the 2025 score.

SPH portal: https://extranet.who.int/sph/spar/analytics

Any machine-readable promotion should therefore cite the year-specific GHO monitoring-framework page, preserve the `2025` reference period, and not treat an unlabeled/latest dashboard value as interchangeable across vintages.

## Interpretation check

The candidate correctly avoids treating 63% as a pandemic probability, mortality estimate, intervention effect, or direct catastrophic-risk measure. WHO describes SPAR as capacity/preparedness measurement, and the self-reporting design creates a material limitation. Aggregation can also conceal country- and capacity-specific bottlenecks.

## Recommendation

Promote **63%** only as a **preparedness-capacity baseline** for P15, with the existing self-assessment and aggregation limitations. Do not encode `196 of 197` as an uncontested 2025 coverage fact without preserving the conflicting A79/7 figure of `191 of 197`. If geography/coverage metadata requires one value, prefer wording that attributes it explicitly to the current GHO extract rather than implying all WHO 2025 publications agree. Preserve a versioning note because WHO surfaces expose different reporting vintages.