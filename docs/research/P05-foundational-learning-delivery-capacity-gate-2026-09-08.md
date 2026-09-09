# P05 decision gate: route foundational-learning interventions by delivery capacity

Date: 2026-09-08  
Updated: 2026-09-09  
Operator: Worker B  
Status: exploration candidate; Tier-2 decision-bearing research; requires independent Worker C verification and Worker D integration

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

### 4. Zambia now provides a concrete incremental-package allocation test

Zambia's Ministry of Education adapted Teaching at the Right Level into the Catch Up program and scaled it through government delivery. J-PAL's July 2026 dissemination material reports results from a cluster-randomized evaluation across 273 public primary schools plus a separate long-run analysis using 4.4 million Grade 7 exam scores.

The reported comparison is unusually useful because it holds the core Catch Up model relatively fixed while varying an additional teacher-support component. Standard Catch Up improved foundational literacy by about 0.10 SD and numeracy by about 0.15 SD over two years. Adding extra continuous professional development (CPD) approximately doubled reported per-student cost, from US$9.63 to US$19.97 over two years, but produced no detectable additional learning gain over standard Catch Up. A separate long-run analysis reports gains of about 0.14 SD in language and 0.11 SD in mathematics for cohorts expected to have full exposure. J-PAL also notes that the estimated cost-effectiveness of the same program changed by a factor of about 2.6 depending on whether mathematics was measured using targeted skills or broader competencies.

Sources:
- J-PAL webinar/dissemination page, 2026-07-28: https://www.povertyactionlab.org/event/webinar-targeting-foundational-skills-improve-learning-scale-zambia
- J-PAL printable 2026 results summary: https://www.povertyactionlab.org/print/pdf/node/8138082
- J-PAL evaluation page: https://www.povertyactionlab.org/evaluation/does-continuous-professional-development-improve-teaching-right-level-zambia

Important source-state caveat: the evaluation landing page still says results are forthcoming, while J-PAL's July 2026 webinar and printable results summary report results. Treat the newer dissemination/results material as the current result source and preserve the website inconsistency for C to verify rather than silently harmonizing it.

Interpretation: this materially sharpens the delivery-capacity gate. The relevant comparison is not "TaRL versus teacher training" in the abstract. It is whether an **incremental support component** produces enough additional learning to justify its marginal cost in a functioning government delivery system. In Zambia, extra generic CPD did not clear that bar in the reported trial. That does not imply CPD is generally ineffective; it implies support components should be evaluated on marginal contribution, not assumed valuable because they increase implementation intensity.

### 5. Unit cost varies enough that intervention labels alone are not adequate for ranking

A 2026 World Bank discussion of education financing gives illustrative costs of roughly $8 per student per year for Kenya's Tusome structured-pedagogy program, around $10 for in-person TaRL in Madagascar, and around $87 for a Guinea TaRL pilot. Those figures are highly context- and design-specific and should not be pooled into a portable "TaRL cost" or "structured pedagogy cost."

Source:
- World Bank, *How to boost learning in low-income countries: Raising revenues or cutting costs?*, 2026: https://blogs.worldbank.org/en/education/how-to-boost-learning-in-low-income-countries

Interpretation: the approximately order-of-magnitude spread is a warning against scalar modality rankings without common definitions of service intensity, scale, included costs, and realized implementation quality.

## Decision delta

The evidence changes the recommended framing from **Which education intervention class is best?** to **Which evidence-backed instructional package can this specific delivery system execute with sufficient fidelity, support intensity, and recurring budget to produce learning gains at scale, and which incremental support components actually earn their marginal cost?**

The Zambia result changes the next allocation materially: when a core targeted-instruction package is already functioning, HumanityAI should not default to "more teacher professional development." It should first identify the binding exposure/fidelity constraint and compare incremental components on common outcomes and marginal cost.

A first-pass routing model should ask:

1. **Learning bottleneck:** Are students substantially below grade-level foundational skills, making targeted instruction/remediation relevant, or is the main bottleneck elsewhere?
2. **Teacher execution capacity:** Can teachers use structured lesson materials or regroup students by current learning level within available instructional time?
3. **Realized exposure:** Are students actually receiving the intended remedial sessions, at the intended frequency and duration?
4. **Support architecture:** Is there a credible coaching/supervision system with realistic visit frequency, travel burden, coach caseload, and role clarity?
5. **Marginal support value:** Does an additional support component measurably improve learning or fidelity enough to justify its incremental cost?
6. **Materials and assessment:** Can student materials and low-burden formative assessments be supplied repeatedly and on time?
7. **Monitoring/fidelity:** Can the system observe whether the intervention is actually being delivered rather than merely procured or announced?
8. **Recurring affordability:** Are teacher support, materials, assessment, and monitoring affordable at target scale, rather than only pilot scale?
9. **Outcome choice:** Are cost-effectiveness comparisons using outcomes that reflect the decision-relevant learning goal rather than whichever assessment makes the ratio look most favorable?

## START / MORE / LESS / STOP

**START**
- Use Zambia as a bounded within-system allocation case: standard Catch Up versus incremental CPD versus an exposure/fidelity-focused alternative if the latter can be costed and measured.
- Build country- or system-specific delivery-capacity profiles before ranking foundational-learning interventions.
- Compare incremental package components on a common learning outcome, horizon, realized exposure, and marginal cost.

**MORE**
- Student attendance and actual remedial-session exposure.
- Component-level cost and effect decomposition for coaching, CPD, materials, assessment, and monitoring.
- Evidence on how effects change as programs move from NGO/pilot delivery to government scale.
- Persistence and transfer to broader skills after intensive implementation support changes.

**LESS**
- Generic "EdTech vs teachers" or "TaRL vs structured pedagogy" comparisons without delivery architecture.
- Assuming additional teacher training is automatically the highest-return complement to an existing instructional package.
- Rankings based on pilot learning effects with no scale, fidelity, or recurring-cost information.

**STOP**
- Treating hardware procurement alone as an evidence-backed learning intervention.
- Using a portable cost-per-student number for TaRL or structured pedagogy across countries.
- Treating training completion, policy adoption, or material distribution as evidence that instructional practice changed.
- Ranking interventions when measured fidelity/exposure is too low to distinguish intervention failure from implementation failure.
- Treating cost-effectiveness as invariant to outcome definition when targeted-skill and broad-skill measures produce materially different ratios.

## Kill test

Do **not** allocate additional comparative-compute slots to a named foundational-learning intervention in a target system if the analysis cannot identify measurable implementation pathways for teacher support, instructional delivery, recurrent materials/assessment, monitoring, and realized student exposure at intended scale.

For an incremental support component such as extra CPD, kill or sharply downgrade further expansion if it materially increases recurrent cost without detectable improvement in learning or a clearly identified intermediate fidelity bottleneck that is itself strongly linked to later learning.

For a proposed technology-heavy pathway, kill or sharply downgrade it if the technology is primarily an input purchase and there is no evidence-backed mechanism tying actual use to changed instruction or learning.

## Highest-value next evidence request

For Zambia, recover enough implementation detail to explain why standard Catch Up produced gains despite low exposure and why added CPD did not add detectable learning. Prioritize:
- realized Catch Up session frequency and student attendance/exposure;
- teacher participation and adoption/fidelity by arm;
- what the extra CPD changed in observed teaching practice, if anything;
- marginal CPD cost decomposition;
- whether exposure/fidelity measures mediate learning differences;
- broad versus targeted outcome definitions and their policy relevance;
- persistence and Grade 7 transfer by expected exposure.

If these fields cannot support a defensible incremental-package comparison, report **insufficient mechanism resolution** rather than extrapolating a general "CPD does not work" claim.

## Confidence and limitations

**Confidence:** high that structured pedagogy and targeted instruction are evidence-backed intervention families and that hardware/input-only strategies are weak default choices; high that the Zambia result makes incremental-package economics a concrete P05 allocation question; moderate-high that delivery capacity, realized exposure, and fidelity should gate ranking; moderate on portability of the Zambia CPD result beyond this delivery architecture.

Limitations:
- GEEAP's Smart Buy categories aggregate heterogeneous studies and should not be treated as universal effect or cost functions.
- Several implementation sources are World Bank syntheses rather than independent causal studies.
- J-PAL's evaluation landing page and newer dissemination materials are temporarily inconsistent on result status; C should verify the current working-paper/result provenance.
- Zambia's no-added-CPD result does not establish that CPD is generally ineffective; component design, baseline teacher skill, intensity, and core-program maturity matter.
- Cost-effectiveness depends materially on the selected learning outcome.
- Illustrative unit costs are context-specific and may use different cost definitions.
- Structured pedagogy and TaRL can overlap or complement each other; this note does not force them into mutually exclusive categories.
- The note does not establish HumanityAI's comparative advantage in funding, implementing, or advocating education programs.

## Recommendation to Worker D

PR #94 now clears the previously missing downstream-use test better than when it was deferred: it contains a named within-system resource-allocation question with a reported marginal-cost contrast. If verifier capacity is available after already-integrated P03/P06 work, prefer one bounded verification/update cycle on this Zambia-specific decision over a generic P05 review. The verifier should explicitly check the current J-PAL result provenance, effect estimates, incremental CPD comparison, cost definitions, exposure interpretation, and outcome-measure sensitivity.

Do not promote this to a global TaRL or CPD ranking. The decision value is the **incremental-package rule**: once a core evidence-backed instructional model is functioning, spend the next dollar on the binding delivery constraint rather than on support intensity by default.
