# Reproduction note — I0011 World Bank high-inequality country count

Status: **reproduced with qualification**

HumanityAI record checked: `I0011` in `data/indicators.json`.

## Claim checked

`I0011` records 52 countries classified by the World Bank as having high within-country inequality for the 2022 classification, using a Gini threshold above 40 and the most recent available household survey for each covered country.

## Independent source check

Primary HumanityAI source: World Bank Data Blog, *Inside the World Bank’s new inequality indicator: The number of countries with high inequality* (17 June 2024):

https://blogs.worldbank.org/en/opendata/inside-the-world-bank-s-new-inequality-indicator--the-number-of-

The World Bank states that its new within-country inequality indicator uses the income-or-consumption Gini Index and classifies countries with Gini greater than 40 as highly unequal. It reports 52 countries with high inequality and a decline from 77 in 2000 to 52 in 2022.

A supporting World Bank working-paper figure derived from the Poverty and Inequality Platform splits the 2022 total into 27 high-inequality countries with recent data and 25 with older data, which sums to 52. The same figure covers 169 countries with at least one household survey in PIP.

Supporting paper:

https://documents1.worldbank.org/curated/en/099549506102441825/pdf/IDU1bd155bac16d78143af188331f87564a9d6c8.pdf

## Result

**Reproduced.** The recorded value of 52, the Gini-above-40 classification rule, and the 2022 framing agree with the cited World Bank material.

## Qualification that matters

The number should not be interpreted as 52 countries measured with surveys conducted in 2022. The World Bank carries forward the most recent available household survey to produce a balanced country classification. For 2022, it reports that 51 countries' Gini estimates across the full 169-country sample were based on household surveys more than five years old. The existing HumanityAI limitations already flag this recency problem.

This also remains a **country-count indicator**, not a population-weighted measure of inequality and not a measure of wealth inequality, global interpersonal inequality, discrimination, or unequal access to opportunity. It therefore supports only one dimension of `P09`.

## Reproduction disposition

- Value: **reproduced**
- Classification threshold: **reproduced**
- Reference-year interpretation: **qualified but defensible**
- Existing limitation about stale household surveys: **reproduced**
- Data correction required: **no**

No change to `data/indicators.json` is warranted from this reproduction. The next useful `P09` work is a genuinely complementary opportunity- or wealth-inequality indicator rather than another country Gini count.
