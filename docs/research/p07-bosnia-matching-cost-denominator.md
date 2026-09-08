# P07 Bosnia private employment services: recovered payment denominator

Date: 2026-09-08  
Producer: Operator A  
Status: Tier-2 decision-bearing research candidate; requires independent Worker C verification and Worker D integration.

## Assignment

Worker D assigned a bounded P07 information-value task: recover a source-grounded incremental cost for the Bosnia and Herzegovina private job-matching intervention used in the canonical youth-ALMP routing framework. If no defensible comparable cost existed, the instruction was to record that negative result rather than invent a denominator.

## Result

The missing **contract payment schedule is recoverable**, but the missing **economic resource cost of matching is not**.

The World Bank implementation-completion documentation for the same Bosnia and Herzegovina Provision of Private Employment Services project reports the first-phase performance-based schedule as:

- **USD 90 per jobseeker** meeting the counseling/job-search-assistance condition (profiling, assessment, and Employment Action Plan); and
- **USD 1,100 per verified formal placement** under intermediation, with the initial first-phase target of 550 verified placements and USD 605,000 allocated.

The experimental paper reports that both randomized arms received the counseling/IAP package, while the treatment arm received access to additional matching. Its analysis sample contained 808 treatment and 812 control jobseekers. The intent-to-treat effect of additional matching was approximately **+6.3 percentage points** in formal employment in the short run and **+4.2 percentage points** in the medium run.

This means the contract schedule supports a narrow derived quantity:

- short-run incremental **outcome-contingent payment** implied by the ITT employment difference: `0.063 × $1,100 ≈ $69.30 per treatment-assigned jobseeker`;
- medium-run equivalent using the later employment difference: `0.042 × $1,100 ≈ $46.20 per treatment-assigned jobseeker`.

These are **not program resource-cost estimates** and must not be used as portable cost-effectiveness denominators.

## Why the recovered denominator is not a true incremental matching cost

1. The USD 1,100 is an **outcome payment for a verified formal placement**, not an invoice for the marginal staff time, employer outreach, screening, introductions, monitoring, or administrative effort used to provide matching.
2. The experimental paper states that the provider received the placement payment when a beneficiary obtained formal employment; matching was a tool available to the provider rather than a separately priced service. Therefore, the payment schedule does not isolate the resource cost of general or specific matching.
3. Both randomized groups received the USD 90-type counseling/IAP service, so the USD 90 base payment is not the incremental treatment cost of matching.
4. The later World Bank completion report explicitly says the provider **spent more funds than it could get back**, because expenses could not be claimed when performance conditions were not achieved. That is direct evidence that disbursement is not equal to economic resource cost.
5. The completion report also identifies sizeable contracting/monitoring transaction costs and concludes that the performance-based conditions were not correctly valued; it specifically says placement incentives should have been increased. This further weakens any interpretation of the USD 1,100 as a market/resource-cost measure.

## Decision delta

**The Bosnia gap is now narrower but not closed.** We can replace “no cost information” with a more precise statement:

> The first-phase contract paid roughly USD 90 per counseled/profiled participant plus USD 1,100 per verified formal placement. Given the experimental ITT, the matching arm implies roughly USD 69 per assigned participant in additional short-run outcome-contingent placement payments, but the true incremental resource cost of matching remains unobserved and was likely higher than reimbursed cost for at least some implementation periods.

This changes P07 routing in two ways:

- **START** distinguishing fiscal/outcome-contingent payment from economic resource cost in employment-service comparisons.
- **STOP** treating “Bosnia cost missing” as a completely blank field; the contract incentive schedule is known.
- **CONTINUE TO BLOCK** any scalar Bosnia-vs-entrepreneurship cost-effectiveness ranking until staff/operating/contracting resource cost or a defensible total incremental implementation cost is recovered.
- **MORE** attention to incentive design: the evidence implies that the USD 1,100 success payment shaped provider effort and cream-skimming, while later implementation evidence suggests it may have undercompensated harder-to-place cases.

Confidence: **high** on the USD 90 / USD 1,100 payment schedule and on the distinction between payment and resource cost; **moderate-high** on the derived per-assigned outcome-payment quantities because they mechanically apply the reported ITT to the placement payment; **low** on any attempt to infer true incremental economic cost from these payments.

## Sources consulted as untrusted evidence

- Balavac-Orlic, Merima; Giles, John T.; Hari, Siddharth; Ovadiya, Mirey (2024), *Private Provisioning of Employment Services: Experimental Evidence from Bosnia and Herzegovina*, World Bank Policy Research Working Paper 10826 / policy note. The note reports the two randomized service intensities, sample sizes, payment structure, and ITT employment effects: https://documents1.worldbank.org/curated/en/099061424085014380/pdf/P1668481ccc5d707183ad1b71222e10572.pdf
- World Bank (2025), *Implementation Completion and Results Report: Bosnia and Herzegovina Provision of Private Employment Services (P171433)*. Table 2 and Annex 1 report the first-phase PBC values; the annex states USD 90 per qualifying counseling/IAP case and USD 1,100 per verified intermediation placement. The report also records unrecovered provider spending and design problems with PBC valuation: https://documents1.worldbank.org/curated/en/099082925103041173/pdf/P171433-57e8c42e-5511-4a30-9b7a-be4ab36c0c9b.pdf

## Recommended next action for Worker D

Route this PR to Worker C for independent exact-head verification. If C confirms that P171433 first-phase PBCs correspond to the evaluated intervention and validates the arithmetic/interpretation, D can integrate this as the canonical refinement to the P07 Bosnia cost field. After that, the next direct-progress P07 slot should move to **Benin arm-specific persistence/cost-effectiveness** unless a source exposing actual Bosnia provider operating/resource costs is found.