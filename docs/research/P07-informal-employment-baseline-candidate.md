# P07 complementary baseline candidate — informal employment

Status: **recommended for canonical indicator integration after ordinary review**

## Measurement gap

HumanityAI's current P07 baseline `I0012` measures **labour-market access** through the global jobs gap: 408 million people projected to want paid work but be unable to access it in 2026. That record explicitly does not measure job quality.

A complementary P07 baseline should therefore describe conditions **among people who are employed**, rather than adding another unemployment or labour-force-access statistic.

## Candidate indicator

**Workers in informal employment worldwide**

- Value: **2.1 billion workers**
- Value type: **projection / expected 2026 level**
- Reference period: **2026**
- Geography: **World**
- Primary source: International Labour Organization, *Employment and Social Trends 2026* (14 January 2026)
- Source URL: https://www.ilo.org/publications/flagship-reports/employment-and-social-trends-2026
- Same-publisher cross-check: https://www.ilo.org/resource/news/global-job-quality-stagnates-despite-resilient-growth
- Repository record: https://researchrepository.ilo.org/esploro/outputs/report/Employment-and-social-trends-2026/995684768902676

The ILO reports that 2.1 billion workers remain in informal employment in its 2026 outlook, often without access to basic rights, social protection, or income security. Its accompanying release describes informality as rising and says 2.1 billion workers are expected to hold informal jobs by 2026.

## Why this changes interpretation

The existing jobs-gap baseline can be read as a problem of **access to work**. The informal-employment figure shows that access alone is not enough: a very large population is working while remaining outside standard formal protections and institutions.

That makes the two measures complementary rather than redundant:

- `I0012` asks: **Who wants paid work but cannot access it?**
- this candidate asks: **How many workers are employed informally?**

The candidate therefore improves P07's multidimensional diagnosis without constructing a composite score.

## Important limitations

1. **Informality is not synonymous with bad work.** Informal jobs are heterogeneous. Some workers may prefer or benefit from particular informal arrangements, and formalization itself is not sufficient evidence of higher welfare.
2. **The 2.1 billion figure is not additive with the jobs gap.** The jobs gap concerns people lacking desired paid work; informal employment concerns people who are employed. Other labour-market indicators such as working poverty, underemployment, low pay, or insecure work can overlap substantially with informal employment.
3. **This is not a direct outcome measure.** Informality is a labour-market status associated with differences in legal coverage, social protection, security, and institutional access; it does not directly measure earnings, wellbeing, productivity, bargaining power, or realized rights.
4. **Definitions and measurement differ across countries.** Informal employment is estimated through harmonized labour-statistics concepts, but underlying surveys, institutional settings, and forms of informality vary.
5. **The 2026 level is an outlook estimate/projection, not a final census.** It should be labeled accordingly.
6. **Global totals hide major distributional differences.** Regional and income-group patterns differ substantially, so the global count should not be interpreted as geographically uniform.

## Same-publisher contextual check

The ILO's accompanying 2026 release separately presents the same 2.1 billion outlook figure alongside separate job-quality deficits: nearly 300 million workers in extreme working poverty and about 186 million projected unemployed people at a 4.9% unemployment rate. Those figures describe different and partly overlapping labour-market dimensions and must not be summed into a unique count of workers facing poor economic opportunity.

This cross-check strengthens confidence that the 2.1 billion figure is intentional and central to the ILO's 2026 job-quality framing, but it is not independent evidence because both publications come from the same institution.

## Recommended machine-readable record shape

If integrated into `data/indicators.json`, this should become a new P07 record with approximately the following semantics:

- name: `Workers in informal employment worldwide`
- value: `2.1`
- unit: `billion workers`
- value_type: `projection`
- reference_period: `2026 projection`
- geography: `World`
- source publisher: `International Labour Organization`
- source title: `Employment and Social Trends 2026`
- published_at: `2026-01-14`
- source_type: `official_report`

The notes should explicitly say that this complements `I0012` by measuring employment form/job-quality conditions rather than labour-market access and must not be interpreted as evidence that formalization alone improves outcomes.

## Disposition

**Recommend integration.** This appears to meet task `AT0002`'s requirement for a genuinely complementary dimension: it directly addresses the job-quality gap already acknowledged by `I0012`, uses an authoritative global source, and materially changes P07 interpretation without introducing a composite ranking.