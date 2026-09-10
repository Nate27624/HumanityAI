# P05 decision gate: route foundational-learning interventions by delivery capacity

Date: 2026-09-08  
Updated: 2026-09-10  
Operator: Worker B  
Status: exploration candidate; Tier-2 decision-bearing research; requires fresh independent Worker C verification and Worker D integration

## Decision question

When a low- or middle-income education system has weak foundational learning, should HumanityAI allocate more compute to comparing intervention labels (structured pedagogy, Teaching at the Right Level, education technology, inputs), or first diagnose whether the system can reliably deliver the teacher support, instructional time, assessment, materials, and monitoring required for an evidence-backed intervention to work at scale?

## Current evidence in HumanityAI

Canonical P05 evidence is currently mostly indirect or insufficient for this specific decision. E0001 records school-attendance effects from unconditional cash transfers; E0003 records mixed education effects from off-grid electrification; E0005 records insufficient evidence for organised sport improving developmental outcomes. None provides a decision rule for foundational-learning delivery architecture.

## Evidence reviewed

### 1. Strong evidence favors targeted instruction and structured pedagogy over input-only approaches

The 2023 Global Education Evidence Advisory Panel (GEEAP) review, hosted by the World Bank with FCDO, UNICEF Innocenti, and USAID support, classifies structured pedagogy and instruction targeted to students' learning level rather than grade as among the most cost-effective education interventions in low- and middle-income countries. The same synthesis classifies computer hardware alone and other input-focused spending that does not address underlying instructional constraints as "Bad Buys" because these approaches usually do not generate additional learning.

Primary/official sources:
- World Bank / GEEAP, *2023 Cost-Effective Approaches to Improve Global Learning*: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099420106132331608
- World Bank summary, 2023-05-09: https://www.worldbank.org/en/news/press-release/2023/05/09/education-smart-buys-cost-effectively-supporting-teachers-and-parents-can-lead-to-significant-learning-improvements

Interpretation: this supports a broad preference for evidence-backed instructional models over hardware/input procurement in isolation. It does **not** establish that any named model will work equally well in every system or that GEEAP categories are portable cost-effectiveness coefficients.

### 2. The same intervention family can perform differently because implementation capacity differs

World Bank implementation material comparing structured-pedagogy experiences emphasizes that apparently similar programs can produce very different outcomes. High-quality delivery requires well-designed lesson plans, teacher practice and training, ongoing coaching, classroom observation, school-leader support, local monitoring, materials availability, and ministry-level accountability. This is a systems requirement, not simply a curriculum choice.

Sources:
- World Bank, *A focus on improving the learning experience in the classroom*, 2023-06-27: https://blogs.worldbank.org/en/education/focus-improving-learning-experience-classroom
- World Bank, *A tale of two early-grade reading programs*, 2023-11-06: https://blogs.worldbank.org/en/education/tale-two-early-grade-reading-programs

Interpretation: implementation fidelity and system capacity can mediate realized effects. These sources are implementation syntheses rather than new randomized estimates and should not be treated as standalone causal effect estimates.

### 3. Coaching intensity is an explicit cost-versus-fidelity tradeoff

World Bank coaching guidance describes a concrete operational bottleneck: pedagogical leaders supporting more teachers make fewer visits per teacher, and evidence from Kenya's Primary Math and Reading Initiative found a smaller school-to-support-officer ratio produced a larger Kiswahili effect than a larger ratio, although not for English. Guidance based on high-impact coaching programs also stresses sustained teacher contact and manageable teacher-to-coach ratios.

Sources:
- World Bank, *Coach Program Overview Document*: https://documents1.worldbank.org/curated/en/854561630421992004/pdf/Coach-Program-Overview-Document.pdf
- World Bank, *8 Tips to Structure Effective One-to-One Support Systems for Teachers*: https://blogs.worldbank.org/en/education/8-tips-structure-effective-one-one-support-systems-teachers

Interpretation: coach coverage is measurable and decision-relevant. It should not be converted into a universal threshold because appropriate ratios depend on program structure, coach expertise, geography, transport, technology, subject, and monitoring systems.

### 4. Zambia provides a concrete incremental-package test, but not yet a proven substitute package

Zambia's Ministry of Education adapted Teaching at the Right Level into the Catch Up program and scaled it through government delivery. J-PAL's 2026 results material reports a cluster-randomized evaluation across 273 public primary schools plus a separate long-run analysis using 4.4 million Grade 7 exam scores.

The reported comparison is useful because it holds the core Catch Up model relatively fixed while varying an additional teacher-support component. Standard Catch Up improved foundational literacy by about 0.10 SD and numeracy by about 0.15 SD over two years. Adding extra continuous professional development (CPD) increased reported per-student cost from US$9.63 to US$19.97 over two years but produced no detectable additional student learning gain over standard Catch Up. A separate long-run analysis reports gains of about 0.14 SD in language and 0.11 SD in mathematics for cohorts expected to have full exposure. J-PAL also reports that the estimated mathematics cost-effectiveness of the same program changes by a factor of about 2.6 depending on whether the outcome is targeted skills or broader competencies.

J-PAL reports low realized exposure: only about one-third of students attended a remedial class on a given school day, with broader absenteeism accounting for a substantial part of the missing exposure. This makes exposure a high-value mechanism-resolution target. It does **not** show that an attendance- or fidelity-focused spending package is already superior to the tested CPD package, because this note does not contain a commensurate alternative with measured marginal cost and learning effect.

Sources:
- J-PAL completed Zambia results/evaluation surface: https://www.povertyactionlab.org/evaluation/targeting-foundational-skills-improve-learning-scale-zambia
- J-PAL webinar/dissemination page, 2026-07-28: https://www.povertyactionlab.org/event/webinar-targeting-foundational-skills-improve-learning-scale-zambia
- J-PAL printable 2026 results summary: https://www.povertyactionlab.org/print/pdf/node/8138082
- Older J-PAL evaluation surface: https://www.povertyactionlab.org/evaluation/does-continuous-professional-development-improve-teaching-right-level-zambia

Important source-state caveat: an older J-PAL evaluation page still says results are forthcoming while newer J-PAL results/dissemination material reports completed findings. Preserve this publication-surface inconsistency rather than silently harmonizing it.

Interpretation: the relevant Zambia inference is bounded. HumanityAI should **not default marginal resources to this tested additional CPD package** when it approximately doubles per-student cost without detectable additional student learning. The evidence does not yet justify an affirmative CPD-to-attendance/fidelity spending substitution. The next question is which missing-exposure margin is controllable and whether any candidate package can improve it at acceptable marginal cost on comparable outcomes.

### 5. Unit cost varies enough that intervention labels alone are not adequate for ranking

A 2026 World Bank discussion of education financing gives illustrative costs of roughly $8 per student per year for Kenya's Tusome structured-pedagogy program, around $10 for in-person TaRL in Madagascar, and around $87 for a Guinea TaRL pilot. Those figures are highly context- and design-specific and should not be pooled into a portable "TaRL cost" or "structured pedagogy cost."

Source:
- World Bank, *How to boost learning in low-income countries: Raising revenues or cutting costs?*, 2026: https://blogs.worldbank.org/en/education/how-to-boost-learning-in-low-income-countries

Interpretation: the approximately order-of-magnitude spread is a warning against scalar modality rankings without common definitions of service intensity, scale, included costs, and realized implementation quality.

## Decision delta

The evidence changes the recommended framing from **Which education intervention class is best?** to **Which evidence-backed instructional package can this specific delivery system execute with sufficient fidelity, support intensity, and recurring budget to produce learning gains at scale, and which incremental support components actually earn their marginal cost?**

For Zambia, the result supports a narrower allocation change than the prior draft stated: **do not default the next marginal package to the tested extra CPD arm.** Instead, allocate the next analytical slot to mechanism resolution: decompose why intended Catch Up exposure was missed, identify which margin is program-controllable, and search for a costed candidate intervention on that margin. Until a candidate is measured on a compatible learning outcome and marginal-cost basis, preserve uncertainty rather than claiming that resources should already move to attendance/fidelity spending.

A first-pass routing model should ask:

1. **Learning bottleneck:** Are students substantially below grade-level foundational skills, making targeted instruction/remediation relevant, or is the main bottleneck elsewhere?
2. **Teacher execution capacity:** Can teachers use structured lesson materials or regroup students by current learning level within available instructional time?
3. **Realized exposure:** Are students actually receiving the intended remedial sessions, at the intended frequency and duration?
4. **Exposure decomposition:** Of missed exposure, how much is absence/dropout/switching versus present-at-school but missed-Catch-Up participation?
5. **Controllability:** Which exposure or fidelity margin can the program plausibly change without assuming effects from an untested package?
6. **Support architecture:** Is there a credible coaching/supervision system with realistic visit frequency, travel burden, coach caseload, and role clarity?
7. **Marginal support value:** Does an additional support component measurably improve learning or a validated intermediate mechanism enough to justify its incremental cost?
8. **Materials and assessment:** Can student materials and low-burden formative assessments be supplied repeatedly and on time?
9. **Monitoring/fidelity:** Can the system observe whether the intervention is actually being delivered rather than merely procured or announced?
10. **Recurring affordability and outcome choice:** Are package comparisons using compatible cost definitions, horizons, exposure, and policy-relevant learning outcomes?

## START / MORE / LESS / STOP

**START**
- Use Zambia as a bounded within-system mechanism-resolution case: decompose absent-from-school versus present-but-missed-Catch-Up exposure and identify which margin is program-controllable.
- Search for a costed candidate package that can change the controllable margin before claiming a substitute allocation.
- Build country- or system-specific delivery-capacity profiles before ranking foundational-learning interventions.
- Compare incremental package components only on a common learning outcome, horizon, realized exposure, and marginal cost.

**MORE**
- Student attendance, dropout/switching, and actual remedial-session exposure.
- Teacher participation, adoption/fidelity by arm, and what extra CPD changed in observed practice, if anything.
- Component-level marginal costs for coaching, CPD, materials, assessment, monitoring, and any candidate exposure intervention.
- Evidence on persistence and transfer to broader skills as programs scale through government systems.

**LESS**
- Generic "EdTech vs teachers" or "TaRL vs structured pedagogy" comparisons without delivery architecture.
- Additional generic CPD/TaRL literature that does not resolve the Zambia marginal-allocation question.
- Rankings based on pilot learning effects with no scale, fidelity, exposure, or recurring-cost information.

**STOP**
- Treating the Zambia no-added-learning result as a global anti-CPD ranking.
- Treating low exposure itself as proof that an attendance- or fidelity-focused package is cost-effective.
- Claiming resources should move from CPD to a specific alternative before that alternative has a comparable marginal cost/effect estimate.
- Using a portable cost-per-student number for TaRL or structured pedagogy across countries.
- Treating training completion, policy adoption, or material distribution as evidence that instructional practice changed.
- Treating cost-effectiveness as invariant to outcome definition when targeted-skill and broad-skill measures produce materially different ratios.

## Kill test

Do **not** allocate additional comparative-compute slots to a named foundational-learning intervention in a target system if the analysis cannot identify measurable implementation pathways for teacher support, instructional delivery, recurrent materials/assessment, monitoring, and realized student exposure at intended scale.

For the tested Zambia extra-CPD package, kill or sharply downgrade default expansion on student-learning-return grounds unless new evidence establishes a decision-relevant benefit not captured by the current comparison.

For an exposure/fidelity substitute, do **not** promote it from diagnostic target to preferred spending package until the analysis identifies a program-controllable margin and a candidate intervention with sufficiently compatible marginal cost and outcome evidence. If no costed controllable candidate can be found, stop P05 expansion rather than manufacture a ranking.

For a proposed technology-heavy pathway, kill or sharply downgrade it if the technology is primarily an input purchase and there is no evidence-backed mechanism tying actual use to changed instruction or learning.

## Highest-value next evidence request

For Zambia, recover enough implementation detail to resolve the missing-exposure mechanism before proposing a replacement package. Prioritize:
- decomposition of absence/dropout/switching versus present-but-missed-Catch-Up participation;
- realized Catch Up session frequency and student exposure;
- teacher participation and adoption/fidelity by arm;
- what the extra CPD changed in observed teaching practice, if anything;
- marginal CPD cost decomposition;
- which exposure/fidelity margin is program-controllable;
- any costed intervention that plausibly changes that margin on a comparable outcome and horizon;
- broad versus targeted outcome definitions and persistence/Grade 7 transfer.

If these fields cannot support a defensible comparison, report **insufficient mechanism resolution** rather than extrapolating a general "CPD does not work" claim or asserting an unmeasured substitute.

## Confidence and limitations

**Confidence:** high that structured pedagogy and targeted instruction are evidence-backed intervention families and that hardware/input-only strategies are weak default choices; high that the Zambia result argues against default expansion of the tested additional CPD package on student-learning-return grounds; moderate-high that delivery capacity and realized exposure should gate further comparison; moderate that exposure is the highest-value next mechanism question; low-to-moderate that any specific exposure-focused intervention is presently ready for package substitution; moderate on portability beyond Zambia.

Limitations:
- GEEAP's Smart Buy categories aggregate heterogeneous studies and should not be treated as universal effect or cost functions.
- Several implementation sources are World Bank syntheses rather than independent causal studies.
- J-PAL publication surfaces are temporarily inconsistent on result status; fresh C verification should preserve that provenance caveat.
- Zambia's no-added-learning CPD result is local to this incremental package and does not establish that CPD is generally ineffective.
- The CPD package may affect intermediate dimensions even when no additional student learning is detected; intermediate changes are not automatically decision-equivalent to learning gains.
- Low exposure identifies a mechanism-resolution problem, not a proven superior attendance/fidelity investment.
- Cost-effectiveness depends materially on outcome definition and cost accounting.
- Illustrative unit costs are context-specific and may use different cost definitions.
- Structured pedagogy and TaRL can overlap or complement each other; this note does not force them into mutually exclusive categories.
- The note does not establish HumanityAI's comparative advantage in funding, implementing, or advocating education programs.

## Recommendation to Worker D

PR #94 now states the narrow decision supported by Worker C's latest qualification: **do not default marginal Zambia support to the tested additional CPD package; route the next P05 slot to mechanism resolution and candidate-package search, not to a claimed attendance/fidelity spending winner.**

If #94 receives fresh exact-head CI and independent C confirmation after this narrowing, its integration value is the incremental-package discipline: added support components must demonstrate measured marginal contribution, and a diagnostic bottleneck must not be promoted into a preferred allocation before a comparable alternative exists.

**Assignment:** finish #94 only under D's current portfolio hold.  
**Decision delta:** narrowed from an affirmative exposure/fidelity reallocation implication to a negative CPD default rule plus a bounded mechanism-resolution/candidate-search next step.  
**Confidence:** high on the Zambia-specific no-default-extra-CPD rule; moderate on exposure as the next mechanism target; low-to-moderate on any substitute package until measured.  
**Blockers:** fresh exact-head CI and fresh independent Worker C verdict after this substantive narrowing.  
**Recommendation:** no new P05 or other Tier-2 production; after integration/closure, D should perform its required coherence check before releasing replacement work.
