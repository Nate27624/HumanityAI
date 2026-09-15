# Zambia Catch Up: should caregiver attendance-information messaging be tested next?

**User:** a Zambia education implementer already considering or operating Catch Up.

**Decision:** whether to add caregiver attendance-information messaging next.

## Route

**Current route: CANNOT DECIDE.** The product does not currently establish that the prerequisite Zambia observations exist. Before committing to a pilot, obtain a small operational sample that establishes whether the four exposure states can be reconstructed reliably, whether intended caregivers have a material/actionable information gap and can reliably receive/understand messages, and the incremental micro-cost of producing the states and sending/monitoring messages.

**Route if the gates pass: TEST only as an information-gap-targeted pilot; do not SCALE.** Run a small randomized add-on pilot only if existing operations can cheaply and reliably distinguish four exposure states—(1) absent from school, (2) present but missed Catch Up, (3) Catch Up was not delivered, and (4) attended Catch Up—and a bounded pre-pilot check shows that targeted caregivers have a material, actionable information gap about those states. Reliable message receipt and a plausible family-controllable response are also required. If a gate fails, route to **DO NOT TEST** when the failure makes the mechanism implausible or uneconomic; otherwise remain **CANNOT DECIDE** until the missing observation is resolved.

This is not a claim that messaging works broadly, works in Zambia, is more cost-effective than Catch Up, or should receive national funding.

## Why this is the contingent test candidate

The integrated P05 evidence gives one unusually useful same-package reference point: in seven low-income schools in Santiago, weekly attendance messages plus monthly grade/behavior messages increased average attendance by 1.1 percentage points, math grades by 0.09 SD, and language scores by 0.11 SD, at a reported cost of US$10.86 per student-year. The closest-source review also indicates message receipt was only about 60% and the attendance effect was concentrated among students at higher dropout risk rather than broadly across low-risk students. This makes an actionable information deficit and deliverability part of the mechanism hypothesis, not optional implementation details. The US$10.86 figure is a research denominator, **not a Zambia budget estimate**.

African evidence reduces—but does not remove—portability uncertainty. In low-income Cape Town neighborhoods, weekly parent messages reporting after-school-program attendance increased attendance by about 5.6%-6.1%, at about R1.01 per child per week, but the study did not establish downstream learning effects. In Zambia, a nine-month parent-facing SMS plus monthly-meeting early-reading package improved reading by roughly 0.19-0.28 SD with an estimated national-expansion cost of US$20-22 per child, but that package changes home reading directly and does not isolate attendance as the mechanism.

These figures are **not mutually comparable cost-effectiveness estimates**. Their settings, intervention bundles, accounting scopes, and outcome denominators differ.

### Compact provenance for the quantitative anchors

The canonical evidence synthesis and its source pointers are in `docs/research/P05-parent-attendance-information-exposure-test-2026-09-11.md` (integrated at `7e73a5458c35022bbfff2ecf78325385cf071227`). Use that file to trace the Santiago +1.1 pp / +0.09 SD / +0.11 SD / US$10.86 / ~60% anchors, the Cape Town ~5.6%-6.1% / ~R1.01 anchors, and the Zambia ~0.19-0.28 SD / US$20-22 anchors to their underlying sources. These are provenance pointers, not claims of denominator comparability.

## Minimum pilot

First establish a targetable information-gap premise: sample intended caregivers and compare their understanding of recent school/Catch Up exposure with administrative records; verify that messages can be received and understood; and identify whether the missed exposure is plausibly family-controllable. If that gate is met, compare existing Catch Up with existing Catch Up plus weekly caregiver information on school and Catch Up attendance. Consider prespecified targeting or stratification by baseline information gap / dropout or absence risk rather than assuming homogeneous effects. Keep the add-on informational; do not bundle tutoring, cash, transport, or additional teacher CPD.

Measure school attendance, Catch Up attendance conditional on school presence, total realized Catch Up sessions, targeted literacy/numeracy, a broader competency outcome where available, persistence, message receipt, caregiver information accuracy, incremental cost per treated child, and incremental cost per additional realized Catch Up session.

## What could make the test a bad use of resources?

Do not test if exposure states cannot be distinguished cheaply, caregivers already know the relevant attendance/exposure state, reliable message receipt is too low, the information is not understandable/actionable, the messaging system cannot target a family-controllable bottleneck, or micro-costing shows a high implementation burden relative to plausible exposure gains. Messaging cannot repair Catch Up sessions that are not delivered, and more attendance has little value if it does not translate into more effective instruction.

After a pilot, stop or downgrade the candidate if messages are not reliably received, caregiver knowledge does not change where an information gap was expected, recorded attendance rises without meaningful additional Catch Up exposure, or additional exposure does not improve policy-relevant learning.

## What would justify considering scale later?

Scale should require Zambia-specific randomized evidence in the relevant target population that messaging materially increases realized Catch Up exposure, that the additional exposure improves policy-relevant learning, that implementation and message receipt remain reliable, and that incremental cost per added session is competitive using genuinely compatible denominators.

## Confidence

Confidence is **moderate** that the evidence justifies a bounded, information-gap-targeted pilot-routing decision **if the prerequisite observations establish the mechanism gates**, **low-to-moderate** that the package would improve learning in Zambia, and **low** for any current scale or portable cost-effectiveness claim. Until those prerequisite observations are available, the present-tense route remains **CANNOT DECIDE**.

## Highest-value next information request

Before committing to the pilot, obtain a small operational sample from Zambia Catch Up that jointly answers three questions: (1) can the four exposure states be reconstructed reliably; (2) do intended caregivers have a material, actionable information gap about those states and can messages reliably reach them; and (3) what is the micro-cost of data cleaning, caregiver-number matching, messaging, failed-message handling, staff time, and monitoring? Those observations directly determine whether the route advances from **CANNOT DECIDE** to an information-gap-targeted **TEST**, remains **CANNOT DECIDE**, or becomes **DO NOT TEST**.

## Provenance, lifecycle, and user-value check

DP0001 is **integrated on canonical main and under bounded post-integration MODIFY review**. The substantive evidence remains the canonical P05 synthesis at `docs/research/P05-parent-attendance-information-exposure-test-2026-09-11.md`, integrated in commit `7e73a5458c35022bbfff2ecf78325385cf071227`. Issue #128 governs the product-value evaluation. This correction changes routing clarity, compact provenance, and lifecycle metadata only; it does not change the previously verified quantitative or substantive claims.

Relative to a literature brief, it reduces search/synthesis burden by returning a present-tense route, a separate contingent route, explicit non-comparability, mechanism and implementation gates, kill conditions, and the next decision-relevant information request. It deliberately avoids an unsupported scalar ranking. Independent Worker C product-decision review is required on this corrected exact head before Worker D integrates the correction.
