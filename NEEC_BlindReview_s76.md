# NEEC Blind Review, Session 76: C2.6, C3.6 and C4.6 for the 17 designs and mechanisms

**Session 76 · 2026-10-18 · Stage 3b, the blind re-read (ledger S59; decisions 69.1, 69.2; ledger D52, D53) ·
Scorer: Claude (Opus 5.5) · Owner: Duke Johnson**

Script: `blind_s76.py` (checked by the harness, which compares its output with `blind_s76_output.txt` and confirms
that this record carries every table it generates). Evidence: `evidence_cache_s76.py` (16 passages of the designs' own
texts, by digest) beside Session 65's and Session 70's files for these criteria, with `evidence_cache/C2.6/`, `C3.6/` and
`C4.6/sources_s76.md` naming the sources cited but not cached. Nothing here changes a published score: the final
readings are applied by generator in ledger step S61 (STATE.md, "Next work").

## 1. Summary

Fifty-one units were read on Opus 5.5: the three criteria v2.0 added (class N), C2.6 Civil Liberties and Rule of Law,
C3.6 Productive and Innovative Capacity and C4.6 Harm Internalization, for the 17 entries that are not configured
economies (nine comprehensive systems, eight mechanisms). Session 65 (part (2.11), Sonnet 5.5) had scored all 51 on a
stated rule without reading their sources: every design "not shown" on each clause, every mechanism "out of reach" on
each, each at 0.5 (`NEEC_Rescoring_s65.md`: "the least-read units in the pass"; open item (a), ledger I6).

- **The designs' own texts were read.** Sixteen passages were cached from the designs' freely published texts (the
  Libertarian Party platform, CCO-PTF-CIP-SZH's research hub, Integral's white paper, participatoryeconomics.info's
  model, Ostrom's Nobel lecture, the Levy Institute's job-guarantee paper, BIEN's definition, *Progress and Poverty*, the
  WEF's stakeholder metrics); the books the other designs rest on are cited by chapter (section 3).
- **Blind against prior: 43 agree, 8 revise, on clause statuses only. No verdict differs**, so nothing is reconciled,
  and every blind reading stands (section 6): the eight prior clauses state the rule, not a source read.
- **Final against prior: no verdict changes.** All 51 stay at 0.5, now on clause readings drawn from the sources. The
  clause changes: Libertarian Minarchism's C2.6 clears consent and the limits of health compulsion (the platform's
  self-ownership, health-care and emergency sections), its clause 1 sitting at the bar (estimate 50 to 56 of 60, flagged
  toward 1.0 as the prior also was); Stakeholder Capitalism's C3.6 clears clauses 1 and 2 on the market economies'
  1999-2019 record; Participatory Economics' C4.6 clears clause 2 (the community of affected parties' compensation
  procedure); Libertarian Minarchism's C4.6 is short on clause 3 (regulation of medicines abolished for voluntary
  certification); four mechanisms move a clause from out of reach to not shown (MMT + Job Guarantee and Universal Basic
  Services on C2.6, Islamic Finance on C3.6, Ostrom-Style Commons Governance on C4.6).
- **No CCO-PTF-CIP-SZH verdict changes** (its three units agree at 0.5).
- **Consequence once applied (S61): none from this group.** With Sessions 71 to 75, Participatory Economics stays
  first alone at 16.5; the tier changes stay Universal Basic Income's and Sovereign Wealth Fund Statism's. **Five flags**,
  two of which would change a tier or first place (section 7): Integral's C2.6 toward 0.0 (to Partially Adequate) and
  Participatory Economics' C2.6 toward 0.0 (first place shared with CCO-PTF-CIP-SZH at 16.0).

## 2. The blind step

The readings were written from `blind_review.blind_view()` (the v2.0 clause text and the cache file names), the
criteria's measurement text, and the sources below, and committed and pushed as checkpoint `600c994` ("NEEC checkpoint
s76: blind readings of C2.6, C3.6 and C4.6 for the 17 designs and mechanisms recorded, before the prior readings are
opened") before part (2.11)'s readings of these units (`rescoring_s65.NEW_UNITS`), Session 65's record, or the units'
published rationales on these criteria were opened. `blind_s76.py` at that commit holds every reading exactly, NEW
unchanged at the session's last commit (`git diff 600c994 -- blind_s76.py` adds the comparison and what follows it,
and the docstring's usage and the checkpoint's closing lines change).

What the session had seen before recording, disclosed so a reader can weigh the blindness:

- **Every prior verdict.** STATE.md, Handoff 75 and `designs_index_s70.json` say that Session 65 scored the 17 at 0.5 on
  a stated rule, so the prior verdict of each of the 51 units was known; their clause statuses were not seen. The index
  also carries Session 70's guesses per unit ("C3.6 and C4.6 clause 2 may be 'not shown'", "likely 'not shown'", "C3.6
  and C4.6 read on the host economy, protocol 3.2", Degrowth's "clauses 1-2 may be 'out of reach' by the design's own
  statement").
- **`rescoring_s65.py`'s structure.** A search for the three criteria's lines, made to find where their units are held,
  printed code lines: the configured economies' units in a loop, Centrally Planned Socialism's `new_unit` calls at 0.0
  on each criterion, the designs' loop at 0.5, and fragments of the notes ("designs and mechanisms are 0.5 on the same
  stated rule as C2.6"). The 0.0s are the configured economies' (ledger S60), not this group's.
- **Three scratch files' rationales on other criteria.** A search of the mechanisms' scratch files printed their v1
  readings of C4.4 (Universal Basic Services, 0.5) and C2.4 (Sovereign Wealth Fund Statism, Mutual Credit, 0.5).
- **The configured economies' productivity.** The Penn World Table file's 1999-2019 changes were computed for all eight
  economies it holds, Norway's and Singapore's falling TFP among them (data of ledger S60's units, not their readings).
- **criteria.json** for the three criteria, printed in full; their anchors carry no examples.

## 3. Sources

Cached (`evidence_cache_s76.py`, each file's md5 in its FILES): for C2.6, `lp_platform_c26_extract.txt`,
`cco_research_hub_c26_extract.txt` (at research-hub commit 8e8a6ba), `integral_wp_v01_c26_extract.txt` (white paper
v0.1, PDF md5 a6defc9a), `pe_model_c26_extract.txt`, `ostrom_nobel_c26_extract.txt`, `levy_jg_wp902_c26_extract.txt`,
`bien_definition_c26_extract.txt`, `george_progress_poverty_c26_extract.txt`; for C3.6, `cco_research_hub_c36_extract.txt`,
`integral_wp_v01_c36_extract.txt`, `pe_model_c36_extract.txt`; for C4.6, `lp_platform_c46_extract.txt`,
`pe_model_c46_extract.txt`, `integral_wp_v01_c46_extract.txt`, `wef_metrics_c46_extract.txt`,
`cco_research_hub_c46_extract.txt`. Session 65's Penn World Table file calibrates reading 3.6.1: output per hour and
TFP rose from 1999 to 2019 in the United States, Denmark, Finland and Sweden (section 5's figure line).

Cited, not cached (`sources_s76.md` in each directory): Roemer (1994) and Schweickart (2011) for Market Socialism;
Nozick (1974) for Libertarian Minarchism; Hickel (2020) and Kallis et al. (2020) for Degrowth; Schwab and Vanham (2021)
and the Davos Manifesto 2020 for Stakeholder Capitalism; Bastani (2019); Albert (2003) and Shalom's parpolity (2005);
Raworth (2017); the IGP's Universal Basic Services proposal (2017); the Government Pension Fund Act and the Council on
Ethics' guidelines; AAOIFI's governance standard and Chapra (1985); Greco (2009) and the LETSystem design manual; Ostrom
(1990). weforum.org, ucl.ac.uk, znetwork.org, lovdata.no and tandfonline.com refused the container (HTTP 403 or 405);
the LETSystem manual's host returned 503 and nbim.no's guideline page 404.

Tooling note: `pdftotext` output is numbered in Python's `splitlines()`, which also breaks at form feeds, so a PDF
passage's line numbers differ from `grep -n`'s; the cache uses Python's numbering throughout.

## 4. Readings

`blind_s76.py`'s docstring states each reading in full. In short:

- **C2.6.** 2.6.1: a design's clause 1 is the fifteen Freedom House civil-liberties questions answered 0-4 from its own
  sources (guarantees, the body that decides disputes between participants and administrators and its independence,
  data limits), cleared only with the estimate's whole range at 53 or more. 2.6.2: a mechanism's clause 1 is out of
  reach (it adds to or takes from the host's liberties; what it adds or takes is recorded). 2.6.3 and 2.6.4: consent and
  the limits of compulsion cleared on stated provisions, or, for compulsion, where none is permitted outside a judicial
  process; a mechanism is within reach only where it delivers medical care, or governs an employment or service whose
  loss could penalise refusal. 2.6.5: the 0.0 band's case.
- **C3.6.** 3.6.1: a design's clauses 1 and 2 are cleared where its investment allocation and reward for improvement
  are a market economy's, unchanged in kind, whose components' record is non-declining (Penn World Table, 1999-2019);
  not shown where it replaces or materially changes them with mechanisms whose record is absent or mixed. 3.6.2: a
  mechanism's clauses 1 and 2 are out of reach unless, generalised, it allocates investment economy-wide. 3.6.3: clause
  3 needs stated hours and a provisioning account on component evidence. 3.6.4: the 0.0 band's case.
- **C4.6.** 4.6.1: a design's projected pollution mortality; a mechanism within reach only where it governs a source of
  the harms counted. 4.6.2: liability to compensate those harmed (tort, or a scheme funded by those who cause the
  harm), enforceable by them and collectively where dispersed; short where liability is limited so a class of harm goes
  uncompensated. 4.6.3: regulators of food, water, air, chemicals and medicines independent of those they regulate;
  short where the design abolishes the regulation. 4.6.4: the 0.0 band's case.

## 5. The readings, and the comparison

### Readings as recorded at the checkpoint

C2.6:

| Unit | Class | Clause statuses | Verdict | Flag |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | design | U U U | 0.5 | — |
| Degrowth Economics | design | U U U | 0.5 | — |
| Doughnut Economics | design | U U U | 0.5 | — |
| Fully Automated Luxury Communism | design | U U U | 0.5 | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | mechanism | R R R | 0.5 | — |
| Integral | design | U U U | 0.5 | toward 0.0 |
| Islamic Finance / Profit-Sharing Banking | mechanism | R R R | 0.5 | — |
| Libertarian Minarchism | design | U C C | 0.5 | toward 1.0 |
| MMT + Job Guarantee | mechanism | R R U | 0.5 | — |
| Market Socialism | design | U U U | 0.5 | — |
| Mutual Credit / LETS | mechanism | R R R | 0.5 | — |
| Ostrom-Style Commons Governance | mechanism | R R R | 0.5 | — |
| Participatory Economics | design | U U U | 0.5 | toward 0.0 |
| Sovereign Wealth Fund Statism | mechanism | R R R | 0.5 | — |
| Stakeholder Capitalism | design | U U U | 0.5 | — |
| Universal Basic Income | mechanism | R R R | 0.5 | — |
| Universal Basic Services | mechanism | R U U | 0.5 | — |

C3.6:

| Unit | Class | Clause statuses | Verdict | Flag |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | design | U U U | 0.5 | — |
| Degrowth Economics | design | U U U | 0.5 | toward 0.0 |
| Doughnut Economics | design | U U U | 0.5 | — |
| Fully Automated Luxury Communism | design | U U U | 0.5 | toward 0.0 |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | mechanism | R R R | 0.5 | — |
| Integral | design | U U U | 0.5 | — |
| Islamic Finance / Profit-Sharing Banking | mechanism | U U R | 0.5 | — |
| Libertarian Minarchism | design | U U U | 0.5 | — |
| MMT + Job Guarantee | mechanism | R R R | 0.5 | — |
| Market Socialism | design | U U U | 0.5 | — |
| Mutual Credit / LETS | mechanism | R R R | 0.5 | — |
| Ostrom-Style Commons Governance | mechanism | R R R | 0.5 | — |
| Participatory Economics | design | U U U | 0.5 | — |
| Sovereign Wealth Fund Statism | mechanism | R R R | 0.5 | — |
| Stakeholder Capitalism | design | C C U | 0.5 | — |
| Universal Basic Income | mechanism | R R R | 0.5 | — |
| Universal Basic Services | mechanism | R R R | 0.5 | — |

C4.6:

| Unit | Class | Clause statuses | Verdict | Flag |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | design | U U U | 0.5 | — |
| Degrowth Economics | design | U U U | 0.5 | — |
| Doughnut Economics | design | U U U | 0.5 | — |
| Fully Automated Luxury Communism | design | U U U | 0.5 | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | mechanism | R R R | 0.5 | — |
| Integral | design | U U U | 0.5 | — |
| Islamic Finance / Profit-Sharing Banking | mechanism | R R R | 0.5 | — |
| Libertarian Minarchism | design | U U S | 0.5 | — |
| MMT + Job Guarantee | mechanism | R R R | 0.5 | — |
| Market Socialism | design | U U U | 0.5 | — |
| Mutual Credit / LETS | mechanism | R R R | 0.5 | — |
| Ostrom-Style Commons Governance | mechanism | U U U | 0.5 | — |
| Participatory Economics | design | U C U | 0.5 | — |
| Sovereign Wealth Fund Statism | mechanism | R R R | 0.5 | — |
| Stakeholder Capitalism | design | U U U | 0.5 | — |
| Universal Basic Income | mechanism | R R R | 0.5 | — |
| Universal Basic Services | mechanism | R R R | 0.5 | — |

### Comparison with part (2.11)'s readings

C2.6:

| Unit | Prior | Blind (Session 76) | Result | Differences |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | U U U / 0.5 | U U U / 0.5 | agree | — |
| Degrowth Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Doughnut Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Fully Automated Luxury Communism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R R / 0.5 | R R R / 0.5 | agree | — |
| Integral | U U U / 0.5 | U U U / 0.5 | agree | — |
| Islamic Finance / Profit-Sharing Banking | R R R / 0.5 | R R R / 0.5 | agree | — |
| Libertarian Minarchism | U U U / 0.5 | U C C / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new); clause 3: U (prior) vs C (new) |
| MMT + Job Guarantee | R R R / 0.5 | R R U / 0.5 | revise (clauses) | clause 3: R (prior) vs U (new) |
| Market Socialism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Mutual Credit / LETS | R R R / 0.5 | R R R / 0.5 | agree | — |
| Ostrom-Style Commons Governance | R R R / 0.5 | R R R / 0.5 | agree | — |
| Participatory Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Sovereign Wealth Fund Statism | R R R / 0.5 | R R R / 0.5 | agree | — |
| Stakeholder Capitalism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Universal Basic Income | R R R / 0.5 | R R R / 0.5 | agree | — |
| Universal Basic Services | R R R / 0.5 | R U U / 0.5 | revise (clauses) | clause 2: R (prior) vs U (new); clause 3: R (prior) vs U (new) |

C3.6:

| Unit | Prior | Blind (Session 76) | Result | Differences |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | U U U / 0.5 | U U U / 0.5 | agree | — |
| Degrowth Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Doughnut Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Fully Automated Luxury Communism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R R / 0.5 | R R R / 0.5 | agree | — |
| Integral | U U U / 0.5 | U U U / 0.5 | agree | — |
| Islamic Finance / Profit-Sharing Banking | R R R / 0.5 | U U R / 0.5 | revise (clauses) | clause 1: R (prior) vs U (new); clause 2: R (prior) vs U (new) |
| Libertarian Minarchism | U U U / 0.5 | U U U / 0.5 | agree | — |
| MMT + Job Guarantee | R R R / 0.5 | R R R / 0.5 | agree | — |
| Market Socialism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Mutual Credit / LETS | R R R / 0.5 | R R R / 0.5 | agree | — |
| Ostrom-Style Commons Governance | R R R / 0.5 | R R R / 0.5 | agree | — |
| Participatory Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Sovereign Wealth Fund Statism | R R R / 0.5 | R R R / 0.5 | agree | — |
| Stakeholder Capitalism | U U U / 0.5 | C C U / 0.5 | revise (clauses) | clause 1: U (prior) vs C (new); clause 2: U (prior) vs C (new) |
| Universal Basic Income | R R R / 0.5 | R R R / 0.5 | agree | — |
| Universal Basic Services | R R R / 0.5 | R R R / 0.5 | agree | — |

C4.6:

| Unit | Prior | Blind (Session 76) | Result | Differences |
|---|---|---|---|---|
| CCO-PTF-CIP-SZH | U U U / 0.5 | U U U / 0.5 | agree | — |
| Degrowth Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Doughnut Economics | U U U / 0.5 | U U U / 0.5 | agree | — |
| Fully Automated Luxury Communism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Georgism / Land Value Tax (LVT + Citizen's Dividend) | R R R / 0.5 | R R R / 0.5 | agree | — |
| Integral | U U U / 0.5 | U U U / 0.5 | agree | — |
| Islamic Finance / Profit-Sharing Banking | R R R / 0.5 | R R R / 0.5 | agree | — |
| Libertarian Minarchism | U U U / 0.5 | U U S / 0.5 | revise (clauses) | clause 3: U (prior) vs S (new) |
| MMT + Job Guarantee | R R R / 0.5 | R R R / 0.5 | agree | — |
| Market Socialism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Mutual Credit / LETS | R R R / 0.5 | R R R / 0.5 | agree | — |
| Ostrom-Style Commons Governance | R R R / 0.5 | U U U / 0.5 | revise (clauses) | clause 1: R (prior) vs U (new); clause 2: R (prior) vs U (new); clause 3: R (prior) vs U (new) |
| Participatory Economics | U U U / 0.5 | U C U / 0.5 | revise (clauses) | clause 2: U (prior) vs C (new) |
| Sovereign Wealth Fund Statism | R R R / 0.5 | R R R / 0.5 | agree | — |
| Stakeholder Capitalism | U U U / 0.5 | U U U / 0.5 | agree | — |
| Universal Basic Income | R R R / 0.5 | R R R / 0.5 | agree | — |
| Universal Basic Services | R R R / 0.5 | R R R / 0.5 | agree | — |

The prior is Session 65's stated rule throughout (designs not shown on each clause, mechanisms out of reach on each, one
flag: Libertarian Minarchism's C2.6 toward 1.0). Every difference is a clause status; no verdict differs.

## 6. The eight clause revisions, and why each stands

No verdict differs, so protocol 5.3 has nothing to reconcile. Under Session 71's rule (`NEEC_BlindReview_s71.md`,
section 6) a blind reading stands unless the prior shows evidence the reading did not weigh, or the reading departs from
its own stated reading; each prior clause below states the rule ("the sources state no ...", "out of reach") without a
source read, so each blind reading stands. The final readings are the blind readings unchanged (`FINAL`).

- **Libertarian Minarchism, C2.6** (clauses 2 and 3, not shown to cleared): the platform's self-ownership (1.1), health
  care (2.13: no mandated treatment or vaccine) and emergency (3.2: no curtailment of rights for war or epidemic)
  sections, with restraint for deliberate endangerment left to criminal trial (1.7). Clause 1 stays not shown: the
  estimate (50 to 56) straddles 53, with labour bargaining (E3), private discrimination (F4) and economic exploitation
  (G4) the weak questions; both readings flag toward 1.0.
- **MMT + Job Guarantee, C2.6** (clause 3, out of reach to not shown): the job is an employment the mechanism governs, so
  whether refusing a health measure could end it is within reach; the sources are silent.
- **Universal Basic Services, C2.6** (clauses 2 and 3, out of reach to not shown): health care is one of its seven
  services, so consent in its delivery and conditions on access are within reach; the proposal is silent.
- **Stakeholder Capitalism, C3.6** (clauses 1 and 2, not shown to cleared): market allocation of investment by private
  capital, unchanged in kind, with output per hour and TFP non-declining over 1999-2019 in the United States, Denmark,
  Finland and Sweden. Clause 3 stays not shown (no stated hours), so the verdict stays 0.5.
- **Islamic Finance, C3.6** (clauses 1 and 2, out of reach to not shown): generalised, profit-and-loss sharing allocates
  all external finance, so the clauses are within reach; no record isolates the mechanism.
- **Libertarian Minarchism, C4.6** (clause 3, not shown to short): licensing is opposed for voluntary certification
  (2.9) and medical products are to be sold "without government restrictions or licenses" (2.13). Clause 2 stays not
  shown: restitution is required where damages "can be proven and quantified in a court of law" (2.2), with no
  collective claim for dispersed harm stated.
- **Ostrom-Style Commons Governance, C4.6** (all three, out of reach to not shown): community water systems and other
  commons lie within its reach, with its own rules, sanctions and monitors (principles 4 to 6); the sources measure no
  mortality effect, describe sanctions rather than compensation, and make the users their own monitors.
- **Participatory Economics, C4.6** (clause 2, not shown to cleared): the community of affected parties sets how much of
  each pollutant may be emitted, the emitter pays the damage price as a cost of production, and the affected are
  credited for the damage they suffer.

## 7. Consequences once applied (not applied here)

This group changes no verdict. The standing on the 29 criteria after the final readings of Sessions 71 to 76 (entries
whose standing differs from the published provisional scores):

| Entry | Total on 29 | After Sessions 71 to 76 | Failures | After | Tier after |
|---|---:|---:|---:|---:|---|
| Nordic Social Democracy | 15.0 | 15.5 | 1 | 0 | Potentially Adequate |
| Centrally Planned Socialism | 7.5 | 6.5 | 15 | 17 | Structurally Inadequate |
| Market Socialism | 14.5 | 15.0 | 2 | 1 | Potentially Adequate |
| Libertarian Minarchism | 8.5 | 9.5 | 13 | 11 | Structurally Inadequate |
| Universal Basic Income | 12.0 | 13.5 | 7 | 5 | Partially Adequate |
| Degrowth Economics | 14.5 | 15.0 | 2 | 1 | Potentially Adequate |
| Stakeholder Capitalism | 10.5 | 11.0 | 8 | 7 | Structurally Inadequate |
| Fully Automated Luxury Communism | 10.5 | 11.0 | 10 | 9 | Structurally Inadequate |
| Participatory Economics | 16.0 | 16.5 | 0 | 0 | Potentially Adequate |
| Doughnut Economics | 10.5 | 9.5 | 8 | 10 | Structurally Inadequate |
| Sovereign Wealth Fund Statism | 14.5 | 15.0 | 3 | 2 | Potentially Adequate |
| State Capitalism / China (Party-State-Directed Market Economy) | 10.5 | 11.0 | 9 | 8 | Structurally Inadequate |
| State Capitalism / Singapore (GLC Developmental Capitalism) | 13.0 | 13.5 | 4 | 3 | Partially Adequate |
| State Capitalism / Qatar (Gulf Rentier-Distributive Statism) | 10.5 | 10.0 | 9 | 10 | Structurally Inadequate |
| Islamic Finance / Profit-Sharing Banking | 13.0 | 14.0 | 5 | 3 | Partially Adequate |

First place: Participatory Economics alone at 16.5. Tier changes: Universal Basic Income from Structurally to Partially
Adequate (ledger D57, confirmed); Sovereign Wealth Fund Statism from Partially to Potentially Adequate (ledger D56,
confirmed).

The final readings' five flags, each taken alone on all six groups' final verdicts:

| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |
|---|---|---:|---:|---:|---:|---|---|
| Integral | C2.6 | 0.5 | 0.0 | 15.0 | 3 | Partially Adequate | tier: Potentially Adequate to Partially Adequate |
| Libertarian Minarchism | C2.6 | 0.5 | 1.0 | 10.0 | 11 | Structurally Inadequate | — |
| Participatory Economics | C2.6 | 0.5 | 0.0 | 16.0 | 1 | Potentially Adequate | first place: shared |
| Degrowth Economics | C3.6 | 0.5 | 0.0 | 14.5 | 2 | Potentially Adequate | — |
| Fully Automated Luxury Communism | C3.6 | 0.5 | 0.0 | 10.5 | 10 | Structurally Inadequate | — |

Two would change a tier or first place: **Integral's C2.6 toward 0.0** (disputes over the contribution assessments that
set access to goods stay with the assessing node, with no appeal beyond it) would take Integral to Partially Adequate;
**Participatory Economics' C2.6 toward 0.0** (consumption rights set by co-workers' effort ratings, grievances heard
inside the council) would bring it to 16.0, sharing first place with CCO-PTF-CIP-SZH. Both rest on the 0.0 band's
"subordinates ... due process ... to its allocation or administration with no independent adjudication"; both designs
leave their participants the host's courts, state non-punitive or council grievance procedures, and do not exclude
independent review, which is why the reading is 0.5. The Report should state both flags beside first place.

## 8. Anchors

The three criteria's anchors carry no examples (v2.0 added them, class N). This group does not propose any: no unit is at
1.0 or 0.0, and a 0.5 example from a stated-rule pass would teach the rule rather than a reading.

## 9. Decisions (Session 76)

- **76.1** (the owner's answer, recorded) ledger D57 confirmed in the ledger on 18 October 2026: Session 75's six C2.5
  verdict changes are applied at S61 as read, including Universal Basic Income's move to Partially Adequate.
- **76.2** (optional, method) readings 2.6.1 to 2.6.5, 3.6.1 to 3.6.4 and 4.6.1 to 4.6.4 (section 4).
- **76.3** (corrections, no verdict effect) the eight clause revisions of section 6; the 51 final readings are the blind
  readings; no verdict, tier or first place changes.
- **76.4** (optional, tooling) `evidence_cache_s76.py`, `blind_s76.py` and harness v46 (128 checks).

Nothing is added for the owner: no verdict changes, and no CCO-PTF-CIP-SZH unit moves (decisions 57.2, 69.4).

## 10. Observations for later sessions

- Session 65's stated rule held every verdict here: read from their own texts, none of the 17 clears every clause of
  these three criteria and none meets a 0.0 case. The rule did hide the clause readings (eight differ) and one design
  at the bar (Libertarian Minarchism's C2.6).
- Two designs whose allocation runs through peer assessment (Participatory Economics, Integral) sit near the 0.0 band of
  C2.6; their flags are the ones that would move a tier or first place, and the limits page (ledger S44) should name them.
- Session 77 (ledger S60) reads the configured economies' units of these criteria; their prior is in
  `rescoring_s65.NEW_UNITS` too (not in `pass_common`'s merged units), read on Freedom House's 1-7 rating, the WJP's
  sub-factor 6.2 file (`wjp_rol_sf62_2012_2025.csv`) and the WHO files. The consequences code should add
  `blind_s76.FINAL` (no verdict change) to the earlier groups' changes (`blind_s76.earlier_changes()`).
- S61 applies `blind_s76.FINAL` as a part like the others; since these criteria are not in the pass's merged units,
  the generator must place the 51 readings (and Session 77's 18) where `rescoring_s65.NEW_UNITS` feeds the v2 files.

## 11. Model and disclosure

Read on Opus 5.5 at high effort, from the designs' own texts where freely published and from the cited books' arguments
as the scorer knows them where not (each such reading names its chapter; the one clause pair cleared partly on a book,
Stakeholder Capitalism's C3.6 clauses 1 and 2, rests on the book's market allocation and the cached productivity
record). The prior was opened only after checkpoint `600c994`.
