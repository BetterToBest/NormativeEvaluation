#!/usr/bin/env python3
"""
baseline_weighting_script.py (RECONSTRUCTED, Session 12)
==========================================================

This file was absent from the project mount across Sessions 9-11 (flagged
each time, never located). This is a reconstruction of its DATA, not a
recovery of the original file, built from two independently-published,
cross-referenced sources that state every legacy C1.2/C1.5 value
identically: NEEC_Step1c_Retrofit_C1.2ab_C1.5.md's own "Legacy text"
citation at the start of each system's subsection, and
neec_scores_csv_builder_v2.py's own per-row revision_note strings. All
21 non-wealth criteria (C1.1, C1.3, C1.4, all of D2-D5) are copied
directly from the current, canonical SCORES dict in
neec_weighting_robustness_analysis_v2.py, since Step 1c's own design
left these untouched -- that is the entire premise
verify_unchanged_from_legacy() checks.

VERIFICATION: every one of the 13 reconstructed 25-criterion totals
below was checked against PUBLISHED_LEGACY_25 (already present in
neec_weighting_robustness_analysis_v2.py, independently stated) and
matches exactly -- see reconstruct_baseline.py (Session 12 output) for
the verification script and its full pass/fail table.

CAVEAT: this reconstruction covers exactly what the two dependent
scripts (verify_unchanged_from_legacy() and step1c_retrofit.py) read
from this file -- a SCORES dict (25-criterion vectors, legacy C1.2/
C1.5 unsplit) and a PUBLISHED dict exposing each system's legacy
Total. It does not attempt to recover the original file's own
docstring, comments, or any content beyond these two dicts, since
none of that is recoverable from already-published sources and none
of it is read by any dependent script.
"""

SCORES = {
    'Status Quo Market Capitalism': {'C1.1':0.5,'C1.2':0.5,'C1.3':0.5,'C1.4':0.0,'C1.5':0.5,'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.5,'C3.1':0.0,'C3.2':1.0,'C3.3':0.0,'C3.4':0.5,'C3.5':0.5,'C4.1':0.0,'C4.2':0.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.0,'C5.1':1.0,'C5.2':1.0,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5},
    'Nordic Social Democracy': {'C1.1':1.0,'C1.2':0.5,'C1.3':1.0,'C1.4':0.5,'C1.5':1.0,'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.0,'C3.1':1.0,'C3.2':1.0,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,'C4.1':0.5,'C4.2':0.5,'C4.3':1.0,'C4.4':1.0,'C4.5':0.5,'C5.1':1.0,'C5.2':1.0,'C5.3':0.5,'C5.4':1.0,'C5.5':0.5},
    'Centrally Planned Socialism': {'C1.1':1.0,'C1.2':0.0,'C1.3':1.0,'C1.4':0.5,'C1.5':0.5,'C2.1':0.0,'C2.2':0.0,'C2.3':0.0,'C2.4':0.0,'C2.5':0.5,'C3.1':0.5,'C3.2':1.0,'C3.3':0.0,'C3.4':0.0,'C3.5':1.0,'C4.1':0.5,'C4.2':0.5,'C4.3':1.0,'C4.4':0.0,'C4.5':1.0,'C5.1':0.5,'C5.2':0.0,'C5.3':0.0,'C5.4':0.0,'C5.5':0.5},
    'Market Socialism': {'C1.1':1.0,'C1.2':1.0,'C1.3':0.5,'C1.4':0.5,'C1.5':0.5,'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.0,'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.5,'C4.1':0.5,'C4.2':0.5,'C4.3':0.5,'C4.4':1.0,'C4.5':0.5,'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.0},
    'Libertarian Minarchism': {'C1.1':0.0,'C1.2':0.0,'C1.3':0.0,'C1.4':0.0,'C1.5':0.0,'C2.1':0.0,'C2.2':0.0,'C2.3':1.0,'C2.4':1.0,'C2.5':1.0,'C3.1':0.0,'C3.2':0.5,'C3.3':0.0,'C3.4':0.0,'C3.5':0.0,'C4.1':0.0,'C4.2':0.0,'C4.3':0.0,'C4.4':0.5,'C4.5':1.0,'C5.1':0.5,'C5.2':1.0,'C5.3':0.5,'C5.4':0.5,'C5.5':0.5},
    'MMT + Job Guarantee': {'C1.1':1.0,'C1.2':0.5,'C1.3':1.0,'C1.4':0.5,'C1.5':1.0,'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':1.0,'C2.5':0.5,'C3.1':1.0,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,'C4.1':0.5,'C4.2':1.0,'C4.3':1.0,'C4.4':0.5,'C4.5':0.5,'C5.1':0.5,'C5.2':1.0,'C5.3':0.5,'C5.4':0.5,'C5.5':0.5},
    'Universal Basic Income': {'C1.1':1.0,'C1.2':0.0,'C1.3':0.5,'C1.4':1.0,'C1.5':0.0,'C2.1':1.0,'C2.2':1.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.0,'C3.1':1.0,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,'C4.1':0.5,'C4.2':0.5,'C4.3':1.0,'C4.4':0.0,'C4.5':1.0,'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.0},
    'Degrowth Economics': {'C1.1':1.0,'C1.2':0.5,'C1.3':1.0,'C1.4':0.5,'C1.5':0.5,'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.0,'C3.1':1.0,'C3.2':0.5,'C3.3':1.0,'C3.4':1.0,'C3.5':0.5,'C4.1':1.0,'C4.2':1.0,'C4.3':1.0,'C4.4':1.0,'C4.5':1.0,'C5.1':0.5,'C5.2':0.5,'C5.3':0.5,'C5.4':0.0,'C5.5':0.5},
    'Stakeholder Capitalism': {'C1.1':0.5,'C1.2':0.5,'C1.3':0.5,'C1.4':0.0,'C1.5':0.5,'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':0.5,'C3.1':0.5,'C3.2':0.5,'C3.3':0.5,'C3.4':1.0,'C3.5':0.0,'C4.1':0.0,'C4.2':0.0,'C4.3':0.5,'C4.4':0.0,'C4.5':0.5,'C5.1':0.5,'C5.2':1.0,'C5.3':1.0,'C5.4':0.0,'C5.5':0.0},
    'Fully Automated Luxury Communism': {'C1.1':1.0,'C1.2':0.5,'C1.3':1.0,'C1.4':1.0,'C1.5':0.5,'C2.1':1.0,'C2.2':1.0,'C2.3':1.0,'C2.4':0.0,'C2.5':0.0,'C3.1':0.5,'C3.2':1.0,'C3.3':0.5,'C3.4':0.5,'C3.5':0.5,'C4.1':1.0,'C4.2':1.0,'C4.3':0.5,'C4.4':0.0,'C4.5':1.0,'C5.1':0.0,'C5.2':0.0,'C5.3':0.0,'C5.4':0.0,'C5.5':0.5},
    'Participatory Economics': {'C1.1':1.0,'C1.2':0.5,'C1.3':1.0,'C1.4':1.0,'C1.5':0.5,'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':0.5,'C3.1':1.0,'C3.2':1.0,'C3.3':1.0,'C3.4':1.0,'C3.5':0.5,'C4.1':1.0,'C4.2':1.0,'C4.3':1.0,'C4.4':1.0,'C4.5':0.0,'C5.1':0.5,'C5.2':0.5,'C5.3':0.5,'C5.4':0.5,'C5.5':1.0},
    'CCO-PTF-CIP-SZH': {'C1.1':1.0,'C1.2':1.0,'C1.3':1.0,'C1.4':1.0,'C1.5':0.5,'C2.1':1.0,'C2.2':1.0,'C2.3':1.0,'C2.4':1.0,'C2.5':1.0,'C3.1':1.0,'C3.2':1.0,'C3.3':1.0,'C3.4':1.0,'C3.5':1.0,'C4.1':1.0,'C4.2':1.0,'C4.3':1.0,'C4.4':1.0,'C4.5':0.5,'C5.1':1.0,'C5.2':1.0,'C5.3':1.0,'C5.4':1.0,'C5.5':0.5},
    'Integral': {'C1.1':0.5,'C1.2':0.0,'C1.3':1.0,'C1.4':0.5,'C1.5':0.0,'C2.1':1.0,'C2.2':0.5,'C2.3':1.0,'C2.4':1.0,'C2.5':1.0,'C3.1':1.0,'C3.2':1.0,'C3.3':1.0,'C3.4':1.0,'C3.5':1.0,'C4.1':1.0,'C4.2':1.0,'C4.3':0.5,'C4.4':1.0,'C4.5':1.0,'C5.1':0.5,'C5.2':0.0,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5},
}

PUBLISHED = {
    'Status Quo Market Capitalism': {'Total': 10.5},
    'Nordic Social Democracy': {'Total': 18.5},
    'Centrally Planned Socialism': {'Total': 10.0},
    'Market Socialism': {'Total': 16.0},
    'Libertarian Minarchism': {'Total': 8.0},
    'MMT + Job Guarantee': {'Total': 16.0},
    'Universal Basic Income': {'Total': 14.5},
    'Degrowth Economics': {'Total': 18.0},
    'Stakeholder Capitalism': {'Total': 10.0},
    'Fully Automated Luxury Communism': {'Total': 14.0},
    'Participatory Economics': {'Total': 19.5},
    'CCO-PTF-CIP-SZH': {'Total': 23.5},
    'Integral': {'Total': 18.5},
}
