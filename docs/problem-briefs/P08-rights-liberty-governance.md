# P08 — Rights, liberty, governance, and institutional quality

**Status:** early synthesis, reviewed 2026-09-07  
**Problem definition:** civil liberties, political rights, corruption, rule of law, state capacity, discrimination, access to justice, and institutional accountability.

This brief summarizes current HumanityAI records. It is not a democracy ranking, a single governance score, or a recommendation for a particular political system or intervention.

## What the current evidence says

### Large-scale political-rights constraints remain a material global condition

HumanityAI evidence record [`E0004`](../../data/evidence.json) summarizes the 2026 peer-reviewed V-Dem assessment of world regime types. V-Dem estimates that **74% of the world's population — about 6 billion people — lived in autocracies in 2025**, with 92 countries classified as autocracies and 87 as democracies.

The same source explicitly preserves classification uncertainty. Around regime thresholds, its uncertainty analysis allows materially different country totals: democracies could range from 74 to 95 and autocracies from 84 to 105. HumanityAI therefore treats the headline classification as a useful descriptive baseline, not as a natural or perfectly measured binary.

Source: V-Dem / *Democratization*, *State of the world 2025: unravelling the democratic era?* (published 18 May 2026): https://doi.org/10.1080/13510347.2026.2661683

### Regime type is only one dimension of P08

A country-level democracy/autocracy classification does **not** directly measure every capability relevant to rights and institutional quality. It can miss or compress differences in:

- civil liberties and freedom of expression;
- due process and access to justice;
- rule of law and judicial independence;
- corruption and administrative integrity;
- state capacity and service delivery;
- minority rights and discrimination;
- local versus national governance;
- practical ability to exercise formally recognized rights.

This is currently one of the clearest measurement gaps in HumanityAI. P08 has a regime-type baseline, but it does not yet have a dedicated canonical rule-of-law, civil-liberties, corruption, justice-access, or state-capacity indicator.

### Forced displacement overlaps with governance and rights failures but is not a governance score

Indicator [`I0006`](../../data/indicators.json) records UNHCR's estimate of **117.8 million forcibly displaced people worldwide at the end of 2025**. The underlying causes include conflict, persecution, violence, human-rights violations, and events seriously disturbing public order, so the record is relevant to P08 as well as P01 and P04.

But displacement must not be interpreted as a direct ranking of institutional quality. A person can be displaced across or within borders for heterogeneous reasons, and changes in the global stock can reflect returns under difficult conditions as well as genuine improvements.

Source: UNHCR, *Global Trends 2025* (11 June 2026): https://www.unhcr.org/global-trends

### Existing tools can support policy analysis without proving policy effectiveness

Resource [`RSC0002`](../../data/resources.json), **OpenFisca**, is an open-source rules-as-code engine for representing and simulating tax and benefit legislation. It is relevant to P08 because transparent, machine-readable rules can help inspect eligibility, administrative design, and distributional consequences across jurisdictions.

Its existence is not evidence that rules-as-code improves governance outcomes, rights protection, compliance, legitimacy, or administrative quality. Model quality depends on the accuracy and maintenance of jurisdiction-specific rulesets, and simulation alone does not establish behavioral or macroeconomic effects.

## What is not yet established

Current HumanityAI records do **not** establish:

- a single defensible global score for rights, liberty, governance, and institutional quality;
- that democracy/autocracy classification fully captures lived freedom or institutional performance;
- which institutional reform reliably improves rights, state capacity, accountability, or access to justice across contexts;
- the comparative cost-effectiveness of anti-corruption, rule-of-law, transparency, electoral, decentralization, civic-information, or public-administration reforms;
- that formal adoption of a law, strategy, institution, or digital system produces effective implementation;
- that institutional change beneficial on average distributes gains and burdens fairly across minorities, dissidents, migrants, or other less-powerful groups;
- HumanityAI's comparative advantage in advocating, funding, or implementing governance reforms.

The current evidence base for P08 is therefore much stronger on **describing one major dimension of the problem** than on **identifying proven interventions**.

## High-value next evidence

The strongest next work should deepen P08 multidimensionally rather than add another near-duplicate regime count:

1. **Rule-of-law baseline.** Add a global or broad cross-national measure with transparent methodology, uncertainty, geographic coverage, and clear distinction between expert-coded and survey-based inputs.
2. **Civil-liberties / rights baseline.** Preserve separate dimensions such as expression, association, due process, and minority rights rather than collapsing them into one convenience number.
3. **State-capacity baseline.** Distinguish effective administration and service delivery from political rights; capable states can be illiberal, and liberal institutions can still have weak implementation capacity.
4. **Corruption and accountability.** Prefer measures with methodological transparency and explicit limits; perception indexes should not be treated as direct observations of all corruption.
5. **Intervention-effectiveness evidence.** Search systematic reviews and strong quasi-experimental or randomized evidence on governance reforms, including null, heterogeneous, or adverse effects.
6. **Implementation fidelity.** Separate adoption of laws, institutions, transparency systems, or digital public infrastructure from whether they are used, enforced, trusted, accessible, and rights-respecting.
7. **Rights and distribution.** Evaluate who gains or loses from institutional reforms and whether apparent aggregate effectiveness depends on coercion, surveillance, exclusion, or concentrated authority.

## Rights and distribution cautions

P08 is unusually vulnerable to false optimization because institutional measures can encode contested values. A high administrative-capacity score can coexist with coercion; a formal-rights framework can coexist with weak enforcement; majority approval can coexist with minority-rights violations.

HumanityAI should therefore keep rights, consent, pluralism, accountability, state capacity, rule of law, and distributional effects visible as separate dimensions. The goal is not to maximize one governance index. It is to understand which institutions expand people's real agency and peaceful cooperation without unjustifiably concentrating power or shifting harms onto less-powerful groups.

## Current HumanityAI records used

- Problem taxonomy: [`PROBLEM_MAP.md`](../../PROBLEM_MAP.md)
- Regime-classification evidence: [`E0004`](../../data/evidence.json)
- Cross-cutting displacement baseline: [`I0006`](../../data/indicators.json)
- Relevant policy-analysis resource: [`RSC0002`](../../data/resources.json)

The external sources remain the evidentiary authority. This brief is HumanityAI-authored synthesis and should be revised as stronger, contradictory, or more multidimensional evidence is added.
