# P05 decision product: parent attendance-information messaging as a bounded exposure test

Date: 2026-09-11
Operator: A
Status: producer-ready Tier-2 candidate for Worker C verification; do not integrate before C verdict and D decision

## Decision question

Worker D released one bounded P05 question: is there a costed intervention that improves realized remedial exposure enough to change the Zambia Catch Up marginal-allocation decision?

PR #94 established that the tested extra-CPD arm should not be the default marginal spend and that no attendance/fidelity substitute should be preferred without a defensible cost denominator, measured exposure effect, and downstream learning/outcome evidence.

## Verdict

**TEST, not SCALE:** high-frequency caregiver attendance/performance messaging is the strongest bounded candidate found.

The closest same-study evidence is a randomized evaluation in seven low-income schools in Santiago, Chile. Weekly attendance messages plus monthly grade/behavior messages increased attendance by 1.1 percentage points, improved math grades by 0.09 SD and language scores by 0.11 SD, and cost US$10.86 per student per year. This clears the strict evidence screen for a candidate test because cost, attendance, and learning were measured in the same intervention.

Source: J-PAL, *Reducing Parent-School Information Gaps and Improving Education Outcomes: Evidence from High-Frequency Text Messages*: https://www.povertyactionlab.org/evaluation/reducing-parent-school-information-gaps-and-improving-education-outcomes-evidence-high
Peer-reviewed paper: https://doi.org/10.3368/jhr.1121-11992R2

Two African studies narrow portability uncertainty without closing it:

- In low-income Cape Town neighborhoods, weekly parent messages reporting after-school-program attendance increased attendance at those sessions by about 5.6%-6.1% and cost about R1.01 per child per week. This is close to the remedial-exposure mechanism but does not establish downstream learning effects. Source: https://open.uct.ac.za/handle/11427/25411
- In Zambia, a nine-month parent-facing SMS plus monthly-meeting early-reading intervention improved reading by roughly 0.19-0.28 SD and had an estimated national-expansion cost of US$20-22 per child. This supports local feasibility of parent-facing low-tech education support with learning effects, but it did not isolate attendance/exposure as the mechanism. Source: https://doi.org/10.1080/09645292.2021.1988518

These studies do not justify assuming the Chile effect transfers to Zambia Catch Up.

## Candidate intervention

For Grade 3-5 Catch Up pupils, send caregivers a short weekly message based on recent administrative data stating whether the child:

1. attended school;
2. attended intended Catch Up sessions while present; and
3. met a simple attendance goal.

Keep the minimum viable intervention informational. Do not bundle new tutoring, transport subsidies, cash incentives, or additional teacher CPD, because bundling would prevent clean identification of the exposure mechanism.

The pilot should distinguish:
- absent from school;
- present at school but missed Catch Up;
- Catch Up unavailable/not delivered;
- Catch Up attended.

Only the first and possibly part of the second are plausibly family-controllable.

## Cost denominator

Use US$10.86 per student-year only as the closest same-package research denominator, **not** as a Zambia budget estimate.

A Zambia micro-costing must include attendance-data capture/cleaning, caregiver-number matching, messaging fees, failed-message handling, staff time, monitoring, and any evaluation costs.

Do not substitute the Cape Town R1.01/week or Zambia US$20-22 reading-package figures as portable Zambia attendance-message costs because the accounting scopes and intervention bundles differ.

## Allocation implication

### TEST

Allocate the next bounded P05 implementation-comparison slot to a small randomized Zambia Catch Up attendance-information pilot only if reliable child-level exposure data can be produced at low incremental cost.

Recommended arms:
- control: existing Catch Up;
- treatment: weekly caregiver information on school + Catch Up attendance.

Primary mechanism outcomes:
1. school attendance;
2. Catch Up attendance conditional on school presence;
3. total realized Catch Up sessions.

Downstream outcomes:
4. targeted literacy/numeracy;
5. broader competency outcome where available;
6. persistence at later assessment.

Required cost outcomes:
7. incremental cost per treated child;
8. incremental cost per additional realized Catch Up session.

### DO NOT SCALE

Do not fund national-scale messaging from current evidence. Chile has stronger administrative data systems and differs materially from Zambia; Cape Town lacks learning outcomes; and the Zambia SMS study changes home reading directly rather than remedial attendance.

### STOP

Stop this candidate if Zambia cannot cheaply distinguish school absence from present-but-missed-Catch-Up and session non-delivery. Without this decomposition, messaging cannot be tied to the bottleneck identified by PR #94.

Also stop or downgrade after a pilot if messaging improves recorded attendance without meaningful added Catch Up exposure, or if added exposure does not improve policy-relevant learning.

## Decision delta

Before this search, P05 had a mechanism target (realized exposure) but no costed candidate package.

After this search:
- parent attendance-information messaging becomes the leading **testable** exposure candidate;
- the next marginal P05 empirical dollar should favor a small mechanism-resolving pilot over more generic CPD research, conditional on usable exposure-data infrastructure;
- the evidence remains insufficient for Zambia scale-up or for claiming superior cost-effectiveness versus standard Catch Up.

## Portability limits

- Chile is a different institutional and income context despite the study's low-income schools.
- Cape Town evidence is mechanism-close but lacks learning outcomes and is a master's thesis.
- The Zambia SMS-reading package is locally relevant but bundles different content and monthly meetings.
- Phone ownership, SIM churn, language, caregiver literacy, message deliverability, and data quality may alter take-up.
- Additional attendance only matters if Catch Up sessions are actually delivered with adequate instructional quality.
- Messaging cannot fix non-family-controllable causes of missed exposure.

## Confidence

- High: caregiver information can improve attendance in some settings at low direct cost.
- Moderate: this mechanism can increase supplementary-program attendance.
- Moderate: parent-facing low-tech education support is operationally plausible in Zambia.
- Low-to-moderate: a Zambia Catch Up attendance-message package would improve learning.
- Low: current evidence supports national rollout or a portable cost-effectiveness estimate.

## Kill-test verdict

**PASS for a bounded TEST candidate; FAIL for SCALE.**

The candidate clears the test-level screen because a randomized low-income-school study measures cost, attendance, and learning together; African evidence separately supports supplementary-session attendance response and Zambia-specific low-tech parent outreach. The cross-study triangulation is not evidence of Zambia effectiveness and must remain explicitly bounded.

## Controller handoff

Assignment: one bounded P05 exposure-intervention decision product.
Decision delta: identified parent attendance-information messaging as a defensible **test** candidate while rejecting scale inference.
Confidence: moderate for pilot allocation; low for scale allocation.
Blockers: independent Worker C verification and exact-head CI.
Recommended next action: C independently verifies cost, attendance, learning definitions, and portability; D integrates or rejects.