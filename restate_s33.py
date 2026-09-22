#!/usr/bin/env python3
"""
restate_s33.py -- NEEC Session 33: decisions D18(b) and D26, restated in place
==============================================================================
The first blind replication (pilot 1, NEEC_OstromCommons_replication_record.md) decided D18(b) and raised
D26; the project owner confirmed both in Session 33.

  D18(b)  Ostrom-style commons governance's register is re-expressed by the stated scope-or-doubt test
          (record 10.1): the four flags whose alternative readings are scope questions (C1.3, C3.1, C3.5,
          C4.2) leave the register and are reported as scenarios (land trusts counted out; thresholds read
          against the governed resource); the two borderline flags (C4.3, C5.2) stay. The joint readings
          become the register's extremes (decision D16's default). No score changes.
  D26     C3.2's 0.0 band is reserved for an active inflationary mechanism (record 10.2). The entry's
          C3.2 moves from 0.0 to 0.5 (14.5/26, 3 failures, Partially Adequate) and its C3.2 flag lapses.
          insert_session33.py applies the score to the canonical scripts; this generator restates the
          documents on the Session 33 corpus.

Seven documents change, each from its Session 32 snapshot (pinned by MD5):
  OS   the four scope sections, the C3.2 section, the headings, the summary table, the flagged calls,
       the joint readings, the scope scenarios, the archetype note, the corpus position, the final
       assessment, the reviewer disclosure, and the summary block (built by d18b_reexpression_s32.py's
       own reexpress(), then D26, exactly as that script's section [7] computes it)
  QA   the upward extreme no longer ties Ostrom            IF   ties, flag counts, D13, share, corpus table
  MC   register item MC-15 (its ties)                     UBS  register item UBS-26 (the 14.0 tie)
  SWF  register item SWF-21 (native rank)                 SG   items SG-54 and SG-59; the share passage
The Step 1c retrofit document is unchanged: item 1C-22 states a pair tie that still holds, and the
Session 33 claims verifier checks it on a re-specified fact list (RESPEC below).

Edits use the D14 generator's own edit function (d14_landing_s29.apply_edit, pinned by MD5): anchors
match across any run of whitespace, exactly once, and the paragraph an edit lands in is re-wrapped at 76
columns. The three long OS sections are replaced between exact markers. Generated tables (the corpus
tables, Ostrom's summary table) are rendered from the Session 33 corpus and the new block; the summary
table's renderer is first checked to reproduce the Session 32 table from the Session 32 block, byte for
byte. Every figure in the new text is asserted against a fresh computation before anything is written.
The claims verifier (Session 33) reads EDITS, SUPERSEDED, NOWSPEC and RESPEC from this file, pinned by
MD5, and asserts the facts.

Usage:   python3 restate_s33.py [INDIR] [OUTDIR]        (defaults: . and out)
Prints file names only; deterministic.
"""
import contextlib
import copy
import hashlib
import importlib.util
import io
import itertools
import os
import sys

DOCS = {
    "OS": "NEEC_Ostrom_Commons_scoring_scratch.md",
    "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
    "IF": "NEEC_IslamicFinance_scoring_scratch.md",
    "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
    "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
    "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
    "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
}
SNAP_MD5 = {"OS": "f280ec44", "QA": "931c2695", "IF": "9643d46d", "MC": "477390c5", "UBS": "895705a2",
            "SWF": "70287ebd", "SG": "d6ad5591"}
D14_GEN = ("d14_landing_s29.py", "6ed2d55c")
D18B = ("d18b_reexpression_s32.py", "8dc8da77")
NEEC_ENTRY = ("neec_entry.py", "6ddd3b0a")
CANON = ("neec_weighting_robustness_analysis_v2.py", "e82ba335")   # the Session 33 corpus (insert_session33.py)


def snapshot(code):
    return DOCS[code][:-3] + "_s32_snapshot.md"


EDITS = []


def E(doc, rids, new_or_sub, claims, start=None, end=None, para=False):
    """One edit for d14_landing_s29.apply_edit: a list of (anchor, replacement) pairs (sub), or a span."""
    if isinstance(new_or_sub, list):
        EDITS.append(dict(doc=doc, rids=list(rids), start=None, end=None, new=None, claims=list(claims),
                          keep=False, para=False, sub=new_or_sub))
    else:
        EDITS.append(dict(doc=doc, rids=list(rids), start=start, end=end, new=new_or_sub, claims=list(claims),
                          keep=False, para=para, sub=None))


# ---------------------------------------------------------------- Ostrom-style commons governance (D18(b), D26)
FLAG = " — flagged as contestable"
E("OS", ["OS-D18b-heads"], [
    ("#### C1.3 Housing Security: 0.5 (Partial)" + FLAG, "#### C1.3 Housing Security: 0.5 (Partial)"),
    ("#### C3.1 Crisis Response Capacity: 0.5 (Partial)" + FLAG, "#### C3.1 Crisis Response Capacity: 0.5 (Partial)"),
    ("#### C3.5 Failure-Mode Transparency: 0.5 (Partial)" + FLAG, "#### C3.5 Failure-Mode Transparency: 0.5 (Partial)"),
    ("#### C4.2 Ecological Compliance: 0.5 (Partial)" + FLAG, "#### C4.2 Ecological Compliance: 0.5 (Partial)")],
  ["#### C1.3 Housing Security: 0.5 (Partial)", "#### C3.1 Crisis Response Capacity: 0.5 (Partial)",
   "#### C3.5 Failure-Mode Transparency: 0.5 (Partial)", "#### C4.2 Ecological Compliance: 0.5 (Partial)"])
E("OS", ["OS-D26-head"], [
    ("#### C3.2 Inflation Control Mechanisms: 0.0 (Structural Failure)" + FLAG,
     "#### C3.2 Inflation Control Mechanisms: 0.5 (Partial)")],
  ["#### C3.2 Inflation Control Mechanisms: 0.5 (Partial)"])
SCOPE_NOTE = "is reported as a scenario below rather than carried as a contestable call."
E("OS", ["OS-D18b-C1.3"], [(
    "**Alternative if resolved the other way: 0.0** — on the reading that community land trusts are an "
    "application of the governance form to land rather than part of the scored mechanism, which is the basis on "
    "which Mutual Credit / LETS and Sovereign Wealth Fund Statism scored 0.0 here.",
    "**Scope scenario, not a flag (decision D18(b)):** on the reading that community land trusts are an "
    "application of the governance form to land rather than part of the scored mechanism, which is the basis on "
    "which Mutual Credit / LETS and Sovereign Wealth Fund Statism scored 0.0 here, C1.3 falls to 0.0. That "
    "reading counts an adjacent instrument out of the mechanism's boundary, so it " + SCOPE_NOTE)],
  ["That reading counts an adjacent instrument out of the mechanism's boundary, so it " + SCOPE_NOTE])
E("OS", ["OS-D18b-C3.1"], [(
    "**Score: 0.5. Alternative if resolved the other way: 1.0** — on the reading that the coverage clause "
    "should be read against the population the institution governs rather than the national population.",
    "**Score: 0.5. Scope scenario, not a flag (decision D18(b)):** on the reading that the coverage clause "
    "should be read against the population the institution governs rather than the national population, C3.1 "
    "rises to 1.0. That reading applies the threshold to a population other than the one the declared population "
    "rule fixes, so it " + SCOPE_NOTE)],
  ["That reading applies the threshold to a population other than the one the declared population rule fixes, "
   "so it " + SCOPE_NOTE])
E("OS", ["OS-D18b-C3.5"], [(
    "**Score: 0.5. Alternative if resolved the other way: 1.0** — on the strength of the monitoring and "
    "sanctioning apparatus, reading externalisation against the governed resource rather than against the wider "
    "economy.",
    "**Score: 0.5. Scope scenario, not a flag (decision D18(b)):** on the strength of the monitoring and "
    "sanctioning apparatus, reading externalisation against the governed resource rather than against the wider "
    "economy, C3.5 rises to 1.0. The apparatus alone does not carry the fourth clause, so the reading turns on "
    "the frame, and it " + SCOPE_NOTE)],
  ["The apparatus alone does not carry the fourth clause, so the reading turns on the frame, and it " + SCOPE_NOTE])
E("OS", ["OS-D18b-C4.2"], [(
    "**Score: 0.5. Alternative if resolved the other way: 1.0** — on the reading that extraction at or below "
    "regeneration, achieved repeatedly across resource types and continents, is what ecological compliance means "
    "for a resource-governance mechanism.",
    "**Score: 0.5. Scope scenario, not a flag (decision D18(b)):** on the reading that extraction at or below "
    "regeneration, achieved repeatedly across resource types and continents, is what ecological compliance means "
    "for a resource-governance mechanism, C4.2 rises to 1.0. That reading applies the criterion in the mechanism's "
    "own frame rather than the economy-wide one, so it " + SCOPE_NOTE)],
  ["That reading applies the criterion in the mechanism's own frame rather than the economy-wide one, so it "
   + SCOPE_NOTE])
E("OS", ["OS-D26-C3.2"], [
    ("This is the one criterion on which it scores below every other system in the corpus, all 22 of which reach "
     "at least 0.5, and the reason is simple absence rather than malfunction.",
     "The reason is simple absence rather than malfunction."),
    ("**Score: 0.0. Alternative if resolved the other way: 0.5** — on the reading that non-market access to fuel, "
     "fodder, water and food insulates members from price shocks in precisely those goods, which is a real "
     "household-level hedge even though it is not a price-level instrument.",
     "**Score: 0.5 (decision D26, Session 33).** C3.2's 0.0 band is reserved for an active inflationary mechanism "
     "with no counterbalancing element, not for inflation left unaddressed. Session 23 scored this entry 0.0 on "
     "absence alone, the corpus's only 0.0 here; with 0.0 no longer open to it, it scores 0.5, the alternative "
     "the Session 23 text offered, and the call is no longer flagged. Non-market access to fuel, fodder, water "
     "and food insulates members from price shocks in precisely those goods, which is a real household-level "
     "hedge even though it is not a price-level instrument, and nothing in the evidence reaches 1.0. The blind "
     "replication (pilot 1) scored 0.5 without a flag; its record attributes the difference to the "
     "self-contradiction in the anchor that decision D26 resolves. No entry in the corpus now scores 0.0 on "
     "C3.2.")],
  ["with 0.0 no longer open to it, it scores 0.5, the alternative the Session 23 text offered, and the call is "
   "no longer flagged.", "No entry in the corpus now scores 0.0 on C3.2."])
E("OS", ["OS-D18b-overview"],
  "Session 23 flagged twenty of twenty-six criteria as contestable. That was not twenty independent doubts. It "
  "was very largely **one** doubt, applied twenty times: whether a mechanism that governs a resource should be "
  "read against a criterion that asks about a population. Four of those calls stated that question outright, "
  "and decision D18(b), taken after the first blind replication, reports them as scope scenarios; decision D26 "
  "retired a fifth (C3.2). Fifteen flags remain, still highly non-independent, so the exhaustive enumeration "
  "required since Session 21 is reported *and* the joint readings are reported alongside it. The joint readings "
  "are the informative summary; the enumeration bounds them.",
  ["Four of those calls stated that question outright, and decision D18(b), taken after the first blind "
   "replication, reports them as scope scenarios; decision D26 retired a fifth (C3.2)."],
  start="Twenty of twenty-six criteria are flagged as contestable below.",
  end="The joint readings are the informative summary; the enumeration bounds them.")
E("OS", ["OS-D26-archetype"], [(
    "profile is unlike the others': it has no monetary channel at all (C3.2 = 0.0, the only such score in the "
    "corpus) while having the best-specified failure-detection apparatus (C3.5).",
    "profile is unlike the others': it has no monetary channel at all (C3.2,\n"
    "   where absence now scores 0.5 under decision D26) while having the\n"
    "   best-specified failure-detection apparatus (C3.5).")],
  ["it has no monetary channel at all (C3.2, where absence now scores 0.5 under decision D26)"])
E("OS", ["OS-D26-tie"],
  "**A three-way exact tie at 14.5/26.** Ostrom-style commons governance, Mutual Credit / LETS and Universal "
  "Basic Income all score exactly 14.5/26 (56%), with 3, 3 and 7 structural failures respectively. Like the "
  "three-way tie at 13.5 (Georgism / Land Value Tax, Universal Basic Services and Islamic finance), it spans two "
  "adequacy tiers, so it illustrates the tier-versus-percentage distinction once more: the same total from two "
  "narrow mechanisms that clear the Partially Adequate bar and from an income-transfer design that does not. "
  "Against Mutual Credit / LETS specifically, this entry **differs on 4 of 26 criteria, is higher on 2 and lower "
  "on 2, and nets exactly zero**. Until decision D26 it tied Sovereign Wealth Fund Statism and State Capitalism / "
  "Singapore at 14.0.",
  ["Ostrom-style commons governance, Mutual Credit / LETS and Universal Basic Income all score exactly 14.5/26 "
   "(56%), with 3, 3 and 7 structural failures respectively.",
   "Like the three-way tie at 13.5 (Georgism / Land Value Tax, Universal Basic Services and Islamic finance), it "
   "spans two adequacy tiers",
   "differs on 4 of 26 criteria, is higher on 2 and lower on 2, and nets exactly zero"],
  start="**A three-way exact tie at 14.0/26.**", end="nets exactly zero**.", para=True)
E("OS", ["OS-D26-SQ"], [("is higher on 11 and lower on 4, and gains 3.5 points",
                        "is higher on 11 and lower on 4, and gains 4.0 points")],
  ["it differs on 15 criteria, is higher on 11 and lower on 4, and gains 4.0 points"])
E("OS", ["OS-D26-nearest"], [
    ("each differing from it on only **5 criteria**", "each differing from it on only **4 criteria**"),
    ("Against Georgism it is higher on 3 and lower on 2, and gains 0.5",
     "Against Georgism it is higher on 3 and lower on 1, and gains 1.0")],
  ["Georgism / Land Value Tax is one of the three systems closest to this entry, each differing from it on only 4 "
   "criteria (the others are Mutual Credit / LETS and Universal Basic Services).",
   "Against Georgism it is higher on 3 and lower on 1, and gains 1.0"])
E("OS", ["OS-D26-final"],
  "**Ostrom-style commons governance scores 14.5/26 (56%) with 3 structural failures — Partially Adequate.** "
  "Domain scores are 2.0 / 2.5 / 3.0 / 3.0 / 4.0. It passes six criteria (C2.5, C3.4, C4.1, C5.1, C5.3, C5.5), "
  "records seventeen Partials, and fails C1.2a, C1.5 and C2.2.",
  ["Ostrom-style commons governance scores 14.5/26 (56%) with 3 structural failures — Partially Adequate.",
   "records seventeen Partials, and fails C1.2a, C1.5 and C2.2."],
  start="**Ostrom-style commons governance scores 14.0/26 (54%) with 4 structural", end="and fails C1.2a, C1.5, C2.2 and C3.2.",
  para=True)
E("OS", ["OS-D26-final-shape"], [
    ("and the four failures are all of that kind — no individual accumulating claim, no universal access by design, "
     "no unconditional provision, no monetary function.",
     "and the three failures are all of that kind — no individual accumulating claim, no universal access by design, "
     "no unconditional provision. It has no monetary function either, but under C3.2's anchor absence is not a "
     "structural failure (decision D26).")],
  ["It has no monetary function either, but under C3.2's anchor absence is not a structural failure (decision D26)."])
E("OS", ["OS-D18b-final-readings"], [
    ("and a reader who adopts Reading A or Reading C will get a materially different answer.",
     "and a reader who resolves its calls together, upward or downward, will get a materially different answer, as "
     "will one who counts the knowledge commons in.")],
  ["a reader who resolves its calls together, upward or downward, will get a materially different answer, as will "
   "one who counts the knowledge commons in."])
E("OS", ["OS-disclosure"], [
    ("- **Scored by:** Claude (Anthropic), Session 23, 2026-09-17. **Not yet independently cross-checked by a "
     "second scorer** (H.9 Step 6).",
     "- **Scored by:** Claude (Anthropic), Session 23, 2026-09-17. **Replicated\n"
     "  blind once** (pilot 1, 2026-09-19, Claude Sonnet 5): 22 of 26 criteria\n"
     "  exact, all 26 within one step, the same tier; the four differences are\n"
     "  attributed in `NEEC_OstromCommons_replication_record.md`."),
    ("Session 25, with State Capitalism / Qatar and Islamic finance; the corpus table above is the canonical "
     "23-system corpus.",
     "Session 25, with State Capitalism / Qatar and Islamic finance; the corpus\n"
     "  table above is the canonical 23-system corpus.\n"
     "- **Revised** in Session 33, after that replication: decision D18(b)\n"
     "  re-expressed the register (four scope questions reported as scenarios) and\n"
     "  decision D26 revised C3.2 from 0.0 to 0.5. Both are applied in place by\n"
     "  `restate_s33.py`; the Session 32 text is kept as\n"
     "  `NEEC_Ostrom_Commons_scoring_scratch_s32_snapshot.md`."),
    ("- **Contestable calls:** twenty, listed above with their alternatives; eleven upward and nine downward.",
     "- **Contestable calls:** fifteen, listed above with their alternatives; seven\n  upward and eight downward.")],
  ["Replicated blind once (pilot 1, 2026-09-19, Claude Sonnet 5): 22 of 26 criteria exact, all 26 within one "
   "step, the same tier;",
   "Revised in Session 33, after that replication: decision D18(b) re-expressed the register",
   "Contestable calls: fifteen, listed above with their alternatives; seven upward and eight downward."])
E("OS", ["OS-block-intro"], [(
    "It is generated from the canonical corpus and the Session 28 staging (`summary_blocks_s28.json`), not typed, "
    "and validated by `neec_entry.py`.",
    "It is generated from the canonical corpus and the Session 28 staging (`summary_blocks_s28.json`), "
    "re-expressed by `restate_s33.py` under decisions D18(b) and D26, not typed, and validated by `neec_entry.py`.")],
  ["re-expressed by `restate_s33.py` under decisions D18(b) and D26, not typed,"])

# ---------------------------------------------------------------- the other six documents (D26's consequences)
E("QA", ["QA-D26"], [(
    "The upward extreme reaches the same 14.0/26 as Sovereign Wealth Fund Statism, Singapore, and Ostrom-style "
    "commons governance, in a different tier:",
    "The upward extreme reaches the same 14.0/26 as Sovereign Wealth Fund Statism and Singapore, in a different "
    "tier:")],
  ["The upward extreme reaches the same 14.0/26 as Sovereign Wealth Fund Statism and Singapore, in a different "
   "tier:"])
E("IF", ["IF-D26-broad"], [(
    "The tier does not move, but the total would tie Mutual Credit / LETS and Universal Basic Income.",
    "The tier does not move, but the total would tie Mutual Credit / LETS, Universal Basic Income and Ostrom-style "
    "commons governance.")],
  ["The tier does not move, but the total would tie Mutual Credit / LETS, Universal Basic Income and Ostrom-style "
   "commons governance."])
E("IF", ["IF-D18b-flags"], [(
    "contestable calls, the second-largest set of any entry in the corpus, after Ostrom-style commons governance's "
    "twenty.",
    "contestable calls, the largest set of any entry in the corpus, ahead of Ostrom-style commons governance's "
    "fifteen.")],
  ["This evaluation carries 16 flagged contestable calls, the largest set of any entry in the corpus, ahead of "
   "Ostrom-style commons governance's fifteen."])
E("IF", ["IF-D18b-D13"], [(
    "(three tiers, 10.0 points and 11 failures, from twenty flags, with no structural failure undisputed)",
    "(three tiers, 7.5 points and 9 failures, from fifteen flags, with no structural failure undisputed)")],
  ["and more tier-robust than Ostrom-style commons governance (three tiers, 7.5 points and 9 failures, from "
   "fifteen flags, with no structural failure undisputed)."])
E("IF", ["IF-D18b-share"], [("against 46.7% of Ostrom's 1,048,576.", "against 65.6% of Ostrom's 32,768.")],
  ["17.1% of this entry's 65,536 combinations keep the Partially Adequate tier, against 65.6% of Ostrom's 32,768."])
E("MC", ["MC-15"], [("its total, 14.5/26, ties Universal Basic Income's.",
                     "its total, 14.5/26, ties those of Universal Basic Income and Ostrom-style commons governance.")],
  ["Mutual Credit / LETS is strictly dominated by no entry and dominates none; its total, 14.5/26, ties those of "
   "Universal Basic Income and Ostrom-style commons governance."])
E("UBS", ["UBS-26"], [(
    "tying instead Sovereign Wealth Fund Statism, State Capitalism / Singapore and Ostrom-style commons governance "
    "at 14.0",
    "tying instead Sovereign Wealth Fund Statism and State Capitalism / Singapore at 14.0")],
  ["would move UBS into Potentially Adequate at 14.0/26 with 2 failures, leaving its tie with Georgism at 13.5 and "
   "tying instead Sovereign Wealth Fund Statism and State Capitalism / Singapore at 14.0"])
E("SWF", ["SWF-21"], [(
    "tied second to fourth, with State Capitalism / Singapore and Ostrom-style commons governance, among the ten "
    "entries scored natively on the v2 structure.",
    "tied third and fourth, with State Capitalism / Singapore, among the ten entries scored natively on the v2 "
    "structure, behind Mutual Credit/LETS and Ostrom-style commons governance.")],
  ["tied third and fourth, with State Capitalism / Singapore, among the ten entries scored natively on the v2 "
   "structure, behind Mutual Credit/LETS and Ostrom-style commons governance."])
E("SG", ["SG-54"], [(
    "and Singapore/SWF Statism/Ostrom-style commons governance (same total and tier; 4, 3 and 4 failures).",
    "and Singapore/SWF Statism (same total and tier; 4 and 3 failures).")],
  ["and Singapore/SWF Statism (same total and tier; 4 and 3 failures)."])
E("SG", ["SG-59"], [(
    "In the 23-system corpus it is tied 10th–12th with Sovereign Wealth Fund Statism and Ostrom-style commons "
    "governance.",
    "In the 23-system corpus it is tied 11th–12th with Sovereign Wealth Fund Statism.")],
  ["In the 23-system corpus it is tied 11th–12th with Sovereign Wealth Fund Statism."])
E("SG", ["SG-D26-share"], [(
    "would rank as less tier-robust than this entry, although their joint readings reach only two tiers.",
    "would rank as less tier-robust than this entry, although their joint readings reach only two tiers, and "
    "Ostrom-style commons governance (65.6% of 32,768) as more tier-robust, although its joint readings reach all "
    "three.")],
  ["Universal Basic Services and MMT + Job Guarantee (50.0% each) would rank as less tier-robust than this entry, "
   "although their joint readings reach only two tiers, and Ostrom-style commons governance (65.6% of 32,768) as "
   "more tier-robust, although its joint readings reach all three."])

# Wording this pass removes; the generator asserts it is gone, and the claims verifier asserts it again.
SUPERSEDED = [
    ("OS", "Twenty of twenty-six criteria are flagged — the largest flagged set in the corpus, exceeding Islamic "
           "finance's sixteen."),
    ("OS", "This is the one criterion on which it scores below every other system in the corpus"),
    ("OS", "all score exactly 14.0/26 (54%), with 4, 3 and 4 structural failures respectively."),
    ("OS", "differs on 8 of 26 criteria, is higher on 4 and lower on 4, and nets exactly zero"),
    ("OS", "is higher on 11 and lower on 4, and gains 3.5 points"),
    ("OS", "each differing from it on only 5 criteria"),
    ("OS", "Against Georgism it is higher on 3 and lower on 2, and gains 0.5"),
    ("OS", "spanning 10.0 points and 11 structural failures"),
    ("OS", "46.7% of this entry's 1,048,576 combinations"),
    ("OS", "Reading A"), ("OS", "Reading C"), ("OS", "The three coherent joint readings"),
    ("OS", "C3.2 = 0.0, the only such score in the corpus"),
    ("OS", "The scenario is therefore tier-neutral"),
    ("OS", "Not yet independently cross-checked by a second scorer"),
    ("QA", "Sovereign Wealth Fund Statism, Singapore, and Ostrom-style commons governance, in a different tier"),
    ("IF", "the total would tie Mutual Credit / LETS and Universal Basic Income."),
    ("IF", "after Ostrom-style commons governance's twenty."),
    ("IF", "three tiers, 10.0 points and 11 failures, from twenty flags"),
    ("IF", "against 46.7% of Ostrom's 1,048,576."),
    ("MC", "its total, 14.5/26, ties Universal Basic Income's."),
    ("UBS", "Sovereign Wealth Fund Statism, State Capitalism / Singapore and Ostrom-style commons governance at 14.0"),
    ("SWF", "tied second to fourth, with State Capitalism / Singapore and Ostrom-style commons governance"),
    ("SG", "Singapore/SWF Statism/Ostrom-style commons governance (same total and tier; 4, 3 and 4 failures)."),
    ("SG", "tied 10th–12th with Sovereign Wealth Fund Statism and Ostrom-style commons governance."),
]

# The Session 28 register's facts, re-specified on the Session 33 corpus in the audit's own fact language
# (audit_claims_s28.evaluate). NOWSPEC: the items this pass restates again. RESPEC: 1C-22, kept as written.
NOWSPEC = {
    "MC-15": [("dominators", "MC", []), ("dominated", "MC", []), ("ties", "MC", ["UBI", "OS"])],
    "UBS-26": [("at_total", 14.0, ["SWF", "SG"]), ("total", "GEO", 13.5), ("single", "UBS", "C1.2b", 0.5, (14.0, 2)),
               ("tier_of_failures", 2, "Potentially Adequate")],
    "SWF-21": [("native_rank", "SWF", (3, 4)), ("ties", "SWF", ["SG"])],
    "SG-54": [("ties", "GEO", ["UBS", "IF"]), ("ties", "SG", ["SWF"]), ("failures", "IF", 5)],
    "SG-59": [("rank", "SG", (11, 12)), ("ties", "SG", ["SWF"])],
}
RESPEC = {
    "1C-22": [("total", "UBI", 14.5), ("total", "MC", 14.5), ("failures", "UBI", 7), ("failures", "MC", 3),
              ("tier", "UBI", "Structurally Inadequate"), ("tier", "MC", "Partially Adequate")],
}

# ---------------------------------------------------------------- the three long Ostrom sections
SECTION_START = "### The flagged calls, and what they do to the tier\n"
SECTION_END = "### Archetype — a decision made in the evaluation, as D7 required\n"
P_FLAGS = [
    "**Fifteen of twenty-six criteria are flagged** — the second-largest flagged set in the corpus, after Islamic "
    "finance's sixteen. Session 23 flagged twenty. Decision D18(b), taken after the first blind replication, "
    "reports four of them as scope scenarios, because their alternative readings are scope questions (C1.3, C3.1, "
    "C3.5 and C4.2; see \"The scope scenarios\" below), and decision D26 retired a fifth, C3.2, whose alternative "
    "is now its score. Seven flags would raise the score if resolved the other way and eight would lower it. The "
    "eleven unflagged criteria are **C1.3, C2.1, C2.3, C3.1, C3.2, C3.4, C3.5, C4.2, C5.1, C5.3 and C5.5**.",
    "Resolving each flag independently gives **32,768 combinations**, spanning **10.5 to 18.0 out of 26** and **0 "
    "to 9 structural failures**, and reaching **all three adequacy tiers**: 9.0% of combinations land in Potentially "
    "Adequate, 65.6% in Partially Adequate, and 25.4% in Structurally Inadequate. **No structural failure is "
    "undisputed** — every one of C1.2a, C1.5 and C2.2 has a stated alternative that removes it, which is weaker "
    "than Islamic finance, where two of five failures were undisputed by any flag.",
    "**By the D13 measure (protocol 6.4), this entry is the least tier-robust in the corpus**: its joint readings "
    "reach all three tiers, spanning 7.5 points and 9 structural failures, against 5.0 points and 9 failures for "
    "Islamic finance, the second least tier-robust, and no failure is undisputed where Islamic finance has two. By "
    "the secondary statistic, the enumeration's share of combinations that keep the scored tier (assuming "
    "independent calls), the order of the two reverses: 65.6% of this entry's 32,768 combinations keep the "
    "Partially Adequate tier, against 17.1% of Islamic finance's 65,536.",
]
P_READINGS = [
    "The flags are strongly non-independent — most of them turn on the single scope question set out in the "
    "Overview — so the exhaustive enumeration overstates the real uncertainty by treating fifteen correlated "
    "judgments as fifteen coin flips; the joint readings, not the enumeration, are the informative summary. Session "
    "23 reported three coherent readings: A, the long-enduring case, and C, strict population scope, either side of "
    "the scored reading. Both were named for the scope question itself, so with the scope questions reported as "
    "scenarios (decision D18(b)) the entry takes the two extremes of its register, decision D16's default.",
]
READINGS_TABLE = (
    "| Reading | Total | % | Failures | Tier |\n"
    "|---|---|---|---|---|\n"
    "| Every call resolved upward (seven flags) | 18.0/26 | 69 | 0 | Potentially Adequate |\n"
    "| As scored | 14.5/26 | 56 | 3 | Partially Adequate |\n"
    "| Every call resolved downward (eight flags) | 10.5/26 | 40 | 9 | Structurally Inadequate |")
P_READINGS_AFTER = [
    "The **upward reading produces zero structural failures**, a count that, as scored, only CCO-PTF-CIP-SZH "
    "reaches in the entire corpus. The **spread of 7.5 points and 9 failures, crossing all three tiers**, is what "
    "remains of the selection-and-scope problem once the scope questions are reported separately; Session 23's "
    "spread was 10.0 points and 11 failures. That spread was the strongest evidence yet produced by this project "
    "that the framework needs an explicit **scope-normalisation rule** — a stated convention for how a "
    "mechanism-scope entry is read against population-scope criteria. This evaluation adopts one and states it; "
    "decision D8 makes such a rule part of the scoring protocol (see \"Scope-normalisation rule\" below), and "
    "decision D18(b) separates a scope question from a doubt by a stated test (`NEEC_OstromCommons_replication_record.md`, "
    "section 10.1).",
]
P_SCENARIOS = [
    "Session 23 flagged four calls whose alternative readings are scope questions rather than doubts about the "
    "evidence: each reads a threshold against a population, domain or frame other than the one the declared "
    "population rule fixes, or counts an adjacent instrument in or out of the mechanism's boundary. Decision D18(b), "
    "taken after the first blind replication (`NEEC_OstromCommons_replication_record.md`, section 10.1), reports "
    "them as scenarios, beside the knowledge-commons scenario Session 23 already carried. None is scored.",
]
SCENARIO_TABLE = (
    "| Scenario | Changes | Total | Failures | Tier |\n"
    "|---|---|---|---|---|\n"
    "| Knowledge and digital commons counted in | C1.5 0.0 → 0.5; C2.3 0.5 → 1.0 | 15.5/26 | 2 | Potentially Adequate |\n"
    "| Community land trusts counted out | C1.3 0.5 → 0.0 | 14.0/26 | 4 | Partially Adequate |\n"
    "| Thresholds read against the governed resource and its members | C3.1, C3.5, C4.2 0.5 → 1.0 | 16.0/26 | 3 | "
    "Partially Adequate |")
P_SCENARIOS_AFTER = [
    "Counting the **knowledge and digital commons** in rather than treating it as adjacent changes two criteria: "
    "**C1.5 rises from 0.0 to 0.5**, because a non-rival commons can be open to everyone and so escapes principle "
    "1's boundedness, and **C2.3 rises from 0.5 to 1.0**, because Wikipedia and open-source software are creative "
    "engagement at exactly the scale the threshold describes. The result is **15.5/26 with 2 structural failures — "
    "Potentially Adequate**: tier-neutral when Session 23 scored it, the scenario crosses a tier boundary now that "
    "C3.2 is no longer a failure (decision D26). It is *not* scored, for the reason given in the Overview: the "
    "Governing Knowledge Commons workshop's own position is that the design principles do not transfer "
    "straightforwardly to knowledge resources. A future reviewer who disagrees should change C1.5 and C2.3 and "
    "nothing else.",
    "Counting **community land trusts** out of the mechanism, the reading set out at C1.3, lowers C1.3 to 0.0; "
    "the blind replication carried the same boundary question as a scenario. Reading the coverage, externalisation "
    "and compliance clauses **against the governed resource and its members** rather than the economy-wide "
    "population raises C3.1, C3.5 and C4.2 to 1.0, as set out in those sections. Neither moves the tier.",
]
SECTION_CLAIMS = [
    "Fifteen of twenty-six criteria are flagged — the second-largest flagged set in the corpus, after Islamic "
    "finance's sixteen.",
    "Resolving each flag independently gives 32,768 combinations, spanning 10.5 to 18.0 out of 26 and 0 to 9 "
    "structural failures, and reaching all three adequacy tiers: 9.0% of combinations land in Potentially "
    "Adequate, 65.6% in Partially Adequate, and 25.4% in Structurally Inadequate.",
    "By the D13 measure (protocol 6.4), this entry is the least tier-robust in the corpus: its joint readings "
    "reach all three tiers, spanning 7.5 points and 9 structural failures, against 5.0 points and 9 failures for "
    "Islamic finance, the second least tier-robust, and no failure is undisputed where Islamic finance has two.",
    "the order of the two reverses: 65.6% of this entry's 32,768 combinations keep the Partially Adequate tier, "
    "against 17.1% of Islamic finance's 65,536.",
    "The upward reading produces zero structural failures, a count that, as scored, only CCO-PTF-CIP-SZH reaches "
    "in the entire corpus.",
    "The result is 15.5/26 with 2 structural failures — Potentially Adequate:",
]


def new_section(D14):
    parts = ["### The flagged calls, and what they do to the tier", *[D14.wrap(p) for p in P_FLAGS],
             "### The joint readings", *[D14.wrap(p) for p in P_READINGS], READINGS_TABLE,
             *[D14.wrap(p) for p in P_READINGS_AFTER],
             "### The scope scenarios", *[D14.wrap(p) for p in P_SCENARIOS], SCENARIO_TABLE,
             *[D14.wrap(p) for p in P_SCENARIOS_AFTER]]
    return "\n\n".join(parts) + "\n\n"


# ---------------------------------------------------------------- the block and the generated tables
def os_block(b32, D18B, NE):
    """The Session 33 block: d18b's reexpress() over the scope classes (D18(b)), then D26 as its section [7] does."""
    scope = [c for c, v in D18B.CLASSIFICATION.items() if v[0] in (D18B.POPULATION, D18B.FRAME, D18B.BOUNDARY)]
    new = D18B.reexpress(b32, scope)
    b = copy.deepcopy(new)
    b["vector"]["C3.2"] = 0.5
    b["flags"] = [f for f in new["flags"] if f["criterion"] != "C3.2"]
    res = NE.result(b["vector"])
    b["summary"] = dict({d: sum(b["vector"][c] for c in cs) for d, cs in NE.DOMAINS.items()}, **res)
    up, down = NE.extremes(b)
    b["joint_readings"] = [
        {"id": "scored", "label": "as scored", "basis": "scored", "resolve": {}, "result": res},
        {"id": "up", "label": "every call resolved upward", "basis": "extremes", "resolve": up,
         "result": NE.result(NE.applied(b["vector"], up))},
        {"id": "down", "label": "every call resolved downward", "basis": "extremes", "resolve": down,
         "result": NE.result(NE.applied(b["vector"], down))}]
    b["scenarios"] = [dict(s, result=NE.result(NE.applied(b["vector"], s["changes"]))) for s in new["scenarios"]]
    return b


SUMMARY_BEGIN = "<!-- BEGIN GENERATED: summary-table -->\n"
SUMMARY_END = "\n<!-- END GENERATED: summary-table -->"
RESULT = {0.0: "Structural Failure", 0.5: "Partial", 1.0: "Pass"}
DOMAIN_ROWS = (("D1", "Material Security", "6.0"), ("D2", "Human Autonomy", "5.0"), ("D3", "System Resilience", "5.0"),
               ("D4", "Ethical Integrity", "5.0"), ("D5", "Implementation Viability", "5.0"))


def summary_names(table):
    """(criterion, name) in table order, read from a rendered summary table (flag marks removed)."""
    out = []
    for row in table.split("\n")[2:]:
        if not row.startswith("| C"):
            break
        cells = [c.strip() for c in row.split("|")[1:-1]]
        out.append((cells[0], cells[1].replace(" *(flagged)*", "")))
    return out


def render_summary_table(names, block):
    v, s = block["vector"], block["summary"]
    flagged = {f["criterion"] for f in block["flags"]}
    rows = ["| Criterion | Name | Score | Result |", "|---|---|---|---|"]
    for c, name in names:
        mark = " *(flagged)*" if c in flagged else ""
        rows.append(f"| {c} | {name}{mark} | {v[c]:.1f} | {RESULT[v[c]]} |")
    rows += ["", "| Domain | Score | Max |", "|---|---|---|"]
    rows += [f"| {label} | {s[d]:.1f} | {mx} |" for d, label, mx in DOMAIN_ROWS]
    rows.append(f"| **Total** | **{s['total']:.1f}** | **26.0** |")
    fails = [c for c, _ in names if v[c] == 0.0]
    rows += ["", f"**Total: {s['total']:.1f}/26 ({int(round(100.0 * s['total'] / 26.0))}%). Structural failures: "
                 f"{len(fails)} ({', '.join(fails)}). Tier: {s['tier']}.**"]
    return "\n".join(rows)


def render_corpus(canon, code, name):
    """The corpus table, laid out as the claims verifier renders it (IF: plain ranks; OS: '=' on shared ranks)."""
    S = canon.SCORES
    tot = {k: sum(v.values()) for k, v in S.items()}
    fails = {k: sum(1 for x in v.values() if x == 0.0) for k, v in S.items()}
    out = ["| Rank | System | Score /26 | % | Failures | Tier |", "|---|---|---|---|---|---|"]
    for k in sorted(S, key=lambda k: (-tot[k], k)):
        t, rank = tot[k], 1 + sum(1 for x in tot.values() if x > tot[k])
        label = f"**{k}**" if k == name else k
        eq = "=" if code == "OS" and sum(1 for x in tot.values() if abs(x - t) < 1e-9) > 1 else ""
        out.append(f"| {rank}{eq} | {label} | {t:.1f} | {int(round(100.0 * t / 26.0))} | {fails[k]} | "
                   f"{canon.tier(fails[k])} |")
    return "\n".join(out)


CORPUS_MARKERS = {"IF": ("<!-- GENERATED:corpus -->\n", "\n<!-- END GENERATED:corpus -->",
                         "Islamic Finance / Profit-Sharing Banking"),
                  "OS": ("<!-- BEGIN GENERATED: corpus-table -->\n", "\n<!-- END GENERATED: corpus-table -->",
                         "Ostrom-Style Commons Governance")}


def between(text, begin, end):
    if text.count(begin) != 1 or text.count(end) != 1:
        raise ValueError(f"markers {begin.strip()!r} / {end.strip()!r} missing or repeated")
    a = text.index(begin) + len(begin)
    return a, text.index(end)


# ---------------------------------------------------------------- the figures the new text states
def facts(canon, NE, block):
    S = canon.SCORES
    C = list(canon.ALL_CRITS)
    code = {"OS": "Ostrom-Style Commons Governance", "MC": "Mutual Credit / LETS", "UBI": "Universal Basic Income",
            "GEO": "Georgism / Land Value Tax", "UBS": "Universal Basic Services", "SQ": "Status Quo Market Capitalism"}
    o = S[code["OS"]]
    tot = {k: sum(v.values()) for k, v in S.items()}
    nf = {k: sum(1 for x in v.values() if x == 0.0) for k, v in S.items()}

    def cmp(k):
        b = S[code[k]]
        hi, lo = sum(1 for c in C if o[c] > b[c]), sum(1 for c in C if o[c] < b[c])
        return hi + lo, hi, lo, round(tot[code["OS"]] - tot[code[k]], 1)
    dist = {k: sum(1 for c in C if o[c] != v[c]) for k, v in S.items() if k != code["OS"]}
    tiers = {}
    for combo in itertools.product(*[[f["scored"]] + f["alternatives"] for f in block["flags"]]):
        w = NE.applied(block["vector"], {f["criterion"]: x for f, x in zip(block["flags"], combo)})
        t = NE.result(w)["tier"]
        tiers[t] = tiers.get(t, 0) + 1
    n = sum(tiers.values())
    pct = {t: round(100.0 * c / n, 1) for t, c in tiers.items()}
    jr = {r["id"]: (r["result"]["total"], r["result"]["failures"], r["result"]["tier"]) for r in block["joint_readings"]}
    sc = {s["id"]: (s["result"]["total"], s["result"]["failures"], s["result"]["tier"]) for s in block["scenarios"]}
    up = sum(1 for f in block["flags"] if f["alternatives"][0] > f["scored"])
    return [
        ("Ostrom: 14.5/26, 3 failures, Partially Adequate", (tot[code["OS"]], nf[code["OS"]]) == (14.5, 3)),
        ("no entry at 0.0 on C3.2", all(v["C3.2"] >= 0.5 for v in S.values())),
        ("tie at 14.5: Mutual Credit / LETS and UBI; 3 and 7 failures",
         sorted(k for k in S if k != code["OS"] and tot[k] == 14.5) == [code["MC"], code["UBI"]]
         and (nf[code["MC"]], nf[code["UBI"]]) == (3, 7)),
        ("vs Mutual Credit / LETS: 4 differ, 2 higher, 2 lower, net zero", cmp("MC") == (4, 2, 2, 0.0)),
        ("vs Status Quo: 15 differ, 11 higher, 4 lower, +4.0", cmp("SQ") == (15, 11, 4, 4.0)),
        ("vs Georgism: 3 higher, 1 lower, +1.0", cmp("GEO")[1:] == (3, 1, 1.0)),
        ("nearest neighbours at 4: Georgism, Mutual Credit / LETS, UBS",
         min(dist.values()) == 4 and sorted(k for k, d in dist.items() if d == 4) == sorted(
             [code["GEO"], code["MC"], code["UBS"]])),
        ("fifteen flags, seven upward and eight downward", (len(block["flags"]), up) == (15, 7)),
        ("32,768 combinations: 9.0% / 65.6% / 25.4%",
         n == 32768 and pct == {"Potentially Adequate": 9.0, "Partially Adequate": 65.6, "Structurally Inadequate": 25.4}),
        ("readings: up 18.0/0, scored 14.5/3, down 10.5/9",
         jr == {"scored": (14.5, 3, "Partially Adequate"), "up": (18.0, 0, "Potentially Adequate"),
                "down": (10.5, 9, "Structurally Inadequate")}),
        ("scenarios: knowledge commons 15.5/2 (PA); land trusts out 14.0/4; resource frame 16.0/3",
         sc == {"knowledge-commons": (15.5, 2, "Potentially Adequate"), "land-trusts-out": (14.0, 4, "Partially Adequate"),
                "resource-frame": (16.0, 3, "Partially Adequate")}),
        ("only CCO-PTF-CIP-SZH has zero failures as scored", [k for k in S if nf[k] == 0] == ["CCO-PTF-CIP-SZH"]),
        ("undisputed failures: none (C1.2a, C1.5, C2.2 each flagged)",
         sorted(c for c in C if block["vector"][c] == 0.0) == sorted({f["criterion"] for f in block["flags"]}
                                                                     & {"C1.2a", "C1.5", "C2.2"})),
    ]


# ---------------------------------------------------------------- run
def pinned(indir, name, md5):
    p = os.path.join(indir, name)
    if not os.path.isfile(p):
        sys.exit(f"ERROR: cannot find {name}")
    raw = open(p, "rb").read()
    got = hashlib.md5(raw).hexdigest()[:8]
    if got != md5:
        sys.exit(f"ERROR: {name} md5 {got}, expected {md5}")
    return raw.decode("utf-8")


def load(indir, modname, name, md5):
    pinned(indir, name, md5)
    spec = importlib.util.spec_from_file_location(modname, os.path.join(indir, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def main(argv):
    indir = argv[0] if len(argv) > 0 else "."
    outdir = argv[1] if len(argv) > 1 else "out"
    print("=" * 96)
    print("restate_s33.py -- decisions D18(b) and D26: seven scoring documents restated in place")
    print("=" * 96)
    sys.path.insert(0, os.path.abspath(indir))
    D14 = load(indir, "d14_landing_s29", *D14_GEN)
    NE = load(indir, "neec_entry", *NEEC_ENTRY)
    D18 = load(indir, "d18b_reexpression_s32", *D18B)
    canon = load(indir, "_neec_canon_s33", *CANON)
    text = {k: pinned(indir, snapshot(k), m) for k, m in SNAP_MD5.items()}
    print(f"inputs: the seven Session 32 snapshots; {D14_GEN[0]} (md5 {D14_GEN[1]}), {D18B[0]} (md5 {D18B[1]}), "
          f"{NEEC_ENTRY[0]} (md5 {NEEC_ENTRY[1]}), {CANON[0]} (md5 {CANON[1]}, the Session 33 corpus)")
    problems = []
    # the block, and the figures the new text states
    old_blocks = NE.blocks_in_markdown(text["OS"])
    if len(old_blocks) != 1:
        sys.exit("ERROR: the Ostrom snapshot does not carry exactly one block")
    old_block = old_blocks[0]
    block = os_block(old_block, D18, NE)
    errs = NE.validate(block)
    if errs:
        problems += [f"OS block: {e}" for e in errs]
    if dict(block["vector"]) != dict(canon.SCORES["Ostrom-Style Commons Governance"]):
        problems.append("OS block: the vector is not the Session 33 canonical vector")
    for label, ok in facts(canon, NE, block):
        print(f"  {'PASS' if ok else 'FAIL'}  fact: {label}")
        if not ok:
            problems.append(f"fact does not hold: {label}")
    # the summary table's renderer reproduces the Session 32 table from the Session 32 block
    a, b = between(text["OS"], SUMMARY_BEGIN, SUMMARY_END)
    names = summary_names(text["OS"][a:b])
    if render_summary_table(names, old_block) != text["OS"][a:b]:
        problems.append("OS summary table: the renderer does not reproduce the Session 32 table")
    # the edits
    for e in EDITS:
        try:
            text[e["doc"]] = D14.apply_edit(text[e["doc"]], e)
        except ValueError as err:
            problems.append(str(err))
    t = text["OS"]
    if t.count(SECTION_START) != 1 or t.count(SECTION_END) != 1 or t.index(SECTION_START) > t.index(SECTION_END):
        problems.append("OS: the flagged-calls section markers are missing, repeated or out of order")
    else:
        t = t[:t.index(SECTION_START)] + new_section(D14) + t[t.index(SECTION_END):]
    a, b = between(t, SUMMARY_BEGIN, SUMMARY_END)
    t = t[:a] + render_summary_table(names, block) + t[b:]
    old_md, new_md = NE.render_markdown(old_block), NE.render_markdown(block)
    if t.count(old_md) != 1:
        problems.append("OS: the Session 32 block is not laid out once as neec_entry.render_markdown writes it")
    t = t.replace(old_md, new_md)
    text["OS"] = t
    for code, (begin, end, name) in CORPUS_MARKERS.items():
        a, b = between(text[code], begin, end)
        text[code] = text[code][:a] + render_corpus(canon, code, name) + text[code][b:]
    # every claimed phrase once; every superseded phrase gone; the block closes the document
    flat = {k: D14.norm(v) for k, v in text.items()}
    for e in EDITS:
        for ph in e["claims"]:
            n = flat[e["doc"]].count(D14.norm(ph))
            if n != 1:
                problems.append(f"{e['doc']} {','.join(e['rids'])}: phrase occurs {n} times: {ph[:60]!r}")
    for ph in SECTION_CLAIMS:
        n = flat["OS"].count(D14.norm(ph))
        if n != 1:
            problems.append(f"OS section: phrase occurs {n} times: {ph[:60]!r}")
    for doc, ph in SUPERSEDED:
        if D14.norm(ph) in flat[doc]:
            problems.append(f"{doc}: superseded wording still present: {ph[:60]!r}")
    if not text["OS"].rstrip("\n").endswith(NE.END):
        problems.append("OS: the summary block no longer closes the document")
    if NE.blocks_in_markdown(text["OS"]) != [block]:
        problems.append("OS: the document's block is not the Session 33 block")
    if problems:
        print("\nPROBLEMS (nothing written):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"\n  {len(EDITS)} edits applied, {sum(len(e['claims']) for e in EDITS)} restated phrases each once; "
          f"{len(SECTION_CLAIMS)} phrases in the three rewritten Ostrom sections; {len(SUPERSEDED)} superseded "
          f"phrases gone")
    print(f"  Ostrom's block: {len(block['flags'])} flags, 3 joint readings, {len(block['scenarios'])} scenarios; "
          f"valid under neec_entry.py; its vector is the Session 33 canonical vector")
    print("  generated: Ostrom's summary table (renderer checked on the Session 32 table), the corpus tables of "
          "IF and OS")
    os.makedirs(outdir, exist_ok=True)
    print()
    for k in DOCS:
        data = text[k].encode("utf-8")
        with open(os.path.join(outdir, DOCS[k]), "wb") as f:
            f.write(data)
        print(f"wrote {DOCS[k]} (md5 {hashlib.md5(data).hexdigest()[:8]})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
