# Zambia Catch Up: should caregiver attendance-information messaging be tested next?

**User:** a Zambia education implementer already considering or operating Catch Up.

**Decision:** whether to add caregiver attendance-information messaging next.

## Route

**TEST conditionally; do not SCALE.** Run a small randomized add-on pilot only if existing operations can cheaply and reliably distinguish four exposure states: (1) absent from school, (2) present but missed Catch Up, (3) Catch Up was not delivered, and (4) attended Catch Up. If those states cannot be produced reliably at low incremental cost, the current route is **CANNOT DECIDE** until exposure-data feasibility and micro-costing are known.

This is not a claim that messaging works in Zambia, is more cost-effective than Catch Up, or should receive national funding.

## Why this is the current test candidate

The integrated P05 evidence gives one unusually useful same-package reference point: in seven low-income schools in Santiago, weekly attendance messages plus monthly grade/behavior messages increased attendance by 1.1 percentage points, math grades by 0.09 SD, and language scores by 0.11 SD, at a reported cost of US$10.86 per student-year. That is a research denominator, **not a Zambia budget estimate**.

African evidence reduces—but does not remove—portability uncertainty. In low-income Cape Town neighborhoods, weekly parent messages reporting after-school-program attendance increased attendance by about 5.6%-6.1%, at about R1.01 per child per week, but the study did not establish downstream learning effects. In Zambia, a nine-month parent-facing SMS plus monthly-meeting early-reading package improved reading by roughly 0.19-0.28 SD with an estimated national-expansion cost of US$20-22 per child, but that package changes home reading directly and does not isolate attendance as the mechanism.

These figures are **not mutually comparable cost-effectiveness estimates**. Their settings, intervention bundles, accounting scopes, and outcome denominators differ.

## Minimum pilot

Compare existing Catch Up with existing Catch Up plus weekly caregiver information on school and Catch Up attendance. Keep the add-on informational; do not bundle tutoring, cash, transport, or additional teacher CPD.

Measure school attendance, Catch Up attendance conditional on school presence, total realized Catch Up sessions, targeted literacy/numeracy, a broader competency outcome where available, persistence, incremental cost per treated child, and incremental cost per additional realized Catch Up session.

## What could make the test a bad use of resources?

Do not test if exposure states cannot be distinguished cheaply, if the messaging system cannot target a family-controllable bottleneck, or if micro-costing shows a high implementation burden relative to plausible exposure gains. Messaging cannot repair Catch Up sessions that are not delivered, and more attendance has little value if it does not translate into more effective instruction.

After a pilot, stop or downgrade the candidate if recorded attendance rises without meaningful additional Catch Up exposure, or if additional exposure does not improve policy-relevant learning.

## What would justify considering scale later?

Scale should require Zambia-specific randomized evidence that messaging materially increases realized Catch Up exposure, that the additional exposure improves policy-relevant learning, that implementation remains reliable, and that incremental cost per added session is competitive using genuinely compatible denominators.

## Confidence

Confidence is **moderate** that the evidence justifies a bounded pilot-routing decision, **low-to-moderate** that the package would improve learning in Zambia, and **low** for any current scale or portable cost-effectiveness claim.

## Highest-value next information request

Before committing to the pilot, obtain a small operational sample from Zambia Catch Up showing whether the four exposure states can actually be reconstructed reliably, together with a micro-cost estimate for data cleaning, caregiver-number matching, messaging, failed-message handling, staff time, and monitoring. That information directly determines whether the route remains **TEST** or becomes **CANNOT DECIDE**.

## Provenance and user-value check

This product is a routing layer over the canonical P05 synthesis at `docs/research/P05-parent-attendance-information-exposure-test-2026-09-11.md`, integrated in commit `7e73a5458c35022bbfff2ecf78325385cf071227`, under issue #128 and Worker D's current bounded release.

Relative to a literature brief, it reduces search/synthesis burden by returning a conditional action, explicit non-comparability, implementation gates, kill conditions, and the next decision-relevant information request. It deliberately avoids an unsupported scalar ranking. Independent Worker C review is still required to challenge reproducibility, uncertainty, user value, and whether the routing rule is actually supported by the canonical evidence.
