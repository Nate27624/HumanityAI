# Zambia Catch Up: should caregiver attendance messaging be tested next?

**Decision for:** a Zambia education implementer already considering or operating Catch Up  
**Routing answer:** **TEST, not SCALE — but only if exposure data are cheap and reliable enough to identify the bottleneck.**

## What to do

Use one bounded implementation-comparison slot for a small randomized pilot of weekly caregiver information on school and Catch Up attendance **only if** participating schools can cheaply produce child-level records that distinguish:

- absent from school;
- present at school but missed Catch Up;
- Catch Up unavailable/not delivered; and
- Catch Up attended.

If that decomposition is not reliable, **do not test the messaging add-on yet**. The message would not be tied cleanly to the exposure bottleneck and a null result would be hard to interpret.

Do **not** scale caregiver messaging nationally from current evidence.

## Why this route

The integrated P05 synthesis identifies caregiver attendance-information messaging as the strongest candidate found in its bounded search for a testable exposure intervention, not as an exhaustively best intervention.

The closest same-package randomized evidence comes from seven low-income schools in Santiago, Chile: weekly attendance messages plus monthly grade/behavior messages increased attendance by **1.1 percentage points**, math grades by **0.09 SD**, and language grades by **0.11 SD**, at a reported research cost of **US$10.86 per student-year**.

African evidence narrows, but does not remove, portability uncertainty. A Cape Town study found roughly **5.6%-6.1%** higher after-school-program attendance with weekly parent attendance messages, but did not establish downstream learning effects. A Zambia parent-facing SMS plus monthly-meeting reading package improved reading by roughly **0.19-0.28 SD**, supporting local feasibility of low-tech caregiver outreach with learning effects, but it bundled different content and did not isolate attendance as the mechanism.

These results make a Zambia mechanism test defensible. They do **not** establish Zambia effectiveness, national-scale value, or portable cost-effectiveness.

## What cannot be compared yet

Do not rank the Zambia pilot against standard Catch Up or other exposure interventions using the published cost figures. The Chile **US$10.86/student-year**, Cape Town **R1.01/child-week**, and Zambia reading-package **US$20-22/child** figures describe different packages, settings, currencies, accounting scopes, and mechanisms.

A Zambia micro-costing is required. It should include attendance-data capture and cleaning, caregiver-number matching, messaging fees, failed-message handling, staff time, monitoring, and evaluation costs.

## Minimum pilot

**Control:** existing Catch Up.  
**Treatment:** weekly caregiver information on school plus Catch Up attendance.

Measure the mechanism first:

1. school attendance;
2. Catch Up attendance conditional on school presence;
3. total realized Catch Up sessions.

Then measure downstream value:

4. targeted literacy/numeracy;
5. broader competency where available;
6. persistence at later assessment.

And measure cost:

7. incremental cost per treated child;
8. incremental cost per additional realized Catch Up session.

## What would change the recommendation

**Stop before testing** if schools cannot cheaply and reliably distinguish absence, missed Catch Up while present, and session non-delivery, or if micro-costing makes the information system implausibly expensive for a bounded mechanism test.

**Downgrade or stop after testing** if messaging improves recorded attendance without meaningful additional Catch Up exposure, if additional exposure does not improve policy-relevant learning, or if data/message delivery is too unreliable.

**Consider a later scale question** only after Zambia evidence shows meaningful additional Catch Up exposure and downstream learning with a defensible incremental cost denominator and acceptable implementation burden.

## Main uncertainties

Chile differs materially from Zambia in institutional context and administrative data. Cape Town evidence is mechanism-close but lacks learning outcomes. The Zambia study changes home reading directly and includes monthly meetings. Phone ownership, SIM churn, language, caregiver literacy, message deliverability, data quality, Catch Up availability, and instructional quality can all change the result. Messaging also cannot fix causes of missed exposure that caregivers do not control.

## Highest-value next information request

Before committing pilot resources, answer one operational question:

> Can the candidate Zambia Catch Up schools reliably and cheaply produce child-level data that separate school absence, present-but-missed Catch Up, session non-delivery, and Catch Up attendance — and what is the incremental cost of turning those data into caregiver messages?

That information determines whether the proposed mechanism can be tested cleanly and is more decision-relevant now than another broad literature search.

## Confidence

**Moderate** that this is a defensible pilot-routing choice conditional on exposure-data feasibility. **Low** that current evidence supports scale-up or a portable Zambia cost-effectiveness estimate.

## Provenance and user-value check

This product uses the integrated canonical synthesis at `docs/research/P05-parent-attendance-information-exposure-test-2026-09-11.md` and the bounded issue #128 assignment in `agent/portfolio.json`; it adds no new external evidence.

Product-value self-check before independent C review:

- reduces search/synthesis burden: **PASS**;
- produces a routing choice rather than a generic brief: **PASS**;
- avoids unsupported scalar rankings: **PASS**;
- surfaces uncertainty and non-comparability: **PASS**;
- reproducible from canonical evidence: **PENDING independent C review**;
- identifies the next highest-value information request: **PASS**.
