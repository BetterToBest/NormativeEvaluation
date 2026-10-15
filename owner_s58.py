#!/usr/bin/env python3
"""
owner_s58.py -- NEEC rescoring pass: the owner's decision 58.1 (ledger d37), as a part of the pass
==================================================================================================
Session 58. Group 2.5 (rescoring_s57.py, decision 57.7) lowered CCO-PTF-CIP-SZH's C3.2 Inflation Control Mechanisms from
1.0 to 0.5 on the overhauled simulation's main reading and sent the change to the owner (S57-3.9). The owner reversed
it in the ledger on 2026-10-15: the backing of the currency by creative output, a community chest, is an original
feature of the design; the pass measured the backing from none to all and took the cautious reading; the unit stays
at 1.0 until an empirical study shows that the backing does not hold in real-world data. Decision 58.1 records it
(NEEC_Rescoring_s58.md, section 3.1).

This file holds that one unit, in the form of the pass's units, so that pass_common.PARTS can apply it as its own part
("58.1") after group 2.5 and before group 2.6, as part "48.3" applied decision 48.3. Group 2.5's script and record are
not edited: its unit stands as the pass's history, and this part supersedes it. rescoring_s58.py checks it.
No main; nothing is printed. Deterministic.
"""

HUB = "research hub at 8e8a6ba"
SIM = ("Compassionism Simulation at d10ed6e (v5.6.0), the v5.6 release's engine; cco_sim_v56_checks_s57_output.txt, "
       "its Reference row at full backing (H1, a = 1)")
INFL = HUB + ", dual-currency-inflation.html (md5 329235ce)"
FRAME = HUB + ", cco-ptf-integrated-framework.html (md5 10ab8364)"
OWNER = "the owner's decision 58.1 (ledger d37, 2026-10-15)"
FIG = {"full": "0.1%", "main": "50.8%", "local": "3.2%", "national": "8.1%"}

UNITS = {
    ("CCO", "C3.2"): dict(
        verdict=1.0,
        clauses=[
            ("C", f"on the owner's reading the design's backing of the currency by creative output, a community chest, "
                  f"is an original feature of the design and is read as backing what the Source pays; at full backing "
                  f"the design's published model raises prices {FIG['full']} a year over 20 years in the Reference "
                  f"environment, in every seed under 3%; the dual-currency paper's own simulations give 0.95% a year; "
                  f"held until an empirical study shows that the backing does not hold in real-world data",
             f"{OWNER}; {SIM}; {INFL}, sections 5.2 and 5.4"),
            ("C", f"carried, as group 2.1 carried it, on the framework paper's 8% scenario, in which local inflation is "
                  f"held to {FIG['local']} while national inflation reaches {FIG['national']}; the design's published "
                  f"model carries no 8% scenario, so it does not contradict the figure",
             f"{OWNER}; {FRAME}, section 5.2"),
            ("C", "carried, as group 2.1 carried it, on the design's automatic parameter adjustment (the dual-currency "
                  "paper's adjustment rules); with every dollar the Source pays backed by new output, the model shows "
                  "no runaway inflation for an adjustment to prevent",
             f"{OWNER}; {INFL}, section 5.4; {SIM}")],
        flag=(f"0.5: group 2.5's reading (decision 57.7): the design states no backing share; on the model's main "
              f"reading the programme raises prices {FIG['main']} a year, no 8% scenario is modelled, and the one "
              f"automatic adjustment modelled raises the payout with prices rather than restraining issuance", "3.1"),
        note="the owner's decision 58.1 restores the published 1.0 and supersedes group 2.5's unit (decision 57.7, "
             "S57-3.9); it reopens toward 0.5 on an empirical study showing that the backing by creative output does "
             "not hold in real-world data"),
}
