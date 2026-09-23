# NEEC Rescoring Pass — Record, Part (b), Second Group: C5.1's Second Clause and C3.1

**Session 39 · 2026-09-23 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b1) are `NEEC_Rescoring_s37.md` and `NEEC_Rescoring_s38.md`; this
record continues the pass and edits neither.** No corpus file, score or scoring document changes until the pass ends.
Its changes are then applied by generator with pinned inputs and restated in place (protocol 10.2, 10.3; decisions
D12, D14), and until then the published totals stand, provisional as `README.md` says. Decisions taken here are
Claude's under the owner's delegation (Handoff 35, section 2); each is recorded with its reasons, and the owner may
reverse any of them.
**Reproduce:** `python3 rescoring_s39.py` (harness check 82). The script holds every clause estimate below, checks
the group against the R4 audit's register and every verdict against D28, lists and asserts every departure from the
audit's codes, computes every figure in section 5 cumulatively with parts (a) and (b1), and checks that this record
contains its generated tables verbatim.

---

## 1. What this group is

Handoff 38 orders part (b) next through two sets of units. **C5.1's second clause** ("with documented outcomes matching
claimed benefits") on the eleven C5.1 1.0s outside D28's population: the audit coded that clause A wherever a
rationale cited documented outcomes, because no rationale was written against it, and its record (section 7) sends it
to be tested in full. **C3.1's five part (b) units** (MMT + Job Guarantee, UBI, Degrowth, Participatory Economics,
Integral), with the step-versus-scaling question part (a) left open (its reading 3.4). Sixteen units in all.

Two stand: UBI's C5.1, on Alaska's documented dividend outcomes, flagged with 0.5, and Ostrom-style commons
governance's C5.1. Fourteen become 0.5 (7.0 points). No failure count and no tier changes. CCO-PTF-CIP-SZH keeps first
place, 22.5 to 22.0.

## 2. How a clause is recorded, and the rule

As in part (a), section 2: each clause is cleared, short, not shown, out of reach or moot; a 1.0 stands only if every
clause is cleared or moot, and otherwise becomes 0.5 (D28, protocol 2.3). A clause the audit coded A is carried as
cleared on the unit's own text ("as audited"). This group departs from that in three listed ways, each asserted by the
script, which also checks that no other A clause departs:

- **C5.1's second clause** is tested in full on all eleven units (the audit record's instruction); three clear.
- **Two own-source exceptions** (part (a), section 2): CCO-PTF-CIP-SZH's and Universal Basic Services' C5.1 clause 1,
  where the design's or document's own component list contradicts the text's proportion (reading 3.2).
- **One reading supersession:** MMT + Job Guarantee's C3.1 clause 2, where the audit's A rests on widening enrolment,
  which part (a)'s reading 3.4 assigns to clause 3 (reading 3.4 below).

"Not estimated in this pass" marks a clause that could not change the verdict once another was shown short or not
shown.

## 3. Decisions and readings (under the delegation)

**3.1 C5.1, clause 2: which benefits, and what counts as a match.** Part (a)'s reading 3.4 compares an entry's
documented outcomes with the benefits its own sources claim, and treats the clause as not shown where the corpus's own
scoring records outcomes short of those claims. Two questions were left open, and the eleven units need both answered
alike. *Which benefits:* those the unit's C5.1 rationale claims, or cites, for the components it counts toward the 70%.
A configured national economy counts the configuration itself as its component, so its claimed benefits are the
configuration's headline claims as its rationale of record states them (Report v1.6's Key Strengths line, or the
scoring document's framing), which is how part (a) read Status Quo. *What counts as a match:* the clause is **cleared**
where documented outcomes, in independent evaluations or official statistics, reach each claimed benefit; **short**
where a documented figure falls below a figure the unit claims; **not shown** where no outcome is located, where
outcomes are mixed across the implementations the unit counts (the anchor's 0.5 band: "the historical precedent's
outcomes are mixed/contested"), or where the corpus's own scoring of the entry — the published vector as amended by
parts (a) and (b) — records an outcome short of a claimed benefit. *Alternative rejected:* testing configured economies
component by component against narrow functions (price stability, growth, extreme-poverty elimination) would clear the
clause for every long-running economy whatever its record on the benefits its defenders claim, and part (a) already
declined it for Status Quo. It is carried as each such unit's flag, toward 1.0, as part (a) carried it for Status Quo.

**3.2 C5.1, clause 1: the own-source exception applied to two component counts.** Clause 1 asks that 70% of the
system's components be proven through twenty years' operation. Two rationales state a proportion that their own
sources do not support. *CCO-PTF-CIP-SZH:* the design's own site lists five components (Creative Currency Octaves,
Public Trust Foundations, Public Trust Housing, Social Zone Harmonization, Citizens Internet Portal); the precedents
the Report's rationale cites cover three of them, the Portal's two precedents (Consul, first deployed by Madrid in
2015; Decidim, by Barcelona in 2016) have run for under twenty years, and none is cited for Social Zone Harmonization.
At most three of five (60%) are shown. *Universal Basic Services:* the entry's document defines seven sectors; its
cited precedents of twenty years or more cover healthcare, education and shelter; its childcare precedent is outside
the seven, and it calls its transit precedents "more recent and more mixed". Three of seven (43%) are shown. Both
clauses are recorded **not shown**, not short: long-running precedents may exist for the uncited components, and the
clause returns to cleared if a scoring document cites them. For CCO-PTF-CIP-SZH the clause decides the unit, since
its clause 2 clears: it reopens if a scoring document cites twenty-year precedents for four of the five components.
For Universal Basic Services it does not, since its clause 2 also falls.

**3.3 C3.1, clause 2: step versus scaling, decided by protocol 4.2.** (1) *Interpretations.* "Scaling 1:1 with crisis
severity (30% GDP decline = 30% benefit increase)" could require support per covered person to rise in proportion to
severity, at least one point per point of decline, across severities (proportional); or it could accept any automatic
increase at least as large as the example's, a fixed step included (step). (2) *Preponderance.* The threshold says
"scaling 1:1 with crisis severity"; the Measurement line measures "percentage increase relative to crisis severity";
the Paper's rationale says "automatic stabilizers scaling with crisis severity — increasing support by 50%+ during
downturns". All three tie the increase to severity, and the rationale's 50% sits inside the same clause as "scaling
with crisis severity", as a magnitude for downturns, not a substitute for the scaling. A fixed step matches the example
only at the severity it happens to cover and falls behind 1:1 above it. The text supports the proportional reading.
(3) *Score* against it: clause 2 is cleared by an automatic rule under which support per covered person rises at
least 1:1 with the decline, tested first at the example. (4) *Alternative:* the step reading would clear a fixed step
of 30% or more. **No unit in the corpus turns on it**: part (a)'s CCO-PTF-CIP-SZH unit has a 20% step, short under
both, and none of this group's five specifies any increase per person. So no unit is flagged on it, and the reading
joins the protocol's register when the pass ends.

**3.4 C3.1, clause 2 and the audit's A codes.** The audit coded MMT + Job Guarantee's clause 2 A on "recession
automatically increases enrollment". Part (a)'s reading 3.4 assigns widening coverage at fixed benefit levels to
clause 3. Applying one criterion's clauses alike (protocol 5), that phrase addresses clause 3, and clause 2 is
estimated afresh: the guarantee pays a fixed wage, so support per covered person does not rise (short).

**3.5 The three state-capitalist entries follow Status Quo.** China's, Singapore's and Qatar's C5.1 rationales adopt
Status Quo's 1.0 reasoning by name — a certification of track record, not of adequacy. Part (a) found that reasoning
does not show clause 2 and flagged Status Quo toward 1.0. The same reading is applied to all four (protocol 5), each
on the outcomes its own rationale cites, and each is flagged in the same direction. Nordic Social Democracy is read on
the same rule (3.1) and falls on the same ground; its flag states the stronger case for 1.0 that its signature
outcomes make.

## 4. The units

### 4.1 Summary (generated)

| Entry | Criterion | Clauses | Verdict | Flag |
|---|---|---|---|---|
| NSD | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| MS | C5.1 | C S | 1.0 → 0.5 |  |
| MMT | C3.1 | C S U | 1.0 → 0.5 |  |
| UBI | C3.1 | C S C | 1.0 → 0.5 |  |
| UBI | C5.1 | C C | 1.0 → 1.0 | alternative 0.5 |
| DG | C3.1 | C U U | 1.0 → 0.5 |  |
| PE | C3.1 | C U U | 1.0 → 0.5 |  |
| CCO | C5.1 | U C | 1.0 → 0.5 |  |
| INT | C3.1 | C U C | 1.0 → 0.5 |  |
| MC | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| UBS | C5.1 | U U | 1.0 → 0.5 |  |
| SWF | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| CN | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| SG | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| QA | C5.1 | C U | 1.0 → 0.5 | alternative 1.0 |
| OS | C5.1 | C C | 1.0 → 1.0 |  |

Clause statuses are listed in Appendix B's order: C cleared, S short, U not shown, R out of reach, M moot.

### 4.2 Clause by clause (generated)

#### NSD C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | decades of operation in Norway, Sweden, Denmark and Finland at national scale (populations of 5-10 million) | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | the configuration's headline claims (near-universal material security; comprehensive security and dignity) are recorded short by the corpus's own amended scoring: housing cost overburden in 2024 at 14.6% in Denmark and 10.6% in Sweden, among the EU's highest (part (b), NSD C1.3), and about 6% of Finland's citizens' initiatives adopted (part (a), NSD C2.4); the rationale asserts validation without estimating a match (reading 3.1) | Report v1.6, NSD C1.1, C5.1 and Key Strengths; NEEC_Rescoring_s38.md, NSD C1.3; NEEC_Rescoring_s37.md, NSD C2.4 |

*Flag:* alternative 1.0: outcomes matched against the configuration's signature claims, low poverty and universal services, with the housing and initiative shortfalls read as outcomes on NEEC's thresholds rather than on the benefits the model claims.

#### MS C5.1 Proven Component Foundation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | Mondragon: 70+ years at a scale far above 10,000 participants | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | short | the rationale claims 80,000+ worker-owners; in 2019 Mondragon's cooperatives employed over 81,000, of whom members were 32-45% depending on sector, with 18% of employment in subsidiaries abroad; the survival record is documented as 3 closures among the 103 cooperatives founded in 1956-1986, and the founding cooperative, Fagor Electrodomesticos, failed in 2013 | Journal of Labor and Society 26(3) (2023), The Mondragon Worker Cooperatives' Employment Record 1983-2019; Participedia, Mondragon case; Fortune (27 November 2013) |

*Note:* correction for Report v2.0: about 81,000 workers, 32-45% of them members, not 80,000+ worker-owners; the '97% over 5 years vs 44%' comparison was not located, and the documented figure is 3 closures in 103.

#### MMT C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | no legislative delay: enrolment rises automatically in a recession | as audited (the unit's own text) |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | short | the guarantee pays a fixed wage (the rationale's $15 an hour), so a downturn widens enrolment, which is clause 3's subject, and leaves support per covered person unchanged: 0% at the threshold's 30% example; the one national precedent, Argentina's Jefes de Hogar, paid a fixed 150 pesos per beneficiary (readings 3.3, 3.4) | Report v1.6, MMT C1.1 and C3.1; Decreto 565/2002 |
| 3 | ≥90% population coverage | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### UBI C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | no application process, no verification, no delay | as audited (the unit's own text) |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | short | the benefit continues at its level regardless of employment: support per covered person does not rise with crisis severity, 0% at the threshold's 30% example; Alaska's dividend is set on an annual cycle, not by crisis severity (part (b), UBI C3.4) (reading 3.3) | Report v1.6, UBI C3.1; NEEC_Rescoring_s38.md, UBI C3.4 |
| 3 | ≥90% population coverage | cleared | immediate crisis cushion for the entire population | as audited (the unit's own text) |

#### UBI C5.1 Proven Component Foundation: 1.0 → 1.0 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | Alaska Permanent Fund dividend: 40+ years, universal | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | cleared | the rationale claims cash transfers effective with positive outcomes, and the Report claims a 20% poverty reduction from Alaska's dividend (UBI C1.1): dividends cut Alaska's poverty rate by an estimated 2.5-4 points a year from 1990, lifting about 25,000 residents out of poverty in 2015, about a third, and from 11% to 9% across 2011-2015; the dividend has not reduced employment | Berman and Reamey, Permanent Fund Dividends and Poverty in Alaska, ISER (2016); Berman, World Development (2018), via Anchorage Daily News; Jones and Marinescu, American Economic Journal: Economic Policy 14(2) (2022) |

*Flag:* alternative 0.5: the documented outcomes are of a dividend of about $1,000-2,000 a year; no component precedent operates at the living-wage level at which the entry claims its benefits.

#### DG C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | commons and mutual aid networks provide automatic crisis support | as audited (the unit's own text) |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | no rule tying the support that commons and mutual-aid networks give to crisis severity is specified or modelled in the design's sources (reading 3.3) | Report v1.6, DG C3.1 |
| 3 | ≥90% population coverage | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### PE C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | democratic councils can rapidly shift priorities during crises | as audited (the unit's own text) |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | support is reallocated by council deliberation; no automatic rule tying support per person to crisis severity is specified, and no implementation or model estimates one (reading 3.3) | Report v1.6, PE C3.1 |
| 3 | ≥90% population coverage | not shown | not estimated in this pass; the verdict is fixed by another clause | — |

#### CCO C5.1 Proven Component Foundation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | not shown | the design's own site lists five components (CCO, PTF, PTH, SZH, CIP); the precedents the rationale cites cover three (CCO: WIR and Alaska's dividend; PTF and PTH: community land trusts); CIP's precedents, Consul (Madrid, 2015) and Decidim (Barcelona, 2016), have run for under twenty years, and none is cited for SZH: at most three of five (60%) are shown (reading 3.2) | research-hub at 8e8a6ba (2026-09-21), index.html; Report v1.6, CCO C5.1 |
| 2 | with documented outcomes matching claimed benefits | cleared | the one benefit the rationale claims for a cited component is documented: at the end of 2010, 0.46% of community land trust mortgages were in foreclosure against 4.63% in the conventional market; Alaska's dividend's documented poverty reduction is recorded under UBI C5.1 above | Thaden, Stable Home Ownership in a Turbulent Economy, Lincoln Institute of Land Policy (2011) |

*Note:* the digital-democracy precedents count at clause 1, where they fall short of twenty years, not at clause 2; the unit reopens if a scoring document cites twenty-year precedents for four of the five components.

#### INT C3.1 Crisis Response Capacity: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Response within 72 hours | cleared | response within 72 hours for clearly defined crises is plausible given the architecture | as audited (the unit's own text) |
| 2 | scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase) | not shown | the Feedback and Review System detects anomalies and suggests corrections; no rule scaling support with crisis severity is specified or estimated (reading 3.3) | Report v1.6, INT C3.1 |
| 3 | ≥90% population coverage | cleared | with universal coverage | as audited (the unit's own text) |

#### MC C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | WIR Bank has operated continuously since 1934 | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | the components the rationale counts have mixed documented outcomes, as the entry's own document records: WIR's credit moves countercyclically (C3.1), but UK LETS declined from its mid-1990s peak once cheap credit returned, its schemes drew participants already socially connected (C1.1), and Argentina's barter networks collapsed as they outgrew their governance (C3.2, C3.5); WIR's 2013 turnover was 1.43 billion francs, and Bank WIR reports demand for the currency falling again in 2024 (reading 3.1) | NEEC_MutualCredit_LETS_scoring_scratch.md, C1.1, C3.1 and C5.4; Monneta, WIR Bank (2013 figures); finews.ch (20 February 2025) |

*Flag:* alternative 1.0: WIR's documented record, nine decades of operation and countercyclical credit, taken as the proof of the mechanism's core component, with the LETS and barter-network outcomes read as weaker implementations.

*Note:* polish for Report v2.0: 'turnover in the billions of Swiss francs' rests on 2013's 1.43 billion; state the year.

#### UBS C5.1 Proven Component Foundation: 1.0 → 0.5

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | not shown | the document defines seven sectors (healthcare, education, democracy and legal services, shelter, food, transport, information); its cited precedents of 20 years or more cover three (healthcare, education, shelter), its childcare precedent lies outside the seven, and it calls its transit precedents more recent and more mixed: three of seven (43%) are shown (reading 3.2) | NEEC_UniversalBasicServices_scoring_scratch.md, overview and C5.1 |
| 2 | with documented outcomes matching claimed benefits | not shown | the rationale states that each precedent has documented outcomes without estimating a match to the benefits claimed, and the document itself records mixed outcomes: Quebec childcare's publicised child-development findings (the Baker, Gruber and Milligan research) and Kansas City's 2026 reversal of zero-fare transit (reading 3.1) | NEEC_UniversalBasicServices_scoring_scratch.md, C3.5, C4.3 and sources |

*Note:* the unit's published flag (alternative 0.5) resolves to its alternative.

#### SWF C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | Norway's fund since 1990 and Alaska's since 1976, both far above the scale bar | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | outcomes are mixed across the three implementations the rationale counts: Norway's fund matches its claims; Alaska's principal is preserved but its 2025 dividend was the smallest in real terms against a statutory formula above $3,800 (the entry's own C5.4); Timor-Leste has withdrawn above its sustainable income almost every year since 2008-09, and the IMF warns the fund could be exhausted by the late 2030s (reading 3.1) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C5.1 and C5.4; East Asia Forum (27 January 2025); World Bank, Macro Poverty Outlook: Timor-Leste (2025); Lowy Institute, The Interpreter (24 March 2026) |

*Flag:* alternative 1.0: Timor-Leste weighed as a single implementation's shortfall (D29(a)), with Norway's and Alaska's funds preserved as the mechanism claims.

#### CN C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | operated continuously since 1978 for more than 1.4 billion people | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | the rationale certifies track record, not adequacy (Status Quo's reasoning, which part (a) found does not show this clause), and cites C1.1 for its documented outcomes, which the entry's own document scores 0.5: a reduction of about 70-80% at the middle-income line the protocol prescribes, though over 99% at the extreme and national lines (reading 3.1) | NEEC_StateCapitalism_China_scoring_scratch.md, C1.1 and C5.1; NEEC_Rescoring_s37.md, SQ C5.1 |

*Flag:* alternative 1.0: outcomes matched against the narrower benefit the configuration's own sources claim, eliminating extreme and national-line poverty, which the World Bank and State Council study documents.

#### SG C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | operated since independence in 1965 at national scale | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | the rationale certifies track record, not adequacy (Status Quo's reasoning), and cites Domains 1 and 3 for its documented outcomes, which the corpus's own scoring records short: C1.1 0.5, housing affordability not maintained for the rental segment (part (a), SG C1.3), and evidence-based updates slow or refused (part (a), SG C3.4) (reading 3.1) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.1 and C5.1; NEEC_Rescoring_s37.md, SG C1.3 and C3.4 |

*Flag:* alternative 1.0: outcomes matched against the narrow functions its sources claim for residents, home ownership and compulsory saving.

#### QA C5.1 Proven Component Foundation: 1.0 → 0.5 — flagged as contestable

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | components with long records at national scale | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | not shown | the rationale claims operation with documented outcomes and follows China and Singapore without estimating a match; the corpus's own scoring of the configuration, over its whole resident population (protocol 3.2), records outcomes short of broad welfare: C1.1 0.5 and ten structural failures, among them C4.5 (reading 3.1) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.1, C4.5 and C5.1 |

*Flag:* alternative 1.0: outcomes matched against the narrow benefit claimed, welfare provision to the configuration's citizens, which the entry's document records.

#### OS C5.1 Proven Component Foundation: 1.0 → 1.0

| # | Clause | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants | cleared | Valencia's tribunal for about a thousand years; Nepal's programme with about 2.9 million households | as audited (the unit's own text) |
| 2 | with documented outcomes matching claimed benefits | cleared | the benefit claimed is that communities governed by these institutions sustain their resources: the three multi-case datasets the unit cites document it, and Cox, Arnold and Villamayor Tomas's review of 91 studies found the design principles well supported empirically; the survivorship caveat is scored where it changes the answer (C3.3, C5.2, C5.4), as the unit says | as audited (the unit's own text); Cox, Arnold and Villamayor Tomas, Ecology and Society 15(4) (2010) |

## 5. What parts (a) and (b) so far change (generated)

| Entry | Published (rank) | After (a) | After (b1) | After this group (rank) | Change here | Failures | Tier | D28 units left | Floor if all fall |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| CCO | 24.5 (1) | 24.0 | 22.5 | 22.0 (1) | -0.5 | 0 | Potentially Adequate | 8 | 18.0 |
| PE | 20.5 (2) | 20.5 | 19.0 | 18.5 (2) | -0.5 | 1 | Potentially Adequate | 9 | 14.0 |
| NSD | 19.5 (3) | 17.0 | 16.0 | 15.5 (5) | -0.5 | 2 | Potentially Adequate | 5 | 13.0 |
| INT | 19.5 (3) | 19.0 | 18.0 | 17.5 (3) | -0.5 | 3 | Partially Adequate | 8 | 13.5 |
| DG | 19.0 (5) | 19.0 | 17.5 | 17.0 (4) | -0.5 | 2 | Potentially Adequate | 7 | 13.5 |
| MS | 16.5 (6) | 15.5 | 14.0 | 13.5 (7) | -0.5 | 2 | Potentially Adequate | 1 | 13.0 |
| MMT | 15.5 (7) | 14.0 | 13.0 | 12.5 (11) | -0.5 | 3 | Partially Adequate | 2 | 11.5 |
| UBI | 14.5 (8) | 13.0 | 12.5 | 12.0 (14) | -0.5 | 7 | Structurally Inadequate | 2 | 11.0 |
| MC | 14.5 (8) | 14.5 | 13.5 | 13.0 (9) | -0.5 | 3 | Partially Adequate | 2 | 12.0 |
| OS | 14.5 (8) | 14.0 | 14.0 | 14.0 (6) | 0.0 | 3 | Partially Adequate | 2 | 13.0 |
| SWF | 14.0 (11) | 14.0 | 14.0 | 13.5 (7) | -0.5 | 3 | Partially Adequate | 2 | 12.5 |
| SG | 14.0 (11) | 13.0 | 12.5 | 12.0 (14) | -0.5 | 4 | Partially Adequate | 0 | 12.0 |
| GEO | 13.5 (13) | 13.0 | 13.0 | 13.0 (9) | 0.0 | 2 | Potentially Adequate | 1 | 12.5 |
| UBS | 13.5 (13) | 13.5 | 13.0 | 12.5 (11) | -0.5 | 3 | Partially Adequate | 1 | 12.0 |
| IF | 13.5 (13) | 12.5 | 12.5 | 12.5 (11) | 0.0 | 5 | Partially Adequate | 2 | 11.5 |
| FALC | 13.0 (16) | 12.5 | 12.0 | 12.0 (14) | 0.0 | 10 | Structurally Inadequate | 6 | 9.0 |
| DE | 11.5 (17) | 11.0 | 10.5 | 10.5 (17) | 0.0 | 8 | Structurally Inadequate | 3 | 9.0 |
| SQ | 10.5 (18) | 10.0 | 10.0 | 10.0 (18) | 0.0 | 9 | Structurally Inadequate | 1 | 9.5 |
| CPS | 10.0 (19) | 8.5 | 8.5 | 8.5 (21) | 0.0 | 12 | Structurally Inadequate | 2 | 7.5 |
| SC | 10.0 (19) | 10.0 | 9.0 | 9.0 (20) | 0.0 | 9 | Structurally Inadequate | 1 | 8.5 |
| CN | 10.0 (19) | 10.0 | 10.0 | 9.5 (19) | -0.5 | 8 | Structurally Inadequate | 0 | 9.5 |
| QA | 9.0 (22) | 8.5 | 8.5 | 8.0 (22) | -0.5 | 10 | Structurally Inadequate | 0 | 8.0 |
| LM | 8.0 (23) | 6.5 | 6.5 | 6.5 (23) | 0.0 | 15 | Structurally Inadequate | 2 | 5.5 |

"D28 units left" counts the entry's units still to be re-estimated in part (b); "Floor if all fall" is the total if
every one of them became 0.5. C5.1's second clause is now tested on all thirteen of the corpus's C5.1 1.0s.

After this group the corpus has 18 dominance pairs against 14 after part (b1) (new: PE>CN, PE>QA, CCO>MMT, GEO>UBS; lost: none), and its frontier holds 12 entries against 13 (NSD, MS, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 22.5 after part (b1), 22.0 now. Across parts (a), (b1) and (b2), 78 units have been re-estimated: 6 stand and 72 become 0.5 (36.0 points).

Left for part (b): 67 D28 units (C1.1 9, C1.4 2, C2.1 5, C2.5 10, C3.2 4, C3.5 2, C4.1 8, C4.2 6, C4.3 6, C4.4 4, C4.5 3, C5.2 4, C5.4 2, C5.5 2).

Flags added in this group: 7; removed: 1. Across the pass so far, 14 entries' flag registers change (CCO, CN, CPS, IF, LM, MC, NSD, OS, QA, SG, SQ, SWF, UBI, UBS).

Anchor examples citing a unit the pass moves: C2.1's 1.0 example, UBI (part (a), to 0.5); C2.3's 1.0 example, DG (part (b1), to 0.5); C2.4's 1.0 example, PE (part (b1), to 0.5); C3.1's 1.0 example, UBI (part (b2), to 0.5); C5.1's 1.0 example, MS (part (b2), to 0.5). When the pass is applied, each band needs an example the corpus then scores at that value.

## 6. Corrections found (not polish)

1. **Report v1.6, Market Socialism C5.1** says "Mondragon Corporation: 70+ years, 80,000+ worker-owners" and "97%
   survival rate over 5 years vs 44% for traditional startups". In 2019 Mondragon's cooperatives employed over 81,000,
   of whom members were 32–45% depending on sector (*Journal of Labor and Society*, 2023). The documented survival
   figure is 3 closures among the 103 cooperatives founded in 1956–1986; the five-year comparison was not located.
   Report v2.0 carries the documented figures. The same quotation is C5.1's 1.0 anchor example (item 3).
2. **Report v1.6, CCO-PTF-CIP-SZH C5.1** asserts "70%+ components proven through ≥20 years operation". Counted
   against the design's own five components, the precedents it cites show at most 60% (reading 3.2). Report v2.0
   states the proportion against the design's component list, with a twenty-year precedent for each component it
   counts, or states the gap.
3. **Anchor examples.** Five of `criteria.json`'s example quotations cite a unit the pass moves (section 5): C2.1's
   and C3.1's 1.0 examples (UBI), C2.3's (Degrowth), C2.4's (Participatory Economics) and C5.1's (Market Socialism).
   Parts (a) and (b1) did not list the first three. `build_criteria.py` checks every example against the published
   scores, so when the pass is applied each of these bands needs an example the corpus then scores at that value, and
   the change is recorded in the file's `source.corrections`. The C3.1 case is the sharpest: the 1.0 band's own
   example ("no application process, no verification, no delay") is a unit this record finds short on clause 2.
4. **The Universal Basic Services document, C5.1**, says each of its precedents "clears NEEC's own Pass Threshold"
   and that they span "at least five of the seven named sectors". Its childcare precedent is outside its seven, and
   its transit precedents are under twenty years (reading 3.2). The document is restated in place when the pass is
   applied.

*Polish, optional:* Mutual Credit's "turnover in the billions of Swiss francs" rests on 2013's 1.43 billion; state the
year. UBI's C1.1 can cite Berman and Reamey's estimate (about a third of poverty removed in 2015; 2.5–4 points a year
since 1990) instead of the unsourced 20%.

## 7. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C5.1 falls here on clause 1, on the design's own component list (reading
3.2), while its clause 2 clears on the one benefit its rationale claims for a cited component, community land trusts'
low foreclosure rate. It keeps first place (22.5 to 22.0). The reading that decides the unit (3.2) is applied in the
same way to Universal Basic Services, the one other entry whose rationale states a proportion of components its own
sources do not support. The second pilot, with a replicator outside the Claude family, is the independent test of these
calls.

## 8. What remains

- **(b), continued:** the 67 D28 units of section 5's last line, criterion by criterion; C1.1 next (9 units), where
  CCO-PTF-CIP-SZH's rationale ("98% poverty elimination in modeling") is to be tested against the design's own engine
  under decision 3.2 of part (b1): the pinned engine's reference run of Session 38 reduced wealth poverty from 71.4%
  to 15.3%, about 79%, a figure the next session reads against the clause, and the stress clause needs a stress run.
- **(c)** the 131 mechanism-class 0.5s against D29, Ostrom's C4.3 first; **(d)** D31's source for Ostrom's community
  land trusts; **(e)** the Islamic finance and Ostrom documents' quoted thresholds restated.

When the pass ends, its changes are applied by generator, and the corpus, CSV, `README.md` and Appendix A.4 are
regenerated; the changed flag registers are recomputed, the five anchor examples are replaced, the protocol's
statements about the corpus are restated, and the claims and protocol verifiers get successors.

## 9. What this record does not show

It is one scorer's re-estimation, on evidence located in one session through web search, the entries' own scoring
documents and the CCO design's published site. "Not shown" means no evidence was located, not that the clause fails.
Reading 3.1 makes C5.1's second clause demanding for configured economies, whose headline claims are broad, and part
of that demand is the corpus's own amended scoring, so C5.1 and the criteria it draws on are not independent; every
such unit is flagged toward 1.0, and the flags carry the question into the joint readings. Whether these calls
reproduce is what the replication programme tests.
