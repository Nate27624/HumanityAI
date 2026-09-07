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

The ILO reports that 2.1 billion workers remain in informal employment in its 2026 outlook, often without basic labour rights, social protection, or income security. Its accompanying release describes informality as rising and says 2.1 billion workers are expected to hold informal jobs by 2026.

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
6. **Global totals hide major distributional differences.** ILOSTAT reports particularly high informality rates in least-developed countries and several low-income regions, so the global count should not be interpreted as geographically uniform.

## Independent contextual check

ILOSTAT's 2026 review of progress toward the 2030 Agenda reports that **57.9% of the global employed population was in informal employment in 2025**, virtually unchanged from 57.4% in 2015. It also reports far higher rates in least-developed countries and Sub-Saharan Africa. This independently supports the interpretation that informality is a persistent structural job-quality dimension rather than merely a transient fluctuation.

Context source: https://ilostat.ilo.org/blog/the-world-of-work-and-the-2030-agenda-a-ten-year-review/

The 57.9% statistic should not be substituted mechanically for the 2.1 billion 2026 count because the reference periods and presentations differ. They are best treated as mutually reinforcing context.

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
