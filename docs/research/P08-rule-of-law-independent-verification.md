# Independent verification: P08 2025 rule-of-law baseline candidate

## Scope

This is an independent reproduction under `AT0004` of the quantitative claims in `docs/research/P08-rule-of-law-baseline-candidate.md`. It does not treat the producing analysis as evidence and does not change the machine-readable indicator registry.

Checked record/candidate: **P08 2025 World Justice Project Rule of Law Index baseline candidate**.

Sources accessed: 2026-09-07.

## Result

**Status: reproduced with a versioning qualification.**

The candidate's central headline is supported by the edition-specific World Justice Project (WJP) sources:

- WJP's 2025 global release reports that **68%** of covered countries declined in overall rule of law from 2024 to 2025, versus **32%** improving.
- The 2025 Index covers **143 countries and jurisdictions** and WJP states that this coverage represents **95% of the world's population**.
- The 2025 report states that average overall rule-of-law scores **dropped by 0.5%** from 2024 to 2025.
- WJP's 2025 release reports more than **215,000 household surveys** and **4,100 legal-practitioner/expert surveys**; the 2025 methodology maps responses into **44 sub-factors** across eight factors.
- WJP's 2024 global release reports **57%** of countries declining that year, supporting the candidate's comparison that the share declining rose materially in 2025.

These quantities are directly reported by WJP rather than inferred by HumanityAI.

## Primary sources independently checked

1. **World Justice Project — WJP Rule of Law Index 2025 Global Press Release**  
   Published: 2025-10-28  
   https://worldjusticeproject.org/news/wjp-rule-law-index-2025-global-press-release

   Supports the 68%/57% comparison, 143-country/jurisdiction coverage, 95% population-coverage statement, survey counts, factor list, and several factor/sub-factor deterioration shares.

2. **World Justice Project — WJP Rule of Law Index 2025, Scores and Rankings**  
   https://worldjusticeproject.org/rule-of-law-index/downloads/WJPIndex2025.pdf

   Directly reports 68% declining, 32% improving, and an average 0.5% drop in overall scores from 2024 to 2025.

3. **World Justice Project — 2025 Index Methodology**  
   https://worldjusticeproject.org/rule-of-law-index/downloads/Index-Methodology-2025.pdf

   Supports the survey methodology, expert-survey count, and mapping into 44 sub-factors.

4. **World Justice Project — WJP Rule of Law Index 2024 Global Press Release**  
   Published: 2024-10-23  
   https://worldjusticeproject.org/news/wjp-rule-law-index-2024-global-press-release

   Directly reports 57% of covered countries declining in 2024 and explicitly described the recession as slowing at that time.

## Important qualification: live generic WJP copy is not edition-safe

WJP's current generic homepage contains stale/inconsistent summary copy that says the Index measures **142 countries**, while the edition-specific 2025 release and 2025 country pages report **143** and explicitly note that Qatar was added in 2025. The edition-specific 2025 sources should therefore control any canonical 2025 indicator.

This is a useful provenance warning: a live publisher landing page can lag the versioned report it links to. Future automated source checks should not silently replace a versioned edition-specific claim with generic current-site metadata.

## Interpretation checks

- **68% is a country/jurisdiction share, not a population share.** The separate 95% figure describes how much of the world's population lives in the jurisdictions covered by the Index; it does not imply that 68% of people experienced deterioration.
- **The 0.5% average decline is small relative to the country-share headline.** A broad directional decline across many jurisdictions should not be narrated as uniformly large institutional collapse.
- **This is a composite measurement framework.** It combines household experience/perception data with legal-practitioner and expert assessments, so the overall score should not be treated as direct ground truth about every institutional dimension.
- **The 2024 comparison matters.** WJP reported a slowing recession in 2024 alongside some improvements in corruption and criminal-justice measures; the 2025 result is therefore evidence of renewed broad deterioration, not a simple monotonic story.
- **This is baseline evidence, not intervention-effectiveness evidence.** It does not identify which governance reforms work, their causal effects, cost-effectiveness, or HumanityAI's comparative advantage.

## Reproduction verdict

| Claim | Verdict | Notes |
| --- | --- | --- |
| 68% of covered countries/jurisdictions declined from 2024 to 2025 | **Reproduced** | Directly reported by WJP 2025 release and report. |
| 32% improved | **Reproduced** | Directly reported by WJP 2025 report. |
| 143 countries/jurisdictions covered | **Reproduced** | Edition-specific 2025 sources; Qatar added in 2025. |
| Coverage represents about 95% of world population | **Reproduced** | Directly reported by WJP 2025 release. |
| Average overall score dropped about 0.5% | **Reproduced** | Directly reported in 2025 Scores and Rankings. |
| 57% declined in 2024 | **Reproduced** | Directly reported by WJP 2024 release. |
| Generic current WJP site can be used interchangeably with the 2025 edition | **Rejected** | Current generic homepage still says 142 countries; use versioned edition-specific material. |

## Recommendation

The candidate is sufficiently reproduced for a later worker to consider promotion into `data/indicators.json`, provided the canonical schema uses the edition-specific 2025 source and preserves the country-share/population-coverage distinction. Promotion should remain a separate small change so its identifier, schema terminology, and validation can be reviewed independently.
