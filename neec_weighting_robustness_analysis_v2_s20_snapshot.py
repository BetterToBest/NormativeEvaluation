#!/usr/bin/env python3
"""
NEEC Appendix A.4 — Alternative Weighting Robustness Check (v2, 26-criterion)
================================================================================
Companion script to NEEC Paper v1.2+, Section 10.9 and Appendix A.4.

STEP 1C UPDATE (this revision): the 13 systems previously scored under the
legacy 25-criterion structure (Systems 1-12 from the Report, Part I, and
Integral from Paper Appendix E) are now retrofitted to the v2, 26-criterion
structure (Section 12.3): each system's legacy 'C1.2' key has been replaced
with 'C1.2a' (Wealth Building for Resilience) and 'C1.2b' (Prevention of
Exploitative Accumulation), and 'C1.5' (Universal Wealth Access) has been
re-derived under its narrowed, access-breadth-only definition. Every new/
revised score is grounded in that system's ALREADY-PUBLISHED C1.2, C1.5, and
(where relevant, e.g. Gini figures) C4.4 rationale text -- this is a
re-review of existing evidence per Paper Section 12.5, not new research. Full
rationale for every retrofitted score, including several explicitly flagged
as close calls, lives in the companion document
`NEEC_Step1c_Retrofit_C1.2ab_C1.5.md`, produced in the same session as this
script update -- read that document for the "why", this script is the "what
it computes to."

ALSO NEW THIS REVISION: Georgism/LVT and Mutual Credit/LETS -- both scored
directly under the v2 structure when first evaluated (Sessions 6-7), added
here for the first time alongside the retrofitted 13, giving a genuinely
complete, single-structure, 15-system corpus. This is what makes a real
cross-system dominance/weighting comparison involving these two systems
possible for the first time (previously they could only be discussed
"qualitatively," per their own scratch documents' own disclaimers).

WHAT THIS SCRIPT DOES NOT DO: it does not alter the Report's or Paper's own
prose (Systems 1-12's write-ups, Part II/III's comparative-analysis text,
Appendix B's summary table, or Section 11's dominance discussion) -- those
still describe the pre-retrofit, 25-criterion corpus and reconciling them is
separately queued as "Step 5 (expanded)" per the project's own handoff
roadmap. This script (and its companion .md) is Step 1c's actual output: the
retrofitted DATA, cross-validated, ready for that future regeneration pass.

SESSION 16 UPDATE: two further Step 1b systems -- Doughnut Economics
(scored Session 14) and Universal Basic Services (scored Session 15) --
are added here for the first time, bringing the corpus from 15 to 17
systems, all on the identical 26-criterion v2 structure. Both score
vectors are transcribed verbatim from their own scratch documents
(`NEEC_DoughnutEconomics_scoring_scratch.md`,
`NEEC_UniversalBasicServices_scoring_scratch.md`) and were independently
re-verified against those documents' own stated domain/total figures
before insertion (see this session's `verify_new_systems.py`), following
the identical scratch-before-insert and re-verify-before-insert discipline
already used for Georgism and Mutual Credit/LETS. No new scoring judgment
is exercised by this update -- this is presentation of already-published,
already-verified scores, not re-analysis. As with the Session 8 insertion
of Georgism/Mutual Credit/LETS, this script's own canonical DATA is now
ahead of the Report's and Paper's own prose, which do not yet include
either system in their Part I write-ups or Part II/Section 11 comparative
analysis -- that regeneration remains separately queued, exactly as it
was for Georgism and Mutual Credit/LETS between their own Session 6-7
scoring and Session 9-10 regeneration.

SESSION 20 UPDATE: three further Step 1b systems -- Sovereign Wealth Fund
Statism (scored Session 17), State Capitalism / China (Session 18), and
State Capitalism / Singapore (Session 19) -- are added here in one
consolidated insertion pass, bringing the corpus from 17 to 20 systems,
all on the identical 26-criterion v2 structure. None of the three vectors
was retyped: each was extracted by AST parsing from the verification
script that checked it against its own scratch document (verify_swf.py,
verify_china.py, verify_singapore.py), formatted programmatically by
`insert_session20.py`, and re-verified after insertion by
`verify_insertion_s20.py`, which also confirms that the 17 previously
canonical systems are unchanged from the Session 16 snapshot
(`neec_weighting_robustness_analysis_v2_s16_snapshot.py`). No new scoring
judgment is exercised by this update. As after Sessions 8 and 16, this
script's canonical DATA is again ahead of the Report's and Paper's prose,
which include none of the five systems scored since Session 14; that
regeneration remains queued as "Step 5 (expanded)".

Run: python3 neec_weighting_robustness_analysis_v2.py
"""
import json

# ---------------------------------------------------------------------------
# SOURCE DATA -- 20 systems, all on the 26-criterion v2 structure.
#
# Systems 1-13 (through 'Integral'): retrofitted this session from their
# already-published legacy C1.2/C1.5 (+ C4.4 for Gini cross-checks); C1.1,
# C1.3, C1.4, and all of D2-D5 are BYTE-IDENTICAL to the legacy SCORES dict
# this script's own v1 predecessor used (verified programmatically against
# that predecessor before this file was written -- see verify_unchanged()
# below, which is new in this revision).
#
# Systems 14-15 (Georgism, Mutual Credit/LETS): scored natively under v2;
# transcribed verbatim from their own scratch documents' Domain-by-Domain
# sections, cross-checked against those documents' own stated domain totals
# before being used here (done in this session -- see the accompanying
# verification transcript in the Step 1c retrofit document).
#
# Systems 16-17 (Doughnut Economics, Universal Basic Services): added
# Session 16, natively on the v2 structure since first scored (Sessions 14
# and 15 respectively). Transcribed verbatim from their own scratch
# documents and independently re-verified against those documents' own
# stated domain/total figures immediately before this insertion (see
# `verify_new_systems.py`, produced in the same session as this update).
#
# Systems 18-20 (Sovereign Wealth Fund Statism, State Capitalism / China,
# State Capitalism / Singapore): added Session 20, natively on the v2
# structure since first scored (Sessions 17, 18, and 19). Extracted by AST
# from verify_swf.py, verify_china.py, and verify_singapore.py (not
# retyped) and re-verified after insertion (see verify_insertion_s20.py).
# Short keys here; the CSV carries the confirmed display names.
# ---------------------------------------------------------------------------
SCORES = {
    'Status Quo Market Capitalism': {
        'C1.1':0.5,'C1.2a':0.5,'C1.2b':0.0,'C1.3':0.5,'C1.4':0.0,'C1.5':0.5,
        'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.5,
        'C3.1':0.0,'C3.2':1.0,'C3.3':0.0,'C3.4':0.5,'C3.5':0.5,
        'C4.1':0.0,'C4.2':0.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.0,
        'C5.1':1.0,'C5.2':1.0,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    'Nordic Social Democracy': {
        'C1.1':1.0,'C1.2a':1.0,'C1.2b':0.5,'C1.3':1.0,'C1.4':0.5,'C1.5':1.0,
        'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.0,
        'C3.1':1.0,'C3.2':1.0,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,
        'C4.1':0.5,'C4.2':0.5,'C4.3':1.0,'C4.4':1.0,'C4.5':0.5,
        'C5.1':1.0,'C5.2':1.0,'C5.3':0.5,'C5.4':1.0,'C5.5':0.5,
    },
    'Centrally Planned Socialism': {
        'C1.1':1.0,'C1.2a':0.0,'C1.2b':0.5,'C1.3':1.0,'C1.4':0.5,'C1.5':0.0,
        'C2.1':0.0,'C2.2':0.0,'C2.3':0.0,'C2.4':0.0,'C2.5':0.5,
        'C3.1':0.5,'C3.2':1.0,'C3.3':0.0,'C3.4':0.0,'C3.5':1.0,
        'C4.1':0.5,'C4.2':0.5,'C4.3':1.0,'C4.4':0.0,'C4.5':1.0,
        'C5.1':0.5,'C5.2':0.0,'C5.3':0.0,'C5.4':0.0,'C5.5':0.5,
    },
    'Market Socialism': {
        'C1.1':1.0,'C1.2a':1.0,'C1.2b':0.5,'C1.3':0.5,'C1.4':0.5,'C1.5':0.5,
        'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.0,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':0.5,'C4.2':0.5,'C4.3':0.5,'C4.4':1.0,'C4.5':0.5,
        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.0,
    },
    'Libertarian Minarchism': {
        'C1.1':0.0,'C1.2a':0.0,'C1.2b':0.0,'C1.3':0.0,'C1.4':0.0,'C1.5':0.0,
        'C2.1':0.0,'C2.2':0.0,'C2.3':1.0,'C2.4':1.0,'C2.5':1.0,
        'C3.1':0.0,'C3.2':0.5,'C3.3':0.0,'C3.4':0.0,'C3.5':0.0,
        'C4.1':0.0,'C4.2':0.0,'C4.3':0.0,'C4.4':0.5,'C4.5':1.0,
        'C5.1':0.5,'C5.2':1.0,'C5.3':0.5,'C5.4':0.5,'C5.5':0.5,
    },
    'MMT + Job Guarantee': {
        'C1.1':1.0,'C1.2a':0.5,'C1.2b':0.0,'C1.3':1.0,'C1.4':0.5,'C1.5':0.5,
        'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':1.0,'C2.5':0.5,
        'C3.1':1.0,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,
        'C4.1':0.5,'C4.2':1.0,'C4.3':1.0,'C4.4':0.5,'C4.5':0.5,
        'C5.1':0.5,'C5.2':1.0,'C5.3':0.5,'C5.4':0.5,'C5.5':0.5,
    },
    'Universal Basic Income': {
        'C1.1':1.0,'C1.2a':0.0,'C1.2b':0.0,'C1.3':0.5,'C1.4':1.0,'C1.5':0.0,
        'C2.1':1.0,'C2.2':1.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.0,
        'C3.1':1.0,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,
        'C4.1':0.5,'C4.2':0.5,'C4.3':1.0,'C4.4':0.0,'C4.5':1.0,
        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.0,
    },
    'Degrowth Economics': {
        'C1.1':1.0,'C1.2a':0.5,'C1.2b':1.0,'C1.3':1.0,'C1.4':0.5,'C1.5':0.5,
        'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.0,
        'C3.1':1.0,'C3.2':0.5,'C3.3':1.0,'C3.4':1.0,'C3.5':0.5,
        'C4.1':1.0,'C4.2':1.0,'C4.3':1.0,'C4.4':1.0,'C4.5':1.0,
        'C5.1':0.5,'C5.2':0.5,'C5.3':0.5,'C5.4':0.0,'C5.5':0.5,
    },
    'Stakeholder Capitalism': {
        'C1.1':0.5,'C1.2a':0.5,'C1.2b':0.0,'C1.3':0.5,'C1.4':0.0,'C1.5':0.5,
        'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.5,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,
        'C4.1':0.0,'C4.2':0.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.5,
        'C5.1':0.5,'C5.2':1.0,'C5.3':1.0,'C5.4':0.0,'C5.5':0.0,
    },
    'Fully Automated Luxury Communism': {
        'C1.1':1.0,'C1.2a':0.0,'C1.2b':0.0,'C1.3':1.0,'C1.4':1.0,'C1.5':0.0,
        'C2.1':1.0,'C2.2':1.0,'C2.3':1.0,'C2.4':0.0,'C2.5':0.0,
        'C3.1':0.5,'C3.2':1.0,'C3.3':0.5,'C3.4':0.5,'C3.5':0.5,
        'C4.1':1.0,'C4.2':1.0,'C4.3':0.5,'C4.4':0.0,'C4.5':1.0,
        'C5.1':0.0,'C5.2':0.0,'C5.3':0.0,'C5.4':0.0,'C5.5':0.5,
    },
    'Participatory Economics': {
        'C1.1':1.0,'C1.2a':0.5,'C1.2b':1.0,'C1.3':1.0,'C1.4':1.0,'C1.5':0.5,
        'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.5,
        'C3.1':1.0,'C3.2':1.0,'C3.3':1.0,'C3.4':1.0,'C3.5':0.5,
        'C4.1':1.0,'C4.2':1.0,'C4.3':1.0,'C4.4':1.0,'C4.5':0.0,
        'C5.1':0.5,'C5.2':0.5,'C5.3':0.5,'C5.4':0.5,'C5.5':1.0,
    },
    'CCO-PTF-CIP-SZH': {
        'C1.1':1.0,'C1.2a':1.0,'C1.2b':1.0,'C1.3':1.0,'C1.4':1.0,'C1.5':0.5,
        'C2.1':1.0,'C2.2':1.0,'C2.3':1.0,'C2.4':1.0,'C2.5':1.0,
        'C3.1':1.0,'C3.2':1.0,'C3.3':1.0,'C3.4':1.0,'C3.5':1.0,
        'C4.1':1.0,'C4.2':1.0,'C4.3':1.0,'C4.4':1.0,'C4.5':0.5,
        'C5.1':1.0,'C5.2':1.0,'C5.3':1.0,'C5.4':1.0,'C5.5':0.5,
    },
    'Integral': {
        'C1.1':0.5,'C1.2a':0.0,'C1.2b':1.0,'C1.3':1.0,'C1.4':0.5,'C1.5':0.0,
        'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':1.0,
        'C3.1':1.0,'C3.2':1.0,'C3.3':1.0,'C3.4':1.0,'C3.5':1.0,
        'C4.1':1.0,'C4.2':1.0,'C4.3':0.5,'C4.4':1.0,'C4.5':1.0,
        'C5.1':0.5,'C5.2':0.0,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    'Georgism / Land Value Tax': {
        'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.5,'C1.3':0.5,'C1.4':0.5,'C1.5':0.0,
        'C2.1':0.5,'C2.2':0.5,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':0.5,'C4.2':0.5,'C4.3':0.5,'C4.4':0.5,'C4.5':0.5,
        'C5.1':0.5,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    'Mutual Credit / LETS': {
        'C1.1':0.5,'C1.2a':0.0,'C1.2b':1.0,'C1.3':0.0,'C1.4':0.5,'C1.5':0.0,
        'C2.1':0.5,'C2.2':0.5,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':0.5,'C4.2':0.5,'C4.3':0.5,'C4.4':0.5,'C4.5':0.5,
        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':1.0,
    },
    # --- Session 16 additions below: both scored natively on the v2 structure,
    # never on the legacy 25-criterion one, so (like Georgism/Mutual Credit/LETS
    # above) there is no retrofit history for either. ---
    'Doughnut Economics': {
        'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.0,'C1.3':0.5,'C1.4':0.0,'C1.5':0.0,
        'C2.1':0.0,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':1.0,'C4.2':1.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.0,
        'C5.1':0.5,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    'Universal Basic Services': {
        'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.0,'C1.3':0.5,'C1.4':0.5,'C1.5':0.0,
        'C2.1':0.5,'C2.2':0.5,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':0.5,'C4.2':0.5,'C4.3':0.5,'C4.4':0.5,'C4.5':0.5,
        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    # --- Session 20 additions below: all three scored natively on the v2
    # structure (Sessions 17-19), so none has retrofit history. China and
    # Singapore are the first two of three state-capitalism sub-entries; the
    # Gulf SWF states are still to be scored. ---
    'Sovereign Wealth Fund Statism': {
        'C1.1':0.5,'C1.2a':0.5,'C1.2b':0.5,'C1.3':0.0,'C1.4':0.5,'C1.5':0.5,
        'C2.1':0.5,'C2.2':0.5,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,
        'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':1.0,'C4.2':0.0,'C4.3':0.5,'C4.4':0.5,'C4.5':0.0,
        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    'State Capitalism / China': {
        'C1.1':0.5,'C1.2a':0.5,'C1.2b':0.5,'C1.3':0.5,'C1.4':0.5,'C1.5':0.5,
        'C2.1':0.0,'C2.2':0.0,'C2.3':0.5,'C2.4':0.0,'C2.5':0.5,
        'C3.1':0.5,'C3.2':1.0,'C3.3':0.5,'C3.4':0.5,'C3.5':0.0,
        'C4.1':0.5,'C4.2':0.0,'C4.3':0.0,'C4.4':0.0,'C4.5':0.0,
        'C5.1':1.0,'C5.2':0.5,'C5.3':0.5,'C5.4':0.5,'C5.5':0.5,
    },
    'State Capitalism / Singapore': {
        'C1.1':0.5,'C1.2a':1.0,'C1.2b':0.5,'C1.3':1.0,'C1.4':0.5,'C1.5':0.5,
        'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.5,
        'C3.1':0.5,'C3.2':1.0,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,
        'C4.1':0.5,'C4.2':0.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.0,
        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
}

PUBLISHED = {
    'Status Quo Market Capitalism':      {'D1':2.0,'D2':2.0,'D3':2.0,'D4':0.5,'D5':4.0,'Total':10.5},
    'Nordic Social Democracy':           {'D1':5.0,'D2':3.5,'D3':3.5,'D4':3.5,'D5':4.0,'Total':19.5},
    'Centrally Planned Socialism':       {'D1':3.0,'D2':0.5,'D3':2.5,'D4':3.0,'D5':1.0,'Total':10.0},
    'Market Socialism':                  {'D1':4.0,'D2':3.5,'D3':3.0,'D4':3.0,'D5':3.0,'Total':16.5},
    'Libertarian Minarchism':            {'D1':0.0,'D2':3.0,'D3':0.5,'D4':1.5,'D5':3.0,'Total':8.0},
    'MMT + Job Guarantee':               {'D1':3.5,'D2':2.5,'D3':3.0,'D4':3.5,'D5':3.0,'Total':15.5},
    'Universal Basic Income':            {'D1':2.5,'D2':3.0,'D3':3.0,'D4':3.0,'D5':3.0,'Total':14.5},
    'Degrowth Economics':                {'D1':4.5,'D2':3.5,'D3':4.0,'D4':5.0,'D5':2.0,'Total':19.0},
    'Stakeholder Capitalism':            {'D1':2.0,'D2':2.0,'D3':2.5,'D4':1.0,'D5':2.5,'Total':10.0},
    'Fully Automated Luxury Communism':  {'D1':3.0,'D2':3.0,'D3':3.0,'D4':3.5,'D5':0.5,'Total':13.0},
    'Participatory Economics':           {'D1':5.0,'D2':4.0,'D3':4.5,'D4':4.0,'D5':3.0,'Total':20.5},
    'CCO-PTF-CIP-SZH':                   {'D1':5.5,'D2':5.0,'D3':5.0,'D4':4.5,'D5':4.5,'Total':24.5},
    'Integral':                          {'D1':3.0,'D2':4.5,'D3':5.0,'D4':4.5,'D5':2.5,'Total':19.5},
    'Georgism / Land Value Tax':         {'D1':2.0,'D2':3.0,'D3':3.0,'D4':2.5,'D5':3.0,'Total':13.5},
    'Mutual Credit / LETS':              {'D1':2.0,'D2':3.0,'D3':3.0,'D4':2.5,'D5':4.0,'Total':14.5},
    'Doughnut Economics':                {'D1':1.0,'D2':2.0,'D3':3.0,'D4':2.5,'D5':3.0,'Total':11.5},
    'Universal Basic Services':          {'D1':1.5,'D2':3.0,'D3':3.0,'D4':2.5,'D5':3.5,'Total':13.5},
    'Sovereign Wealth Fund Statism':     {'D1':2.5,'D2':3.0,'D3':3.0,'D4':2.0,'D5':3.5,'Total':14.0},
    'State Capitalism / China':          {'D1':3.0,'D2':1.0,'D3':2.5,'D4':0.5,'D5':3.0,'Total':10.0},
    'State Capitalism / Singapore':      {'D1':4.0,'D2':2.0,'D3':3.5,'D4':1.0,'D5':3.5,'Total':14.0},
}

# Original (pre-retrofit, 13-system, 25-criterion) totals -- retained here only
# for the before/after comparison table this revision adds; NOT used in any
# of the 26-criterion computations below.
PUBLISHED_LEGACY_25 = {
    'Status Quo Market Capitalism':      10.5, 'Nordic Social Democracy': 18.5,
    'Centrally Planned Socialism':       10.0, 'Market Socialism': 16.0,
    'Libertarian Minarchism':            8.0,  'MMT + Job Guarantee': 16.0,
    'Universal Basic Income':            14.5, 'Degrowth Economics': 18.0,
    'Stakeholder Capitalism':            10.0, 'Fully Automated Luxury Communism': 14.0,
    'Participatory Economics':           19.5, 'CCO-PTF-CIP-SZH': 23.5,
    'Integral':                          18.5,
}

ALL_CRITS = ['C1.1','C1.2a','C1.2b','C1.3','C1.4','C1.5'] + \
            [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
D1_CRITS = ['C1.1','C1.2a','C1.2b','C1.3','C1.4','C1.5']
D5_CRITS = [f'C5.{i}' for i in range(1, 6)]


def verify_transcription(verbose=True):
    """Sums every system's 26 criterion scores by domain and checks against
    the PUBLISHED domain totals and overall totals -- the same discipline
    the v1 script applied to the legacy 25-criterion structure, now applied
    to the retrofitted 26-criterion one. MUST pass before anything downstream
    is trustworthy."""
    all_ok = True
    if verbose:
        print(f"{'System':<36}{'D1/6':>7}{'D2':>6}{'D3':>6}{'D4':>6}{'D5':>6}{'Total/26':>10}  Check")
    for sys, crit in SCORES.items():
        assert len(crit) == 26, f"{sys} has {len(crit)} criteria, not 26!"
        d1 = sum(crit[c] for c in D1_CRITS)
        d2 = sum(crit[f'C2.{i}'] for i in range(1, 6))
        d3 = sum(crit[f'C3.{i}'] for i in range(1, 6))
        d4 = sum(crit[f'C4.{i}'] for i in range(1, 6))
        d5 = sum(crit[f'C5.{i}'] for i in range(1, 6))
        dsums = {1: d1, 2: d2, 3: d3, 4: d4, 5: d5}
        total = sum(dsums.values())
        pub = PUBLISHED[sys]
        ok = all(abs(dsums[d] - pub[f'D{d}']) < 1e-9 for d in range(1, 6)) and abs(total - pub['Total']) < 1e-9
        all_ok = all_ok and ok
        if verbose:
            flag = "OK" if ok else "MISMATCH <<<<<"
            print(f"{sys:<36}{d1:>7.1f}{d2:>6.1f}{d3:>6.1f}{d4:>6.1f}{d5:>6.1f}{total:>10.1f}  {flag}")
    if not all_ok:
        raise AssertionError("Transcription mismatch found -- fix SCORES before trusting downstream analysis.")
    if verbose:
        print(f"\nAll {len(SCORES)} systems' criterion-level transcriptions verified against published domain/overall totals.\n")
    return all_ok


def verify_unchanged_from_legacy(legacy_scores_path='baseline_weighting_script.py', verbose=True):
    """NEW this revision. Confirms that for the 13 retrofitted systems,
    C1.1, C1.3, C1.4, and every D2-D5 criterion are BYTE-IDENTICAL to the
    pre-retrofit (legacy 25-criterion) SCORES dict -- i.e. that Step 1c only
    ever touched C1.2/C1.5's replacement, nothing else. This is exactly the
    kind of "verify, don't assume" check this project's own culture
    (Appendix G's re-derivation discipline; the CSV builder's cross-check
    against this very script) already establishes as standard practice."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("legacy", legacy_scores_path)
    legacy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(legacy)
    unchanged_crits = ['C1.1', 'C1.3', 'C1.4'] + [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
    all_ok = True
    for sys in legacy.SCORES:
        for c in unchanged_crits:
            old_v = legacy.SCORES[sys][c]
            new_v = SCORES[sys][c]
            if abs(old_v - new_v) > 1e-9:
                all_ok = False
                print(f"  UNEXPECTED CHANGE: {sys} {c}: legacy={old_v} new={new_v}")
    if verbose:
        print(f"verify_unchanged_from_legacy: {'PASS -- all 21 non-wealth criteria byte-identical across all 13 retrofitted systems' if all_ok else 'FAIL -- see above'}")
    return all_ok


# ---------------------------------------------------------------------------
# WEIGHTING SCHEMES (Appendix A.4) -- unchanged in intent; D1_CRITS now has
# 6 members instead of 5, so Material-Security-Weighted's max-possible grows
# accordingly (this is the correct, intended behavior, not a bug: doubling a
# now-6-criterion domain should weight more total points than doubling a
# 5-criterion one).
# ---------------------------------------------------------------------------
def weights_equal():
    return {c: 1.0 for c in ALL_CRITS}


def weights_material_security():
    w = weights_equal()
    for c in D1_CRITS:
        w[c] = 2.0
    return w


def weights_feasibility_discounted():
    w = weights_equal()
    for c in D5_CRITS:
        w[c] = 0.5
    return w


def weights_crisis_risk():
    w = weights_equal()
    w['C1.4'] = 3.0
    w['C4.2'] = 3.0
    return w


SCHEMES = {
    'Equal (baseline)': weights_equal(),
    'Material-Security-Weighted (D1 x2)': weights_material_security(),
    'Feasibility-Discounted (D5 x0.5)': weights_feasibility_discounted(),
    'Crisis-Risk-Weighted (C1.4, C4.2 x3)': weights_crisis_risk(),
}


def weighted_total(sys_scores, w):
    return sum(sys_scores[c] * w[c] for c in ALL_CRITS)


def max_possible(w):
    return sum(w[c] for c in ALL_CRITS)


def failure_count(sys_scores):
    return sum(1 for c in ALL_CRITS if sys_scores[c] == 0.0)


def tier(fails):
    if fails < 3:
        return 'Potentially Adequate'
    elif fails <= 5:
        return 'Partially Adequate'
    return 'Structurally Inadequate'


def dominates(a, b):
    ge_all = all(SCORES[a][c] >= SCORES[b][c] for c in ALL_CRITS)
    gt_some = any(SCORES[a][c] > SCORES[b][c] for c in ALL_CRITS)
    return ge_all and gt_some


def run_full_report():
    verify_transcription()
    verify_unchanged_from_legacy()

    print("\n" + "=" * 100)
    print("BEFORE/AFTER: legacy 25-criterion total vs. retrofitted 26-criterion total")
    print("(13 systems that existed under the old structure; Georgism/Mutual Credit")
    print("were never on the old structure, so have no 'before' row)")
    print("=" * 100)
    print(f"{'System':<36}{'Old /25':>10}{'Old %':>8}{'New /26':>10}{'New %':>8}{'Old Fail':>10}{'New Fail':>10}  Tier change?")
    for sys, old_total in PUBLISHED_LEGACY_25.items():
        new_total = PUBLISHED[sys]['Total']
        old_pct = round(old_total / 25 * 100)
        new_pct = round(new_total / 26 * 100)
        # old failure count needs the legacy 25-crit vector; skip if unavailable here
        new_fail = failure_count(SCORES[sys])
        print(f"{sys:<36}{old_total:>10.1f}{old_pct:>7}%{new_total:>10.1f}{new_pct:>7}%{'':>10}{new_fail:>10}")

    results = {}
    for name, w in SCHEMES.items():
        mx = max_possible(w)
        rows = sorted(((s, weighted_total(c, w), weighted_total(c, w) / mx * 100)
                        for s, c in SCORES.items()), key=lambda r: -r[1])
        results[name] = rows

    print("\n" + "=" * 100)
    print(f"RANKINGS UNDER EACH SCHEME, ALL {len(SCORES)} SYSTEMS (by weighted %, descending)")
    print("=" * 100)
    for name, rows in results.items():
        print(f"\n--- {name} (max possible = {max_possible(SCHEMES[name]):.1f}) ---")
        for i, (sys, wt, pct) in enumerate(rows, 1):
            print(f"  {i:2d}. {sys:<36} {wt:6.2f}  ({pct:5.1f}%)")

    print("\n" + "=" * 100)
    print("ADEQUACY TIER (failure-count based) -- invariant to ALL weighting by construction")
    print("=" * 100)
    for sys, crit in SCORES.items():
        f = failure_count(crit)
        print(f"  {sys:<36} {f:2d} failures -> {tier(f)}")

    print("\n" + "=" * 100)
    print("FULL PAIRWISE STRICT-DOMINANCE MATRIX (26-criterion basis)")
    print("Note: some pairs that were 'Strong Dominance' language in Section 11.3")
    print("were already NOT strict formal dominance under the legacy 25-criterion")
    print("structure either (typically via C4.5, which Step 1c never touches) --")
    print("this is a pre-existing corpus property, independently confirmed this")
    print("session, not something the retrofit introduces.")
    print("=" * 100)
    systems = list(SCORES.keys())
    cco = 'CCO-PTF-CIP-SZH'
    for sys in systems:
        if sys == cco:
            continue
        d_fwd = dominates(cco, sys)
        d_back = dominates(sys, cco)
        rel = "CCO-PTF strictly dominates" if d_fwd else ("dominated BY " + sys if d_back else "non-dominated pair")
        print(f"  CCO-PTF-CIP-SZH  vs  {sys:<32} {rel}")

    print("\n" + "=" * 100)
    print("DOMINANCE-PAIR SPOT CHECK (guaranteed positive under any positive weighting")
    print("by Appendix A.2 Theorem 5 wherever strict dominance holds at all --")
    print("confirmatory for genuine dominance pairs only)")
    print("=" * 100)
    pairs = [
        ('CCO-PTF-CIP-SZH', 'Status Quo Market Capitalism'),
        ('CCO-PTF-CIP-SZH', 'Nordic Social Democracy'),
        ('Participatory Economics', 'Stakeholder Capitalism'),
        ('Mutual Credit / LETS', 'Georgism / Land Value Tax'),
        # Session 16 additions -- Universal Basic Services lands at an EXACT
        # total-score tie with Georgism (13.5/26 each), which by Theorem 5
        # guarantees neither can strictly dominate the other; confirmed here
        # rather than left to that guarantee alone (see verify_ubs.py, Session 15).
        ('Universal Basic Services', 'Georgism / Land Value Tax'),
        ('Universal Basic Services', 'Doughnut Economics'),
        ('Universal Basic Services', 'Mutual Credit / LETS'),
        ('CCO-PTF-CIP-SZH', 'Doughnut Economics'),
        ('CCO-PTF-CIP-SZH', 'Universal Basic Services'),
        # Session 20 additions. State Capitalism / Singapore ties Sovereign
        # Wealth Fund Statism exactly (14.0/26), and State Capitalism / China
        # ties Centrally Planned Socialism and Stakeholder Capitalism exactly
        # (10.0/26), so none of those three pairs can be a dominance relation;
        # they are listed to show how each tie behaves under the alternative
        # schemes. Singapore strictly dominates China (verify_singapore.py).
        ('State Capitalism / Singapore', 'Sovereign Wealth Fund Statism'),
        ('State Capitalism / Singapore', 'State Capitalism / China'),
        ('State Capitalism / China', 'Centrally Planned Socialism'),
        ('State Capitalism / China', 'Stakeholder Capitalism'),
        ('CCO-PTF-CIP-SZH', 'Sovereign Wealth Fund Statism'),
        ('CCO-PTF-CIP-SZH', 'State Capitalism / China'),
        ('CCO-PTF-CIP-SZH', 'State Capitalism / Singapore'),
    ]
    for a, b in pairs:
        strict = dominates(a, b)
        print(f"\n  {a}  vs  {b}   (strict formal dominance: {strict})")
        for name, w in SCHEMES.items():
            wa, wb = weighted_total(SCORES[a], w), weighted_total(SCORES[b], w)
            print(f"    {name:<38} {wa:6.2f} > {wb:6.2f}" if wa > wb else f"    {name:<38} {wa:6.2f} <= {wb:6.2f}")

    return results


if __name__ == '__main__':
    run_full_report()
