# Reproduction note — I0012 ILO global jobs-gap projection

Status: **reproduced with qualification**

HumanityAI record checked: `I0012` in `data/indicators.json`.

## Claim checked

`I0012` records a projected global jobs gap of 408 million people in 2026: people who want paid work but cannot access it. Its note separately says projected unemployment is about 186 million (4.9%) and warns that the broader jobs-gap total already contains unemployed people.

## Independent source check

Primary source: International Labour Organization, *Employment and Social Trends 2026* (14 January 2026):

https://www.ilo.org/publications/flagship-reports/employment-and-social-trends-2026

The ILO's 2026 flagship report states that the broader global jobs gap is projected to reach 408 million in 2026. It describes the measure as capturing people who want paid work but cannot access it. The same report projects the global unemployment rate at 4.9% in 2026.

Independent same-publisher cross-check: ILO news release, *Global job quality stagnates despite resilient growth*:

https://www.ilo.org/resource/news/global-job-quality-stagnates-despite-resilient-growth

The release gives the 4.9% unemployment projection as equivalent to 186 million people and separately reports large job-quality deficits, including nearly 300 million workers in extreme working poverty and 2.1 billion workers in informal employment.

For temporal context, an earlier ILO release reported a 402 million global jobs gap for 2024, including 186 million unemployed people, 137 million temporarily unavailable to work, and 79 million discouraged workers. That earlier decomposition should not be assumed to be the exact composition of the 408 million 2026 projection without the underlying 2026 tables.

## Result

**Reproduced.** The 408 million value, 2026 projection framing, broader-than-unemployment interpretation, and 4.9% unemployment projection agree with the cited ILO source. The separate ILO release independently confirms that 4.9% corresponds to about 186 million unemployed people.

## Qualification that matters

The 408 million figure is a **projection**, not an observed 2026 census. It measures unmet desire for paid work and is broader than unemployment, but it is not itself a measure of job quality, earnings adequacy, informality, productivity, bargaining power, or whether available work expands human capability.

The 186 million unemployed population is nested within the broader jobs-gap concept and must not be added to 408 million. Likewise, the nearly 300 million workers in extreme working poverty and 2.1 billion in informal employment describe different, overlapping dimensions of labour-market conditions; they cannot be summed into a unique count of people facing poor economic opportunity.

## Reproduction disposition

- `I0012` value (408 million): **reproduced**
- 2026 projection status: **reproduced**
- Jobs-gap interpretation: **reproduced**
- Unemployment comparison (4.9%, about 186 million): **reproduced**
- Existing warning against adding unemployment to the jobs gap: **reproduced and important**
- Data correction required: **no**

No change to `data/indicators.json` is warranted from this reproduction. A higher-value next `P07` baseline would measure a complementary dimension such as job quality, working poverty, informality, earnings adequacy, or underemployment rather than another measure of labour-market access.