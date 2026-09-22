#!/usr/bin/env python3
"""
d14_landing_s29.py -- NEEC Session 29: the D14 landing, one generator for the eleven scoring documents
=====================================================================================================
Decisions D12 and D14 (protocol 10.3): every scoring document states its comparative claims on the
current canonical corpus, restated in place by generator, never by an appended dated note, and each
document is edited once. This is the one generator of the D14 pass. From the Session 26 texts of the
eleven scoring documents -- pinned, byte-identical copies named *_s26_snapshot.md -- it writes the
documents as restated on the canonical 23-system corpus:

  1. the 75 items the Session 28 claim audit (audit_claims_s28.py) found stale, in error, required by a
     decision (D16, D18(a)) or a pasted script transcript, each restated from the facts the audit asserts
     for it (its "nowspec"), together with one phrase that decision D18(a) also made stale in the
     Singapore document ("the twelve flagged calls") and two sentences that pointed at removed text;
  2. the tier-robustness statements of Islamic finance (F4) and Ostrom-style commons governance (O12,
     and its final assessment), restated on the D13 measure with the enumeration share beside it and the
     reversal of the two entries' order under that share disclosed (protocol 6.4);
  3. decision D21, scores displayed as whole percents (protocol 2.4): every "<total>/26 (<p.p>%)" and the
     percent column of the two generated corpus tables (Islamic finance, Ostrom), each old figure checked
     against its total before it is replaced; enumeration shares keep one decimal;
  4. the Session 28 summary blocks (summary_blocks_s28.json, rendered by neec_entry.render_markdown),
     embedded as each document's last section (protocol 9.1): one per entry, thirteen in the Step 1c
     retrofit document.
Headings marked "[pending renumbering]" are left to Step 5, as the handoff specifies.

METHOD. Each edit names its span by a start anchor and an end anchor. An anchor matches with any run
of whitespace standing for any other, because the documents are hard-wrapped; each anchor must occur
exactly once in its document, the end at or after the start, and the span is replaced whole (an edit
that only inserts repeats its anchor in the replacement). The paragraph an edit lands in is re-wrapped
at 76 columns when it is plain prose (lists, tables, headings and code are left as they are). Every document is built in memory; nothing is written unless every edit applied and every
restated claim -- the phrase the claims verifier asserts for an audit item -- occurs exactly once in its
output document. The claims themselves (the facts behind each phrase) are asserted by
verify_comparative_claims.py, not here.

Usage:   python3 d14_landing_s29.py [INDIR] [OUTDIR]        (defaults: . and out)
Inputs (pinned by MD5): the eleven *_s26_snapshot.md files, summary_blocks_s28.json and neec_entry.py
(which loads the canonical corpus: neec_weighting_robustness_analysis_v2.py and neec_scores.csv).
Writes the eleven documents under their canonical names into OUTDIR. Prints file names only;
deterministic.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
import textwrap

DOCS = {
    "GEO": "NEEC_Georgism_LVT_scoring_scratch.md",
    "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
    "DE": "NEEC_DoughnutEconomics_scoring_scratch.md",
    "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
    "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
    "CN": "NEEC_StateCapitalism_China_scoring_scratch.md",
    "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
    "1C": "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
    "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
    "IF": "NEEC_IslamicFinance_scoring_scratch.md",
    "OS": "NEEC_Ostrom_Commons_scoring_scratch.md",
}
SNAP_MD5 = {"GEO": "56236eb4", "MC": "0cec0f4a", "DE": "a0990bb1", "UBS": "2abab03b", "SWF": "48e78c20",
            "CN": "4c907e60", "SG": "64f7201e", "1C": "aa627d9e", "QA": "08aab121", "IF": "600ab19f",
            "OS": "763fc173"}
BLOCKS = ("summary_blocks_s28.json", "7973e170")
NEEC_ENTRY = ("neec_entry.py", "b9bf5acf")
STEP1C_CODES = ("SQ", "NSD", "CPS", "MS", "LM", "MMT", "UBI", "DG", "SC", "FALC", "PE", "CCO", "INT")


def snapshot(code):
    return DOCS[code][:-3] + "_s26_snapshot.md"


# ------------------------------------------------------------------ the edits
EDITS = []


def E(doc, rids, start, end, new, claims, keep=False, para=False, sub=None):
    """One edit. rids: the audit items it resolves ([] for a consequential edit). start/end: anchors of
    the span to replace with `new`. claims: the phrases, one per rid, the claims verifier asserts.
    keep: the audited phrase stays (a D16 disclosure added beside it). sub: instead of one span, a
    list of (anchor, replacement) pairs, each an anchor replaced by its text."""
    EDITS.append(dict(doc=doc, rids=list(rids), start=start, end=end, new=new, claims=list(claims), keep=keep,
                      para=para, sub=sub))

# ---- GEO: Georgism / Land Value Tax
E("GEO", ["GEO-01", "GEO-02"], "**SCRATCH DRAFT — Step 1b, Session 6.**", "disclosure norms (NEEC_CONTRIBUTING.md §2, Appendix H.6).",
  "**Scoring document — Step 1b; scored in Session 6, natively on the v2 structure; in the canonical corpus "
  "(`neec_scores.csv`) since Session 8.** Follows Appendix H.9's submission template exactly. Scored against the "
  "fully-specified 26-criterion v2 structure (Section 12.3, Appendix H.7v2) rather than the legacy 25-criterion "
  "structure, since this is a new system with no prior C1.2 score to preserve — consistent with the handoff's "
  "explicit instruction that Step 1b systems use the v2 structure directly. Its row was added to `neec_scores.csv` "
  "in Session 8. It has not been independently cross-checked by a second scorer (H.9 Step 6) — flagged as open per "
  "this project's disclosure norms (NEEC_CONTRIBUTING.md §2, Appendix H.6).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 8.", "Its row was added to `neec_scores.csv` in Session 8."],
  para=True)
E("GEO", ["GEO-03"], "**On the canonical CSV.** This evaluation is deliberately", "to add whenever that schema pass happens.",
  "**On the canonical CSV.** This evaluation was added as a row of `neec_scores.csv` in Session 8, after the "
  "schema update Step 1c required (Domain 1 out of 6, Total out of 26). It was held back until then because the "
  "schema of the time assumed the legacy 25-criterion structure, with Domain 1 out of 5, and a partial, single-row "
  "update would have created exactly the kind of schema inconsistency the project's scratch-before-insert discipline "
  "exists to prevent.",
  ["This evaluation was added as a row of `neec_scores.csv` in Session 8, after the schema update Step 1c "
   "required (Domain 1 out of 6, Total out of 26)."], para=True)
E("GEO", ["GEO-13"], "well below the next-lowest current", "25-criterion count).",
  "well below the next-lowest member, Market Socialism (16.5/26, 63%; MMT + Job Guarantee, 64% under the legacy "
  "25-criterion count when this was written, has been Partially Adequate since the Step 1c retrofit).",
  ["well below the next-lowest member, Market Socialism (16.5/26, 63%;"])
E("GEO", ["GEO-15", "GEO-16"], "**Comparison to already-scored systems (qualitative, not a formal", "on raw percentage, and its profile",
  "**Comparison to other systems in the corpus.** On the canonical corpus, Georgism is strictly dominated by one "
  "system, CCO-PTF-CIP-SZH, and dominates none. It scores below every other Potentially Adequate entry (Nordic Social "
  "Democracy, Market Socialism, Degrowth Economics, Participatory Economics and CCO-PTF-CIP-SZH) on raw percentage. "
  "Qualitatively, its profile",
  ["Georgism is strictly dominated by one system, CCO-PTF-CIP-SZH, and dominates none.",
   "It scores below every other Potentially Adequate entry (Nordic Social Democracy, Market Socialism, Degrowth "
   "Economics, Participatory Economics and CCO-PTF-CIP-SZH) on raw percentage."])
E("GEO", ["GEO-17"], "land-valuation mechanism; presented as a close call rather than a", "confidently-resolved one.",
  "land-valuation mechanism; presented as a close call rather than a\nconfidently-resolved one. Under protocol 6.1 "
  "(decision D16) the call is encoded with both alternatives, 0.0 and 1.0, and the tier is not robust to it: at 0.0 "
  "the entry would score 13.0/26 with 3 structural failures (Partially Adequate); at 1.0, 14.0/26 with 2 (Potentially "
  "Adequate, as scored).",
  ["the tier is not robust to it: at 0.0 the entry would score 13.0/26 with 3 structural failures (Partially Adequate)"],
  keep=True)
# ---- MC: Mutual Credit / LETS
E("MC", ["MC-01", "MC-02"], "**SCRATCH DRAFT — Step 1b, Session 7.**", "was left as a scratch draft for one full session before insertion.",
  "**Scoring document — Step 1b; scored in Session 7, natively on the v2 structure; in the canonical corpus "
  "(`neec_scores.csv`) since Session 8.** Follows Appendix H.9's submission template, matching the research depth "
  "and disclosure norms established by the Georgism/LVT evaluation (Session 6). Scored against the fully-specified "
  "26-criterion v2 structure (Section 12.3, Appendix H.7v2). Its row was added to `neec_scores.csv` in Session 8, "
  "and it has been in the Report (System 15) since Report v1.5. It has not been independently cross-checked by a "
  "second scorer (H.9 Step 6) — flagged as open per this project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, "
  "Appendix H.6).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 8.", "Its row was added to `neec_scores.csv` in Session 8,"],
  para=True)
E("MC", ["MC-11"], "— the third system in this corpus's history to", "(which instead landed in Potentially Adequate with only 2).",
  "— the second system in this corpus's history to occupy this tier, after Integral (the first, 3 failures); "
  "Georgism, scored the session before, landed instead in Potentially Adequate with only 2. The tier now has eight "
  "members: MMT + Job Guarantee, Integral, Mutual Credit / LETS, Universal Basic Services, Sovereign Wealth Fund "
  "Statism, State Capitalism / Singapore, Islamic finance and Ostrom-style commons governance.",
  ["the second system in this corpus's history to occupy this tier, after Integral (the first, 3 failures); Georgism, "
   "scored the session before, landed instead in Potentially Adequate with only 2. The tier now has eight members: "
   "MMT + Job Guarantee, Integral, Mutual Credit / LETS, Universal Basic Services, Sovereign Wealth Fund Statism, "
   "State Capitalism / Singapore, Islamic finance and Ostrom-style commons governance."])
E("MC", ["MC-03"], "**On the canonical CSV.** This evaluation is **not** yet added as a row to", "session after scoring.",
  "**On the canonical CSV.** This evaluation was added as a row of `neec_scores.csv` in Session 8. The CSV's schema "
  "had been updated in Session 7 (`criteria_count`, `domain1_max` columns added, per the session 5/6 handoffs' Step "
  "1c preparation) so that a v2-structure row like this one could be added correctly; the row itself was left until "
  "after review, consistent with this project's scratch-before-insert discipline.",
  ["This evaluation was added as a row of `neec_scores.csv` in Session 8."], para=True)
E("MC", ["MC-13", "MC-14"], "This project now has three systems in the", "Adequate).",
  "Three systems in the Partially Adequate tier's near neighborhood are worth considering together, all on the v2 "
  "structure since the Step 1c retrofit: Integral (19.5/26, 75%, 3 failures, Partially Adequate), Georgism "
  "(13.5/26, 52%, 2 failures, Potentially Adequate), and Mutual Credit/LETS (14.5/26, 56%, 3 failures, Partially "
  "Adequate).",
  ["Three systems in the Partially Adequate tier's near neighborhood are worth considering together, all on the v2 "
   "structure since the Step 1c retrofit:", "Integral (19.5/26, 75%, 3 failures, Partially Adequate)"])
E("MC", ["MC-15"], "**Comparison to already-scored systems (qualitative, not a formal", "splits first. Qualitatively:",
  "**Comparison to other systems in the corpus.** On the canonical corpus, Mutual Credit / LETS is strictly "
  "dominated by no entry and dominates none; its total, 14.5/26, ties Universal Basic Income's. Qualitatively:",
  ["Mutual Credit / LETS is strictly dominated by no entry and dominates none; its total, 14.5/26, ties Universal "
   "Basic Income's."])
# ---- DE: Doughnut Economics
E("DE", ["DE-01", "DE-02"], "**SCRATCH DRAFT — Step 1b, Session 14.**", "(`NEEC_CONTRIBUTING.md` §2, Appendix H.6).",
  "**Scoring document — Step 1b; scored in Session 14, natively on the v2 structure; in the canonical corpus "
  "(`neec_scores.csv`) since Session 16.** Follows Appendix H.9's submission template, matching the research depth "
  "and disclosure norms established by the Georgism/LVT (Session 6) and Mutual Credit/LETS (Session 7) evaluations. "
  "Scored against the fully-specified 26-criterion v2 structure (Section 12.3, Appendix H.7v2). Its row was added "
  "to `neec_scores.csv` in Session 16; it is not yet a Part I entry of the Report (the Step 5 revision adds it). It "
  "has not been independently cross-checked by a second scorer (H.9 Step 6) — flagged as open per this project's "
  "disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 16.",
   "Its row was added to `neec_scores.csv` in Session 16; it is not yet a Part I entry of the Report"], para=True)
E("DE", ["DE-03", "DE-04"], "**On the canonical CSV.** This evaluation is deliberately **not** yet added", "ready to add whenever this write-up is reviewed and accepted.",
  "**On the canonical CSV.** This evaluation was added as a row of `neec_scores.csv` in Session 16, after review, "
  "consistent with the scratch-before-insert discipline established for Georgism and Mutual Credit/LETS.",
  ["This evaluation was added as a row of `neec_scores.csv` in Session 16, after review,",
   "consistent with the scratch-before-insert discipline established for Georgism and Mutual Credit/LETS."], para=True)
E("DE", ["DE-05"], "The 26-criterion score vector above was checked programmatically this", "for two things before this document was finalized:",
  "The 26-criterion score vector above was checked programmatically in Session 14, by an ad hoc script "
  "(`verify_doughnut.py`) that is not among the project files, for two things before this document was finalized:",
  ["by an ad hoc script (`verify_doughnut.py`) that is not among the project files,"])
E("DE", ["DE-06"], "When this evaluation is reviewed and folded into the canonical CSV, this", "replacement for that step.",
  "In Session 16 this row was added to `neec_weighting_robustness_analysis_v2.py`'s own `SCORES`/`PUBLISHED` "
  "dictionaries, where `verify_transcription()` re-verifies it, as it does Georgism's and Mutual Credit/LETS's rows. "
  "Because the Session 14 script is not on file, the arithmetic above is also checked from this document's summary "
  "block by `neec_entry.py`, which the harness (`run_all_checks.py`) runs.",
  ["In Session 16 this row was added to `neec_weighting_robustness_analysis_v2.py`'s own `SCORES`/`PUBLISHED` "
   "dictionaries, where `verify_transcription()` re-verifies it,"], para=True)
E("DE", ["DE-07"], "**Comparison to already-scored systems (qualitative, not a formal dominance", "One comparison is worth making explicitly, however, because it",
  "**Comparison to other systems in the corpus.** On the canonical corpus, Doughnut Economics is strictly dominated "
  "by one system, CCO-PTF-CIP-SZH, and dominates none. One further comparison is worth making explicitly, because it",
  ["Doughnut Economics is strictly dominated by one system, CCO-PTF-CIP-SZH, and dominates none."])
# ---- UBS: Universal Basic Services
E("UBS", ["UBS-01", "UBS-02"], "**SCRATCH DRAFT — Step 1b, Session 15.**", "reviewable scratch draft for at least one session before insertion.",
  "**Scoring document — Step 1b; scored in Session 15, natively on the v2 structure; in the canonical corpus "
  "(`neec_scores.csv`) since Session 16.** Follows Appendix H.9's submission template, matching the research depth "
  "and disclosure norms established by the Georgism/LVT (Session 6), Mutual Credit/LETS (Session 7), and Doughnut "
  "Economics (Session 14) evaluations. Scored against the fully-specified 26-criterion v2 structure (Section 12.3, "
  "Appendix H.7v2). Its row was added to `neec_scores.csv` in Session 16; it is not yet a Part I entry of the Report "
  "(the Step 5 revision adds it). It has not been independently cross-checked by a second scorer (H.9 Step 6) — "
  "flagged as open per this project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 16.",
   "Its row was added to `neec_scores.csv` in Session 16; it is not yet a Part I entry of the Report"], para=True)
E("UBS", ["UBS-19"], "among this corpus's targeted-mechanism", "Credit/LETS's own 4.0/5 here.",
  "among the entries of the mechanism scope class, below Islamic finance (4.5/5) and Mutual Credit/LETS and "
  "Ostrom-style commons governance (4.0/5 each), and level with Sovereign Wealth Fund Statism (3.5/5).",
  ["among the entries of the mechanism scope class, below Islamic finance (4.5/5) and Mutual Credit/LETS and "
   "Ostrom-style commons governance (4.0/5 each), and level with Sovereign Wealth Fund Statism (3.5/5)."])
E("UBS", ["UBS-03", "UBS-04"], "**On the canonical CSV.** This evaluation is deliberately **not** yet added", "and ready to add whenever this write-up is reviewed and accepted.",
  "**On the canonical CSV.** This evaluation was added as a row of `neec_scores.csv` in Session 16, after review, "
  "consistent with the scratch-before-insert discipline established for Georgism, Mutual Credit/LETS, and Doughnut "
  "Economics.",
  ["This evaluation was added as a row of `neec_scores.csv` in Session 16, after review,",
   "consistent with the scratch-before-insert discipline established for Georgism, Mutual Credit/LETS, and Doughnut "
   "Economics."], para=True)
E("UBS", ["UBS-26"], "resolving that single\ncall would move UBS", "not merely 13.5",
  "resolving that single call upward would move UBS into Potentially Adequate at 14.0/26 with 2 failures, leaving "
  "its tie with Georgism at 13.5 and tying instead Sovereign Wealth Fund Statism, State Capitalism / Singapore and "
  "Ostrom-style commons governance at 14.0",
  ["would move UBS into Potentially Adequate at 14.0/26 with 2 failures, leaving its tie with Georgism at 13.5 and "
   "tying instead Sovereign Wealth Fund Statism, State Capitalism / Singapore and Ostrom-style commons governance at "
   "14.0"])
E("UBS", ["UBS-07"], "Whether a future\nOstrom-commons or sovereign-wealth-fund-statism evaluation", "these three now-named shapes is worth checking explicitly",
  "Sovereign Wealth Fund Statism (Session 17) and Ostrom-style commons governance (Session 23) have since been "
  "scored, both declaring the mechanism scope class; whether each shares one of these three now-named shapes is "
  "worth checking explicitly",
  ["Sovereign Wealth Fund Statism (Session 17) and Ostrom-style commons governance (Session 23) have since been "
   "scored, both declaring the mechanism scope class;"])
E("UBS", ["UBS-06"], "**Comparison to already-scored systems (qualitative plus three verified", "inserted. Three specific comparisons *were* checked programmatically this\nsession,",
  "**Comparison to other systems in the corpus.** On the canonical corpus, UBS is strictly dominated by one system, "
  "CCO-PTF-CIP-SZH, and dominates none. Three specific comparisons were also checked programmatically in Session "
  "15,",
  ["UBS is strictly dominated by one system, CCO-PTF-CIP-SZH, and dominates none."])
E("UBS", ["UBS-31"], "(both are Partially Adequate, both have their strongest domain in", "both fail the wealth cluster cleanly)",
  "(both are Partially Adequate and both have their strongest domain in Implementation Viability; both fail C1.2a "
  "and C1.5, though Mutual Credit/LETS passes C1.2b, which UBS fails)",
  ["both fail C1.2a and C1.5, though Mutual Credit/LETS passes C1.2b, which UBS fails"])
E("UBS", ["UBS-09"], "session (`verify_ubs.py`, ad hoc, not yet folded", "had in Session 14)",
  "session (`verify_ubs.py`, written in Session 15, before this system entered the canonical CSV; the harness, "
  "`run_all_checks.py`, re-runs it against the 15-system corpus it was written for and compares its output with "
  "`verify_ubs_output.txt`, byte for byte)",
  ["the harness, `run_all_checks.py`, re-runs it against the 15-system corpus it was written for and compares its "
   "output with `verify_ubs_output.txt`, byte for byte"])
E("UBS", ["UBS-08"], "corpus. Full output:\n\n```\nCanonical 15-system corpus", "```\n\n(Doughnut Economics' own dominance-relevant escape from UBS runs via C4.1",
  "corpus. The full output is captured in `verify_ubs_output.txt` and is not reproduced here: it describes the "
  "15-system corpus of Session 15, including a ranking of what it calls the soon-to-be 17-system corpus, and the "
  "corpus now holds 23 systems.\n\n(Doughnut Economics' own dominance-relevant escape from UBS runs via C4.1",
  ["The full output is captured in `verify_ubs_output.txt` and is not reproduced here:"])
E("UBS", [], "alongside the script's own boolean check above,", "alongside the script's own boolean check above,",
  "alongside the script's own boolean check (in that captured output),", [])
E("UBS", ["UBS-10", "UBS-11"], "When this evaluation is reviewed and folded into the canonical CSV, this", "than two separate insertion sessions.",
  "In Session 16 this row was added to `neec_weighting_robustness_analysis_v2.py`'s own `SCORES`/`PUBLISHED` "
  "dictionaries, where `verify_transcription()` re-verifies it, in the same insertion pass as Doughnut Economics' "
  "own vector — as Georgism and Mutual Credit/LETS had been inserted together in Session 8.",
  ["In Session 16 this row was added to `neec_weighting_robustness_analysis_v2.py`'s own `SCORES`/`PUBLISHED` "
   "dictionaries,", "in the same insertion pass as Doughnut Economics' own vector"], para=True)
# ---- SWF: Sovereign Wealth Fund Statism
E("SWF", ["SWF-01", "SWF-02"], "**SCRATCH DRAFT — Step 1b, Session 17.**", "(`NEEC_CONTRIBUTING.md` §2, Appendix H.6).",
  "**Scoring document — Step 1b; scored in Session 17, natively on the v2 structure; in the canonical corpus "
  "(`neec_scores.csv`) since Session 20.** Follows Appendix H.9's submission template exactly. Scored directly "
  "against the fully-specified 26-criterion v2 structure (Section 12.3, Appendix H.7v2), consistent with how "
  "Georgism, Mutual Credit/LETS, Doughnut Economics, and Universal Basic Services were each scored. Its row was "
  "added to `neec_scores.csv` in Session 20; it is not yet a Part I entry of the Report (the Step 5 revision adds "
  "it). It has not been independently cross-checked by a second scorer (H.9 Step 6) — flagged as open per this "
  "project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 20.", "Its row was added to `neec_scores.csv` in Session 20;"],
  para=True)
E("SWF", ["SWF-12"], "matches the established pattern for", "here for the same structural reason).",
  "matches the established pattern for the jurisdiction-layered mechanisms scored before it (Georgism, Mutual "
  "Credit/LETS, Doughnut Economics and UBS all score 1.0 here for the same structural reason); among the entries "
  "scored natively on the v2 structure, Islamic finance and Ostrom-style commons governance score 1.0 here as well.",
  ["among the entries scored natively on the v2 structure, Islamic finance and Ostrom-style commons governance score "
   "1.0 here as well."])
E("SWF", ["SWF-20"], "This is disclosed\nexplicitly rather than left for a reader to work out, per this project's", "own contestable-call practice.",
  "This is disclosed\nexplicitly rather than left for a reader to work out, per this project's\nown contestable-call "
  "practice. Under protocol 6.1 (decision D16), this entry carries four flagged criteria in three independent calls: "
  "C1.2a with C1.5, which tracks it; C4.3 (0.5, encoded with both alternatives, 0.0 and 1.0); and C5.4 (0.5, "
  "alternative 1.0). The tier-neutrality shown above holds for the C1.2a/C1.5 call alone. The joint readings are not "
  "tier-neutral: the joint downward reading (C1.2a, C1.5 and C4.3 at 0.0) gives 12.5/26 with 6 structural failures, "
  "Structurally Inadequate; the joint upward reading (C4.3 and C5.4 at 1.0) gives 15.0/26 with 3, Partially "
  "Adequate as scored.",
  ["the joint downward reading (C1.2a, C1.5 and C4.3 at 0.0) gives 12.5/26 with 6 structural failures, Structurally "
   "Inadequate;"], keep=True)
E("SWF", ["SWF-03", "SWF-04"], "**On the canonical CSV.** Consistent with this project's scratch-before-", "or a single-system pass) takes it up.",
  "**On the canonical CSV.** Consistent with this project's scratch-before-insert discipline, this evaluation was "
  "added as a row of `neec_scores.csv` in a dedicated insertion pass, Session 20, together with State Capitalism / "
  "China and State Capitalism / Singapore.",
  ["this evaluation was added as a row of `neec_scores.csv` in a dedicated insertion pass, Session 20,",
   "together with State Capitalism / China and State Capitalism / Singapore."], para=True)
E("SWF", ["SWF-05"], "**Comparison to already-scored systems (qualitative, not a formal", "this project's own verification discipline).**",
  "**Comparison to other systems in the corpus.** On the canonical corpus, Sovereign Wealth Fund Statism is "
  "strictly dominated by one system, CCO-PTF-CIP-SZH, and dominates none.",
  ["Sovereign Wealth Fund Statism is strictly dominated by one system, CCO-PTF-CIP-SZH, and dominates none."])
E("SWF", ["SWF-21"], "the second-highest\ntotal among the four systems", "without\ntying any of them exactly.",
  "tied second to fourth, with State Capitalism / Singapore and Ostrom-style commons governance, among the ten "
  "entries scored natively on the v2 structure.",
  ["tied second to fourth, with State Capitalism / Singapore and Ostrom-style commons governance, among the ten "
   "entries scored natively on the v2 structure."])
# ---- CN: State Capitalism / China
E("CN", ["CN-01", "CN-02", "CN-03"], "**SCRATCH DRAFT — Step 1b, Session 18 (2026-09-16).**", "`verify_china_output.txt`.",
  "**Scoring document — Step 1b; scored in Session 18 (2026-09-16), natively on the v2 structure; in the canonical "
  "corpus (`neec_scores.csv`) since Session 20.** Follows Appendix H.9's submission template exactly. Scored "
  "directly against the fully specified 26-criterion v2 structure (Section 12.3, Appendix H.7v2), as Georgism, "
  "Mutual Credit/LETS, Doughnut Economics, Universal Basic Services, and Sovereign Wealth Fund Statism were. This is "
  "the first of the three state-capitalism sub-entries specified in Paper Section 8.1 (v1.2 decision). Its row was "
  "added to `neec_scores.csv` in Session 20; it is not yet a Part I entry of the Report (the Step 5 revision adds "
  "it). It has not been independently cross-checked by a second scorer (H.9 Step 6) — flagged as open, per this "
  "project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6). Every arithmetic, transcription and "
  "sensitivity claim below is checked by `verify_china.py`, against the 17-system corpus it was written for (its "
  "output is captured in `verify_china_output.txt`); every comparative claim is checked on the canonical corpus by "
  "`verify_comparative_claims.py` (protocol 8.2).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 20.", "Its row was added to `neec_scores.csv` in Session 20;",
   "every comparative claim is checked on the canonical corpus by `verify_comparative_claims.py` (protocol 8.2)."],
  para=True)
E("CN", ["CN-40"], "Sovereign Wealth Fund Statism's single flagged\ncall was checked", "this evaluation's\ntier depends instead on a *set* of calls.",
  "Sovereign Wealth Fund Statism's C1.2a/C1.5 call was checked to be tier-neutral in both directions, though under "
  "protocol 6.1 (decision D16) that entry carries four flagged criteria in three calls and its joint downward "
  "reading reaches Structurally Inadequate; this evaluation's tier depends on a *set* of calls.",
  ["under protocol 6.1 (decision D16) that entry carries four flagged criteria in three calls and its joint "
   "downward reading reaches Structurally Inadequate;"])
E("CN", ["CN-04", "CN-05", "CN-06"], "**On the canonical CSV.** Consistent with the scratch-before-insert", "scored systems are now outstanding.",
  "**On the canonical CSV.** Consistent with the scratch-before-insert discipline, this evaluation was added to "
  "`neec_scores.csv` in a dedicated insertion pass, Session 20, together with Sovereign Wealth Fund Statism and "
  "State Capitalism / Singapore. The insertion adopted the display name this evaluation proposed, `State Capitalism "
  "/ China (Party-State-Directed Market Economy)`, which follows the existing slash convention (\"Georgism / Land "
  "Value Tax,\" \"Mutual Credit / LETS\") so that the three sibling sub-entries sort together.",
  ["this evaluation was added to `neec_scores.csv` in a dedicated insertion pass, Session 20,",
   "The insertion adopted the display name this evaluation proposed, `State Capitalism / China "
   "(Party-State-Directed Market Economy)`,",
   "together with Sovereign Wealth Fund Statism and State Capitalism / Singapore."], para=True)
E("CN", ["CN-42"], "**Domain 2 (1.0/5) is the second-lowest in the prospective corpus", "ties Status Quo for the lowest.**",
  "**Domain 2 (1.0/5) is tied with State Capitalism / Qatar for the second-lowest in the corpus, above only CPS, "
  "and Domain 4 (0.5/5) is the lowest in the corpus, in a three-way tie with Status Quo and State Capitalism / "
  "Qatar.**",
  ["Domain 2 (1.0/5) is tied with State Capitalism / Qatar for the second-lowest in the corpus, above only CPS, and "
   "Domain 4 (0.5/5) is the lowest in the corpus, in a three-way tie with Status Quo and State Capitalism / Qatar."])
E("CN", ["CN-08", "CN-44"], "**Comparison to the corpus (every formal claim checked by", "system dominates no other.",
  "**Comparison to the corpus (every formal claim checked on the canonical corpus by "
  "`verify_comparative_claims.py`).** Two systems dominate this one, CCO-PTF-CIP-SZH and State Capitalism / "
  "Singapore, and it dominates none.",
  ["Comparison to the corpus (every formal claim checked on the canonical corpus by `verify_comparative_claims.py`).",
   "Two systems dominate this one, CCO-PTF-CIP-SZH and State Capitalism / Singapore, and it dominates none."])
E("CN", ["CN-46"], "In the prospective 19-system corpus it is tied for 16th–18th,", "ahead of only Libertarian Minarchism (8.0/26).",
  "In the 23-system corpus it is tied 19th–21st with Centrally Planned Socialism and Stakeholder Capitalism, ahead "
  "of State Capitalism / Qatar (9.0/26) and Libertarian Minarchism (8.0/26).",
  ["In the 23-system corpus it is tied 19th–21st with Centrally Planned Socialism and Stakeholder Capitalism, ahead "
   "of State Capitalism / Qatar (9.0/26) and Libertarian Minarchism (8.0/26)."])
# ---- SG: State Capitalism / Singapore
E("SG", ["SG-01", "SG-02", "SG-03"], "**SCRATCH DRAFT — Step 1b, Session 19 (2026-09-16).**", "`verify_singapore_output.txt`.",
  "**Scoring document — Step 1b; scored in Session 19 (2026-09-16), natively on the v2 structure; in the canonical "
  "corpus (`neec_scores.csv`) since Session 20.** Follows Appendix H.9's submission template. Scored directly "
  "against the fully specified 26-criterion v2 structure (Section 12.3, Appendix H.7v2), as the five earlier Step 1b "
  "systems and State Capitalism / China were. This is the second of the three state-capitalism sub-entries "
  "specified in Paper Section 8.1 (v1.2 decision). Its row was added to `neec_scores.csv` in Session 20; it is not "
  "yet a Part I entry of the Report (the Step 5 revision adds it). It has not been independently cross-checked by a "
  "second scorer (H.9 Step 6) — flagged as open, per this project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, "
  "Appendix H.6). The arithmetic, transcription and sensitivity claims below were checked by `verify_singapore.py`, "
  "against the 17-system corpus it was written for (its output is captured in `verify_singapore_output.txt`, and "
  "the harness re-runs it on this document as it stood before decision D18(a)); since D18(a), the flag register, "
  "joint readings and scenario are checked from this document's summary block by `neec_entry.py`, and every "
  "comparative claim is checked on the canonical corpus by `verify_comparative_claims.py` (protocol 8.2).",
  ["in the canonical corpus (`neec_scores.csv`) since Session 20.", "Its row was added to `neec_scores.csv` in Session 20;",
   "every comparative claim is checked on the canonical corpus by `verify_comparative_claims.py` (protocol 8.2)."],
  para=True)
E("SG", ["SG-14"], "#### C1.5 Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial) — flagged as contestable",
  "#### C1.5 Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial) — flagged as contestable",
  "#### C1.5 Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial)",
  ["C1.5 Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial)"])
E("SG", ["SG-15"], "**Flagged as contestable (the population-scope decision):** a", "Scores checks this reading jointly with C4.5.",
  "**The population-scope decision is a scenario, not a flag** (protocol 3.4, decision D18(a)): scoring citizens "
  "and permanent residents only would score 1.0 here on the Nordic anchor and raise C4.5 to 0.5, giving 15.0/26 "
  "with 3 failures (Partially Adequate). Summary Scores reports this scenario beside the joint readings.",
  ["scoring citizens and permanent residents only would score 1.0 here on the Nordic anchor and raise C4.5 to 0.5, "
   "giving 15.0/26 with 3 failures (Partially Adequate)."])
E("SG", ["SG-16"], "| C1.5 | 0.5 | 1.0 — citizen-and-PR-only scope", "| Partially Adequate |\n| C2.1 | 0.5 | 0.0 — permit regime",
  "| C2.1 | 0.5 | 0.0 — permit regime", [])
E("SG", ["SG-50"], "**Tier robustness — the weakest in the corpus so far, and in both", "directions.** No single flagged call changes the tier.",
  "**Tier robustness — by the D13 measure (protocol 6.4), the third least tier-robust entry in the corpus, after "
  "Ostrom-style commons governance and Islamic finance, and in both directions.** Its joint readings reach all "
  "three tiers, spanning 5.5 points and 6 structural failures. The secondary statistic, assuming independent calls: "
  "64.1% of the 2,048 combinations of its eleven flagged calls keep the Partially Adequate tier. By that share alone "
  "the order changes: Universal Basic Services and MMT + Job Guarantee (50.0% each) would rank as less tier-robust "
  "than this entry, although their joint readings reach only two tiers. No single flagged call changes the tier.",
  ["by the D13 measure (protocol 6.4), the third least tier-robust entry in the corpus, after Ostrom-style commons "
   "governance and Islamic finance, and in both directions.",
   ])
E("SG", ["SG-17"], "All upward readings together give 16.5/26 with", "2 failures (Potentially Adequate)",
  "All upward readings together give 16.0/26 with 2 failures (Potentially Adequate)",
  ["All upward readings together give 16.0/26 with 2 failures (Potentially Adequate)"])
E("SG", ["SG-04", "SG-05"], "**On the canonical CSV.** Consistent with the scratch-before-insert", "three-system batch that Handoffs 17 and 18 proposed.",
  "**On the canonical CSV.** Consistent with the scratch-before-insert discipline, this evaluation was added to "
  "`neec_scores.csv` in a dedicated insertion pass, Session 20, together with Sovereign Wealth Fund Statism and "
  "State Capitalism / China — the three-system batch that Handoffs 17 and 18 proposed. The insertion adopted the "
  "display name this evaluation proposed, `State Capitalism / Singapore (GLC Developmental Capitalism)`, which "
  "follows the China entry's pattern so that the sibling sub-entries sort together.",
  ["this evaluation was added to `neec_scores.csv` in a dedicated insertion pass, Session 20,",
   "The insertion adopted the display name this evaluation proposed, `State Capitalism / Singapore (GLC "
   "Developmental Capitalism)`,"], para=True)
E("SG", ["SG-52"], "tying Stakeholder Capitalism\n  for third-lowest", "above only China and Status\n  Quo.",
  "tying Stakeholder Capitalism for fourth-lowest in the corpus, above only Status Quo, China and State Capitalism "
  "/ Qatar.",
  ["tying Stakeholder Capitalism for fourth-lowest in the corpus, above only Status Quo, China and State Capitalism "
   "/ Qatar."])
E("SG", ["SG-54"], "Georgism/UBS (same total, different tiers),", "failure counts).",
  "Georgism/UBS/Islamic finance (same total; 2, 3 and 5 failures, in two tiers), China/CPS/Stakeholder Capitalism "
  "(same total, radically different profiles), and Singapore/SWF Statism/Ostrom-style commons governance (same "
  "total and tier; 4, 3 and 4 failures).",
  ["Georgism/UBS/Islamic finance (same total; 2, 3 and 5 failures, in two tiers),",
   "Singapore/SWF Statism/Ostrom-style commons governance (same total and tier; 4, 3 and 4 failures)."])
E("SG", ["SG-58", "SG-59"], "Only CCO-PTF-CIP-SZH dominates this system, and it\n   dominates only China.", "10th–11th with Sovereign Wealth Fund Statism.",
  "Only CCO-PTF-CIP-SZH dominates this system, and it dominates two: China and State Capitalism / Qatar. In the "
  "23-system corpus it is tied 10th–12th with Sovereign Wealth Fund Statism and Ostrom-style commons governance.",
  ["Only CCO-PTF-CIP-SZH dominates this system, and it dominates two: China and State Capitalism / Qatar.",
   "In the 23-system corpus it is tied 10th–12th with Sovereign Wealth Fund Statism and Ostrom-style commons "
   "governance."])
E("SG", ["SG-D18a"], "are the twelve\nflagged calls in Summary Scores", "are the twelve\nflagged calls in Summary Scores",
  "are the eleven flagged calls in Summary Scores",
  ["The clearest candidates for independent disagreement are the eleven flagged calls in Summary Scores"])
# ---- 1C: the Step 1c retrofit (13 systems)
E("1C", ["1C-01"], "**SCRATCH DELIVERABLE — Session 8.**", "**SCRATCH DELIVERABLE — Session 8.**",
  "**Step 1c retrofit deliverable — Session 8; its retrofitted scores have been canonical since Session 8.**",
  ["its retrofitted scores have been canonical since Session 8."])
E("1C", ["1C-02"], "followed by Integral (Paper\nAppendix E, not yet in the Report).", "followed by Integral (Paper\nAppendix E, not yet in the Report).",
  "followed by Integral (Paper Appendix E; Report System 13 since Report v1.6).",
  ["followed by Integral (Paper Appendix E; Report System 13 since Report v1.6)."])
E("1C", ["1C-03"], "### 13. Integral (Paper Appendix E — not yet in the Report)", "### 13. Integral (Paper Appendix E — not yet in the Report)",
  "### 13. Integral (Paper Appendix E — Report System 13 since Report v1.6)",
  ["13. Integral (Paper Appendix E — Report System 13 since Report v1.6)"])
E("1C", ["1C-20", "1C-21"], "**Precisely\nstated: the Partially Adequate tier itself now has three members**", "tier that existed before this session (Integral alone)",
  "**Precisely stated: in Session 8 the Partially Adequate tier had three members** (Mutual Credit/LETS, MMT+JG, "
  "Integral, spanning 56–75%), **with Georgism sitting just below them in percentage while remaining in the better, "
  "Potentially Adequate tier** — it is this adjacency, not co-membership, that makes the four-system table above an "
  "instructive unit. On the canonical corpus the tier has eight members — MMT + Job Guarantee, Integral, Mutual "
  "Credit / LETS, Universal Basic Services, Sovereign Wealth Fund Statism, State Capitalism / Singapore, Islamic "
  "finance and Ostrom-style commons governance — spanning 52% to 75%: a meaningfully richer basis than the "
  "single-member tier that existed before Session 8 (Integral alone)",
  ["Precisely stated: in Session 8 the Partially Adequate tier had three members",
   "On the canonical corpus the tier has eight members — MMT + Job Guarantee, Integral, Mutual Credit / LETS, "
   "Universal Basic Services, Sovereign Wealth Fund Statism, State Capitalism / Singapore, Islamic finance and "
   "Ostrom-style commons governance — spanning 52% to 75%:"])
E("1C", [], "See the ranking table under\nVerification, below.", "See the ranking table under\nVerification, below.",
  "See Verification, below, for where the ranking is printed.", [])
E("1C", ["1C-23"], "Running the full\n15-system pairwise dominance check under the retrofitted structure", "out an accidental Step 1c side-effect before including this observation.",
  None, ["On the canonical 23-system corpus, CCO-PTF-CIP-SZH fails to strictly dominate eleven entries: the eight "
         "named above, Mutual Credit / LETS, Islamic finance and Ostrom-style commons governance."],
  sub=[("Running the full\n15-system pairwise dominance check under the retrofitted structure",
        "Running the pairwise dominance check under the retrofitted structure (in Session 8, on the 15-system corpus)"),
       ("out an accidental Step 1c side-effect before including this observation.",
        "out an accidental Step 1c side-effect before including this observation. On the canonical 23-system corpus, "
        "CCO-PTF-CIP-SZH fails to strictly dominate eleven entries: the eight named above, Mutual Credit / LETS, "
        "Islamic finance and Ostrom-style commons governance.")])
E("1C", ["1C-26"], "**Full 15-system ranking under the retrofitted structure** (equal", "| 15 | Libertarian Minarchism | 8.0/26 | 31% | 15 | Structurally Inadequate |",
  "**Ranking under the retrofitted structure.** `step1c_retrofit.py` prints the ranking of the 13 retrofitted "
  "systems by percentage; its captured output, `step1c_retrofit_output.txt`, is reproduced byte for byte by the "
  "harness (`run_all_checks.py`) and notes that Georgism (52%) and Mutual Credit/LETS (56%), already on the v2 "
  "structure, merge in by eye. The ranking of all 23 systems of the canonical corpus, under equal weighting and the "
  "three alternative schemes of Appendix A.4, is printed by `neec_weighting_robustness_analysis_v2.py` and captured "
  "in `session25_v2script_output.txt`.",
  ["`step1c_retrofit.py` prints the ranking of the 13 retrofitted systems by percentage; its captured output, "
   "`step1c_retrofit_output.txt`, is reproduced byte for byte by the harness"], para=True)
E("1C", ["1C-04"], "- Rewrite the Report's Part I system write-ups (Systems 1–12's own Domain 1", "legacy C1.2/C1.5 text as of this session)",
  "- Rewrite the Report's Part I system write-ups (in Session 8, Systems 1–12's Domain 1 sections still showed the "
  "legacy C1.2/C1.5 text; Report v1.6 carries all 15 of its systems on the 26-criterion structure)",
  ["Report v1.6 carries all 15 of its systems on the 26-criterion structure"])
# ---- IF and OS: tier robustness restated on the D13 measure (protocol 6.4)
E("IF", ["IF-F4"], "Measured by\nthe span of the enumeration, 8.0 points and 10 structural failures, this", "structural failure undisputed).",
  "By the D13 measure (protocol 6.4), which compares entries on their joint readings, this entry is the second "
  "least tier-robust in the corpus: its joint readings reach all three tiers, spanning 5.0 points and 9 structural "
  "failures. It is less tier-robust than State Capitalism / Singapore (three tiers, 5.5 points and 6 failures, from "
  "eleven flags) and more tier-robust than Ostrom-style commons governance (three tiers, 10.0 points and 11 "
  "failures, from twenty flags, with no structural failure undisputed). The secondary statistic, the enumeration's "
  "share of combinations that keep the scored tier (assuming independent calls), orders this entry and Ostrom-style "
  "commons governance the other way: 17.1% of this entry's 65,536 combinations keep the Partially Adequate tier, "
  "against 46.7% of Ostrom's 1,048,576.",
  ["By the D13 measure (protocol 6.4), which compares entries on their joint readings, this entry is the second "
   "least tier-robust in the corpus: its joint readings reach all three tiers, spanning 5.0 points and 9 structural "
   "failures.",
   "It is less tier-robust than State Capitalism / Singapore (three tiers, 5.5 points and 6 failures, from eleven "
   "flags) and more tier-robust than Ostrom-style commons governance (three tiers, 10.0 points and 11 failures, from "
   "twenty flags, with no structural failure undisputed).",
   "17.1% of this entry's 65,536 combinations keep the Partially Adequate tier, against 46.7% of Ostrom's 1,048,576."])
E("OS", ["OS-O12"], "**This entry therefore replaces Islamic finance as the least tier-robust in the", "undisputed where Islamic finance has two.",
  "**By the D13 measure (protocol 6.4), this entry is the least tier-robust in the corpus**: its joint readings "
  "reach all three tiers, spanning 10.0 points and 11 structural failures, against 5.0 points and 9 failures for "
  "Islamic finance, the second least tier-robust, and no failure is undisputed where Islamic finance has two. By the "
  "secondary statistic, the enumeration's share of combinations that keep the scored tier (assuming independent "
  "calls), the order of the two reverses: 46.7% of this entry's 1,048,576 combinations keep the Partially Adequate "
  "tier, against 17.1% of Islamic finance's 65,536.",
  ["By the D13 measure (protocol 6.4), this entry is the least tier-robust in the corpus: its joint readings reach "
   "all three tiers, spanning 10.0 points and 11 structural failures, against 5.0 points and 9 failures for Islamic "
   "finance, the second least tier-robust, and no failure is undisputed where Islamic finance has two.",
   "the order of the two reverses: 46.7% of this entry's 1,048,576 combinations keep the Partially Adequate tier, "
   "against 17.1% of Islamic finance's 65,536."], para=True)
E("OS", ["OS-O12b"], "this is now the least tier-robust entry in the corpus, with all three", "tiers reachable and no undisputed failure,",
  "by the D13 measure this is the least tier-robust entry in the corpus, with all three tiers reachable on its "
  "joint readings and no undisputed failure,",
  ["by the D13 measure this is the least tier-robust entry in the corpus, with all three tiers reachable on its joint "
   "readings and no undisputed failure,"])


# ------------------------------------------------------------------ machinery
def norm(s):
    """As the claims verifier normalises: bold markers removed, whitespace collapsed."""
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()


def anchor(a):
    return re.compile(r"\s+".join(re.escape(t) for t in a.split()))


def find_once(text, a, what):
    hits = list(anchor(a).finditer(text))
    if len(hits) != 1:
        raise ValueError(f"{what}: anchor occurs {len(hits)} times: {a[:60]!r}")
    return hits[0]


def wrap(s):
    return textwrap.fill(s, width=76, break_long_words=False, break_on_hyphens=False)


MAX_SPAN = 5000  # characters: a paragraph, or one pasted script transcript (the longest, about 4,200)


def apply_edit(text, e):
    tag = f"{e['doc']} {','.join(e['rids']) or '(consequential)'}"
    if e["sub"]:
        for a, rep in e["sub"]:
            m = find_once(text, a, tag)
            text = reflow(text[:m.start()] + rep + text[m.end():], m.start())
        return text
    s, t = find_once(text, e["start"], tag), find_once(text, e["end"], tag)
    if t.end() < s.start() or (t.end() - s.start()) > MAX_SPAN:
        raise ValueError(f"{tag}: span {s.start()}..{t.end()} is out of order or too long")
    new = wrap(e["new"]) if e["para"] else e["new"]
    text = text[:s.start()] + new + text[t.end():]
    return text if e["para"] else reflow(text, s.start())


LIST_OR_BLOCK = re.compile(r"^(?:[-*+] |\d+\. |[|#>`\s])")


def reflow(text, pos):
    """Re-wrap, at 76 columns, the paragraph an in-place edit landed in -- if it is plain prose (not a list
    item, table, heading, quotation or code), so that the documents stay hard-wrapped."""
    a = text.rfind("\n\n", 0, pos)
    a = 0 if a < 0 else a + 2
    b = text.find("\n\n", pos)
    b = len(text) if b < 0 else b
    par = text[a:b]
    if LIST_OR_BLOCK.match(par) or "\n|" in par or "```" in par:
        return text
    return text[:a] + wrap(" ".join(par.split())) + text[b:]


# Decision D21: a score's percent is displayed whole (protocol 2.4). 0.5-point totals never fall on .5.
PCT = re.compile(r"(\d+\.\d)/26(\s+)\((\d+\.\d)%\)")
TABLES = {"IF": ("<!-- GENERATED:corpus -->\n", "\n<!-- END GENERATED:corpus -->"),
          "OS": ("<!-- BEGIN GENERATED: corpus-table -->\n", "\n<!-- END GENERATED: corpus-table -->")}


def whole(total):
    return int(round(100.0 * total / 26.0))


def d21(code, text):
    def inline(m):
        t = float(m.group(1))
        if f"{100.0 * t / 26.0:.1f}" != m.group(3):
            raise ValueError(f"{code}: '{m.group(0)}' does not match its total")
        return f"{m.group(1)}/26{m.group(2)}({whole(t)}%)"
    text, n_inline = PCT.subn(inline, text)
    n_rows = 0
    if code in TABLES:
        begin, end = TABLES[code]
        if text.count(begin) != 1 or text.count(end) != 1:
            raise ValueError(f"{code}: corpus table markers missing or repeated")
        a = text.index(begin) + len(begin)
        b = text.index(end)
        rows = text[a:b].split("\n")
        for i, row in enumerate(rows[2:], start=2):
            cells = row.split("|")
            t = float(cells[3])
            if cells[4].strip() != f"{100.0 * t / 26.0:.1f}":
                raise ValueError(f"{code}: table row {i}: percent does not match its total")
            cells[4] = f" {whole(t)} "
            rows[i] = "|".join(cells)
            n_rows += 1
        text = text[:a] + "\n".join(rows) + text[b:]
    return text, n_inline, n_rows


def block_section(code, NE, BL):
    if code == "1C":
        parts = ["## Summary blocks", "",
                 wrap("The machine-readable summaries of the thirteen entries this document retrofits (protocol "
                      "section 9; schema `neec-summary-block/1.0`, `summary_block_schema.json`), one per entry, in "
                      "the order of the canonical corpus. They are generated from the canonical corpus and the "
                      "Session 28 staging (`summary_blocks_s28.json`), not typed, and validated by "
                      "`neec_entry.py`.")]
        for c in STEP1C_CODES:
            parts += ["", f"### {BL[c]['display_name']}", "", NE.render_markdown(BL[c])]
    else:
        parts = ["## Summary block", "",
                 wrap("The machine-readable summary of this entry (protocol section 9; schema "
                      "`neec-summary-block/1.0`, `summary_block_schema.json`). It is generated from the canonical "
                      "corpus and the Session 28 staging (`summary_blocks_s28.json`), not typed, and validated by "
                      "`neec_entry.py`."),
                 "", NE.render_markdown(BL[code])]
    return "\n\n---\n\n" + "\n".join(parts) + "\n"


def pinned(indir, name, md5):
    p = os.path.join(indir, name)
    if not os.path.isfile(p):
        sys.exit(f"ERROR: cannot find {name}")
    raw = open(p, "rb").read()
    got = hashlib.md5(raw).hexdigest()[:8]
    if got != md5:
        sys.exit(f"ERROR: {name} md5 {got}, expected {md5}")
    return raw


def main(argv):
    indir = argv[0] if len(argv) > 0 else "."
    outdir = argv[1] if len(argv) > 1 else "out"
    print("=" * 96)
    print("d14_landing_s29.py -- the D14 landing: eleven scoring documents restated on the canonical corpus")
    print("=" * 96)
    src = {c: pinned(indir, snapshot(c), m).decode("utf-8") for c, m in SNAP_MD5.items()}
    BL = {b["code"]: b for b in json.loads(pinned(indir, *BLOCKS))}
    pinned(indir, *NEEC_ENTRY)
    cwd = os.getcwd()
    os.chdir(indir)
    try:
        spec = importlib.util.spec_from_file_location("neec_entry", NEEC_ENTRY[0])
        NE = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(NE)
    finally:
        os.chdir(cwd)
    print(f"inputs: {len(src)} snapshots (*_s26_snapshot.md), {BLOCKS[0]} (md5 {BLOCKS[1]}), "
          f"{NEEC_ENTRY[0]} (md5 {NEEC_ENTRY[1]})")
    rids = [r for e in EDITS for r in e["rids"]]
    if len(rids) != len(set(rids)):
        sys.exit("ERROR: an item is resolved by more than one edit")
    problems, out, report = [], {}, []
    for code in DOCS:
        text = src[code]
        mine = [e for e in EDITS if e["doc"] == code]
        try:
            for e in mine:
                text = apply_edit(text, e)
            text, n_inline, n_rows = d21(code, text)
        except ValueError as err:
            problems.append(str(err))
            continue
        if "<!-- NEEC-SUMMARY-BLOCK -->" in text:
            problems.append(f"{code}: already carries a summary block")
        text = text.rstrip("\n") + block_section(code, NE, BL)
        flat = norm(text)
        for e in mine:
            for ph in e["claims"]:
                n = flat.count(norm(ph))
                if n != 1:
                    problems.append(f"{code} {','.join(e['rids'])}: restated phrase occurs {n} times: {ph[:60]!r}")
        nblocks = len(NE.blocks_in_markdown(text))
        out[code] = text
        report.append(f"  {code:4s} {DOCS[code]:52s} edits {len(mine):2d} (items {sum(len(e['rids']) for e in mine):2d}); "
                      f"D21 {n_inline} inline, {n_rows} table rows; blocks {nblocks}")
    for line in report:
        print(line)
    if problems:
        print("\nPROBLEMS (nothing written):")
        for p in problems:
            print(f"  - {p}")
        return 1
    audit_items = [r for r in rids if r[:3] not in ("IF-", "OS-") and r != "SG-D18a"]
    print(f"\naudit items resolved: {len(audit_items)}; D13 restatements: "
          f"{sum(1 for r in rids if r[:3] in ('IF-', 'OS-'))}; other D18(a) edits: "
          f"{sum(1 for r in rids if r == 'SG-D18a')}; consequential edits: {sum(1 for e in EDITS if not e['rids'])}")
    os.makedirs(outdir, exist_ok=True)
    for code in DOCS:
        data = out[code].encode("utf-8")
        with open(os.path.join(outdir, DOCS[code]), "wb") as f:
            f.write(data)
        print(f"  wrote {DOCS[code]} (md5 {hashlib.md5(data).hexdigest()[:8]})")
    print("\nALL EDITS APPLIED; every restated phrase occurs exactly once in its document.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
