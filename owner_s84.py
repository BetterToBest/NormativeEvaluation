#!/usr/bin/env python3
"""
owner_s84.py -- NEEC: the owner's items applied and two consistency gaps closed (Session 84, ledger S68)
====================================================================================================
Session 83's adjudication of the outside review put four readings to the owner (adjudicate_s83.OWNER) and found two gaps it
could not close within its scope. The owner answered in the ledger (2026-10-20): D66, return Degrowth's and Participatory
Economics' C3.4 to 0.5; D67, apply CCO-PTF-CIP-SZH's C2.2 and C5.3 at 0.5 (superseding D65's hold under decision 69.4). This
file holds the layer that applies them, over the adjudicated state (final_pass.settled_state(); apply_owner_s84.py writes the
v2 files from it). Record: NEEC_OwnerItems_s84.md.

  OWNER      the four owner items, each applied as the adjudication reads it (adjudicate_s83.OWNER's unit, unchanged);
             decision 84.1 (D66) and 84.2 (D67).
  REVISIONS  CCO-PTF-CIP-SZH's C3.4: clauses 1 and 3 rested on "as audited (the unit's own text)", the footing rule 3 of
             decision 83.4 rejected for Degrowth and Participatory Economics. Each is re-read on the design's own documents
             (the Research Hub at 8e8a6ba, cached in outside_kit_sources/); the verdict holds (decision 84.3). Decision 79.3
             governs clause 4 only, which is carried.
  UNITS      Participatory Economics' C1.2b, read by rule 4 of decision 83.4 (one reading per class; ledger I12 item 1):
             decision 84.4.

No main; nothing is printed. Deterministic.
"""

TAG = "owner s84"
SESSION = 84
RECORD = "NEEC_OwnerItems_s84.md"
DATE = "2026-10-21"
LABEL = "the owner's items and the consistency gaps of Session 84"

HUB = "the Research Hub at 8e8a6ba"

# the owner's answers (ledger, 2026-10-20): the adjudication's reading of each cell is applied unchanged
OWNER = {
    ("DG", "C3.4"): dict(decision="84.1", ledger="D66"),
    ("PE", "C3.4"): dict(decision="84.1", ledger="D66"),
    ("CCO", "C2.2"): dict(decision="84.2", ledger="D67"),
    ("CCO", "C5.3"): dict(decision="84.2", ledger="D67"),
}

# CCO-PTF-CIP-SZH C3.4: the two clauses that rested on the unit's own text, each re-read on a cited source
REVISIONS = {
    ("CCO", "C3.4"): dict(decision="84.3", clauses={
        1: ("C", "cleared: the design's documents give adjustable ranges well beyond 30% for several parameters without "
                 "redesign: the inflation paper's sensitivity analysis cuts the maximum octaves from 8 to 4 (50%) and runs "
                 "participation from 5% to 35%, keeping inflation below 1.8% and 89% of the welfare gains; the integrated "
                 "framework sets the conversion multiplier at 1-9x against tested alternatives of 1-5x and 1-12x and a "
                 "regional adjustment factor of 0.8-1.2; and the scorer's adjustment run on the v5.6 engine moves the Basic "
                 "Unit by 30% either way (0.7 to 1.3) from year 10",
            f"{HUB}: dual-currency-inflation.html, section 5.3; cco-ptf-integrated-framework.html, sections 3.1.2 and 5.4 "
            f"(outside_kit_sources/cco_hub__dual-currency-inflation.txt, cco_hub__cco-ptf-integrated-framework.txt); "
            f"NEEC_Rescoring_s57.md, reading 3.11"),
        3: ("C", "cleared: under the Citizens Internet Portal any citizen can submit a proposal (a signature threshold, a "
                 "30-90 day comment period, amendment), and a binding change passes by a 60-67% supermajority with "
                 "geographic distribution, so those affected can challenge a parameter change and have it reversed by a "
                 "process that does not run through the officials who made it; referenda move from advisory to binding in "
                 "the second phase (years 4-7); the PTH charter template adds notice, hearing and appeal rights on every "
                 "enforcement action",
            f"{HUB}: citizens-internet-portal.html, sections 4.4 and 7.1; democratic-governance-pth.html, Appendix "
            f"B.1 (charter template), Article VI, section 2 (outside_kit_sources/cco_hub__citizens-internet-portal.txt, "
            f"cco_hub__democratic-governance-pth.txt)"),
    }, note="Session 84 re-read clauses 1 and 3 on the design's own documents (decision 84.3): each had rested on the "
            "unit's own text, which rule 3 of decision 83.4 does not accept; both clear, and the verdict holds"),
}

ADJ = "NEEC_Adjudication_s83.md, sections 3 and 9"
OR = "the outside review r1, the reader's reading (outside_review_r1/results/reader.jsonl.gz)"

UNITS = {
    # rule 4 of decision 83.4: Degrowth, Integral and Mutual Credit's class W 1.0s fell for want of an estimate of the
    # distribution or a structural argument that bounds all of it; Participatory Economics' sources distinguish it in
    # strength, not on that point
    ("PE", "C1.2b"): dict(kind="change", verdict=0.5, decision="84.4", clauses=[
        ("U", "not shown: the design removes private productive property, capital markets and income from ownership, and "
              "rates incomes by effort and sacrifice, which bounds the top of the distribution more firmly than Degrowth's "
              "caps or Integral's parallel network; but it states no bound on personal holdings, which unequal effort "
              "ratings and saving across a lifetime leave unequal, and no source the unit cites, and none the outside "
              "reader names (it projects the Gini from the design's mechanisms, closed book), estimates the wealth Gini; a "
              "bound on the top does not bound a Gini, which the bottom of the distribution also sets",
         f"Report v1.6, PE C1.2b; {ADJ}; {OR}")],
        flag=[[1.0], "the published reading and the outside reader's: no private capital ownership is a structural "
                     "ceiling of the kind the 1.0 band describes"],
        note="read in Session 84 by rule 4 of decision 83.4 (ledger I12 item 1): the class W 1.0 rested on the same "
             "reading the adjudication found insufficient for Degrowth, Integral and Mutual Credit", zero=None),
}
