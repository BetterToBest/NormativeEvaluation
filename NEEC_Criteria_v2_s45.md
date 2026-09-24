# NEEC Criteria v2.0, Session 45

**Status: the v2.0 criteria, adopted. Nothing in the corpus is rescored here.** Session 45, 2026-09-23; amended in
place in Session 46, 2026-09-24, by decisions 46.1 to 46.4 (Package C), and tag `s45` keeps the Session 45 text;
amended in place again in Session 47, 2026-09-24, by decisions 47.1 and 47.2 (C4.6's clause 3 bar), and tag `s46`
keeps the Session 46 text.
Scorer and engineer: Claude. Inputs: `NEEC_Criteria_Review_s44.md` (the review), `criteria_s44_snapshot.json`
(the 26 criteria as they stood at `s44`), `neec_corpus.json`. Appendix V below is the one source of the v2.0 text:
`build_criteria.py` reads it, applies it to the snapshot, asserts the rules in section 6, and writes `criteria.json`
and protocol draft.8 (Appendix B regenerated, seven asserted edits; 47.2). Evidence tables: `criteria_v2_s45.py`, output `criteria_v2_s45_output.txt`.

## 1. Decisions

- **45.1 (the owner's decision).** Package B is adopted in full: C2.6 Civil Liberties and Rule of Law (G2) and C3.6
  Productive and Innovative Capacity (G1). The framework has 28 criteria (29 after decision 46.1); Domains 2 and 3 have maxima of 6. The tier
  bands stay integer failure counts (0–2, 3–5, 6+), as the review proposed, and the choice is disclosed; Paper v2.0's
  Appendix A.4 reports the proportional alternative.
- **45.2 (under the delegation; flagged; the owner may reverse).** Package A is fixed in the wording of Appendix V,
  with four Requirement-versus-threshold gaps the review missed (section 3) and one duplication that Package B creates
  (K7, section 2).
- **45.3 (under the delegation; flagged).** The indicator and bar choices listed in section 4, each with its reason.
  The consequential ones are marked there.
- **45.4 (under the delegation).** Four clauses are declared **aspirational**: no agency publishes the quantity, and
  a 1.0 requires evidence the scorer names (section 5). The Paper says so.
- **45.5 (the owner's direction, recorded).** The v2.0 site has its own visual design, not the Research Hub's; it is
  still linked from the Hub. This amends Handoff 44 section 7, stage 6 (brief: `NEEC_Site_Design_Brief_s45.md`).
- **45.6 (under the delegation; flagged).** On 28 criteria, four totals fall exactly on a half percent: 3.5, 10.5,
  17.5 and 24.5 give 12.5%, 37.5%, 62.5% and 87.5% (on 26 none can, which is why D21 needed no tie rule). They are
  rounded half up. The corpus generators use Python's `round()`, which rounds halves to even (12.5 to 12, 37.5 to
  38), so the generator that applies the pass (stage 3) must round with an explicit half-up rule. No published figure
  changes now; the protocol's 2.4 carries the rule. On the 29 criteria of decision 46.1 no total falls on a half
  percent (that needs 200 × Total / 29 to be an odd whole number; with Total in half-points it is whole only at
  Totals of 0, 14.5 and 29, giving 0, 100 and 200); the rule stands for any structure that produces one, and the
  stage 3 generators still round half up.
- **The owner's confirmation.** The owner confirmed decisions 45.2, 45.3 (every choice marked ▲ included), 45.4 and
  45.6 as recorded here.
- **45.7 (the owner's direction).** The owner leaves the repository loop. A Claude Code cloud session ends with a
  commit whose message begins "NEEC Session <n>: " and pushes its branch; `.github/workflows/land-session.yml`
  merges it into main, runs every check on the merged tree, and only if all pass pushes main, tags the merge commit
  s<n> and publishes a release. Main therefore takes commits without human review, and the harness is the gate.
  Standing session instructions are in `CLAUDE.md`. This amends Handoff 44, sections 4 and 7.
- **46.1 (the owner's decision, Session 46).** Package C (section 9): C-1 and C-2 are adopted; C-3 is not, and is
  recorded for v2.1. C2.6 gains two clauses: informed consent to medical treatment protected in law, and any
  compulsory treatment, vaccination, quarantine or isolation prescribed by law, time-limited and open to independent
  judicial review; its derivation is unchanged. C4.6 Harm Internalization (N13 Incentive Alignment + N6 Ecological
  Compliance) joins Domain 4 with three clauses: mortality attributed to pollution non-increasing over 20 years;
  those who cause harm to health or the environment liable for it, enforceably by those harmed; regulation of food,
  water, air, chemicals and medicines applied and enforced without improper influence. The framework has 29
  criteria, domain maxima 6, 6, 6, 6, 5. The wording, measures and bars are in Appendix V.
- **46.2 (under the delegation; flagged; the owner may reverse).** Where the adopted text left a choice, Appendix V
  fixes it as follows.
  (a) C4.6 clause 1 is the sum of the three age-standardized SDG 3.9 mortality rates (air pollution, unsafe water
  and sanitation, unintentional poisoning), end of the 20-year window against its start. The SDG indicators are
  rates; a count would rise with population alone. Where the SDG series do not span the window, the Global Burden
  of Disease study's rates for the same risks are used, and a disagreement between the two is flagged.
  (b) C4.6 clause 2 is met by liability in tort, product-liability or environmental-liability law, or by a
  compensation scheme funded by a levy on those who cause the harm, since either makes the harm their cost; an
  immunity that leaves a class of harm uncompensated, or compensated from public funds alone, does not meet it.
  "Enforceably" means that those harmed have standing before an independent court, collectively where the harm is
  dispersed, and the scoring document names at least one such claim decided and paid in the scoring window.
  (c) C4.6 clause 3 reads "applied and enforced", the title of the measure it names.
  (d) Compulsion in C2.6 includes a penalty for refusal (a fine, detention, or loss of employment, schooling or an
  essential benefit). The European Court of Human Rights treats a vaccination duty enforced by a fine and by
  exclusion from preschool as an interference that must be justified (*Vavřička and Others v. the Czech Republic*,
  Grand Chamber, 2021).
  (e) **▲** "Time-limited" applies, as adopted, to every compulsion, a standing statutory requirement included: the
  measure lapses at a stated time unless renewed by a decision itself open to review. This is stricter than the
  instruments section 9 cited: they require a time limit of emergency measures (derogations must be "of an
  exceptional and temporary nature", Human Rights Committee General Comment 29), and accept a standing requirement
  prescribed by law and necessary (Oviedo Convention, Article 26; *Vavřička*). Consequence: an entry whose law
  imposes a standing vaccination requirement, enforced by a penalty and with no lapse date, does not show clause 3
  and scores at most 0.5 on C2.6 (protocol 2.3). The alternative, a time limit on orders and emergency powers only,
  with standing requirements tested by law and judicial review alone, changes one sentence of C2.6's measurement
  field and is recorded for the owner.
- **46.3 (corrections).** (a) Section 9 said C-1's compulsion clause "is the limitation test" of the Siracusa
  Principles and the Oviedo Convention; with its time limit it is stricter than that test (46.2(e)), and section 9
  now says so. (b) Protocol 1.2 described `criteria.json` as the 26 criteria generated from Paper v1.4, which it has
  not been since Session 45; draft.7's 1.2, generated by `build_criteria.py`, describes the v2.0 file.
- **46.4 (recorded; not a choice).** C4.6 clause 3 names the World Justice Project Rule of Law Index, sub-factor
  6.2, for configured national economies, but the score that meets it is not yet fixed. Session 46's cloud
  environment could not reach the Project's data: its network policy denied that host, and also WHO's, IHME's,
  Freedom House's and the World Bank's. The bar is fixed from the Index's published data before any configured
  national economy is scored on C4.6. Designs, mechanisms and comprehensive systems are scored on their stated
  provisions and do not wait for it. *Resolved in Session 47 by 47.1.*
- **47.1 (under the delegation; flagged ▲; the owner may reverse).** C4.6 clause 3's bar, for a configured national
  economy, is a World Justice Project sub-factor 6.2 score of 0.77 or more, read at the two decimals the Index
  publishes; the Pass Threshold carries it, and the measurement field states it with its reason. Session 47's
  environment reached the Project's data: the 2025 edition's historical data file
  (`2025_wjp_rule_of_law_index_HISTORICAL_DATA_FILE.xlsx`, md5 `56724a01`), from which
  `wjp_rol_sf62_2012_2025.csv` extracts sub-factor 6.2 for every edition, 1,484 scores; `criteria_v2_s45.py`,
  section 5, computes every figure below from it and asserts them.
  (a) *From the distribution.* The Index codes each answer from 0 to 1, but it normalizes country scores by the
  Min-Max method against a 2015 base year (its 2025 Methodology), so a point on its scale does not say how often
  regulation is influenced. It publishes no bands, unlike the Freedom House rating whose top band sets C2.6's bar.
  (b) *The upper quartile.* The clause asks that regulation be applied without improper influence, which describes
  the jurisdictions whose regulators the Index's questions find least often bribed or influenced, not the typical
  one. The upper quartile is the conventional cut for that group and the nearest the Index comes to C2.6's top
  band. It is 0.7665 on the inclusive (linear) definition and 0.7712 on the exclusive, 0.77 on both; 36 of the 143
  jurisdictions meet it.
  (c) *Fixed as a figure.* A quartile re-derived for each edition would make the clause relative, met by a quarter
  of the world whatever the world does; fixed, it is absolute. It is also stable: the upper quartile lies between
  0.75 and 0.78 in every edition from 2014 to 2025 (0.73 in 2012–2013, on 97 jurisdictions).
  (d) *What the sub-factor measures.* Its expert questions ask what most likely follows when an environmental
  authority notifies a plant polluting a river, or a public-health authority a food producer tied to a salmonella
  outbreak (compliance, bribery or influence of the authority, or nothing), and how often bribes are paid for
  permits, licences, and public-health and welfare services; its household questions ask about bribes for permits
  and documents (Table of Variables 2025, 6.2.1 and 6.2.2). It measures capture by bribery and influence, the
  clause's subject; the formal independence of regulators (funding, appointment, the movement of staff) is what a
  design is scored on, from its stated provisions.
  *Consequence, indicative only.* No C4.6 unit is scored before stage 2, on each entry's stated date and
  configuration. On the 2025 edition: United States 0.87; Denmark 0.97, Finland 0.97, Norway 0.99, Sweden 0.92
  (the Index does not cover Iceland); Singapore 0.94; Qatar 0.66; China 0.61. The first six meet the bar; Qatar and
  China do not. Every bar from 0.67 to 0.87 gives the same verdicts. The alternative recorded for the owner, the
  median (0.61), would pass Qatar and China as well. The Index covers neither the Soviet Union nor Cuba nor North
  Korea, so Centrally Planned Socialism's clause 3 cannot be read from it. How a historical configuration is read
  on a series that does not reach it is a question for all of that entry's class I units, and it is decided once,
  when they are re-checked in stage 2.
- **47.2 (correction).** The status line above said that `build_criteria.py` writes protocol draft.6 with six
  asserted edits. Since Session 46 it has written draft.7 with seven (1.2's was added by 46.3(b)); from 47.1 it
  writes draft.8, whose Appendix B carries C4.6's bar. The line now says so.

## 2. Method

A restatement changes the measure named, or deletes a clause, or removes a date or a place-bound construct; it keeps
the bar's own figure wherever the bar is sound. Where only the indicator was missing, the Pass Threshold's words stay
and the measurement field names the published source (class I below), so the clause and Appendix B are unchanged.
One class I threshold is reworded without a change of bar: C1.4's "across all three displacement scenarios" names
the scenarios (30%, 50% and 70% of paid hours displaced) instead of the dated ones its measurement field set (R1); its
two clauses stand, and the scenario list is their scope.
Where a threshold is restated, the Pass Threshold remains operative over every other field (protocol 2.3), and v2.0
carries one figure per quantity. For a design, every named indicator is the measure its projection must estimate
(protocol 4.1); for a mechanism, reach (3.2) applies as before.

**K7 (new).** Package B's C2.6 measures association rights (Freedom House's associational category). C2.5's fourth
clause, "voluntary association protected", measures the same quantity, and the R4 audit's reach notes show scorers
read it as civil freedom of association. It is deleted from C2.5 and measured once, in C2.6. C2.5 keeps exit and
mobility, under N9.

Each criterion has a class, which sets what the pass must re-check (section 7):

| Class | Meaning | Criteria |
|---|---|---|
| W | wording, commentary or disclosure only; no verdict can change | C1.2b, C1.5, C2.2, C3.3, C5.1 |
| D | clauses deleted only; a unit can keep or raise its score | C2.5, C4.4, C4.5 |
| I | indicator named for an unchanged clause and bar | C1.1, C1.4, C2.1, C2.3, C2.4, C3.1, C3.5 |
| M | bar, measure or clause restated | C1.2a, C1.3, C3.4, C4.1, C4.2, C4.3, C5.2 |
| N | new criterion | C2.6, C3.6, C4.6 |
| U | unchanged | C3.2, C5.3, C5.4, C5.5 |

## 3. Gaps the review missed

The review listed Requirement-versus-threshold gaps by hand. The generator now scans every Requirement and
measurement field for figures its Pass Threshold lacks (`criteria_v2_s45.py`, section 1, runs the scan on the
snapshot). Beyond C1.1, C1.2a and C1.4 it finds four: **C1.3** (Requirement 90%+, threshold ≥88%), **C3.3**
(measurement: poverty rise under 5 points, housing ≥85%, services ≥90%, democratic functions ≥80%, against the
threshold's degradation under 20%), **C4.1** (measurement: debt "sustainable <60%", threshold <80%) and **C5.1**
(Requirement "40+ years preferred", threshold ≥20 years). Each is resolved to the Pass Threshold, the operative text
under protocol 2.3, so no published score changes. C3.3's stricter measurement figures are retired as C1.4's were.

## 4. Indicator and bar choices (45.3)

Consequential choices are marked ▲; each is a candidate for the owner's review.

- **C1.1, C1.4 ▲ poverty line.** The World Bank Societal Poverty Line replaces the US Supplemental Poverty Measure.
  It is built to track the cost of basic needs as median income rises (a floor at the international line, plus half
  the median), published for 168 countries on the Poverty and Inequality Platform in 2021 PPP. The alternative, the
  Bank's fixed $8.30 line, understates basic needs in high-income economies. Consequence: rich economies' measured
  poverty is near-relative, so 90% reductions are rare; C1.1 had no 1.0 after the pass already (review R3).
- **C1.2a ▲ price basis.** $60,000 in constant 2019 US dollars at PPP. 2019 is the year the Paper calibrated the
  figure on (US median household wealth, 2019); PPP is the international method the Paper's own justification names.
  The Cultural/Geographic Adaptation field (a $70,000 figure and 150–300% ranges of median expenses) is removed: its
  ranges are not reproducible and its figure contradicts the threshold. This raises the bar for middle-income
  contexts (China is the only one in the corpus) relative to the removed ranges; the relative alternative is recorded
  for the owner.
- **C1.3 affordability.** "80% area median income" (a US construct) becomes housing costs ≤30% of disposable income
  at 80% of the regional median household disposable income. The 30% is the US standard the original clause implied,
  now stated.
- **C2.1** Gallup World Poll share satisfied with freedom to choose what they do with their lives, published in the
  World Happiness Report data, measures clause 1. Clause 2 (revealed preference) is aspirational (section 5).
- **C2.3** time-use surveys (clause 2); the EU-SILC and ONS "worthwhile" item on 0–10, read as 70/100 = 7.0
  (clause 3); clause 1 aspirational.
- **C2.4** International IDEA turnout (clause 1); the official record of initiative, petition or participatory
  budgeting processes, none meaning not met (clause 2); the OECD Trust Survey item on whether the political system
  lets people like the respondent have a say (clause 3; OECD mean 30% in 2023).
- **C3.1** dated record of the most recent major shock (IMF database of COVID-19 fiscal measures) or the rules
  (clause 1); household social benefits in the national accounts against real GDP (clause 2); ILO social protection
  coverage, SDG 1.3.1 (clause 3).
- **C3.4** "democratic governance for changes" names an instrument (R4); restated as contestability: changes open to
  challenge and reversal by those affected.
- **C3.5 ▲** supreme audit institutions' published recommendation-implementation rates (clause 3); the IMF's implicit
  fossil-fuel subsidies, unpriced environmental costs as a share of GDP, as the published lower bound of
  externalization, with GDP standing for "total costs" (clause 4); clauses 1–2 aspirational.
- **C4.1 ▲** after K3–K4 it measures fiscal and wealth sustainability: IMF general government gross debt, and net
  national saving (gross saving less consumption of fixed capital) for "positive wealth transfer". Its derivation
  changes from N12 + N6 to N12 + N5: nothing ecological remains in it, and fiscal space is N5's content.
  Consequence: N6's implicit weight falls from 3.8% to 1.8%, the lowest with N11 (`criteria_v2_s45.py`, section 2);
  N6 then rests on C4.2 and on the A.4 constraint scheme (S2), which is the reading that treats it as a constraint.
  Decision 46.1's C4.6 (N13 + N6) returns it to 3.4% of 29.
- **C4.2 ▲** consumption-based accounts (G3). Carbon: the rate of a 35% cut over 2019–2030, the low end of the
  IPCC AR6 1.5 °C range the Paper cites (43% GHG from 2019 levels), is 3.8% a year, and binds at any date.
  Biodiversity: IUCN Red List Index non-declining. Regeneration: ecological footprint of consumption per person no
  greater than world biocapacity per person (National Ecological Footprint and Biocapacity Accounts). Boundaries:
  the four downscaled nationally (phosphorus, nitrogen, freshwater, land-system change; O'Neill et al. 2018, Fanning
  et al. 2022); "no more than two transgressed" keeps the original clause's own count. The requirement's "hard
  constraint" sentence is restated to describe the Applied scoring (S2).
- **C4.3** renamed Group Equity (R6); clause 2 (150%+ proportional benefits, an instrument) deleted, since clauses 1
  and 3 measure the outcome it serves (R4); non-citizen residents included (G3); disparity defined on median income
  and wealth.
- **C5.2** plans become feasibility: each element shown by precedent or component evidence (R4).
- **C2.6 ▲** Freedom House civil-liberties score ≥53 of 60, the top band of its former 1–7 rating. Its fifteen
  questions cover expression and belief, association, rule of law and personal autonomy (surveillance included) and
  exclude the electoral questions C2.4 and C4.4 measure. V-Dem's Civil Liberties Index is the cross-check; a
  disagreement about the threshold is flagged. A design answers the fifteen questions from its own sources.
- **C3.6 ▲** real GDP per hour worked and total factor productivity (Penn World Table 11.0, `rtfpna`), each
  non-declining over 20 years; basic-needs output at the system's own working time. TFP is a separate clause because
  output per hour can rise on capital accumulation alone while methods stagnate. Defined on productivity, not output
  growth, so designs that choose shorter hours or lower consumption can pass.
- **C2.6 clauses 2–3 and C4.6** (Package C): their measures and bars are decision 46.2's, listed there; C4.6's
  clause 3 bar, 0.77 on the World Justice Project's sub-factor 6.2, is decision 47.1's ▲.

## 5. Aspirational clauses (45.4)

C2.1 clause 2 (revealed preference), C2.3 clause 1 (weekly creative engagement), C3.5 clauses 1 and 2 (detection
within a week, diagnosis ≥80%). No agency publishes these quantities; a 1.0 on the criterion requires the scoring
document to name evidence that shows the clause (a study, an audit, a design's own record), and silence is not
clearance (2.3(b)). Paper v2.0 states that these criteria can in practice separate only 0.0 from 0.5 until such
evidence exists. C3.1 clause 1 is not aspirational: the rules or a dated record show it.

## 6. What the generator asserts

`build_criteria.py` (version 2.2) starts from `criteria_s44_snapshot.json` (md5 checked), applies Appendix V, and exits
1 unless: every Requirement figure appears in its Pass Threshold, and every measurement figure does or is declared
descriptive in the criterion's block; each registered quantity (wealth Gini, citizen proposals, carbon,
regeneration, autonomy share, association, housing stability, debt, productivity, inflation, and, from decision
46.1, medical consent and compulsion, pollution mortality, liability for harm and regulatory independence) appears
in exactly one Pass Threshold; no Pass Threshold carries a year other than a declared price year; no field names a US-only measure
(area median income, the Supplemental Poverty Measure, CPI-U, the Census Bureau); every clause is a verbatim
substring of its threshold, once, in order, leaving only connectives and a declared scope; every anchor threshold equals its Pass Threshold (D28(g)); the structure is
the one Appendix V's structure line states (29 criteria; domain maxima 6, 6, 6, 6, 5). `build_criteria.py --selftest` plants one violation of each rule and
confirms each is rejected (negative control).

## 7. Consequences for the rescoring pass

Counts are from `criteria_v2_s45.py`, section 3 (23 entries; scores in force, before the pass is applied).
Class W (115 units): nothing to re-check. Class D (69 units, 25 at 0.5): units can only keep or rise; C4.4 and C4.5
were not yet re-estimated and are scored on v2.0 clauses in stage 2; for C2.5, a 0.5 whose only unshown clause was
the association clause rises. Class I (161 units): a unit is re-checked where the named indicator could give a
different clause verdict from the one recorded, which means the 42 units of the six configured national economies,
where the indicator is a published series, and any other unit whose clause record cites a different measure.
Class M (161 units): every unit is re-checked clause by clause against Appendix V, in the D28 clause-record form.
Class N: 69 new units (23 entries × 3, C4.6's 23 added by decision 46.1). C2.6's two new clauses add no re-check:
none of its units has been scored, and each is scored on all three clauses. Class U (92 units): nothing beyond the
pass already planned. Unlike D28, the v2.0 criteria can change failure counts and tiers: every entry gains three
criteria, and seven are restated. Under equal weighting the implicit norm weights on 29 criteria range from 1.7% to
15.5% (`criteria_v2_s45.py`, section 2).

## 8. Not done here

The S1 norm-weight table is computed (`criteria_v2_s45.py` section 2) but belongs in Paper v2.0. The A.4 constraint
scheme (S2) and the per-system count of units resting on unshown clauses (R5) are stage 3. Band texts of restated
criteria still carry Paper v1.4 examples; `criteria.json` marks them, and anchors describe while thresholds govern
(2.3(g)). The corpus, CSV and totals change only when the pass is applied by generator, which also carries decision 45.6.
C4.6's bar on the World Justice Project's sub-factor 6.2, not fixed in Session 46 (46.4), is fixed by 47.1.

## 9. Package C (decision 46.1: C-1 and C-2 adopted; C-3 recorded for v2.1)

Proposed in Session 45; the owner adopted C-1 and C-2 in Session 46 (decision 46.1). The proposal stands below as
written, with one correction marked (46.3(a)); the adopted wording is Appendix V's.

The owner asked whether NEEC covers bodily autonomy and medical freedom, and the perverse incentive of an owner who
profits from both a harm and its treatment (food or agriculture that damages health, and the healthcare that treats
it). Checked against the v2.0 text: no criterion measures health outcomes, consent to medical treatment, the health
burden of pollution, or whether harm is a cost to the one who causes it. Healthcare appears only as an item of
C2.2's basic-needs basket, and fuel-related pollution only in C3.5's externalization clause. The Session 44 review
did not consider health.

The documented pattern behind the concern is concealment of known harm to protect product revenue, and capture of
the regulators who should detect it (tobacco, leaded fuel, PFAS, industry-funded nutrition research). Common
ownership of harm-causing and remedy-selling businesses creates the incentive structurally. That record does not
establish deliberate harm to create patients, and the criteria need not assume it: they test whether harm is a net
cost to whoever causes it, which removes the incentive whatever the ownership.

- **C-1 (recommended).** C2.6 gains a clause: informed consent to medical treatment is protected in law, and any
  compulsion (treatment, vaccination, quarantine) rests on law, is time-limited and is open to independent judicial
  review. This is the limitation test of the Siracusa Principles and of the Oviedo Convention (Articles 5 and 26),
  which neither forbids public-health measures nor exempts them from review. *[Corrected, 46.3(a): with its time
  limit on every compulsion the clause is stricter than that test, which asks a time limit of emergency measures
  only; 46.2(e) records the consequence and the alternative.]* It covers consent and refusal;
  entitlement to particular procedures or unapproved treatments (abortion, assisted dying, right-to-try) is
  contested and is not decided by the criterion. Derivation unchanged.
- **C-2 (recommended).** A new C4.6 Harm Internalization (N13 Incentive Alignment + N6 Ecological Compliance), with
  three clauses: deaths attributable to pollution (SDG indicators 3.9.1 to 3.9.3) non-increasing over 20 years;
  those who cause harm to health or the environment liable for it, enforceably by those harmed; regulation of food,
  water, air, chemicals and medicines applied without improper influence (the World Justice Project Rule of Law
  Index, sub-factor 6.2, is the nearest published measure; its bar is to be fixed). N6's implicit weight returns
  from 1.8% to about 3.4%.
- **C-3 (found; not recommended now).** A new C1.6 Health Security: the universal health coverage service index
  (SDG 3.8.1) and catastrophic out-of-pocket health spending (SDG 3.8.2). It fills the larger gap but goes beyond
  the owner's question; it is recorded for v2.1 unless the owner adopts it now.

C-1 and C-2 give 29 criteria (Domain 4 maximum 6); with C-3, 30. Each new criterion adds 23 units to the pass. On
29 or 30 criteria no total falls on a half percent, and 45.6 stands as the general rule. The session that applies
the owner's decision fixes the wording and bars, with sources, in Appendix V; `build_criteria.py` reads the
structure line, so no code changes.

**Outcome (Session 46).** Appendix V now carries C2.6's clauses 2 and 3 and the C4.6 block, with the readings of
46.2; C4.6's bar on the World Justice Project's sub-factor 6.2 awaited its data (46.4) and is fixed by 47.1. The structure needed no code
change, as expected, but three things did: `build_criteria.py` (version 2.1) and `criteria_v2_s45.py` register the
four new quantities; the generator took each new criterion's source from a hard-coded "Package B, decision 45.1",
which would have been wrong for C4.6, and now reads it from the block's `adopted` field; and the protocol it
generates is draft.7, since draft.6 already names the 28-criterion text of tag `s45`.

## Appendix V. The v2.0 text (read by `build_criteria.py`)

Fields are the keys of `criteria.json`'s `definition`; `clauses` are separated by ` | `; `scope` is text in the
threshold that applies to every clause; `allow` lists descriptive figures a measurement field may carry; `adopted`
names the decision that adopted a new criterion, for its `sources`.

- **structure**: 29 criteria; domain maxima 6, 6, 6, 6, 5

### C1.1
- **class**: I
- **codes**: K6, R2
- **requirement**: Near-universal elimination of poverty within a measurable timeframe: ≥90% poverty reduction within 20 years under base scenario, ≥85% under stress testing.
- **measurement_protocol**: Poverty definition: a person is poor whose household income or consumption per person is below the World Bank Societal Poverty Line (SPL) for their economy, the line the Bank derives from the cost of basic needs as it rises with median income (a floor at the international poverty line plus half the median), in 2021 PPP international dollars; the line's parameters are revised with each PPP round, and the round used is stated. Data sources: the World Bank Poverty and Inequality Platform; for a design, the rate projected at the same line in the economy the design is proposed for. Calculation: poverty reduction = (baseline rate − rate at year 20) / baseline rate × 100%, the baseline being the rate at the stated base year (the adoption year for a design; for a configured national economy, the start of the 20-year window ending at its stated date). Temporal tracking: at baseline and at 5-year intervals, distinguishing temporary from persistent poverty.
- **indicators**: World Bank Poverty and Inequality Platform, poverty headcount at the Societal Poverty Line (2021 PPP).
- **allow**: 2021, 100%, 5

### C1.2a
- **class**: M
- **codes**: K6, R2
- **requirement**: Genuine asset building enabling ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity, for participants who engage with whatever wealth-building mechanism the system provides.
- **measurement_protocol**: Wealth definition: net worth (total assets − total liabilities), including housing equity, retirement accounts, savings, investment accounts, business ownership and system-specific wealth mechanisms (e.g., PTF acres). Data: longitudinal tracking of the same households over 20-year periods in a household wealth survey (the Luxembourg Wealth Study, the Eurosystem Household Finance and Consumption Survey, or a national equivalent); for a design, the projected accumulation. Price basis: local-currency values are deflated to 2019 prices by the national consumer price index and converted at the World Bank's 2019 PPP conversion factor for private consumption; the figure is the one the Paper calibrated on 2019 US data. Median focus: the median, not the mean, to avoid skew from top wealth holders.
- **pass_threshold**: ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity
- **clauses**: ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity
- **remove**: cultural_geographic_adaptation
- **price_year**: 2019
- **indicators**: Luxembourg Wealth Study; Eurosystem HFCS; national wealth surveys; World Bank WDI PPP conversion factor, private consumption (2019).

### C1.2b
- **class**: W
- **codes**: W
- **pass_threshold**: Gini <0.35 for wealth distribution
- **clauses**: Gini <0.35 for wealth distribution
- **threshold_note**: Moved from legacy C1.5's Pass Threshold, per the boundary resolution in Paper Section 12.2 (commentary moved out of the threshold in v2.0).

### C1.3
- **class**: M
- **codes**: K6, R2
- **requirement**: ≥88% housing stability resistant to market volatility, with housing affordable to households at 80% of the regional median disposable income.
- **measurement**: Housing stability rate = percentage of participants maintaining stable housing over 5-year periods without involuntary displacement from foreclosure, eviction, or inability to afford rent increases. Affordability: housing costs (rent or mortgage payments plus utilities) no more than 30% of disposable income for a household at 80% of the regional median household disposable income, from the OECD Affordable Housing Database, EU-SILC or national household surveys; for a design, projected on the same measure.
- **pass_threshold**: ≥88% housing stability over 5-year periods, housing costs ≤30% of disposable income at 80% of regional median household disposable income
- **clauses**: ≥88% housing stability over 5-year periods | housing costs ≤30% of disposable income at 80% of regional median household disposable income
- **indicators**: household panel surveys for displacement; OECD Affordable Housing Database; EU-SILC; national household surveys.

### C1.4
- **class**: I
- **codes**: K6, R1
- **requirement**: Maintain material security as human labor becomes increasingly optional: poverty <8% and aggregate demand >85% of baseline in each of three scenarios in which 30%, 50% and 70% of baseline paid working hours are displaced by automation.
- **measurement**: Stress test across the three automation scenarios, a displacement of 30%, 50% or 70% of baseline paid working hours, with no assumption about when each occurs. In each, poverty is measured at the Societal Poverty Line, as in C1.1, and aggregate demand as real final consumption expenditure relative to the pre-displacement baseline. The Pass Threshold's figures apply in every scenario.
- **pass_threshold**: Poverty <8% and aggregate demand >85% baseline in each of the 30%, 50% and 70% displacement scenarios
- **clauses**: Poverty <8% | aggregate demand >85% baseline
- **scope**: in each of the 30%, 50% and 70% displacement scenarios
- **indicators**: Societal Poverty Line (as C1.1); national accounts final consumption expenditure; for a design, its own model of the three scenarios.

### C1.5
- **class**: W
- **codes**: W
- **pass_threshold**: ≥80% population with an active wealth-accumulation pathway
- **clauses**: ≥80% population with an active wealth-accumulation pathway
- **threshold_note**: Gini clause removed, moved to C1.2b, Paper Section 12.2 (commentary moved out of the threshold in v2.0).

### C2.1
- **class**: I
- **codes**: K5, R3
- **measurement**: Clause 1: the share of adults satisfied with their freedom to choose what they do with their life (Gallup World Poll; published as "freedom to make life choices" in the World Happiness Report data), read as the share reporting genuine autonomy in major life decisions. Clause 2 is aspirational: no agency publishes revealed-preference evidence of this kind, and a 1.0 requires the scoring document to name a study or record that shows it (for example, behavior observed when an unconditional alternative exists). This is the one home of the share of decisions free of coercion; C4.5 no longer measures it. For a design, both clauses are estimated on the same measures.
- **indicators**: clause 1, Gallup World Poll (World Happiness Report data); clause 2, aspirational.
- **allow**: 1.0

### C2.2
- **class**: W
- **codes**: R4
- **disclosure**: "Unconditional" is the content of N2 itself, not an instrument clause, and stays; this is the one criterion that favors unconditional-provision designs by definition, and Paper v2.0 says so.

### C2.3
- **class**: I
- **codes**: R3
- **measurement**: Clause 1 (regular creative engagement): the share of adults engaging at least weekly in arts, music, writing, crafts, study or invention; no statistical agency publishes this share on a comparable basis, so the clause is aspirational unless the scoring document names a survey that records weekly frequency. Clause 2 (non-subsistence pursuits): average weekly hours of leisure, time outside paid work, unpaid work and personal care, in national time-use surveys (OECD Time Use Database, HETUS, American Time Use Survey). Clause 3 (meaning/purpose): the mean answer on a 0–10 scale to "Overall, to what extent do you feel that the things you do in your life are worthwhile?" (EU-SILC well-being module; UK ONS personal well-being), multiplied by 10. For a design, each is projected on the same measure.
- **indicators**: clause 1, aspirational; clause 2, OECD Time Use Database, HETUS, ATUS; clause 3, EU-SILC and ONS "worthwhile" item.
- **allow**: 0

### C2.4
- **class**: I
- **codes**: K2, R3
- **measurement**: Clause 1 (participation): turnout as a share of the voting-age population in national elections (International IDEA Voter Turnout Database), or, where the system takes its binding decisions otherwise, participation in those processes; binding economic-domain decisions (workplace democracy, community asset governance) count. Clause 2 (influence): the share of citizen-initiated proposals (popular initiatives, petitions with a right to a decision, participatory-budgeting proposals) reaching a binding decision that are adopted, from the official record of the process; where no such process exists the clause is not met. This is the one home of the proposal-adoption quantity; C4.4 no longer measures it. Clause 3 (responsiveness): the share answering that the political system allows people like them to have a say in what the government does (OECD Survey on Drivers of Trust in Public Institutions, or the equivalent European Social Survey item). For a design, each is projected on the same measure.
- **indicators**: International IDEA Voter Turnout Database; official records of initiative and participatory processes; OECD Trust Survey external-efficacy item.

### C2.5
- **class**: D
- **codes**: K7
- **requirement**: Participants can opt out without penalty and relocate without losing essential benefits; freedom of association is measured in C2.6.
- **measurement**: Ease of exit (time and resources required to leave the system). Penalties for non-participation (differential treatment of non-participants). Capacity to leave for alternative arrangements, including forming or joining alternative communities. Geographic mobility (freedom to relocate without losing essential benefits).
- **pass_threshold**: Exit feasible within 3 months without material penalty, no differential treatment, geographic mobility maintained
- **clauses**: Exit feasible within 3 months without material penalty | no differential treatment | geographic mobility maintained

### C2.6 · Civil Liberties and Rule of Law
- **class**: N
- **codes**: G2, C-1
- **adopted**: Package B, decision 45.1; clauses 2 and 3, Package C, decision 46.1
- **domain**: D2
- **derivation**: From N3 (Coercion Minimization) + N7 (Governance Legitimacy and Anti-Capture)
- **requirement**: Economic security is not bought with liberty: expression, belief, association, due process, equal treatment under law and personal autonomy, privacy and consent to medical treatment included, are protected in practice; compulsion in the name of health rests on law, is time-limited and is open to independent review; and those who administer the system answer to independent courts.
- **rationale**: Domain 2 measures freedom from economic coercion, participation and exit, but not the civil liberties and legal protections those freedoms depend on. The omission matters most where allocation runs through the state or through shared data systems: a system can provide for everyone and still punish dissent, surveil its participants or deny them an independent hearing against its administrators. It is also the dimension on which the corpus's configured national economies differ most from the rest. Bodily integrity belongs to personal autonomy, but none of the fifteen civil-liberties questions of the Freedom House checklist asks about consent to medical treatment or about the limits of compulsion in public health, and a system that allocates care, or conditions benefits on health measures, is where that liberty is most exposed; clauses 2 and 3 measure it.
- **distinguishes**: C2.6 from C2.4 and C4.4: participation and the distribution and accountability of power are measured there; C2.6 measures rights held against that power, whoever holds it. The Freedom House civil-liberties checklist is used because it covers exactly this set (expression and belief, associational and organizational rights, rule of law, personal autonomy and individual rights) and leaves out the electoral questions that C2.4 and C4.4 measure. Clauses 2 and 3 cover consent, refusal and the legal form of compulsion; they do not decide entitlement to particular procedures or to treatments not approved (abortion, assisted dying, a right to try), which are contested and on which the criterion takes no side. Restrictions on movement also enter the Freedom House score, through its freedom-of-movement question; clause 3 tests whether compulsion is prescribed by law, limited in time and reviewable, not how much of it there is.
- **measurement_protocol**: Clause 1. Configured national economy: the Freedom House civil-liberties score, 0–60, in Freedom in the World for the stated date, cross-checked against V-Dem's Civil Liberties Index; where the two sources disagree about whether the threshold is met, the call is flagged (protocol 6.1), not resolved silently. Design, mechanism or comprehensive system: the fifteen civil-liberties questions of the Freedom House checklist are answered from the system's own sources, 0–4 each, crediting only what the system states and provides for (protocol 4.1): its guarantees, the body that decides disputes between participants and the system's administrators and that body's independence from them, and, where allocation depends on personal data, stated limits on collection, access, use and retention. A mechanism operating inside a wider economy is scored on what it adds to or takes from the liberties of that economy (protocol 3.2). Clauses 2 and 3 are shown from the law in force at the stated date, which the scoring document names. Clause 2: a statute, code or constitutional provision requires the free and informed consent of the person concerned before any medical intervention, or of a lawful representative where the person cannot consent, and protects the right to refuse consent or to withdraw it at any time, as Article 5 of the Council of Europe's Convention on Human Rights and Biomedicine (the Oviedo Convention) states it; the only exceptions are an emergency in which consent cannot be obtained and compulsion that meets clause 3. Clause 3: compulsion is any measure that applies treatment, vaccination, quarantine or isolation to a person without their consent, or that penalizes refusal by a fine, by detention or by loss of employment, schooling or an essential benefit. Every such measure is prescribed by law; is time-limited, lapsing at a stated time unless renewed by a decision itself open to review, so that a standing requirement with no such limit does not meet the clause; and is open to challenge by the person concerned before an independent court or tribunal with power to end it. Where the scoring window contains a public-health emergency, the measures actually taken are read as well: V-Dem's Pandemic Violations of Democratic Standards Index, which codes emergency measures without a time limit, and the Oxford COVID-19 Government Response Tracker for what was imposed. For a design, both clauses are answered from its own sources, crediting only what it states and provides for (protocol 4.1); a mechanism is scored on what it adds to or takes from the protections of the economy it operates in (protocol 3.2).
- **pass_threshold**: Civil-liberties score ≥53 of 60 on the Freedom House checklist; informed consent to medical treatment protected in law; any compulsory treatment, vaccination, quarantine or isolation prescribed by law, time-limited and open to independent judicial review
- **clauses**: Civil-liberties score ≥53 of 60 on the Freedom House checklist | informed consent to medical treatment protected in law | any compulsory treatment, vaccination, quarantine or isolation prescribed by law, time-limited and open to independent judicial review
- **indicators**: clause 1, Freedom House, Freedom in the World, civil-liberties score (0–60); cross-check, V-Dem Civil Liberties Index; clauses 2 and 3, the law in force, with the Oviedo Convention's Article 5 as the consent standard and, for a public-health emergency, V-Dem's Pandemic Violations of Democratic Standards Index and the Oxford COVID-19 Government Response Tracker.
- **allow**: 0, 4, 5
- **band_1.0**: Score of 53 or more of 60 (the top band of Freedom House's former 1–7 civil-liberties rating), consent to medical treatment protected in law, and every medical or public-health compulsion prescribed by law, time-limited and open to an independent court; or a design whose stated guarantees and independent adjudication answer the checklist at that level and state the same protections, with component evidence where it relies on institutions not yet built.
- **band_0.5**: Score of 17 to 52; or a score of 53 or more with consent or the limits of compulsion not shown; or a design whose guarantees are partial, unstated for some questions, or left to administrators' discretion without an independent hearing, where the gap has a credible pathway to close under the system's own logic.
- **band_0.0**: Score of 16 or less (the two lowest bands of the former rating), or a design that subordinates expression, association, due process or consent to medical treatment to its allocation or administration with no independent adjudication.

### C3.1
- **class**: I
- **codes**: R3
- **measurement**: Clause 1 (response time): days from a shock's trigger, the first official data showing it, to the first increased payment, established from the system's rules (automatic triggers, payment frequency) and, for a configured national economy, from the dated record of its response to its most recent major shock (for 2020, the IMF's database of country fiscal measures in response to the COVID-19 pandemic); no legislative delay (automatic activation based on triggers). Clause 2 (scaling): the percentage change in social benefits received by households (national accounts, SNA item D.62) against the percentage fall in real GDP in that shock; a 30% GDP decline requires at least a 30% benefit increase; for a design, from its rules. Clause 3 (coverage): the share of the population covered by at least one social protection cash benefit (ILO World Social Protection Database, SDG indicator 1.3.1).
- **indicators**: system rules or IMF database of COVID-19 fiscal measures; national accounts D.62 and real GDP; ILO World Social Protection Database (SDG 1.3.1).
- **allow**: 2020

### C3.3
- **class**: W
- **codes**: K6
- **measurement**: Core functions: poverty (the share of the population above the C1.1 poverty line), housing stability (the C1.3 rate), essential-service capacity and democratic-function capacity. Degradation is each function's fall from its pre-shock level, as a share of that level; the Pass Threshold's figures apply to every function in each scenario counted.

### C3.4
- **class**: M
- **codes**: R4
- **measurement**: Parameter flexibility (range of adjustable variables without system redesign). Evidence integration (speed of policy updates in response to data). Contestability: those affected by a parameter change can challenge it and have it reversed through a process that does not depend on the officials who made it, whatever governance form the system uses; the criterion does not require a particular form. Stability during transitions (no collapse from parameter adjustments).
- **pass_threshold**: ≥30% parameter adjustability range, policy updates within 6 months of evidence, changes open to challenge and reversal by those affected, zero collapses during parameter adjustments
- **clauses**: ≥30% parameter adjustability range | policy updates within 6 months of evidence | changes open to challenge and reversal by those affected | zero collapses during parameter adjustments

### C3.5
- **class**: I
- **codes**: R3
- **measurement**: Clause 1 (detection) is aspirational: the time from a failure's occurrence to its official identification can be shown from the dated record of the entry's most consequential failure in the scoring window (an official inquiry, audit or evaluation) or, for a design, from its monitoring rule, and the scoring document must name that record. Clause 2 (diagnosis) is aspirational: no agency publishes the share of failures whose cause is established; it can be shown only from a design's documented diagnostic record or an independent evaluation that reports it. Clause 3 (correction): the share of the supreme audit institution's recommendations implemented, as the US Government Accountability Office and other INTOSAI members publish, or for a design its correction record. Clause 4 (externalization): unpriced environmental costs of fuel use as a share of GDP, the implicit subsidies in the IMF's Fossil Fuel Subsidies Data, a lower bound on externalized cost, with GDP standing for total costs; for a design, projected.
- **indicators**: clauses 1–2, aspirational; clause 3, supreme audit institutions' recommendation-implementation rates; clause 4, IMF Fossil Fuel Subsidies Data (implicit subsidies, % of GDP).

### C3.6 · Productive and Innovative Capacity
- **class**: N
- **codes**: G1
- **adopted**: Package B, decision 45.1
- **domain**: D3
- **derivation**: From N13 (Incentive Alignment) + N1 (Human Flourishing)
- **requirement**: The system sustains and improves the output its other criteria distribute: productivity does not decline, improvement comes from better methods and not only from more capital, and basic needs are provisioned at the working time the system itself assumes.
- **rationale**: Every distributive criterion can be passed on projections that hold output fixed. Whether a system can produce, and improve, what it proposes to distribute, including how it allocates resources when information is dispersed, is the question comparative economics most often puts to alternative systems. The criterion is defined on productivity and provisioning, not on growth of total output, so it builds in no preference against designs that choose shorter hours or lower consumption: a system may produce less in total and pass, provided output per hour does not decline and basic needs are met at its own hours.
- **distinguishes**: Labor productivity from total factor productivity: output per hour can rise on capital accumulation alone while methods stagnate, as in the extensive growth of Soviet-type economies, so the second clause tests improvement in methods and allocation. C3.6 from C1.4: C3.6 asks whether output can be produced and improved; C1.4 asks whether security survives when labor is no longer needed to produce it.
- **measurement_protocol**: Clause 1: real GDP per hour worked at constant prices (OECD Productivity Database, Penn World Table, Conference Board Total Economy Database), compound annual change over the 20 years to the stated date. Clause 2: total factor productivity at constant national prices (Penn World Table, rtfpna), compound annual change over the same window. Clause 3: the goods and services in the C1.1 poverty basket produced for the whole population at the average working time the system assumes (for a configured economy, its actual hours; for a design, its stated hours), shown by the economy's record or, for a design, by its own accounting of output per hour at those hours with component evidence. For a design, clauses 1 and 2 are scored on its mechanisms for allocating investment and rewarding improvement, calibrated by the record of the components it cites (protocol 4.1); a design that suppresses price or other allocation signals without a stated replacement for them cannot show either.
- **pass_threshold**: Real output per hour worked non-declining over 20 years, total factor productivity non-declining over 20 years, basic-needs output sustained at the system's own working time
- **clauses**: Real output per hour worked non-declining over 20 years | total factor productivity non-declining over 20 years | basic-needs output sustained at the system's own working time
- **indicators**: OECD Productivity Database; Penn World Table 11.0 (rtfpna); Conference Board Total Economy Database.
- **band_1.0**: All three clauses shown: productivity and TFP non-declining over 20 years on published data, or, for a design, mechanisms for allocating investment and rewarding improvement whose components have that record, and a provisioning account at its stated hours.
- **band_0.5**: One or more clauses not shown, or shown only by projection resting on untested assumptions, where the system has a functioning allocation mechanism of its own (markets, planning with feedback, or another stated mechanism).
- **band_0.0**: Productivity or TFP declining over 20 years with no credible pathway under the system's own logic, or a design whose own assumptions imply that basic needs cannot be provisioned at its stated hours, or that suppresses allocation signals with no replacement.

### C4.1
- **class**: M
- **codes**: K3, K4, K6, R1
- **derivation**: From N12 (Intergenerational Equity) + N5 (Crisis Robustness)
- **requirement**: Preserve resources and opportunities for future generations through fiscal and wealth sustainability: debt-to-GDP below 80% and a positive wealth transfer to the next generation; the ecological transfer is measured in C4.2.
- **measurement**: Debt-to-GDP: general government gross debt as a share of GDP (IMF World Economic Outlook database). Intergenerational wealth transfer: net national saving (gross national saving less consumption of fixed capital) as a share of gross national income, positive over the scoring window (national accounts; World Bank World Development Indicators). A design is scored on its projected debt path and net saving. Carbon and resource-regeneration trajectories are measured once, in C4.2.
- **pass_threshold**: Debt-to-GDP <80%, positive wealth transfer to next generation
- **clauses**: Debt-to-GDP <80% | positive wealth transfer to next generation
- **indicators**: IMF World Economic Outlook, general government gross debt; national accounts net national saving (World Bank WDI).

### C4.2
- **class**: M
- **codes**: K3, K4, R1, G3, S2
- **requirement**: Economic activity within ecological carrying capacity, measured on consumption so that emissions and extraction moved abroad are not counted as reductions. Scored as one criterion among the rest; the constraint reading, in which a failure here caps the tier at Partially Adequate, is reported as a named Appendix A.4 scheme.
- **measurement**: Clause 1 (carbon): consumption-based CO2 emissions (Global Carbon Budget national consumption-based accounts), compound annual rate of change over the scoring window; the bar is the rate of a 35% cut over 2019–2030, the low end of the 1.5 °C pathways of the IPCC Sixth Assessment Report (2023) that the Paper cites, and it binds at any date. Clause 2 (biodiversity): the IUCN Red List Index for the economy (SDG indicator 15.5.1), non-declining over the scoring window; for a design, the projected pressure on species and habitat. Clause 3 (resource extraction against regeneration): the ecological footprint of consumption per person no greater than world biocapacity per person (National Ecological Footprint and Biocapacity Accounts, Footprint Data Foundation and York University). Clause 4 (other boundaries): phosphorus, nitrogen, freshwater and land-system change, downscaled to national per-person boundaries and compared with consumption-based footprints (O'Neill et al. 2018; Fanning et al. 2022; goodlife.leeds.ac.uk). Circular-economy metrics (waste reduction, material reuse) are supporting evidence. For a design, each clause is projected on the same measure.
- **pass_threshold**: Consumption-based carbon emissions falling ≥3.8% a year, biodiversity neutral or positive, resource extraction ≤ regeneration, no more than two of the four nationally downscaled planetary boundaries transgressed
- **clauses**: Consumption-based carbon emissions falling ≥3.8% a year | biodiversity neutral or positive | resource extraction ≤ regeneration | no more than two of the four nationally downscaled planetary boundaries transgressed
- **indicators**: Global Carbon Budget consumption-based emissions; IUCN Red List Index (SDG 15.5.1); National Ecological Footprint and Biocapacity Accounts; O'Neill et al. (2018) and Fanning et al. (2022) national boundary accounts.
- **allow**: 35%, 2019, 2030, 1.5, 2023, 2018, 2022

### C4.3 · Group Equity
- **class**: M
- **codes**: R4, R6, G3
- **requirement**: Close historical disparities between groups rather than perpetuate them through "neutral" policies, on the axes salient in the entry's society (race, ethnicity, gender, caste, religion or citizenship), non-citizen residents included.
- **measurement**: Disparity: the gap between the median household income, and wealth where published, of the least and most advantaged groups on each declared axis, as a percentage of the most advantaged group's median, from national household surveys. Axes are declared in the entry's scope declaration (protocol 3.3); non-citizen residents are included in the population measured and counted as a group where citizenship is a salient axis. Reduction is the fall in each gap in percentage points per 5 years; convergence is whether the trend reaches the threshold's level within 30 years. Disproportionate benefit flows are evidence for the trajectory, not a separate test.
- **pass_threshold**: Disparity reduction ≥5 percentage points every 5 years, convergence trajectory toward <20% disparities within 30 years, on each declared axis, non-citizen residents included
- **clauses**: Disparity reduction ≥5 percentage points every 5 years | convergence trajectory toward <20% disparities within 30 years
- **scope**: on each declared axis, non-citizen residents included
- **indicators**: national household income and wealth surveys, by declared group.

### C4.4
- **class**: D
- **codes**: K1, K2
- **measurement**: Power concentration indices (economic decision-making distribution). Democratic control mechanisms (accountability of major decisions to those they affect). Accountability structures (capacity to remove/replace decision-makers). Wealth concentration and the adoption of citizen proposals are measured once, in C1.2b and C2.4.
- **pass_threshold**: Democratic accountability for ≥80% of major decisions, removal/replacement mechanisms functional
- **clauses**: Democratic accountability for ≥80% of major decisions | removal/replacement mechanisms functional

### C4.5
- **class**: D
- **codes**: K5
- **measurement**: Extraction rates (wealth transfer from labor to capital, tenants to landlords, borrowers to lenders). Power asymmetries (capacity to refuse participation without penalty). The share of decisions made under duress is measured once, in C2.1.
- **pass_threshold**: Extraction rates <10% GDP, genuine exit rights from exploitative relationships
- **clauses**: Extraction rates <10% GDP | genuine exit rights from exploitative relationships

### C4.6 · Harm Internalization
- **class**: N
- **codes**: C-2
- **adopted**: Package C, decision 46.1
- **domain**: D4
- **derivation**: From N13 (Incentive Alignment) + N6 (Ecological Compliance)
- **requirement**: Harm to health and to the environment is a cost to whoever causes it, not a source of revenue: the toll of pollution on health does not rise, those who cause harm answer for it to those harmed, and the regulators who should detect it are free of the influence of those they regulate.
- **rationale**: No other criterion measures the health burden of pollution, or whether harm is a cost to the one who causes it: healthcare appears only in C2.2's basket of basic needs, and fuel-related pollution only in C3.5's externalization clause. The documented pattern the criterion answers is concealment of known harm to protect product revenue, and capture of the regulators who should detect it, as in the histories of tobacco, leaded fuel, PFAS chemicals and industry-funded nutrition research. Where one owner profits from both a harm and its treatment, the incentive to tolerate the harm is structural. The criterion does not assume that harm is caused deliberately: it tests whether harm is a net cost to whoever causes it, which removes the incentive whatever the ownership.
- **distinguishes**: C4.6 from C3.5 and C4.2: C3.5's fourth clause measures the unpriced environmental cost of fuel use as a share of GDP, a price gap, and C4.2 the pressure of consumption on the biosphere; C4.6 measures harm to human health from polluted air and water and from poisoning, whatever its source, and the liability and regulation that make harm a cost to whoever causes it. A system can price fuel fully and still see pollution deaths rise from household fuel or unsafe water, or leave fuel unpriced while those deaths fall. The third clause measures whether regulators are free of the influence of those they regulate; C2.6 measures rights held against the state and the independence of its courts, and C4.4 the accountability of major decisions to those they affect. Health outcomes in general, coverage and financial protection, are not measured; a Health Security criterion is recorded for v2.1.
- **measurement_protocol**: Clause 1: the sum of the age-standardized mortality rates per 100,000 population attributed to household and ambient air pollution (SDG 3.9.1), to unsafe water, unsafe sanitation and lack of hygiene (SDG 3.9.2) and to unintentional poisoning (SDG 3.9.3), in the World Health Organization's Global Health Observatory, at the start and at the end of the 20 years to the stated date; the clause is met if the rate at the end is no higher than at the start. Where the SDG series do not span the window, the Global Burden of Disease study's (IHME) age-standardized death rates attributable to air pollution and to unsafe water, sanitation and handwashing, and from unintentional poisonings, are used, cross-checked against the SDG series where both exist; where the two disagree about whether the clause is met, the call is flagged (protocol 6.1). Clause 2 is shown from the law in force and its record, which the scoring document names: those who cause harm to health or to the environment are liable to compensate those harmed and to remedy the damage, under tort, product-liability or environmental-liability law or through a compensation scheme funded by a levy on those who cause the harm, and no immunity leaves a class of harm uncompensated or compensated from public funds alone; those harmed can bring the claim before an independent court, collectively where the harm is dispersed (a class or representative action, or the standing of associations, as Article 9 of the Aarhus Convention provides in environmental matters); and the scoring document names at least one such claim decided against those who caused the harm, and paid, within the scoring window. Clause 3: for a configured national economy, the World Justice Project Rule of Law Index, sub-factor 6.2 (government regulations are applied and enforced without improper influence), in the edition for the stated date, read at the two decimals the Index publishes. Its questions ask whether an environmental authority's notice to a plant polluting a river, or a public-health authority's to a food producer tied to an outbreak, ends in compliance or in the authority being bribed or influenced to ignore it, and how often bribes are paid for permits, licences and public-health and welfare services. The bar, 0.77, is the upper quartile of the 143 jurisdictions' scores in the Index's 2025 edition, fixed as a figure so that later editions do not move it: the Index publishes no bands, and it normalizes its scores against a 2015 base year, so a point on its scale has no meaning of its own. For a design, clause 1 is the projected rate in the economy it is proposed for; clause 2 is its stated provisions; clause 3 is its stated provisions for the bodies that regulate food, water, air, chemicals and medicines, their independence of those they regulate in funding, appointment and the movement of staff, and the disclosure of who funded the evidence they rely on. Only what the design states and provides for is credited (protocol 4.1); a mechanism is scored on what it adds to or takes from the economy it operates in (protocol 3.2).
- **pass_threshold**: Mortality attributed to pollution non-increasing over 20 years; those who cause harm to health or the environment liable for it, enforceably by those harmed; regulation of food, water, air, chemicals and medicines applied and enforced without improper influence (for a configured national economy, a World Justice Project sub-factor 6.2 score of 0.77 or more)
- **clauses**: Mortality attributed to pollution non-increasing over 20 years | those who cause harm to health or the environment liable for it, enforceably by those harmed | regulation of food, water, air, chemicals and medicines applied and enforced without improper influence (for a configured national economy, a World Justice Project sub-factor 6.2 score of 0.77 or more)
- **indicators**: clause 1, WHO Global Health Observatory (SDG 3.9.1, 3.9.2 and 3.9.3); IHME Global Burden of Disease, risk-attributable death rates; clause 2, the law in force and the record of claims; clause 3, World Justice Project Rule of Law Index, sub-factor 6.2 (bar 0.77, the upper quartile of its 2025 edition).
- **allow**: 100,000, 6.2, 9, 143, 2025, 2015
- **band_1.0**: All three clauses shown: the pollution mortality rate no higher at the end of the 20 years than at their start; those who cause harm liable for it in the law in force, enforceably by those harmed, with a record of claims paid; and regulation applied without improper influence (for a configured national economy, a score of 0.77 or more on the World Justice Project's sub-factor 6.2); or a design whose stated provisions do the same, with component evidence where it relies on institutions not yet built.
- **band_0.5**: One or more clauses not shown, or shown only by projection resting on untested assumptions, where the system has a functioning mechanism that makes some harm a cost to whoever causes it (liability, a compensation scheme funded by those who cause the harm, pricing, or independent regulation).
- **band_0.0**: No structural mechanism makes harm a cost to whoever causes it (those who cause harm are shielded from liability with no compensation they fund, and its regulation is controlled by those it regulates), or pollution mortality rising over 20 years with no credible pathway to reverse it under the system's own logic.

### C5.1
- **class**: W
- **codes**: K6
- **requirement**: Build on empirically validated mechanisms, ≥20 years in operation, rather than untested speculation.

### C5.2
- **class**: M
- **codes**: R4
- **requirement**: Deployable both gradually in stable contexts and rapidly in crisis contexts, each shown feasible rather than only planned.
- **pass_threshold**: Staged (≥4 phases) and rapid (≤36 months) deployment, with specific milestones, resource requirements and risk mitigation, each shown feasible by precedent or component evidence
- **clauses**: Staged (≥4 phases) | rapid (≤36 months) deployment | specific milestones | resource requirements | risk mitigation
- **scope**: each shown feasible by precedent or component evidence

### C5.3
- **class**: U
- **codes**: none
- **allow**: 10,000, 1, 100
