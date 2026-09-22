#!/usr/bin/env python3
"""
neec_scores_csv_builder_v2.py
===============================
Session 8 rebuild. Two changes from the Session 7 builder:

1. RETROFIT (Step 1c): the 13 systems previously carried on the CSV under
   the legacy 25-criterion structure (criteria_count=25, domain1_max=5.0)
   are updated to the retrofitted 26-criterion structure (criteria_count=26,
   domain1_max=6.0), with new D1/Total/failures/tier values. Every value is
   sourced directly from `neec_weighting_robustness_analysis_v2.py`'s own
   PUBLISHED dict (imported and cross-checked below, exactly as the Session
   7 builder cross-checked against that script's v1 predecessor), and full
   rationale for every changed number lives in the companion document
   `NEEC_Step1c_Retrofit_C1.2ab_C1.5.md`.

   IMPORTANT: this makes the CSV, as of this session, MORE CURRENT than the
   Report's or Paper's own prose for these 13 systems -- Part I of the
   Report (Systems 1-12) and the Paper's Appendix E (Integral) still show
   the legacy, pre-retrofit scores as of this session, and will continue to
   until a future "Step 5 (expanded)" regeneration pass. Every retrofitted
   row's `notes` field says this explicitly. This is a deliberate choice,
   not an oversight: the CSV's own `notes` column exists specifically to
   carry this kind of cross-document-currency caveat (see Georgism's own
   row, added Session 7, which already established the pattern: "NOT
   directly comparable to the 13 rows above without Step 1c's pending
   retrofit").

2. NEW ROW: Mutual Credit/LETS (Session 7's scoring pass), added alongside
   Georgism as a second system natively on the v2 structure.

SESSION 16 UPDATE: two further rows added in a consolidated review/insert
pass -- Doughnut Economics (scored Session 14) and Universal Basic
Services (scored Session 15) -- bringing the builder from 15 to 17
systems. Both are natively on the v2, 26-criterion structure (like
Georgism and Mutual Credit/LETS, neither was ever scored under the legacy
25-criterion structure, so neither has retrofit history). Both rows'
D1-D5/failures/tier values are cross-validated below against
`neec_weighting_robustness_analysis_v2.py`'s own (also Session-16-updated)
PUBLISHED dict, which was itself updated first and independently
re-verified against each system's own scratch document before this
builder was touched (see `verify_new_systems.py`). This mirrors exactly
the Session 8 precedent of inserting two new v2-native systems together
rather than one at a time.

CROSS-VALIDATION: every domain/total figure below (all 17 systems) is
checked programmatically against neec_weighting_robustness_analysis_v2.py's
own PUBLISHED dict before the CSV is written, exactly as the Session 7
builder checked against that script's predecessor.

Run: python3 neec_scores_csv_builder_v2.py
"""
import csv
import importlib.util

# ---------------------------------------------------------------------------
# All 17 systems, now uniformly on the 26-criterion structure.
# Columns: system, D1, D2, D3, D4, D5, failures, adequacy_tier,
#          revision_note, notes
# ---------------------------------------------------------------------------
ALL_SYSTEMS = [
    ("Status Quo Market Capitalism", 2.0, 2.0, 2.0, 0.5, 4.0, 9, "Structurally Inadequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.5 -> C1.2a=0.5, C1.2b=0.0 (Gini 0.85, "
     "H.7v2's own 0.0 anchor case). Legacy C1.5=0.5 carried forward unchanged (60% access "
     "breadth). D1 2.0/5 (42% overall) -> 2.0/6 (40% overall); failures 8->9.",
     "Baseline system. Domain 1 raw sum unchanged by the split (0.5 -> 0.5+0.0); the drop "
     "in overall percentage is purely the denominator growing from 25 to 26. Report Part I "
     "(System 1) still shows the legacy, pre-retrofit C1.2/C1.5 text and 10.5/25 total as "
     "of this session -- see NEEC_Step1c_Retrofit_C1.2ab_C1.5.md for full rationale and the "
     "'Step 5 (expanded)' regeneration this unblocks."),
    ("Nordic Social Democracy", 5.0, 3.5, 3.5, 3.5, 4.0, 2, "Potentially Adequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.5 -> C1.2a=1.0 (inferential -- pension/"
     "homeownership mechanisms read as robust for engaged participants; flagged as the "
     "retrofit's most inferential 1.0), C1.2b=0.5 (Gini 0.65-0.75, meaningful reduction, not "
     "under 0.35). Legacy C1.5=1.0 carried forward unchanged (H.7v2's own worked anchor). "
     "D1 4.0/5 (74% overall) -> 5.0/6 (75% overall); failures 2->2, no tier change.",
     "Now EXACTLY tied with Integral at 19.5/26 (75%) under the retrofit -- both were "
     "already tied at 18.5/25 (74%) pre-retrofit; the tie persists at the percentage level "
     "even though each system's Domain 1 moved independently. Tiers still differ (2 vs 3 "
     "failures) -- see the retrofit document's Part 3 for the full discussion. Report Part I "
     "(System 2) still shows legacy scores as of this session."),
    ("Centrally Planned Socialism", 3.0, 0.5, 2.5, 3.0, 1.0, 12, "Structurally Inadequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.0 -> C1.2a=0.0 (explicit absence, "
     "no named mechanism), C1.2b=0.5 -- FLAGGED CONTESTABLE, revised down from an initial "
     "1.0 read after cross-checking this system's own C4.4 rationale, which documents "
     "nomenklatura 'concentrated economic power' outside formal markets that a narrow "
     "wealth-Gini reading would miss. Legacy C1.5=0.5 -> 0.0 (follows C1.2a=0.0 pattern). "
     "D1 3.0/5 (40% overall) -> 3.0/6 (38% overall); failures 11->12, no tier change.",
     "See NEEC_Step1c_Retrofit_C1.2ab_C1.5.md Part 2.2 for the full nomenklatura-tension "
     "discussion behind the C1.2b=0.5 call. Report Part I (System 3) still shows legacy "
     "scores as of this session."),
    ("Market Socialism", 4.0, 3.5, 3.0, 3.0, 3.0, 2, "Potentially Adequate",
     "RETROFITTED Session 8 (Step 1c): matches Appendix H.8a's own worked-example preview "
     "exactly -- legacy C1.2=1.0 -> C1.2a=1.0 (Mondragon capital accounts), C1.2b=0.5 "
     "('cooperative systems: Gini 0.40-0.50'). Legacy C1.5=0.5 carried forward unchanged "
     "(membership-gated access, pure access-breadth reasoning already). D1 3.5/5 (64% "
     "overall) -> 4.0/6 (63% overall); failures 2->2, no tier change.",
     "The FIRST system this retrofit's own anchors were checked against, via Appendix "
     "H.8a's preview pass (written before this full 13-system retrofit) -- confirmed to "
     "match exactly. Report Part I (System 4) still shows legacy scores as of this session."),
    ("Libertarian Minarchism", 0.0, 3.0, 0.5, 1.5, 3.0, 15, "Structurally Inadequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.0 -> C1.2a=0.0, C1.2b=0.0 ('concentration "
     "accelerates' is the literal opposite of prevention). Legacy C1.5=0.0 carried forward "
     "unchanged. D1 0.0/5 (all zero) -> 0.0/6 (all zero); failures 14->15 (Domain 1 goes "
     "from 5-of-5 zero to 6-of-6 zero), no tier change -- already the corpus's most-failed "
     "system either way.",
     "No raw-sum change in Domain 1 (already fully zero); overall percentage drops purely "
     "from the larger denominator (32%->31%). Report Part I (System 5) still shows legacy "
     "scores as of this session."),
    ("MMT + Job Guarantee", 3.5, 2.5, 3.0, 3.5, 3.0, 3, "Partially Adequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.5 -> C1.2a=0.5 (same traditional-market "
     "mechanism as Status Quo), C1.2b=0.0 -- FLAGGED CONTESTABLE AND CONSEQUENTIAL, this is "
     "the retrofit's ONLY tier-crossing case. Legacy C1.5=1.0 -> 0.5 (the legacy score "
     "conflated universal income/employment access with universal wealth-MECHANISM access; "
     "narrowed and scored more conservatively). D1 4.0/5 (64% overall) -> 3.5/6 (60% "
     "overall); failures 2->3.",
     "TIER CHANGE: Potentially Adequate -> Partially Adequate. See "
     "NEEC_Step1c_Retrofit_C1.2ab_C1.5.md Part 2.1 for the full disclosure, including the "
     "counter-consideration (this system's own C4.4='reduces capital power' could support "
     "a 0.5 read instead, which would keep this system out of the tier change -- flagged "
     "explicitly as the single most consequential close call in the entire retrofit). "
     "Report Part I (System 6) still shows the legacy 16.0/25, Potentially-Adequate figures "
     "as of this session."),
    ("Universal Basic Income", 2.5, 3.0, 3.0, 3.0, 3.0, 7, "Structurally Inadequate",
     "RETROFITTED Session 8 (Step 1c): no raw-sum change -- legacy C1.2=0.0 and C1.5=0.0 "
     "were ALREADY the canonical anchor case this project cites repeatedly (Georgism, "
     "Mutual Credit/LETS both invoke this precedent directly); C1.2a=0.0, C1.2b=0.0 (this "
     "system's own C4.4 rationale: 'Provides income but not economic power... remain "
     "subordinate to capital owners'), C1.5=0.0. D1 2.5/5 (58% overall) -> 2.5/6 (56% "
     "overall); failures 6->7, no tier change.",
     "Now EXACTLY tied with Mutual Credit/LETS at 14.5/26 (56%) -- on opposite sides of the "
     "Structurally-Inadequate/Partially-Adequate boundary (7 failures vs. 3), arguably the "
     "sharpest single illustration in the whole corpus of percentage and failure-count "
     "measuring different things. Report Part I (System 7) still shows legacy scores as of "
     "this session."),
    ("Degrowth Economics", 4.5, 3.5, 4.0, 5.0, 2.0, 2, "Potentially Adequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.5 -> C1.2a=0.5 (Appendix H.7v2's own "
     "explicit worked anchor, written using this exact system's CLT/cooperative language), "
     "C1.2b=1.0 (this system's own C4.4 names an explicit 'wealth caps' mechanism -- clean "
     "structural-cap anchor). Legacy C1.5=0.5 carried forward unchanged. D1 3.5/5 (72% "
     "overall) -> 4.5/6 (73% overall); failures 2->2, no tier change.",
     "One of the retrofit's cleanest upward moves -- C1.2b's full 1.0 reflects a mechanism "
     "(wealth caps) already published elsewhere in this system's own write-up but never "
     "credited under the old, conflated C1.2. Report Part I (System 8) still shows legacy "
     "scores as of this session."),
    ("Stakeholder Capitalism", 2.0, 2.0, 2.5, 1.0, 2.5, 9, "Structurally Inadequate",
     "RETROFITTED Session 8 (Step 1c): no raw-sum change -- legacy C1.2=0.5 -> C1.2a=0.5 "
     "(stock options/profit-sharing, explicitly 'incremental'), C1.2b=0.0 (this system's own "
     "C4.4: 'One-share-one-vote maintains wealth-based power concentration'). Legacy C1.5=0.5 "
     "carried forward unchanged. D1 2.0/5 (40% overall) -> 2.0/6 (38% overall); failures "
     "8->9, no tier change.",
     "Report Part I (System 9) still shows legacy scores as of this session."),
    ("Fully Automated Luxury Communism", 3.0, 3.0, 3.0, 3.5, 0.5, 10, "Structurally Inadequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.5 -> C1.2a=0.0 (no named mechanism of "
     "any kind, unlike Degrowth/ParEcon's identified collective institutions), C1.2b=0.0 "
     "-- REVISED DURING DRAFTING from an initial 0.5 (theoretical 'abundance reduces "
     "concentration-driving scarcity' read) after cross-checking this system's own C4.4, "
     "which is explicit about UNRESOLVED risk of technocratic-elite concentration, not "
     "prevention. Legacy C1.5=0.5 -> 0.0 (follows C1.2a=0.0). D1 4.0/5 (56% overall) -> "
     "3.0/6 (50% overall); failures 7->10, no tier change (already Structurally Inadequate "
     "before and after).",
     "The largest single percentage drop in this retrofit (56%->50%), driven by all three "
     "Domain 1 wealth criteria landing at 0.0 once cross-checked consistently against this "
     "system's own already-published C4.4 finding. Report Part I (System 10) still shows "
     "legacy scores as of this session."),
    ("Participatory Economics", 5.0, 4.0, 4.5, 4.0, 3.0, 1, "Potentially Adequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.5 -> C1.2a=0.5 ('community investment "
     "councils' is a named collective mechanism, matching H.7v2's own Degrowth-anchor logic "
     "for the 0.5 band -- an EARLIER PASS IN THIS RETROFIT initially scored this 0.0 by "
     "analogy to Centrally Planned Socialism's flat absence, then was revised to 0.5 for "
     "consistency with the anchor's own stated distinguishing logic; see the retrofit "
     "document for the full reconsideration), C1.2b=1.0 (this system's own C4.4: 'No "
     "concentrated wealth, no capital owners, no managerial hierarchy'). Legacy C1.5=0.5 "
     "carried forward. D1 4.0/5 (78% overall) -> 5.0/6 (79% overall); failures 1->1, no tier "
     "change.",
     "This system's C1.2a call was the retrofit's most closely re-examined single score, "
     "since an initial 0.0 read would have pushed this system's failure count to 3 and "
     "crossed it into Partially Adequate -- the revision to 0.5 (which this row uses) keeps "
     "it at 1 failure. See NEEC_Step1c_Retrofit_C1.2ab_C1.5.md, System 11 entry, for the "
     "full reasoning. Report Part I (System 11) still shows legacy scores as of this "
     "session."),
    ("CCO-PTF-CIP-SZH", 5.5, 5.0, 5.0, 4.5, 4.5, 0, "Potentially Adequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=1.0 -> C1.2a=1.0 (this system's own text "
     "states the NEEC C1.2a threshold figure verbatim: '$70,000+ over 20 years' -- the "
     "cleanest 1.0 in the corpus), C1.2b=1.0 (this system's own C4.4 states the C1.2b "
     "threshold directly: 'Wealth Gini projected <0.35'). Legacy C1.5=0.5 carried forward "
     "unchanged. D1 4.5/5 (94% overall) -> 5.5/6 (94% overall); failures 0->0, no tier "
     "change.",
     "Author Duke Johnson's own framework -- self-referential-bias concern addressed "
     "directly in Paper Section 10.5 and this project's CONTRIBUTING document. Remains the "
     "corpus's strongest system, essentially unaffected in percentage terms by the retrofit "
     "(94% either way) since both new criteria clear their thresholds as cleanly as the old "
     "single criterion did. Report Part I (System 12) still shows legacy scores as of this "
     "session."),
    ("Integral", 3.0, 4.5, 5.0, 4.5, 2.5, 3, "Partially Adequate",
     "RETROFITTED Session 8 (Step 1c): legacy C1.2=0.0 -> C1.2a=0.0, C1.2b=1.0 (both already "
     "appear as Appendix H.7v2's own worked anchors for this exact system -- 'close to the "
     "strongest possible C1.2b answer in the corpus'). Legacy C1.5=0.0 -> 0.0 (follows "
     "C1.2a=0.0). D1 2.0/5 (74% overall) -> 3.0/6 (75% overall); failures 3->3 (the 0.0/1.0 "
     "split doesn't add a new zero -- Domain 1 keeps exactly the two zeros, C1.2a and C1.5, "
     "it had before), no tier change.",
     "This is the retrofit's cleanest validation of the theoretical motivation Paper "
     "Section 12.1 gave for the whole C1.2a/C1.2b split in the first place: Domain 1 moves "
     "from a weak 40% to a much stronger 50% once C1.2b's genuine strength is no longer "
     "averaged against C1.2a's genuine weakness. Now EXACTLY tied with Nordic Social "
     "Democracy at 19.5/26 (75%) -- both were already tied pre-retrofit too. Not yet in the "
     "Report (still Paper Appendix E only, as before this session)."),
    ("Georgism / Land Value Tax (LVT + Citizen's Dividend)", 2.0, 3.0, 3.0, 2.5, 3.0, 2, "Potentially Adequate",
     "N/A (scored Session 6, natively on the v2, 26-criterion structure -- not part of the "
     "13-system legacy corpus and therefore not touched by Step 1c's retrofit).",
     "Unchanged from the Session 7 CSV row. NOT directly comparable to Systems 1-12/Integral "
     "above without accounting for the fact that those 13 rows are NOW ALSO on the 26-"
     "criterion structure as of this session's Step 1c retrofit -- a real, meaningful "
     "cross-system comparison is possible against this row for the first time (see "
     "neec_weighting_robustness_analysis_v2.py's full ranking output). Both failures "
     "(C1.2a, C1.5) trace to the same finding a classical Citizen's Dividend is an income-"
     "distribution mechanism, not a wealth-building one, mirroring UBI's own precedent. "
     "Lowest percentage score (52%) of any Potentially Adequate system in the corpus as of "
     "this session -- see the retrofit document's Part 3 for the sharpened, now-four-member "
     "version of this finding (Georgism 52%/Potentially Adequate vs. Mutual Credit/LETS "
     "56%/Partially Adequate vs. MMT+JG 60%/Partially Adequate vs. Integral 75%/Partially "
     "Adequate). Report System 13; excluded from Report Part II due to the (now resolved "
     "for Systems 1-12, but not re-applied to Part II's own prose) scale mismatch."),
    ("Mutual Credit / LETS", 2.0, 3.0, 3.0, 2.5, 4.0, 3, "Partially Adequate",
     "N/A (scored Session 7, natively on the v2, 26-criterion structure -- not part of the "
     "13-system legacy corpus and therefore not touched by Step 1c's retrofit).",
     "NEW ROW this session. Both C1.2a and C1.5 failures trace to the same design choice "
     "that produces this system's own strongest score (C1.2b=1.0, prevention of "
     "exploitative accumulation) -- no value-storage function of any kind exists, by "
     "design, which is simultaneously this system's greatest anti-concentration strength "
     "and its clearest material-security weakness. C1.3 (Housing Security) fails outright, "
     "this system's own distinct addition to the corpus pattern (no housing channel "
     "identified at all, unlike Georgism's partial evidence). Lands in Partially Adequate "
     "(3 failures) with a HIGHER percentage (56%) than Georgism's Potentially Adequate "
     "(52%) -- a direct, one-on-one, same-structure tier/percentage crossover. Report "
     "System 14; excluded from Report Part II for the same scale-mismatch reason as "
     "Georgism."),
    # --- Session 16 additions below (inserted together, per the consolidated review/insert
    # pass Session 15's own handoff recommended over adding a third scratch draft) ---
    ("Doughnut Economics", 1.0, 2.0, 3.0, 2.5, 3.0, 8, "Structurally Inadequate",
     "N/A (scored Session 14, natively on the v2, 26-criterion structure -- not part of the "
     "13-system legacy corpus and therefore not touched by Step 1c's retrofit).",
     "NEW ROW Session 16 (scoring itself completed Session 14; scratch-before-insert "
     "discipline held for one intervening session, then this and the UBS row below were "
     "inserted together). Eight structural failures -- the most of any Step 1b system to "
     "date -- nearly all traceable to one root cause stated in the system's own Overview: "
     "Doughnut Economics is explicitly a 'compass, not a map' (Raworth's own framing), "
     "naming the social-foundation and power-distribution problems this framework's "
     "criteria measure with unusual precision while declining to commit to any single "
     "redistributive mechanism of its own for solving them. C1.2a and C1.2b are both "
     "flagged contestable. Strongest domain by far is Ethical Integrity's ecological pair "
     "(C4.1, C4.2 both 1.0) -- the ecological ceiling IS current planetary-boundary "
     "science, anchored by the framework's own October 2025 peer-reviewed Nature update. "
     "C3.4 (Epistemic Adaptability) and C5.3 (Partial/Parallel Deployability) are also "
     "clean Passes. Does NOT formally dominate, and is not dominated by, Degrowth Economics "
     "despite Degrowth's far higher total (19.0 vs. 11.5) -- Doughnut Economics escapes via "
     "C2.5, C5.3, and C5.4, all implementation-viability-side criteria where its voluntary, "
     "piecemeal adoption pattern (50+ jurisdictions, one national government) is a genuine "
     "structural advantage over Degrowth's more totalizing ambition. Report System 16 "
     "[pending renumbering]; not yet in Report Part I or Part II."),
    ("Universal Basic Services", 1.5, 3.0, 3.0, 2.5, 3.5, 3, "Partially Adequate",
     "N/A (scored Session 15, natively on the v2, 26-criterion structure -- not part of the "
     "13-system legacy corpus and therefore not touched by Step 1c's retrofit).",
     "NEW ROW Session 16 (scoring itself completed Session 15; inserted together with the "
     "Doughnut Economics row above in this session's consolidated pass). Lands at an EXACT "
     "score tie with Georgism / Land Value Tax -- 13.5/26 to the tenth of a point, "
     "independently verified by this session's own script (see verify_ubs.py) -- differing "
     "on only two of 26 criteria (Georgism ahead via C1.2b's land-rent-capture mechanism; "
     "UBS ahead via C5.1's broader, more diverse proven-component base), confirmed "
     "non-dominated in either direction, and landing in a DIFFERENT adequacy tier despite "
     "the exact tie (Georgism: 2 failures, Potentially Adequate; UBS: 3 failures, Partially "
     "Adequate) -- arguably the cleanest illustration in the corpus to date of the tier-vs-"
     "percentage design distinction, since it is an exact tie rather than mere proximity. "
     "C1.2b was revised during drafting from an initial 0.5 to a final 0.0, disclosed "
     "explicitly rather than silently resolved: providing a new free service (the shelter "
     "sector's zero-rent housing) is not the same kind of mechanism as capturing an "
     "existing wealth stream the way Georgism's land value tax does. This system's own "
     "write-up names a third corpus-wide structural archetype -- a 'federation of committed "
     "mechanisms,' comprehensive in scope like Doughnut Economics but mechanism-bearing in "
     "every sector like Georgism or Mutual Credit/LETS, rather than merely mechanism-citing. "
     "Strongest domain is Implementation Viability (3.5/5, 70%) on the strength of an "
     "unusually broad, independently-proven, multi-sector component base (health, "
     "education, housing, childcare, transport each separately proven somewhere in the "
     "world). Report System 17 [pending renumbering]; not yet in Report Part I or Part II."),
]

# ---------------------------------------------------------------------------
# Cross-validation against neec_weighting_robustness_analysis_v2.py's own
# PUBLISHED dict.
# ---------------------------------------------------------------------------
spec = importlib.util.spec_from_file_location("v2script", "neec_weighting_robustness_analysis_v2.py")
v2script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2script)

PUBLISHED = v2script.PUBLISHED
mismatches = []
csv_names_to_published = {
    "Status Quo Market Capitalism": "Status Quo Market Capitalism",
    "Nordic Social Democracy": "Nordic Social Democracy",
    "Centrally Planned Socialism": "Centrally Planned Socialism",
    "Market Socialism": "Market Socialism",
    "Libertarian Minarchism": "Libertarian Minarchism",
    "MMT + Job Guarantee": "MMT + Job Guarantee",
    "Universal Basic Income": "Universal Basic Income",
    "Degrowth Economics": "Degrowth Economics",
    "Stakeholder Capitalism": "Stakeholder Capitalism",
    "Fully Automated Luxury Communism": "Fully Automated Luxury Communism",
    "Participatory Economics": "Participatory Economics",
    "CCO-PTF-CIP-SZH": "CCO-PTF-CIP-SZH",
    "Integral": "Integral",
    "Georgism / Land Value Tax (LVT + Citizen's Dividend)": "Georgism / Land Value Tax",
    "Mutual Credit / LETS": "Mutual Credit / LETS",
    "Doughnut Economics": "Doughnut Economics",
    "Universal Basic Services": "Universal Basic Services",
}

for row in ALL_SYSTEMS:
    name, d1, d2, d3, d4, d5 = row[0], row[1], row[2], row[3], row[4], row[5]
    pub_name = csv_names_to_published[name]
    if pub_name not in PUBLISHED:
        mismatches.append(f"{name}: not found in v2 script's PUBLISHED dict")
        continue
    pub = PUBLISHED[pub_name]
    total = round(d1 + d2 + d3 + d4 + d5, 4)
    for label, mine, theirs in [("D1", d1, pub["D1"]), ("D2", d2, pub["D2"]), ("D3", d3, pub["D3"]),
                                 ("D4", d4, pub["D4"]), ("D5", d5, pub["D5"]), ("Total", total, pub["Total"])]:
        if abs(mine - theirs) > 1e-9:
            mismatches.append(f"{name} {label}: CSV builder has {mine}, v2 script has {theirs}")
    # also cross-check failure count against the script's own criterion vectors
    failure_count_script = sum(1 for c in v2script.ALL_CRITS if v2script.SCORES[pub_name][c] == 0.0)
    if failure_count_script != row[6]:
        mismatches.append(f"{name}: CSV builder failures={row[6]}, script computes {failure_count_script}")

if mismatches:
    print("MISMATCHES FOUND -- fix before writing CSV:")
    for m in mismatches:
        print("  " + m)
    raise SystemExit(1)
else:
    print(f"Cross-validation PASSED: all {len(ALL_SYSTEMS)} systems' D1-D5/Total/failures match "
          f"neec_weighting_robustness_analysis_v2.py's independently-maintained PUBLISHED dict "
          f"and SCORES vectors exactly.")

# ---------------------------------------------------------------------------
# Write out the CSV
# ---------------------------------------------------------------------------
HEADER = ["system", "criteria_count", "domain1_max", "domain1_material_security",
          "domain2_human_autonomy", "domain3_system_resilience", "domain4_ethical_integrity",
          "domain5_implementation_viability", "total_score", "total_percent", "failures",
          "adequacy_tier", "revision_note", "notes"]

rows_out = []
for row in ALL_SYSTEMS:
    name, d1, d2, d3, d4, d5, failures, tier, revnote, notes = row
    total = round(d1 + d2 + d3 + d4 + d5, 4)
    pct = f"{round(total/26*100)}%"
    rows_out.append([name, 26, 6.0, d1, d2, d3, d4, d5, total, pct, failures, tier, revnote, notes])

with open("neec_scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    writer.writerows(rows_out)

print(f"\nWrote neec_scores.csv: {len(rows_out)} rows, all on the uniform 26-criterion "
      f"structure, {len(HEADER)} columns.")
print("Schema change this session: 'corrected_in_v1_1' column renamed 'revision_note' to "
      "reflect that it now also carries Step 1c retrofit provenance, not just the v1.1 "
      "arithmetic-audit history. All prior row content preserved in spirit; see individual "
      "notes fields for the full old-v1.1-audit-history text where applicable (unchanged) "
      "vs. new Step-1c-retrofit text (new this session).")
print("\nSession 16: Doughnut Economics and Universal Basic Services added (rows 16-17), "
      "bringing the canonical CSV from 15 to 17 systems. Report and Paper regeneration to "
      "fold both into Part I/II and Appendix B/Section 11 remains separately queued, per "
      "this project's established precedent of treating CSV insertion and Report/Paper "
      "regeneration as distinct passes (Georgism/Mutual Credit/LETS: Session 8 insertion, "
      "Sessions 9-10 regeneration).")
