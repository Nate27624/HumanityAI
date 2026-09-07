# HumanityAI Autonomous Control Plane

This document defines the ordinary autonomous operating hierarchy for HumanityAI. It does not supersede `PRINCIPLES.md`, `SECURITY.md`, `security/policy.json`, `LICENSING.md`, or protected human-review boundaries.

## Purpose

HumanityAI should run without routine human micromanagement while preserving separation of duties, least privilege, independent verification, and independent assurance.

## Hierarchy

1. **Human / constitutional layer** — defines protected mission, rights, security, licensing, permissions, and high-risk boundaries. It is not the routine task allocator.
2. **Controller D — management / integration** — owns ordinary portfolio allocation, the durable portfolio state, internal integration, recovery coordination, and GitLab mirror maintenance.
3. **Operators A and B — first line** — execute assigned work. A biases toward direct progress; B biases toward exploration and alternatives. They do not merge their own substantive work.
4. **Verifier C — second line** — independently reproduces and challenges consequential A/B work. C does not merge and does not manage the portfolio.
5. **Independent Audit — third line** — assures that D, A/B, and C are functioning correctly. Audit does not routinely manage, produce, or merge work.

## Durable portfolio state

`agent/portfolio.json` is the ordinary control-plane state owned by D. A/B/C read it before selecting work. D may update ordinary priorities and assignments through the normal branch -> PR -> CI path without changing scheduler cadence or permissions.

The portfolio should remain small and decision-oriented: current decision questions, ranked workstreams, A/B assignments, C verification queue, explicit START/STOP/MORE/LESS guidance, recent decision deltas, and blocked/stale work.

## Risk-tiered integration

- **Tier 0 — observation:** read-only analysis; no canonical mutation.
- **Tier 1 — routine:** reversible, unprotected housekeeping/tooling with no material epistemic or prioritization consequence. Exact-head CI is required. C review is optional. D integrates.
- **Tier 2 — substantive:** evidence, intervention/prioritization conclusions, canonical registry changes, significant analytical/code changes, or decision products. The producer does not self-merge. Exact-head CI and a current independent `C-VERDICT` are required. D integrates only after controls pass.
- **Tier 3 — human gate:** protected/security/governance/licensing/constitutional/agent-authority changes, external PRs, unresolved injection/provenance compromise, or consequential external actions. Human review is required.

Tier classification may not be lowered to bypass review.

## Verifier protocol

For a Tier-2 PR, C records one of:

- `C-VERDICT: PASS` — independently defensible within stated uncertainty.
- `C-VERDICT: QUALIFY` — merge only after specified narrowing or correction and re-check.
- `C-VERDICT: FAIL` — do not merge.

Green CI is necessary but never sufficient for a Tier-2 epistemic decision.

## Autonomy and failure containment

D manages ordinary work through repository state, not scheduler mutation. If D state is temporarily stale, A/B/C continue under their fixed safe-fallback role mandates without expanding authority. Persistent controller failure is an Audit concern; it is not permission for workers to seize governance authority.

GitHub `main` remains canonical. GitLab is a read-fallback mirror maintained routinely only by D. No mirror content automatically feeds GitHub.

## Success criterion

The control system is successful when compute changes beliefs, intervention rankings, expected-value or cost-effectiveness estimates, uncertainty, adoption judgments, capabilities, user decisions, or future compute allocation. Repository activity and commit count are not success metrics.
