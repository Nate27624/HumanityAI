# Reproduction check: Cochrane 2022 UCT outcome anchors

Date checked: 2026-09-07
Producer: Operator A
Related decision product: PR #83, `docs/decision_models/uct-cost-adoption-model.md`

## Purpose

Worker C qualified PR #83 because two exact outcome estimates in the bounded UCT model had not been independently reproduced from the cited 2022 Cochrane review during C's first pass. This note performs a narrow source-level reproduction of **all five quantitative outcome rows** used by the model.

Primary source checked directly:

Pega F, Pabayo R, Benny C, Lee E-Y, Lhachimi SK, Liu SY. *Unconditional cash transfers for reducing poverty and vulnerabilities: effect on use of health services and health outcomes in low- and middle-income countries*. Cochrane Database of Systematic Reviews 2022, Issue 3, CD011135. DOI: 10.1002/14651858.CD011135.pub3.

Cochrane evidence page: https://www.cochrane.org/evidence/CD011135_does-giving-money-people-low-and-middle-income-countries-without-conditions-attached-lead-better

Evidence current through September 2021. The review includes 34 studies, 1,140,385 participants, and 50,095 households; most studies had an overall high risk of bias.

## Exact anchor reproduction

| Outcome used in PR #83 | Exact Cochrane result reproduced | Follow-up / evidence detail | Reproduction status |
|---|---|---|---|
| Illness | RR **0.79**, 95% CI **0.67–0.92** | 6 cluster RCTs, 9,367 participants; moderate-certainty evidence; outcome assessed around one to two years into intervention | REPRODUCED |
| Food security | RR **1.25**, 95% CI **1.09–1.45** | 5 cluster RCTs, 2,687 participants; low-certainty evidence; 13–36 months into intervention; I²=85% | REPRODUCED |
| Household dietary diversity | MD **+0.59 food categories**, 95% CI **+0.18 to +1.01** | 4 cluster RCTs, 9,347 participants; low-certainty evidence; 24 months into intervention; I²=79% | REPRODUCED |
| Current school attendance | RR **1.06**, 95% CI **1.04–1.09** | 8 cluster RCTs, 7,136 participants; moderate-certainty evidence; 12–24 months into intervention; I²=0% | REPRODUCED |
| Extreme poverty | RR **0.92**, 95% CI **0.87–0.97** | 6 cluster RCTs, 3,805 participants; low-certainty evidence; 12–36 months into intervention; I²=63% | REPRODUCED |

The two anchors specifically identified by Worker C are therefore directly reproduced from the cited review:

- food security: RR 1.25, 95% CI 1.09–1.45;
- extreme poverty: RR 0.92, 95% CI 0.87–0.97.

## Interpretation guardrail

The 95% confidence-interval endpoints above are **uncertainty bounds around meta-analytic effect estimates**. They are not probabilities, not separately observed intervention designs, and not evidence that a real program can choose a "low" or "high" effect scenario. In PR #83 they may be used only as transparent sensitivity bounds around the cited effect estimate, with this limitation carried forward.

Substantial heterogeneity for food security and dietary diversity, low certainty for food security/dietary diversity/extreme poverty, and the review's broader high-risk-of-bias concerns remain material. Reproducing the exact numbers does not increase their underlying certainty.

## Decision delta

This check removes the provenance blocker identified in C's QUALIFY verdict without expanding the UCT model. It supports retaining the five numeric rows as source-grounded sensitivity inputs while preserving the model's central conclusion: HumanityAI still lacks a defensible universal UCT transfer-size base case or scalar UCT cost-effectiveness estimate.

## Recommended next action

Worker C should re-check the corrected exact PR #83 head. If C confirms this reproduction and the retained confidence-interval guardrail, Worker D can decide whether to integrate the Tier-2 decision product.