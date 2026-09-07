# P07 — Economic opportunity, work, and abundance

**Status:** early synthesis, reviewed 2026-09-07  
**Problem definition:** unemployment, underemployment, exploitative labor, productivity, technological unemployment, access to capital, market failures, and pathways toward reducing involuntary labor through abundance.

This brief summarizes current HumanityAI records and a small amount of current authoritative context. It is not a priority ranking or policy recommendation.

## What the current evidence says

### Access to paid work remains a major constraint

HumanityAI indicator [`I0012`](../../data/indicators.json) records the International Labour Organization's **2026 projection of a 408 million-person global jobs gap**: people who want paid work but cannot access it. The same ILO source projects global unemployment at 4.9%, about 186 million people. The unemployment count is contained within the broader jobs-gap concept and must not be added to it.

Worker B independently reproduced the 408 million projection and its interpretation in [`docs/reproductions/I0012-ilo-global-jobs-gap.md`](../reproductions/I0012-ilo-global-jobs-gap.md).

Source: International Labour Organization, *Employment and Social Trends 2026* (14 January 2026): https://www.ilo.org/publications/flagship-reports/employment-and-social-trends-2026

### Having a job is not the same as having a high-quality job

The same 2026 ILO assessment reports **2.1 billion workers in informal employment** and **nearly 300 million workers in extreme working poverty**. These are different, overlapping dimensions of economic opportunity and cannot be summed with each other or with the jobs gap to create a unique count of people facing poor labor-market conditions.

The ILO describes informal employment as often lacking basic rights, social protection, or income security. It also reports that progress in job quality has slowed sharply and that low-income countries face especially weak productivity growth and structural transformation.

This is an important measurement gap in HumanityAI's current canonical indicators: `I0012` measures access to desired paid work, but not job quality, earnings adequacy, informality, bargaining power, or productive opportunity.

### Youth face distinct barriers

The ILO's 2026 assessment reports global youth unemployment at **12.4%** and about **260 million young people not in employment, education, or training (NEET)**. These measures describe different populations and should not be treated as interchangeable with the overall jobs gap.

### Intervention evidence is mixed rather than uniformly positive

HumanityAI evidence record [`E0006`](../../data/evidence.json) summarizes a Campbell systematic review of 107 youth active-labour-market interventions in 31 countries. Employment and earnings effects were positive on average but small and highly heterogeneous. Skills training and entrepreneurship promotion showed significant average gains, while employment services and subsidized employment had negligible or statistically insignificant average effects; business-performance effects were not statistically significant.

That synthesis has an important age limitation: its literature search was current only through January 2015. It is evidence about intervention classes, not proof that a specific contemporary program will work or be cost-effective.

Other current HumanityAI records reinforce the need for intervention-specific caution:

- [`E0002`](../../data/evidence.json): evidence for U.S. medical-financial partnerships for lower-income people is insufficient overall, with small non-significant financial effects in a sparse evidence base and one positive health-service-use finding.
- [`E0003`](../../data/evidence.json): off-grid electrification in low- and middle-income countries is associated with small income gains alongside mixed or null findings on several other outcomes; that does not establish cost-effectiveness or general labor-market transformation.

## What is not yet established

Current records do **not** establish:

- a single global measure of “economic opportunity”;
- which job-quality dimension should dominate P07 diagnosis;
- that formalization by itself improves worker welfare in every context;
- which active-labour-market intervention class has the highest contemporary cost-effectiveness;
- whether positive average intervention effects transfer across countries, populations, implementation systems, or macroeconomic conditions;
- HumanityAI's comparative advantage in implementing, funding, or advocating a labor-market intervention.

## High-value next evidence

The strongest next work is complementary rather than another unemployment-style count:

1. **Job quality / informality baseline.** Add a canonical, clearly defined global measure of informal employment or working poverty, preserving overlap and definitional limits.
2. **Updated intervention synthesis.** Find newer systematic reviews or meta-analyses of active-labour-market policies, especially evidence that separates training, wage subsidies, employment services, entrepreneurship, and context.
3. **Formalization outcomes.** Separate evidence that formalization changes worker income, security, productivity, or rights from evidence that registration systems merely exist or expand.
4. **Cost-effectiveness.** Preserve program costs, implementation intensity, and distributional effects when credible comparative evidence exists.
5. **Heterogeneity.** Track differences by country income level, gender, age, disability, migration status, and baseline labor-market conditions rather than relying only on global averages.
6. **Abundance and productivity.** Add measures that distinguish access to work from productivity, real earnings, and the possibility of reducing involuntary labor without reducing material capability.

## Rights and distribution cautions

“More employment” is not automatically equivalent to greater human capability. Work can be unsafe, coercive, underpaid, insecure, discriminatory, or incompatible with caregiving and other valued activities. Conversely, policies that reduce measured employment could still increase capability if they raise income security or expand meaningful choice.

P07 analysis should therefore preserve worker rights, bargaining power, social protection, distributional effects, unpaid work, and the voluntary or involuntary nature of labor alongside headline employment outcomes.

## Current HumanityAI records used

- Problem taxonomy: [`PROBLEM_MAP.md`](../../PROBLEM_MAP.md)
- Baseline indicator: [`I0012`](../../data/indicators.json)
- Independent reproduction: [`I0012 ILO global jobs-gap projection`](../reproductions/I0012-ilo-global-jobs-gap.md)
- Intervention evidence: [`E0002`, `E0003`, `E0006`](../../data/evidence.json)

The external sources remain the evidentiary authority; this brief is HumanityAI-authored synthesis and should be revised as stronger or contradictory evidence is added.
