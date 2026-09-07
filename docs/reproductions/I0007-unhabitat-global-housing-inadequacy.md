# Reproduction note — I0007 UN-Habitat global housing inadequacy

Status: **reproduced with material qualification**

HumanityAI record checked: `I0007` in `data/indicators.json`.

## Claim checked

`I0007` records UN-Habitat's 2026 estimate that **up to 3.4 billion people worldwide lack access to secure, safe, and adequate housing**, and explicitly treats the figure as a broad, overlapping measure rather than a census of one precisely defined housing deficit.

## Independent source check

Primary source: UN-Habitat, *World Cities Report 2026: The Global Housing Crisis — Pathways to Action*.

https://unhabitat.org/world-cities-report-2026

The report's key findings state that **up to 3.4 billion people worldwide lack access to adequate housing**. The same passage says this encompasses more than 1.1 billion people living in informal settlements and describes the global crisis as multidimensional, including affordability, displacement, informality, sustainability/resilience, and liveability.

The report page independently repeats the `up to 3.4 billion` framing and describes more than 1 billion people in informal settlements and slums.

## Cross-publication consistency check

UN-Habitat communications around the same housing agenda do not always use the same headline count. A November 2025 World Urban Forum briefing described **nearly 3 billion** people as living in inadequate housing, while a May 2026 WUF summary similarly described **nearly 3 billion** as affected by inadequate conditions, unaffordable costs, or lack of basic services. Later 2026 UN-Habitat communications use the **up to 3.4 billion** figure.

These are not necessarily contradictory estimates: the wording and covered dimensions differ. But the variation is evidence that 3.4 billion should not be treated as a stable point estimate with census-like precision.

## Result

**Reproduced with qualification.** The canonical value and `up to` wording are directly supported by UN-Habitat's flagship 2026 report. HumanityAI's existing limitations correctly warn that housing inadequacy is multidimensional and overlapping.

## Qualification that matters

The figure is best interpreted as a broad upper estimate of people affected by one or more forms of inadequate housing, not as a unique count produced from one globally harmonized binary housing-status variable.

At least four interpretation risks should remain explicit:

1. **Definition sensitivity:** affordability, tenure security, crowding, physical adequacy, service access, environmental hazards, informality, and displacement are distinct but overlapping dimensions.
2. **Overlap:** the 3.4 billion figure should not be added to counts for informal settlements, homelessness, or forced displacement.
3. **Communication variance:** UN-Habitat materials around the same period also use `nearly 3 billion`, indicating that headline counts depend on scope and framing.
4. **Decision limits:** the scale estimate says nothing by itself about which housing intervention is effective or cost-effective in a particular context.

## Reproduction disposition

- `I0007` headline value: **reproduced**
- `up to` qualifier: **reproduced and essential**
- interpretation as a broad overlapping estimate: **reproduced**
- machine-readable correction required: **no**
- additional caution warranted: **yes — do not present 3.4 billion as a precise point estimate**

No correction to `data/indicators.json` is warranted from this reproduction. The existing P04 brief already preserves the `up to` qualifier and overlap warning. The highest-value next P04 work is intervention-effectiveness evidence or a genuinely complementary baseline with a clearly different construct, rather than another headline count of housing inadequacy.
