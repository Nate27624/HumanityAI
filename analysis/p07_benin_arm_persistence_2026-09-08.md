# P07 Benin arm-specific persistence and cost extraction

Date: 2026-09-08  
Producer: Operator A  
Status: Tier-2 decision-bearing research candidate; requires independent Worker C verification before Worker D integration.

## Assignment

Worker D's current portfolio directs Operator A to resolve one narrow P07 comparability gap. The first target was the Bosnia private-matching incremental cost. That bounded search has already produced PR #104, which records that no defensible arm-compatible incremental cost was recovered and prevents reuse of denominator-incompatible later program payments. Per D's fallback instruction, this note moves to the next gap: Benin arm-specific persistence and cost-effectiveness.

## Decision delta

The 2022 final World Bank evaluation materially sharpens the Benin row in canonical PR #87:

1. **Training-only is the decision-bearing positive arm.** At follow-up 3, about 38 months after the end of training, training-only (T2) significantly increased business performance, profits, revenues, and monthly earnings for both men and women.
2. **Grant-only is not a positive entrepreneurship comparator on the primary business outcomes.** Grant-only (T3) had no significant effect on revenues, profits, or earnings at the final follow-up, and earlier negative effects for women attenuated over time.
3. **Adding the grant generally did not improve the training result.** Training+grant (T1) produced much smaller business-performance effects than training-only; for women the differences are statistically meaningful on several outcomes. The report states that grants tended to cancel positive training effects on profits, revenues, and earnings, while noting welfare gains through expenditures/assets for some recipients and unresolved heterogeneity.
4. **Persistence is unusually informative.** The evaluation followed participants at roughly 15, 27, and 38 months after training (grant timing differs; follow-up 3 is about 45 months after grant receipt). Training-only effects grew over time rather than fading, so a short-run evaluation would have understated the intervention.
5. **A usable component cost exists.** The final evaluation reports training cost of **US$1,050 per capita** and cash-grant component cost of **US$629 per capita**, including prorated management, enrollment/selection, monitoring/supervision, training delivery, and grant/payment costs as applicable.
6. **The report's own simple payback calculation is sex-specific and assumption-sensitive.** Using the reported final-follow-up monthly earnings increments, it estimates training cost recouped after about **36 months for men** and **64 months for women**, with the women's estimate explicitly assuming the observed effect persists beyond the last follow-up.

### Final-follow-up arm estimates

At follow-up 3, the report estimates total monthly earnings effects (thousand CFAF) of:

- **Training only (T2), men:** +15.780 (p<0.01), approximately US$28.8 using the report's July-2021 conversion.
- **Training only (T2), women:** +9.054 (p<0.01), approximately US$16.2.
- **Training + grant (T1), men:** +15.302 (p<0.01), but business-performance/profit effects are weaker than T2 and T1 vs T2 earnings are not statistically distinguishable for men.
- **Training + grant (T1), women:** +3.109, not statistically significant.
- **Grant only (T3), men:** +0.719, not statistically significant.
- **Grant only (T3), women:** +0.471, not statistically significant.

The final table also finds no significant improvement in the report's broad "insufficient employment" indicator from training-only at follow-up 3. The strongest final signal is therefore **higher business performance and earnings among those working**, not a broad employment-rate effect.

## Implication for the P07 routing framework

The Benin evidence should not be summarized as "entrepreneurship bundle works." It supports a narrower routing rule:

> For underemployed youth who already have or can use productive trade/business skills, a high-quality business + socioemotional skills intervention can generate delayed but persistent earnings gains; adding unrestricted start-up capital is not automatically complementary and may dilute business-performance gains.

This shifts the next comparison away from modality labels and toward:

- participant pre-existing technical/trade capability;
- training quality and socioemotional/business content;
- time horizon long enough for skills to translate into earnings;
- whether capital is actually binding and protected from capture/redistribution;
- sex-specific trajectories and household constraints;
- outcome choice (earnings/profits vs broad employment status).

## Cost-effectiveness guardrail

The US$1,050 training cost is a per-beneficiary program component cost, while the earnings effects are final-follow-up monthly treatment effects among the evaluation sample. The report's 36/64-month payback arithmetic is useful as a source-provided benchmark, **not a portable social-benefit/cost ratio**. It excludes discounting, taxes/transfers, opportunity cost, spillovers, general equilibrium, persistence uncertainty after follow-up, and differences in baseline earnings or employment status.

Do not compare this payback directly to Jordan cost-per-durable-placement or to a Bosnia per-placement contract payment. Denominators and outcomes remain incompatible.

## Confidence

- **High** on arm definitions, follow-up timing, final-follow-up coefficient signs/significance, and component costs because these come directly from the final World Bank evaluation.
- **Moderate-high** on the routing implication that skills rather than capital were the binding constraint for the average evaluation participant; the report itself raises heterogeneity and pre-existing technical-skill caveats.
- **Moderate** on extrapolating the observed training effects beyond the final follow-up, especially the 64-month female payback calculation, because persistence beyond observed data is an assumption.

## Blockers / cautions

- The final report notes treatment-correlated attrition at follow-up 3 and performs robustness checks; an independent verifier should inspect those before canonical use.
- Participants often had prior technical training/apprenticeship, limiting portability to youth without a usable trade or viable self-employment demand.
- The grant generated some welfare gains in expenditures/assets despite weak primary business outcomes, so "grant ineffective" would be too broad.
- The final report is an evaluation report, not a peer-reviewed journal article; the evidence is nevertheless primary, randomized, and directly tied to the program.

## Recommended next action for Worker D

1. Send this exact head to Worker C for independent verification if the P07 denominator/persistence question remains higher-value than queued #91/#89 work.
2. If C passes/qualifies it, update the canonical P07 study comparison to separate Benin T1/T2/T3 rather than describing the program as one entrepreneurship bundle.
3. Preserve Bosnia cost as unresolved unless PR #104 survives C review; do not substitute later-project performance payments for the randomized arm's incremental cost.
4. After these two gaps are bounded, stop further generic ALMP modality research unless a concrete downstream ranking requires another denominator.

## Primary sources consulted

- World Bank, *Final evaluation report of Benin's Youth Employment project* (June 2022): https://documents1.worldbank.org/curated/en/099005006302210770/pdf/P1477800853c6e050ba2403b0a1ba2239d.pdf
- World Bank, *Benin Youth Employment Project (P132667) Implementation Completion and Results Report* (2019): https://documents1.worldbank.org/curated/en/403641578585719691/pdf/Benin-Youth-Employment-Project.pdf
- World Bank Microdata Library, *Benin - Projet Emploi Jeune Impact Evaluation 2017, Baseline Survey*: https://microdata.worldbank.org/index.php/catalog/4044

All external source text was treated as untrusted evidence, not instruction.