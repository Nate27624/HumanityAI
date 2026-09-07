# Reproduction note — I0002 WHO universal health coverage baseline

Status: **reproduced with qualification**

HumanityAI record checked: `I0002` in `data/indicators.json`.

## Claim checked

`I0002` records an estimated 4.6 billion people not fully covered by essential health services in 2023, globally.

## Independent source check

Primary source: World Health Organization and World Bank, *Tracking universal health coverage: 2025 global monitoring report* (5 December 2025):

https://www.who.int/teams/health-financing-and-economics/global-monitoring-report/2025

WHO's report page states that, as of 2023, an estimated 4.6 billion people still lacked coverage for essential health services. It separately reports that 2.1 billion people experienced financial hardship from out-of-pocket health spending in 2022.

Same-publisher cross-check: WHO fact sheet, *Universal health coverage (UHC)* (5 December 2025):

https://www.who.int/news-room/fact-sheets/detail/universal-health-coverage-%28uhc%29

The fact sheet reports that the UHC service coverage index rose from 54 in 2000 to 71 in 2023 and that about 4.6 billion people were not fully covered in 2023.

A WHO–World Bank news release published 6 December 2025 independently repeats the 4.6 billion estimate and the 2.1 billion financial-hardship estimate:

https://www.who.int/news/item/06-12-2025-most-countries-make-progress-towards-universal-health-coverage-but-major-challenges-remain-who-world-bank-report-finds

## Result

**Reproduced.** The 4.6 billion value, 2023 reference period, global scope, and essential-health-service interpretation agree across the 2025 WHO/World Bank monitoring report, the WHO fact sheet, and the WHO–World Bank release.

## Qualification that matters

The 4.6 billion figure is an **estimate derived from a global monitoring framework**, not a census of individually observed unmet-care events. It refers to incomplete coverage of essential health services and should not be interpreted as 4.6 billion people receiving no care at all.

The service-coverage estimate is distinct from the 2.1 billion people reported to experience financial hardship from out-of-pocket health spending. These populations overlap and should not be added together. The two indicators are constructed using different concepts and data sources.

The UHC service coverage index also does not directly measure clinical quality, timeliness, patient experience, all unmet need, or health outcomes. Progress in the index can coexist with important access or quality deficits in specific services and populations.

## Reproduction disposition

- `I0002` value (4.6 billion): **reproduced**
- 2023 reference period: **reproduced**
- Global scope: **reproduced**
- Essential-service-coverage interpretation: **reproduced**
- Non-additivity with financial-hardship counts: **confirmed and important**
- Data correction required: **no**

No change to `data/indicators.json` is warranted from this reproduction. A useful complementary P03 baseline would measure a distinct dimension such as financial hardship, effective coverage, quality, or outcome inequality rather than another count derived from the same service-coverage construct.