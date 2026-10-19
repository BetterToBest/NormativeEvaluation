#!/usr/bin/env python3
"""
owner_s79.py -- NEEC: the owner's decisions 79.1 to 79.4 (Session 79), as a layer over the final readings
==========================================================================================================
Session 78 applied the blind re-read's final readings (final_pass.py, apply_final_s78.py). On 2026-10-18 the owner, who
had waited until every reading was in (decision 58.2), took up the CCO-PTF-CIP-SZH scores below 1.0; on 2026-10-19 he
asked that three be reconsidered (C1.2a, C2.5, C3.4), and, after the reconsideration (NEEC_OwnerDecisions_s79.md,
section 1), decided to apply all three now as his decisions (as decision 58.1 applied C3.2), and to adopt for C3.4's
clause 4 a rule that also raises Integral, Participatory Economics, Degrowth and Ostrom-style commons governance.

This file holds those changes in the form of the pass's units. Each change names the unit it revises, the clause it
re-reads (every other clause of the unit is carried from the final reading unchanged), the clause's new status,
estimate and source, the flag that keeps the prior reading as the close call, and the note with the reopening
condition. final_pass.owner_state() lays the revised units over final_pass.final_state(); apply_owner_s79.py writes the
v2 files from it. Decision 57.2 reserves CCO-PTF-CIP-SZH's score changes to the owner; decision 79.4 is the owner's too,
though it reaches four other entries. No main; nothing is printed. Deterministic.
"""

TAG = "owner s79"
SESSION = 79
RECORD = "NEEC_OwnerDecisions_s79.md"
DATE = "2026-10-19"

SIM = ("Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the v5.6 "
       "release's engine; cco_sim_v56_checks_s57_output.txt")
LADDER = "Compassionism Simulation at d986a8d, dev/reports/v5-33-visual-suite.md (md5 e276c80b), the BLEI ladder"
C25 = "evidence_cache/C2.5/cco_research_hub_c25_extract.txt"
RULE_794 = ("on the rule of decision 79.4: clauses 1 to 3 are cleared (the parameters adjust over a range of 30% or more, "
            "updates follow evidence within six months, and those affected can challenge and reverse them), and no "
            "implementation record or model located shows a collapse caused by a parameter adjustment, so clause 4 is "
            "cleared, as Georgism's clause 4 is read ('no collapse caused by an adjustment located')")
REOPEN_794 = ("it reopens toward 0.5 on an implementation record or a model of the design's own adjustments showing a "
              "collapse that an adjustment caused")

# (code, criterion): decision, the clause re-read (1-based), (status, estimate, source), flag, note
CHANGES = {
    ("CCO", "C1.2a"): dict(
        decision="79.1", clause=1,
        new=("C", "on the owner's reading (decision 79.1, as decision 58.1 reads C3.2), the backing of the currency by "
                  "creative output, a community chest, is an original feature of the design and is read as backing what "
                  "the Source pays; at full backing the design's published model at v5.6.0 (500 seeds, Reference) has "
                  "91.1% of participants reach net wealth with Acre Equity of $60,000 in 2019 dollars at year 20, in 500 "
                  "of 500 seeds, median $437,409 (77.9% in the Adverse environment), and its BLEI ladder puts 76.2% of "
                  "adults at Flourishing (two years of basic living and more); in the main reading, with no backing, the "
                  "figures are 13.9% and 3.4% (48.0% Flourishing with no programme); held until an empirical study shows "
                  "that the backing does not hold in real-world data",
             f"the owner's decision 79.1 ({DATE}); {SIM}, its Reference row at full backing (H1, a = 1); "
             f"NEEC_Rescoring_s57.md, reading 3.5; {LADDER}"),
        flag=("0.5", "group 2.5's reading (decision 57.3): the clause holds only if new output backs what the Source pays, "
              "a condition the design's sources do not state; the release row shows 13.9%"),
        note="the owner's decision 79.1 raises the unit to 1.0 on decision 58.1's reading of the backing, which lifts no "
             "other CCO-PTF-CIP-SZH unit (C1.1, C1.2b, C1.3 and C3.3 stay short at full backing); it supersedes group "
             "2.5's unit and reopens toward 0.5 on an empirical study showing that the backing by creative output does "
             "not hold in real-world data"),
    ("CCO", "C2.5"): dict(
        decision="79.2", clause=1,
        new=("C", "on the owner's reading (decision 79.2), exit is leaving the system entirely: a member may stop taking "
                  "Basic Units at any time, with no work requirement or other condition attached; Public Trust Housing's "
                  "tenure-graded access to Acre Equity at exit (about 10-20% in the first six months, rising to 80-90% "
                  "after five years) is read not as a material penalty but as a provision for the stability of the "
                  "remaining members, on an asset a non-member never accrues: a member who leaves early keeps part of an "
                  "equity that a renter outside the system does not build, so is no worse off than one who never joined; "
                  "a member who moves (a job transfer, a new home) moves within the network keeping the equity",
             f"the owner's decision 79.2 ({DATE}); {C25}"),
        flag=("0.5", "the blind re-read's reading (Session 75, reading 2.5.1): Acre Equity is accessible at exit only in "
              "part in the early years, so an early leaver forfeits most of it, a material penalty"),
        note="the owner's decision 79.2 raises the unit to 1.0; the reading changes no other entry's verdict (Mutual "
             "Credit's clause 1 stays short: a leaver forfeits a credit balance earned by supplying goods or services, "
             "which leaves them worse off than a non-member paid in national currency; the other entries short on clause "
             "1 restrict leaving a country); it reopens toward 0.5 if the design's sources make a leaver worse off than "
             "a non-member, or attach a condition to leaving the Basic Unit system"),
    ("CCO", "C3.4"): dict(
        decision="79.3", clause=4,
        new=("C", "on the owner's reading (decision 79.3), a collapse is a breakdown that an adjustment causes (runaway "
                  "prices, a run that fails), not the direct effect of a smaller allowance on the share below the cost "
                  "of living; on the scorer's adjustment run (the Basic Unit multiplied by 0.7, 0.8, 1.2 or 1.3 from "
                  "year 10, 500 seeds, Reference) no step causes such a breakdown at either backing: the 1.2 and 1.3 "
                  "steps add at most 6.8 points to a year's price rise, and the 0.7 and 0.8 steps raise the share below "
                  "the cost of living (the test fixed before the run counted 339 and 43 of 500 seeds in the release row, "
                  "largest excess 16.6 points) as a smaller allowance does directly",
             f"the owner's decision 79.3 ({DATE}); {SIM}; NEEC_Rescoring_s57.md, reading 3.11"),
        flag=("0.5", "group 2.5's reading (reading 3.11): on the test fixed before the run, a 20-30% cut in the allowance "
              "raises the share below the cost of living by 10 points or more in 339 and 43 of 500 seeds"),
        note="the owner's decision 79.3 raises the unit to 1.0 and reads the test fixed before the run as counting the "
             "cut's direct effect, which the record discloses; the reading changes no other entry (the four other "
             "entries short on clause 4 record banking crises, excess deaths or a regime's collapse, which are "
             "breakdowns on any reading); it reopens toward 0.5 on a run in which an adjustment causes a breakdown"),
    ("INT", "C3.4"): dict(
        decision="79.4", clause=4,
        new=("C", RULE_794 + "; the design bounds recalibration within democratically approved ranges and detects "
                             "drift early (CDS Module 10), and has no implementation record or model of its adjustments",
             f"the owner's decision 79.4 ({DATE}); evidence_cache/C3.4/integral_wp_v01_c34_extract.txt"),
        flag=("0.5", "the blind re-read's reading (Session 71, reading 3.4.4): no implementation record of a parameter "
              "adjustment and no modelling of the design's own adjustments in operation, so clause 4 is not shown"),
        note="the owner's decision 79.4 raises the unit to 1.0 on a rule applied to every entry; " + REOPEN_794),
    ("PE", "C3.4"): dict(
        decision="79.4", clause=4,
        new=("C", RULE_794 + "; the design's councils adjust proposals on feedback, and it has no implementation record "
                             "or model of its adjustments",
             f"the owner's decision 79.4 ({DATE}); Report v1.6, Participatory Economics C3.4"),
        flag=("0.5", "part (b1)'s reading (reading 3.1): no implementation record, and no modelling of adjustments to the "
              "design's parameters in operation, so clause 4 is not shown"),
        note="the owner's decision 79.4 raises the unit to 1.0 on a rule applied to every entry; " + REOPEN_794),
    ("DG", "C3.4"): dict(
        decision="79.4", clause=4,
        new=("C", RULE_794 + "; the design's democratic governance and decentralised experimentation adjust its "
                             "parameters, and it has no implementation record or model of its adjustments",
             f"the owner's decision 79.4 ({DATE}); Report v1.6, Degrowth Economics C3.4"),
        flag=("0.5", "part (b1)'s reading (reading 3.1): no implementation record, and no modelling of adjustments to the "
              "design's parameters in operation located in its sources, so clause 4 is not shown"),
        note="the owner's decision 79.4 raises the unit to 1.0 on a rule applied to every entry; " + REOPEN_794),
    ("OS", "C3.4"): dict(
        decision="79.4", clause=4,
        new=("C", RULE_794 + "; the outright failures and fragile institutions the founding literature records are "
                             "not attributed to rule changes, and principle 3 is the procedure by which those affected "
                             "change the rules",
             f"the owner's decision 79.4 ({DATE}); Ostrom, Governing the Commons (1990), ch. 5"),
        flag=("0.5", "part (a)'s reading: the founding literature records outright failures and fragile appropriator-"
              "designed institutions, and no analysis located attributes them to, or clears them of, adjustments, so "
              "clause 4 is not shown"),
        note="the owner's decision 79.4 raises the unit to 1.0 on a rule applied to every entry; " + REOPEN_794),
}

# the decisions, for the record (apply_owner_s79.py prints them)
DECISIONS = (
    ("79.1", "owner", "CCO-PTF-CIP-SZH C1.2a Wealth Building for Resilience, 0.5 to 1.0",
     "The owner reads C1.2a as decision 58.1 read C3.2: the backing of the currency by creative output is an original "
     "feature of the design and is read as backing what the Source pays. At full backing the design's model clears the "
     "bar in every seed (91.1% of participants at $60,000 or more), and the simulation's BLEI ladder agrees (76.2% "
     "Flourishing). Applied to CCO-PTF-CIP-SZH's other units, the same reading lifts none: C1.1, C1.2b, C1.3 and C3.3 "
     "stay short at full backing. No other entry has a published model with a backing parameter. Reopens toward 0.5 on "
     "an empirical study showing that the backing does not hold in real-world data."),
    ("79.2", "owner", "CCO-PTF-CIP-SZH C2.5 Exit Rights and Mobility, 0.5 to 1.0",
     "Exit is leaving the system entirely: a member may stop taking Basic Units at any time, and no one is made to work. "
     "The early-exit haircut on Acre Equity is read as a stability provision on an asset a non-member never accrues, so "
     "a leaver is no worse off than one who never joined; moving within the network keeps the equity. Applied to every "
     "entry short on clause 1, the reading changes no verdict: Mutual Credit's forfeited credit balance was earned by "
     "supplying goods or services and leaves a leaver worse off than a non-member (and its clause 3 is short in any "
     "case); the other five restrict leaving a country."),
    ("79.3", "owner", "CCO-PTF-CIP-SZH C3.4 Epistemic Adaptability, 0.5 to 1.0",
     "A collapse is a breakdown an adjustment causes (runaway prices, a run that fails), not the direct effect of a "
     "smaller allowance on hardship; on that reading no step of the scorer's adjustment run collapses at either backing, "
     "and group 2.5 kept its flag toward 1.0 on the same reading. The test was fixed before the run; reading it "
     "afterwards as counting the cut's direct effect is disclosed here. Applied to every entry, the reading changes no "
     "other: the four other entries short on clause 4 (China, Centrally Planned Socialism, Nordic Social Democracy, "
     "Status Quo Market Capitalism) record banking crises, excess deaths or a regime's collapse."),
    ("79.4", "owner", "C3.4 clause 4: cleared where clauses 1 to 3 are cleared and no collapse is located; Integral, "
     "Participatory Economics, Degrowth Economics and Ostrom-Style Commons Governance, 0.5 to 1.0",
     "The owner asked that Integral's C3.4 be raised with CCO-PTF-CIP-SZH's. The reconsideration found that it does not "
     "follow from decision 79.3 (Integral's clause 4 was not shown, never tested), and that raising it needs a rule which "
     "reaches every entry with the same pattern; the owner adopted the rule for all of them. Where an entry clears "
     "clauses 1 to 3 (the parameters adjust over 30% or more, updates follow evidence within six months, those affected "
     "can challenge and reverse them) and no implementation record or model located shows a collapse caused by an "
     "adjustment, clause 4 is cleared, as Georgism's is. Four entries match (Integral, Participatory Economics, Degrowth "
     "Economics, Ostrom-Style Commons Governance), each with clauses 1 to 3 cleared and clause 4 not shown. Entries with "
     "clause 4 not shown and another clause short or not shown do not meet the rule's first condition and keep their "
     "readings. The rule departs from protocol 2.3(b) ('silence is not clearance') for this one clause, as Georgism's "
     "reading already did; the outside review (decision 79.6) reads all five C3.4 units blind."),
)
