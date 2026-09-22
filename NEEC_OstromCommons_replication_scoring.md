# NEEC Scoring: Ostrom-Style Commons Governance

**Status.** Blind replication scoring document (SCORING_PROTOCOL.md section 11), produced for a single-target replication kit. Scored natively on the v2 structure (26 criteria, `record.structure = native-v2`). Not yet inserted into any corpus; this document and its summary block are the complete deliverable of the pilot. Scored 2026-09-19.

**System.** Ostrom-style commons governance: the self-governance of common-pool resources (CPRs) by the communities that use them, through rules those communities make, monitor and enforce, in the tradition of Elinor Ostrom's *Governing the Commons* (1990) and the research programme that followed it — most systematically the eight "design principles" for robust CPR institutions (clearly defined boundaries; congruence between rules and local conditions; collective-choice arrangements; monitoring; graduated sanctions; conflict-resolution mechanisms; minimal recognition of rights to organize; and, for larger systems, nested governance).

---

## 1. Overview

**What is scored.** The institutional mechanism itself — locally crafted, monitored and enforced rules for governing a common-pool resource — not any single implementation and not a comprehensive economic system. Commons governance is applied, in the literature it draws on, to natural-resource domains with the classic CPR properties (subtractability of use, costly exclusion): irrigation water, forests, inshore fisheries, grazing land, and — by a documented extension of the same design-principle logic to land tenure — community land trusts (CLTs) for housing. It is not applied, in that literature, to wage-labour markets, currency issuance, macroeconomic stabilisation, or comprehensive political governance of the state; those remain outside the mechanism's own reach however far it is generalised.

**Scope declaration.** Class: **mechanism** (protocol 3.1) — an institution that operates inside a wider economy without itself specifying that economy. Basis: **stated** (this document's own declaration; no project owner has confirmed it — see §9). Population rule: **generalisation, not best-casing** (protocol 3.2's mechanism rule). The vector below scores the mechanism as though it governed every common-pool-resource domain it is capable of governing — forests, fisheries, grazing/pasture, irrigation and other shared water management, and CLT-style land-tenure commons — and then applies each criterion's population-scope threshold to the resulting economy-wide population, crediting the mechanism only where it does the work. Sectors the mechanism does not reach (wage labour, currency, fiscal and monetary stabilisation, comprehensive state governance) are treated as continuing under whatever other arrangements the wider economy uses; nothing is credited there. §6.5 reports a scope-narrowing scenario that excludes the CLT/housing extension, to show how much of the vector depends on that one interpretive choice.

**Evidentiary tier (protocol 4.1).** Mixed, criterion by criterion. Where a criterion is directly addressed by documented case studies — exit/opt-out (C2.5), adaptive rule-change (C3.4), internal monitoring (C3.5), cross-cultural replication (C5.5), partial/parallel operation (C5.3), and the track record itself (C5.1) — this is scored as a **real-world implementation**, on documented outcomes. Where a criterion asks about performance at unprecedented, economy-wide scale that no commons-governance case study has ever been run at (aggregate poverty elimination, automation-era demand management, compound macro-financial stress tests, national wealth Gini) this is scored as a **component-validated theoretical** extrapolation (4.1's third bullet): the claimed mechanism is scored, confidence is calibrated by the track record of the real components it draws on, and that record is treated as evidence only for the criteria it actually bears on. No criterion here is treated as purely theoretical; even the most speculative extrapolations rest on a real, if narrower, empirical base.

**Source mix (protocol 4.4).**
- *Founding literature:* Ostrom, *Governing the Commons: The Evolution of Institutions for Collective Action* (1990); the eight design principles and their later restatements (Ostrom 2005; McGinnis & Ostrom 2011 on polycentricity).
- *Peer-reviewed empirical work:* Cox, Arnold & Villamayor-Tomás, "A Review of Design Principles for Community-Based Natural Resource Management," *Ecology and Society* 15(4) (2010) — a meta-analysis of 91 case studies concluding the design principles are "well supported empirically"; the expanded 112-study version and the authors' 2016 response to a critique of that meta-analysis (below).
- *Real-world implementations at scale:* Nepal's Community Forest User Groups; the Maine lobster fishery's co-management zones; the Törbel (Switzerland) alpine grazing and irrigation commons documented since the 15th century; U.S. community land trusts.
- *Critical sources from more than one direction:* from within the empirical commons-governance field itself, Araral's (2014) methodological critique of the Cox et al. meta-analysis and the authors' point-by-point response (Cox & Villamayor-Tomás, *Environmental Science & Policy*, 2016); from a political-economy direction sceptical of "the commons" as a framework, Harvey, "The Future of the Commons," *Radical History Review* 109 (2011); and, on equity within CPR institutions themselves, Agrawal & Gupta, "Decentralization and Participation: The Governance of Common Pool Resources in Nepal's Terai," *World Development* 33(7) (2005), and Agarwal, "Participatory Exclusions, Community Forestry, and Gender," *World Development* 29(10) (2001).

**Central disclosures.** (1) This entry's real-world track record is unusually deep for a "mechanism"-class entry — centuries-long in several cases — but no single implementation operates at national economic scale, so every criterion touching economy-wide thresholds required the generalisation step in §1's scope rule, which is itself contestable (§6.5's scenario, and several flags in §6, turn on exactly how far that generalisation should reach). (2) The equity record of real CPR institutions (elite and gender/caste capture, documented across multiple countries and decades) pulls C2.4 and C4.3 down from where the design principles' own logic would place them; §6 flags both. (3) Blindness note: the protocol's own scope-class text (§3.1) lists this entry's declared examples as "Georgism / Land Value Tax, Mutual Credit / LETS, Sovereign Wealth Fund Statism, Islamic finance and one example withheld from this blind copy (the 'narrow single-mechanism' archetype)" — which discloses, ahead of any independent analysis, that the withheld target is a **mechanism** of the **narrow single-mechanism archetype**. My own analysis of what Ostrom-style commons governance actually is independently supports exactly that classification (see §9), so I do not believe the leak changed my scope call — but I record it because it is a genuine limit on how blind this particular pilot's test of "the scope question" (protocol §13, D24) can be, and it is not mine to fix.

---

## 2. Peer calibration (protocol 5)

**Declared peers.** Georgism / Land Value Tax; Mutual Credit / LETS; Sovereign Wealth Fund Statism; Islamic Finance / Profit-Sharing Banking — the corpus's other four "narrow single-mechanism" entries within the mechanism scope class, per protocol 3.1's own archetype grouping. No entry outside that archetype is declared as a peer, since the archetype match, not merely the scope-class match, is what protocol 5.1 asks for.

**The matrix (generated by `neec_entry.py --candidate`, §9.3).**

```
[OSR] Ostrom-Style Commons Governance  --  13.0/26, 5 failures, Partially Adequate
      scope: mechanism (stated); record: native-v2
        entry  Georgism / Lan  Mutual Credit   Sovereign Weal  Islamic Financ
C1.1      0.5            0.5             0.5             0.5             0.5
C1.2a     0.0            0.0             0.0             0.5*            0.5*
C1.2b     0.5            0.5             1.0*            0.5             0.0*
C1.3      0.5            0.5             0.0*            0.0*            0.5
C1.4      0.0            0.5*            0.5*            0.5*            0.0
C1.5      0.0            0.0             0.0             0.5*            0.5*
C2.1      0.5            0.5             0.5             0.5             0.5
C2.2      0.0            0.5*            0.5*            0.5*            0.0
C2.3      0.5            0.5             0.5             0.5             0.5
C2.4      0.5            0.5             0.5             0.5             0.5
C2.5      1.0            1.0             1.0             1.0             1.0
C3.1      0.5            0.5             0.5             0.5             0.5
C3.2      0.5            0.5             0.5             0.5             0.5
C3.3      0.5            0.5             0.5             0.5             0.5
C3.4      1.0            1.0             1.0             1.0             1.0
C3.5      0.5            0.5             0.5             0.5             0.5
C4.1      0.5            0.5             0.5             1.0*            0.5
C4.2      0.5            0.5             0.5             0.0*            0.0*
C4.3      0.0            0.5*            0.5*            0.5*            0.5*
C4.4      0.5            0.5             0.5             0.5             0.0*
C4.5      0.5            0.5             0.5             0.0*            0.5
C5.1      1.0            0.5*            1.0             1.0             1.0
C5.2      0.5            0.5             0.5             0.5             1.0*
C5.3      1.0            1.0             1.0             1.0             1.0
C5.4      0.5            0.5             0.5             0.5             0.5
C5.5      1.0            0.5*            1.0             0.5*            1.0
vs Georgism / Land Value Tax: differs on 5, higher on 2, lower on 3, total -0.5; neither dominates
vs Mutual Credit / LETS: differs on 5, higher on 1, lower on 4, total -1.5; neither dominates
vs Sovereign Wealth Fund Statism: differs on 10, higher on 4, lower on 6, total -1.0; neither dominates
vs Islamic Finance / Profit-Sharing Banking: differs on 7, higher on 3, lower on 4, total -0.5; neither dominates
```

**Reconciling the differences.**

- **C1.4 (vs. Georgism, Mutual Credit, SWF, all 0.5):** flagged (§6.1) with 0.5 as the named alternative — the peers' value is exactly this entry's alternative reading, so the flag *is* the reconciliation.
- **C4.3 (vs. all four peers, all 0.5):** likewise flagged with 0.5 as the alternative, for the same reason.
- **C1.2b (vs. Mutual Credit, 1.0):** flagged with 1.0 as the named alternative (§6.1); the two mechanisms differ in kind (a currency system's structural cap on the whole medium of exchange, versus a resource-specific harvest cap), which is why the scored value differs from the peer's, but the peer's evidence is close enough to warrant naming it as the alternative rather than only arguing past it.
- **C2.2 (vs. Georgism and Mutual Credit, both 0.5):** not flagged; explained instead. Both peer mechanisms provide a payment or credit line that, however modest, is not conditioned on an ongoing contribution from the recipient. Commons governance is the opposite case: continued access to the pool is conditioned on the member's own labour or dues (irrigation-maintenance duty, monitoring duty, grazing-rights dues), which is a textbook case of the criterion's own "conditional... requires some ongoing contribution" 0.5 band failing into structural failure once that condition is itself close to universal across the documented cases — see C2.2 below. The peers' evidence does not look similar enough on this point to warrant a flag; the mechanisms simply work differently.
- **C1.3 (vs. Mutual Credit and SWF, both 0.0):** not flagged; explained instead. Neither peer mechanism touches housing at all, so their 0.0 reflects absence of reach, not a judgment that a housing-commons mechanism fails the threshold. This entry's 0.5 rests on the CLT extension specifically (§6.5's scenario removes it and the score drops to 0.0, converging with these two peers).
- **C5.1 and C5.5 (vs. Georgism, both 0.5):** not flagged; explained instead. Georgism's own component record (chiefly the Alaska Permanent Fund Dividend, ~40 years, one jurisdiction) is real but narrower than the multi-country, multi-century, 91-to-112-study meta-analytic base behind the design principles (§5, §1); the higher score here reflects a materially deeper evidentiary base on this specific criterion, not a closer call.
- **C4.1 and C4.2 (vs. Sovereign Wealth Fund Statism and Islamic Finance):** not flagged; explained instead. A sovereign wealth fund is *purpose-built* for intergenerational fiscal transfer, which is why it outscores this entry on C4.1; neither a sovereign fund nor a profit-sharing bank constrains physical resource extraction at all, which is why both score below this entry on C4.2, where sustainable-yield harvest rules are commons governance's central, most direct mechanism.
- **C4.4 and C4.5 (vs. Islamic Finance and SWF respectively):** not flagged; explained instead. Neither peer mechanism's evidence engages the specific question (diffusing control over a shared physical resource; capping peer-to-peer over-extraction) that gives commons governance its higher score here — again, different mechanisms doing different work, not a close call on shared evidence.

---

## 3. Criterion by criterion

### Domain 1 — Material Security

#### C1.1 Poverty Elimination Capacity: 0.5 (Partial)
Estimated performance: real but partial, well below the 90%/85% threshold, concentrated among resource-dependent households. **Evidence.** Nepal's community forests are explicitly credited with a livelihoods role for the rural poor — leasehold community forestry was written into the 1995 Forest Rules specifically for households below the poverty line, and the wider CFUG programme is reported to benefit on the order of 15–16 million people, a large share of them subsistence-dependent on forest products (fuelwood, fodder, non-timber products) that substitute directly for cash expenditure. Maine's and other co-managed fisheries similarly secure a livelihood floor for harvester households. **Score justification.** This is a genuine, non-trivial, in-kind income effect for the population that depends on a specific commons, not a cash transfer or tax-and-dividend mechanism reaching the whole population; it reduces poverty depth for that population without approaching economy-wide elimination. This matches the corpus's standard "real but partial" 0.5 band for narrow mechanisms (identical to all four declared peers) rather than either the 1.0 or 0.0 bands.

#### C1.2a Wealth Building for Resilience: 0.0 (Structural Failure)
Estimated performance: no mechanism for individual, transferable asset accumulation exists. **Evidence.** The design principles secure *usufruct* — a right to draw a sustainable share of a resource flow — not an accumulable, transferable household asset; nothing in the Ostrom literature, or in the Nepal, Törbel, or Maine case material, describes a member building a $60,000-order household buffer through commons participation. The CLT extension (community land trusts) is the partial exception discussed under C1.3 and C1.5, but even there the ground lease is designed precisely to cap, not build, the resident's speculative equity. **Score justification.** No accumulation mechanism at all — the cleanest possible 0.0 case, on the same logic as Integral's and UBI's published 0.0 anchors for this criterion (criteria.json).

#### C1.2b Prevention of Exploitative Accumulation: 0.5 (Partial) — flagged as contestable
Estimated performance: a genuine structural cap, but on extraction from the specific pool, not on the member's wealth overall. **Evidence.** The design principles' proportionality rule ties each member's allowed take to an objective, monitored measure (Törbel: cattle grazed in summer capped in proportion to winter fodder produced; Maine: trap limits and licence caps per harvester) precisely to stop any one member from capturing a disproportionate share — this is structural, not merely a favourable outcome. **Score justification / flag.** The cap operates on the specific resource flow, not on the member's wealth taken as a whole (off-commons income, financial assets, or business ownership are untouched), which is why this is scored 0.5 rather than the 1.0 that Integral's and CCO-PTF's economy-wide anti-capture mechanisms earn. A careful second scorer could reasonably read the proportionality rule as functionally equivalent to Mutual Credit/LETS's published 1.0 on this criterion (a self-limiting medium with no possibility of unbounded individual accumulation) once the mechanism is generalised to govern every CPR in the economy simultaneously. Alternative: **1.0**, reading "structural cap read as economy-wide anti-capture, on the Mutual Credit/LETS precedent."

#### C1.3 Housing Security: 0.5 (Partial)
Estimated performance: strong on the sub-population reached, small in reach. **Evidence.** Community land trusts — the direct extension of commons-governance design principles to land tenure — are the criterion's own cited benchmark: a 10x-lower foreclosure rate than conventional mortgages (0.46% vs. 3.26% during the 2008–2010 crisis) (criteria.json, C1.3 and C5.1). But there were only 313 CLTs in the United States as of the figure the kit itself cites (criteria.json, C5.1), a small fraction of the national housing stock. **Score justification.** A real, well-evidenced, structurally decommodifying mechanism that reaches a small population share — squarely the "some cooperative/social housing alongside a still-dominant market allocation" 0.5 band, not the 1.0 band, which requires the stability rate at or above threshold *at the population scale being scored*. §6.5 reports the scenario in which this extension is excluded from the mechanism's counted domain.

#### C1.4 Automation Resilience: 0.0 (Structural Failure) — flagged as contestable
Estimated performance: no mechanism decoupling income or demand from wage labour; at most, a subsistence-in-kind buffer for the population with existing CPR access. **Evidence.** Nothing in the design-principle literature, which predates and never engages the automation-and-aggregate-demand problem this criterion tests, proposes or evidences a mechanism maintaining poverty and demand thresholds across 30/50/70% displacement scenarios. **Score justification / flag.** Scored 0.0 because the threshold is a specific, monetised stress test that the mechanism has never been designed for, evaluated against, or shown to survive — "component-validated theoretical" reasoning (4.1) cannot borrow confidence the components never earned on this specific question. Alternative: **0.5**, reading "in-kind subsistence access to commons resources credited as a partial automation-resilience buffer" — the reading under which a displaced worker's continuing access to fuel, water, fodder or fish softens (without resolving) the material impact of lost wage income, on the same logic that gives the four declared peers 0.5 here.

#### C1.5 Universal Wealth Access: 0.0 (Structural Failure)
Estimated performance: no wealth-accumulation pathway exists to be broadly or narrowly accessible. **Evidence.** As C1.2a establishes, there is no individual accumulation mechanism in the first place; access is therefore a moot question on the mechanism's own terms, consistent with the three peers (Georgism, Mutual Credit, Universal Basic Services) that also score 0.0 here precisely because their C1.2a is 0.0 too. **Score justification.** Where SWF and Islamic Finance score 0.5 on C1.5, it is because their C1.2a is 0.5 (a real, if narrow, accumulation mechanism exists to have access to); commons governance has no analogous mechanism, so 0.0 tracks its own C1.2a cleanly rather than representing a separate judgment call.

### Domain 2 — Human Autonomy

#### C2.1 Freedom from Coercion: 0.5 (Partial)
Estimated performance: meaningfully reduces one specific coercion (loss of access to a subsistence resource under pure market allocation) without addressing wage-labour coercion generally. **Evidence.** Secure, rule-based CPR access removes one axis of survival pressure for the dependent population (a Nepali household is not at the mercy of a private timber concessionaire's pricing for its fuel and fodder; a Maine lobsterman is not squeezed out by unlimited entry). **Score justification.** A real, evidenced reduction in one domain of coercion for the population that has it, well short of the 70%-reporting-genuine-autonomy threshold economy-wide — matching all four declared peers' 0.5 here exactly.

#### C2.2 Labor Non-Necessity: 0.0 (Structural Failure)
Estimated performance: access is structurally conditional on an ongoing labour or dues contribution, which the criterion's own note treats as disqualifying for partial credit. **Evidence.** Continued membership in essentially every documented CPR institution requires an active contribution — irrigation-canal maintenance duty in the Valais bisses and in South Asian systems generally, monitoring duty in Maine's zone councils, dues or in-kind labour in Nepal's CFUGs — enforced by graduated sanctions against those who do not contribute (Ostrom's design principles 4 and 5 exist specifically to make this enforcement credible). **Score justification.** C2.2's own anchor note is explicit that the criterion is "binary in character... partial credit here specifically means *time-limited or conditional* provision" (criteria.json); a right of access conditioned on continuing labour contribution is a clean example of exactly the conditionality the 0.0 band is for, more so than Georgism's or Mutual Credit's peer mechanisms (see §2), which condition on citizenship or membership rather than on an ongoing labour duty.

#### C2.3 Creative Development Opportunities: 0.5 (Partial)
Estimated performance: no direct mechanism, but a documented time/security spillover for the dependent population. **Evidence.** The literature does not evaluate arts, music or cultural-participation outcomes directly; the inference here rests on the same logic that gives every one of this entry's five declared and near peers (Georgism, Mutual Credit, SWF, Islamic Finance, MMT+JG, UBI) 0.5 on this exact criterion — a real but time-poverty-constrained security gain, not a structural time-liberation design. **Score justification.** Calibrated to the corpus-wide pattern for mechanisms with a genuine but partial material-security effect, rather than independently evidenced; flagged here in prose (not as a §6.1 flag, since it is not a close call so much as an extrapolation with thin direct evidence) as the one criterion scored primarily by peer-pattern consistency rather than commons-specific sources.

#### C2.4 Democratic Participation: 0.5 (Partial) — flagged as contestable
Estimated performance: by design, a strong instance of collective-choice economic democracy; by documented practice, diluted by elite and gender/caste capture. **Evidence.** Design principle 3 (collective-choice arrangements: those affected by a rule can participate in changing it) is realised concretely in irrigation-user assemblies, forest-user-group general meetings, and fishery zone councils — genuine "workplace democracy, community asset governance" in the criterion's own terms. Against this: Agrawal & Gupta (2005) and Agarwal (2001) document that key decision-making positions in Nepal's forest user groups sit disproportionately with land-rich, high-caste, male members, notwithstanding formal participation rights and even statutory minimum-representation quotas for women; a 2002 ForestAction Nepal review states plainly that "FUGs have been hijacked by local elites"; elite capture in participatory natural-resource management is documented well beyond Nepal (Ethiopia, Tanzania, Mexico). **Score justification / flag.** Scored 0.5 because the *practice*, not merely the *design*, is what the criterion measures, and the practice falls short of the ≥70%-participation / ≥35%-adoption thresholds once capture is accounted for. Alternative: **1.0**, reading "collective-choice governance credited at its designed strength rather than its elite-capture-discounted performance" — capture treated as a correctable implementation defect rather than a feature of the design-principle logic itself.

#### C2.5 Exit Rights and Mobility: 1.0 (Pass)
Estimated performance: clears the threshold cleanly. **Evidence.** A commons institution is, definitionally in Ostrom's own account, one among several arrangements coexisting in a wider economy; a member can decline to join or can leave a given user group, co-op, or fishery zone and participate in the surrounding market instead, and the institution's own funding does not depend on near-universal participation the way a national tax-funded programme's does — the Maine lobster zones, for instance, continue to function at whatever membership the co-management councils actually achieve. **Score justification.** Matches all four declared peers' 1.0 here exactly, and for the same underlying reason common to every genuinely narrow, opt-in mechanism in this corpus (protocol 3.2's "mechanism" logic: a mechanism does not require the whole economy's participation to keep functioning).

### Domain 3 — System Resilience

#### C3.1 Crisis Response Capacity: 0.5 (Partial)
Estimated performance: real local/firm-level resilience; no automatic, system-wide stabiliser. **Evidence.** Nepal's community forests are widely reported to have continued functioning as a source of resources and local governance through the 1996–2006 civil conflict, when many state services did not; Maine's co-management councils adapted (with strain) through the 2008 and 2012 price collapses. Neither case shows an automatic, trigger-based, economy-wide response of the kind C3.1 asks for. **Score justification.** The same "firm-level resilience doesn't translate to system-level response" logic that gives Market Socialism 0.5 on this criterion applies here; matches all four declared peers.

#### C3.2 Inflation Control Mechanisms: 0.5 (Partial)
Estimated performance: no novel safeguard, but also nothing actively inflationary. **Evidence.** Commons governance does not issue currency or set prices in a way that bears on the money supply at all. **Score justification.** The anchor note itself instructs scorers to reserve 0.0 "for cases with an active inflationary mechanism and literally no counterbalancing design element, rather than merely 'unaddressed'" (criteria.json); every mechanism-class entry in the declared and near-peer set — Georgism, Mutual Credit, SWF, Islamic Finance, MMT+JG, UBI — scores 0.5 here for exactly this reason, and this entry follows the same rule rather than departing from a uniform corpus-wide pattern.

#### C3.3 Multi-Failure Resistance: 0.5 (Partial)
Estimated performance: decentralisation gives real, but only partial and undocumented-at-compound-scale, resilience. **Evidence.** Polycentric governance theory (Ostrom 2010; V. Ostrom, Tiebout & Warren 1961) argues explicitly that many independent, self-adjusting local units are more robust to shocks than one centralised point of failure, and Nepal's and Maine's continuity through serious single-domain shocks (§C3.1) is consistent with that. No commons-governance case study has been run against, or evaluated for, the specific *compound* multi-domain stress scenarios (recession+automation; inflation+climate; cyber+economic; pandemic+supply-chain) the criterion specifies. **Score justification.** 0.5, matching every mechanism-class peer in the corpus (none of which reaches 1.0 here either) rather than borrowing Degrowth Economics' comprehensive-system 1.0, which rests on a deliberately whole-economy redesign this entry does not attempt.

#### C3.4 Epistemic Adaptability: 1.0 (Pass)
Estimated performance: clears the threshold; this is close to the mechanism's defining feature. **Evidence.** Design principles 4, 5 and 6 (monitoring, graduated sanctions, low-cost conflict resolution) exist specifically to let a CPR institution detect a rule that is failing and change it without collapsing; Törbel's rules have been adapted continuously since the 15th century, and Cox, Arnold & Villamayor-Tomás's 91-study meta-analysis (2010) treats this adaptive capacity as one of the best-supported findings in the whole design-principle literature. **Score justification.** Matches all four declared peers' 1.0 exactly, and is arguably the single best-evidenced 1.0 in this vector.

#### C3.5 Failure-Mode Transparency: 0.5 (Partial)
Estimated performance: strong internal visibility; weak visibility of costs pushed onto non-members. **Evidence.** Design principle 4 (monitoring, ideally by or accountable to the users themselves) makes within-pool failures — over-harvesting, free-riding, resource decline — visible to members quickly, on the same logic that gives Market Socialism 0.5 here ("worker ownership makes firm failures visible to members immediately"). Against this, the commons literature documents leakage and boundary-externalisation problems: pressure diverted onto unprotected forests or non-member users outside a given CPR's boundary is a standard critique of community-based natural resource management generally. **Score justification.** 0.5, matching the four declared peers exactly, for the same internally-visible/externally-opaque pattern.

### Domain 4 — Ethical Integrity

#### C4.1 Intergenerational Justice: 0.5 (Partial)
Estimated performance: a real, structural positive transfer of the specific resource, alongside an untouched wider emissions/debt picture. **Evidence.** Sustained-yield harvest rules are, on their face, a mechanism for leaving the resource itself no worse for the next generation — Törbel's grasslands and the Valais bisses have supported continuous use for five centuries specifically because extraction has been kept within regeneration. This does not touch the criterion's carbon-trajectory or debt-to-GDP components, which lie almost entirely outside CPR-governed sectors. **Score justification.** "Some positive transfer exists but is incomplete," the criterion's own 0.5 band — matching three of the four declared peers; Sovereign Wealth Fund Statism's 1.0 reflects a fiscal savings vehicle purpose-built for intergenerational transfer, a different and more direct fit for this specific criterion (§2).

#### C4.2 Ecological Compliance: 0.5 (Partial) — flagged as contestable
Estimated performance: a hard, structural constraint within the resources the mechanism governs; no constraint at all on the much larger share of economic activity it does not reach. **Evidence.** Harvest ceilings tied to measured regeneration (grazing capped to winter-fodder capacity; lobster escape vents and size limits keyed to breeding stock; forest cutting cycles keyed to regrowth) are exactly the "hard design constraint, not an optimization target traded against growth" language the criterion's 1.0 band uses. But CPR-eligible sectors are a minority of a modern economy's ecological footprint; energy, industry, transport and most land-use conversion lie outside them entirely, and the criterion demands ≥7 of 9 planetary boundaries respected economy-wide. **Score justification / flag.** Scored 0.5 because the hard constraint, real as it is, does not extend past the sectors the mechanism actually governs. Alternative: **1.0**, reading "sustainable-yield rule read as a hard ecological constraint" if the mechanism's own domain — rather than the whole economy — is taken as the relevant frame, which is also the reading under which this entry would clearly outscore Sovereign Wealth Fund Statism and Islamic Finance, neither of which constrains physical extraction at all (§2).

#### C4.3 Racial and Gender Equity: 0.0 (Structural Failure) — flagged as contestable
Estimated performance: membership and benefit-flow rules that in documented practice concentrate access and control among existing local elites, without a disproportionate corrective mechanism for historically disadvantaged groups. **Evidence.** Agrawal & Gupta (2005) and Agarwal (2001) document, across South Asian community forestry specifically, systematic exclusion of women, Dalits and the landless from both decision-making and benefit capture, notwithstanding formal, facially neutral membership rules and even statutory representation quotas, which multiple sources describe as producing token rather than substantive inclusion; comparable elite-capture patterns are documented in Ethiopia, Tanzania and Mexico. **Score justification / flag.** CPR membership rules are typically tied to existing land tenure, residency or customary status, which built-in disparities transmit forward rather than correct — closer to "formally neutral... with no active correction" than to "formal equality" with unclear reach. Scored 0.0, but genuinely contestable: none of the four declared peers score below 0.5 here, and a second scorer could reasonably read the same evidence, plus the existence of reform efforts (representation quotas), as "formal equality without reparative mechanisms" — the 0.5 band. Alternative: **0.5**, reading "documented elite/gender/caste capture read as a correctable implementation shortfall rather than a structural failure."

#### C4.4 Power Distribution: 0.5 (Partial)
Estimated performance: real diffusion of control over a specific resource away from the state or a market monopolist, undercut by concentration within the receiving community and by the wider economy's power structure being untouched. **Evidence.** Devolving forest, water or fishery control to a user body is a genuine transfer of decision rights away from a central state agency or a private concessionaire; the same elite-capture literature cited under C4.3 shows that within the receiving body, control frequently re-concentrates among local elites, and nothing in the mechanism touches wealth or political power outside the specific commons. **Score justification.** "Some diffusion of one form of power while the other remains concentrated," matching three of the four declared peers.

#### C4.5 Exploitation Elimination: 0.5 (Partial)
Estimated performance: peer-to-peer over-extraction within a pool is structurally curbed; landlord-tenant, employer-employee and creditor-debtor relationships in the wider economy are untouched. **Evidence.** Graduated sanctions against free-riders (design principle 5) are, in substance, an anti-exploitation mechanism among co-equal resource users — no member can appropriate more than the agreed share at another's expense without triggering an enforced penalty. This says nothing about wage or rental relationships outside the commons. **Score justification.** "Reduced but not eliminated... elimination in one relationship type while another persists," matching three of the four declared peers.

### Domain 5 — Implementation Viability

#### C5.1 Proven Component Foundation: 1.0 (Pass)
Estimated performance: clears the threshold with an unusually deep record. **Evidence.** Törbel's grazing and irrigation (*bisses*) rules are documented continuously since at least 1483, and by one economist's account the underlying grazing-cap arrangement dates to around 1200 CE — on the order of 500 to 800 years of continuous operation; more than 200 working bisses and 1,800 km of channels were in use across the Valais alone by the early 20th century; Nepal's Community Forest User Groups have operated at large scale for well over 40 years and, on recent counts, number in the tens of thousands, managing over 2 million hectares and reaching tens of millions of people; Maine's lobster co-management has run for over a century, with the fishery's catches "stable since World War II" and "record highs... since the late 1980s"; and Cox, Arnold & Villamayor-Tomás's meta-analysis rests on 91 (later 112) independent case studies across dozens of countries. **Score justification.** Comfortably above the ≥70%-of-components-at-≥20-years-and-≥10,000-participants threshold — arguably the best-evidenced 1.0 available in this corpus for this specific criterion, exceeding even Market Socialism's Mondragón-anchored published 1.0 (§2).

#### C5.2 Staged Transition Pathways: 0.5 (Partial)
Estimated performance: a real, documented gradual/staged rollout precedent; no rapid, crisis-context deployment doctrine anywhere in the literature. **Evidence.** Nepal's national rollout has genuine phase structure with dated legal milestones — the 1970s panchayat forest rules, the 1982 Decentralization Act, the 1993 Forest Act and 1995 Forest Regulations, expanding from pilot to tens of thousands of groups over roughly three decades. Nothing in the Ostrom literature or the case material specifies an ≤36-month rapid/crisis deployment pathway of the kind the criterion also requires. **Score justification.** "A pathway is sketched but lacks the [full] specificity... the threshold requires" — the staged half is real and dated, the crisis-deployment half is absent, which is short of Integral's "starts small and expands, that's it" 0.0 case but also short of a 1.0; matches three of the four declared peers.

#### C5.3 Partial and Parallel Deployability: 1.0 (Pass)
Estimated performance: clears the threshold; this is close to a defining structural feature. **Evidence.** Every documented case operates as one arrangement coexisting with a surrounding market economy at far below universal adoption — Maine's lobstermen sell into ordinary seafood markets, Nepal's CFUGs operate inside Nepal's broader market economy, Törbel's commons coexist with private cultivation on the same mountainside. **Score justification.** Matches all four declared peers' 1.0 exactly, for the same reason common to every genuinely narrow mechanism in this corpus.

#### C5.4 Political Coalition Potential: 0.5 (Partial)
Estimated performance: genuinely broad, cross-ideological appeal, offset by resistance from more than one direction. **Evidence.** Commons governance draws support from environmentalists and localists (sustainability, subsidiarity), from some market-oriented and property-rights-adjacent thinkers (voluntary, non-state, decentralised — Ostrom's own Nobel citation for challenging both pure state- and pure market-based solutions), and from indigenous-rights and communitarian movements (customary tenure recognition). It also draws resistance: from state-centralising traditions uncomfortable devolving control, and from a left-critical tradition (Harvey 2011) that regards "the commons" framing itself as vulnerable to being used to justify the state's withdrawal from provision it ought to be making. **Score justification.** "Appeals strongly to part of the spectrum while facing real resistance from another part," matching all four declared peers.

#### C5.5 Cultural Adaptability: 1.0 (Pass)
Estimated performance: clears the threshold with an unusually broad documented base. **Evidence.** The design principles were derived from, and have been tested against, case studies spanning high-, middle- and low-income contexts and a wide range of cultural settings — Swiss alpine villages, South Asian (Nepali, Indian) hill and plains communities, Japanese and American coastal fishing communities, and others across the 91-to-112-study meta-analytic base (§5) — with real, not merely modelled, implementation in each. **Score justification.** "Explicit... mechanisms for diverse economic/cultural contexts, with reasoning for how they'd apply" documented with real rather than modelled cross-cultural validation — matching Mutual Credit/LETS and Islamic Finance's 1.0 here, and arguably better evidenced than either given the deliberately comparative design of the underlying research programme.

---

## 4. Domain subtotals

- Domain 1 (Material Security) = 0.5 + 0.0 + 0.5 + 0.5 + 0.0 + 0.0 = **1.5/6 (25%)**
- Domain 2 (Human Autonomy) = 0.5 + 0.0 + 0.5 + 0.5 + 1.0 = **2.5/5 (50%)**
- Domain 3 (System Resilience) = 0.5 + 0.5 + 0.5 + 1.0 + 0.5 = **3.0/5 (60%)**
- Domain 4 (Ethical Integrity) = 0.5 + 0.5 + 0.0 + 0.5 + 0.5 = **2.0/5 (40%)**
- Domain 5 (Implementation Viability) = 1.0 + 0.5 + 1.0 + 0.5 + 1.0 = **4.0/5 (80%)**

## 5. Summary scores

- **Total = 1.5 + 2.5 + 3.0 + 2.0 + 4.0 = 13.0/26 (50%)**
- **Failures (criteria scored exactly 0.0):** C1.2a, C1.4, C1.5, C2.2, C4.3 — **5**
- **Tier:** 5 failures → **Partially Adequate** (3 to 5 failures, protocol 2.5)

## 6. Uncertainty

**Flag register** (5 flagged criteria, 5 independent calls; no tracking flags; all basis `stated`):

| Criterion | Scored | Alternative | Reading |
|---|---|---|---|
| C1.2b | 0.5 | 1.0 | structural cap read as economy-wide anti-capture, on the Mutual Credit/LETS precedent |
| C1.4 | 0.0 | 0.5 | in-kind subsistence access credited as a partial automation-resilience buffer |
| C2.4 | 0.5 | 1.0 | collective-choice governance credited at its designed strength rather than its elite-capture-discounted performance |
| C4.2 | 0.5 | 1.0 | sustainable-yield rule read as a hard ecological constraint rather than a resource-specific partial one |
| C4.3 | 0.0 | 0.5 | documented elite/gender/caste capture read as a correctable implementation shortfall |

**Undisputed failures** (0.0 scores no flag disputes): C1.2a, C1.5, C2.2 — 3. (C1.4 and C4.3 are 0.0 but flagged upward, so excluded from this count per protocol's definition.)

**Exhaustive enumeration** (`neec_entry.py`, protocol 6.3): 32 combinations (2⁵, all five calls independent); all 32 fall in **Partially Adequate**; totals range 13.0–15.5, failures range 3–5; **keep-scored-tier share: 100.0%** (reported as the enumeration's independence-assuming secondary statistic, per protocol 6.4, not as tier robustness itself).

**Joint readings** (protocol 6.2; one stated reading beyond the required scored/extremes pair, since two of the five flags share a common underlying question — whether documented elite/gender/caste capture is read as inherent to the design-principle logic or as a correctable implementation defect — while the other three turn on unrelated questions and are left as scored in this intermediate reading):

| id | basis | total | failures | tier | label |
|---|---|---|---|---|---|
| scored | scored | 13.0/26 | 5 | Partially Adequate | as scored |
| reform_optimistic | stated | 14.0/26 | 4 | Partially Adequate | capture treated as a correctable implementation shortfall; collective-choice credited at designed strength (resolves C2.4→1.0, C4.3→0.5) |
| extremes_down | extremes | 13.0/26 | 5 | Partially Adequate | every flagged call resolved downward — identical to the scored reading, since no flag in this register has an alternative *below* its scored value |
| extremes_up | extremes | 15.5/26 | 3 | Partially Adequate | every flagged call resolved upward (resolves all five flags to their alternatives) |

**Tier robustness (decision D13, protocol 6.4).** Reach: **{Partially Adequate}** — a single tier; every joint reading, including both extremes, lands in Partially Adequate. **Span:** 2.5 points / 2 failures. **This entry is tier-robust.** The secondary statistic (6.3's enumeration share, assuming independence) agrees: 100.0% of the 32 enumerated combinations keep the scored tier. Both measures order this entry the same way; there is no case here of the two measures disagreeing (protocol 6.4's full-disclosure rule).

**Scenario** (protocol 6.5 — a scope/boundary change, not a scoring judgment, and not counted in the enumeration or joint readings):

- **`no_housing_extension`** (kind: scope): the mechanism's counted domain is narrowed to exclude the community-land-trust/housing extension, so that only the literature's natural-resource CPR institutions (forests, fisheries, grazing, irrigation and other shared water management) count as the mechanism's reach. Change: C1.3 → 0.0. **Result: 12.5/26, 6 failures, Structurally Inadequate.** This is the single largest lever on this entry's outcome in the whole document: excluding the one extension beyond Ostrom's own core CPR domain moves the tier down a full band, from Partially Adequate to Structurally Inadequate.

## 7. Where the entry sits in the corpus

This kit does not include `verify_comparative_claims.py` (protocol 8.2's corpus-level checker; Appendix A lists it as part of the full repository, not of a replication kit), so no comparative claim about this entry's rank, ties, dominance or position relative to any other corpus entry can be machine-asserted here. Per protocol 8.3 ("A claim that cannot be asserted is not made"), none is made. What §2's peer matrix already gives — this entry's vector set beside its four declared peers, every difference marked and reconciled — is offered in its place as the entry's documented context; it is generated output (`neec_entry.py --candidate`), not typed by hand.

## 8. Final assessment

**What the scores mean.** Ostrom-style commons governance is a well-evidenced, narrow mechanism. Its strongest domain by far is Implementation Viability (4.0/5, 80%) — an unusually deep, centuries-spanning, cross-cultural real-world track record, a genuinely opt-in and partially-deployable structure, and demonstrated adaptive governance. Its weakest domain is Material Security (1.5/6, 25%): the mechanism secures access to a resource flow, not accumulable household wealth or universal, unconditional provision, and three of its five Domain 1/2 failures (C1.2a, C1.5, C2.2) are clean, undisputed structural absences rather than close calls. The tier (Partially Adequate) is robust to every flagged uncertainty in the register — but not to the single interpretive choice tested by §6.5's scenario: whether the housing/CLT extension counts as part of the mechanism's domain. A reviewer who rejects that extension should read this entry as bordering Structurally Inadequate rather than as comfortably Partially Adequate.

**What would change the scores.** A credible, at-scale demonstration of commons-governance design principles maintaining outcomes under the specific automation-displacement or compound-crisis stress tests (C1.4, C3.1, C3.3) would be new evidence, not a reinterpretation, and could move those criteria on its own terms. A resolution — in either direction — of the elite-capture question (C2.4, C4.3) is more a matter of which body of evidence a scorer weights more heavily than of new data; both bodies of evidence already exist and are cited above.

**Evidence that will date.** Nepal's CFUG counts and managed hectarage are reported differently across sources and years (this document cites figures ranging from roughly 14,000 to 30,000 groups and 1.2 to 2.8 million hectares, depending on the year and the counting method of the source); a later review should re-check the current official figures rather than these. The 313-CLT figure (criteria.json) and the Cox et al. 91/112-study counts are similarly snapshots that will be superseded. Gender/caste representation-quota reforms in community forestry are an active policy area; a later review should re-check whether documented substantive (not merely token) inclusion has improved, which bears directly on C2.4 and C4.3.

## 9. Reviewer disclosure

- **Scorer:** Claude (Sonnet 5, Anthropic), via the claude.ai chat interface. **Date:** 2026-09-19. **Session:** single pass; no prior session's scoring of this or any other NEEC entry informed this document.
- **Second scorer:** none; this document has not been cross-checked by an independent scorer. That cross-check is the pilot this kit exists to support.
- **Tools used:** web search (author, title and figure verification for the sources cited in §1 and §3); code execution (Python), to run `neec_entry.py --candidate` for structural validation and to compute the enumeration, joint-reading arithmetic, tier-robustness measure and peer matrix reported in §2 and §6, so that every figure in this document is generated output rather than hand arithmetic.
- **NEEC material encountered:** none. Per the brief's rules of blindness, I did not consult the NEEC repository, site, Paper, Report or Visual Suite, and encountered no other account of how this system has been scored. The one qualification to that, recorded in §1's central disclosures and repeated here because it belongs in this section: the blind copy's own withheld-passage marker in protocol §3.1 discloses, ahead of any analysis, that the target is a mechanism of the "narrow single-mechanism archetype." That is a leak internal to the kit, not outside material, so it is not a Rule-1 violation, but it is a genuine limit on this pilot's test of the scope question, and I record it rather than let it pass unremarked.
- **Scope decisions and who confirmed them:** the class (mechanism), archetype (narrow single-mechanism) and population rule (§1) are this document's own declaration (`basis: stated`), made by the scorer alone. No project owner has reviewed or confirmed it. Per protocol 3.3, a scope decision of this kind ordinarily requires such confirmation before scores are fixed, as it did for the Singapore, Qatar and Islamic finance evaluations; that confirmation step has not happened here and could not happen inside a solo blind-replication pass. This is disclosed as an open item, not resolved by this document.
- **Conflict of interest:** none. This is not an evaluation of CCO-PTF-CIP-SZH, so the self-referential-bias disclosure the protocol asks for wherever that framework is scored or compared does not apply; noted here as not applicable rather than silently omitted.
- **Protocol ambiguities and silences encountered** (per the brief, the most useful output of a pilot):
  1. **How far a mechanism's "generalisation, not best-casing" (3.2) may reach by analogy.** The protocol says to score a mechanism "as though it governed every part of an economy it could govern," but does not say how to handle a mechanism whose own literature is internally divided about its domain's outer boundary (here: whether land-tenure commons/CLTs count as an extension of the same design-principle logic, or as a different mechanism wearing similar language). §6.5's scenario exists because this single interpretive choice moves the entry a full tier, and no rule in the protocol says which reading is the "correct" generalisation.
  2. **Whether documented, extensive implementation failure counts against "the system's own logic."** Section 2.1 defines Structural Failure partly as "the best evidence shows performance far below the threshold with no credible pathway to close the gap under the system's own logic" — but does not say whether a well-documented empirical pattern (elite/gender/caste capture, replicated across several countries and decades) that the design principles themselves do not obviously predict or require should be read as revealing the system's actual logic, or as an separable implementation defect the same logic could in principle correct. C2.4 and C4.3 turn on exactly this, and I resolved it by flagging rather than by finding a rule that settles it.
  3. **What "archetype" match means for peer declaration (5.1) beyond scope class.** Protocol 3.1 names a "narrow single-mechanism archetype" as a sub-grouping within the mechanism scope class, but never defines archetype matching as a general concept the way it defines scope class. I inferred the grouping from which entries the protocol's own text lists together — which is also how I learned the withheld entry's archetype (see above) — and I record that this criterion for peer selection is currently readable only by example, not by rule.


---

## 10. Summary block

<!-- NEEC-SUMMARY-BLOCK -->
```json
{
  "schema": "neec-summary-block/1.0",
  "key": "Ostrom-Style Commons Governance",
  "code": "OSR",
  "display_name": "Ostrom-Style Commons Governance",
  "record": {"documents": ["NEEC_OstromCommons_replication_scoring.md"], "scored": "Claude (Sonnet 5, Anthropic; claude.ai); 2026-09-19; blind replication pilot, single pass", "structure": "native-v2"},
  "scope": {"class": "mechanism", "basis": "stated", "population": "Generalisation, not best-casing (protocol 3.2): scored as though Ostrom-style self-governance were the operating institution for every common-pool-resource domain it can govern (forests, fisheries, grazing/pasture, irrigation and other water management, and land-tenure commons such as community land trusts), with population-scope thresholds then applied to the resulting economy-wide population; credited only where the mechanism itself does the work. Wage-labour markets, currency issuance, macroeconomic stabilisation and comprehensive political governance of the state are treated as remaining under whatever other arrangements the wider economy uses."},
  "vector": {
    "C1.1": 0.5, "C1.2a": 0.0, "C1.2b": 0.5, "C1.3": 0.5, "C1.4": 0.0, "C1.5": 0.0,
    "C2.1": 0.5, "C2.2": 0.0, "C2.3": 0.5, "C2.4": 0.5, "C2.5": 1.0,
    "C3.1": 0.5, "C3.2": 0.5, "C3.3": 0.5, "C3.4": 1.0, "C3.5": 0.5,
    "C4.1": 0.5, "C4.2": 0.5, "C4.3": 0.0, "C4.4": 0.5, "C4.5": 0.5,
    "C5.1": 1.0, "C5.2": 0.5, "C5.3": 1.0, "C5.4": 0.5, "C5.5": 1.0
  },
  "summary": {"D1": 1.5, "D2": 2.5, "D3": 3.0, "D4": 2.0, "D5": 4.0, "total": 13.0, "failures": 5, "tier": "Partially Adequate"},
  "flags": [
    {"criterion": "C1.2b", "scored": 0.5, "alternatives": [1.0], "basis": "stated", "reading": "structural cap read as economy-wide anti-capture, on the Mutual Credit/LETS precedent, rather than resource-specific only"},
    {"criterion": "C1.4", "scored": 0.0, "alternatives": [0.5], "basis": "stated", "reading": "in-kind subsistence access to commons resources credited as a partial automation-resilience buffer"},
    {"criterion": "C2.4", "scored": 0.5, "alternatives": [1.0], "basis": "stated", "reading": "collective-choice governance credited at its designed strength rather than its elite-capture-discounted performance"},
    {"criterion": "C4.2", "scored": 0.5, "alternatives": [1.0], "basis": "stated", "reading": "sustainable-yield rule read as a hard ecological constraint rather than a resource-specific partial one"},
    {"criterion": "C4.3", "scored": 0.0, "alternatives": [0.5], "basis": "stated", "reading": "documented elite/gender/caste capture read as a correctable implementation shortfall rather than a structural failure"}
  ],
  "joint_readings": [
    {"id": "scored", "label": "as scored", "basis": "scored", "resolve": {}, "result": {"total": 13.0, "failures": 5, "tier": "Partially Adequate"}},
    {"id": "reform_optimistic", "label": "capture treated as a correctable implementation shortfall; collective-choice credited at designed strength", "basis": "stated", "resolve": {"C2.4": 1.0, "C4.3": 0.5}, "result": {"total": 14.0, "failures": 4, "tier": "Partially Adequate"}},
    {"id": "extremes_down", "label": "every flagged call resolved downward (identical to the scored reading: no flag here has an alternative below its scored value)", "basis": "extremes", "resolve": {}, "result": {"total": 13.0, "failures": 5, "tier": "Partially Adequate"}},
    {"id": "extremes_up", "label": "every flagged call resolved upward", "basis": "extremes", "resolve": {"C1.2b": 1.0, "C1.4": 0.5, "C2.4": 1.0, "C4.2": 1.0, "C4.3": 0.5}, "result": {"total": 15.5, "failures": 3, "tier": "Partially Adequate"}}
  ],
  "scenarios": [
    {"id": "no_housing_extension", "label": "Domain narrowed to exclude the community-land-trust/housing extension: only natural-resource CPR institutions count", "kind": "scope", "changes": {"C1.3": 0.0}, "result": {"total": 12.5, "failures": 6, "tier": "Structurally Inadequate"}}
  ],
  "peers": ["Georgism / Land Value Tax", "Mutual Credit / LETS", "Sovereign Wealth Fund Statism", "Islamic Finance / Profit-Sharing Banking"]
}
```
<!-- /NEEC-SUMMARY-BLOCK -->
