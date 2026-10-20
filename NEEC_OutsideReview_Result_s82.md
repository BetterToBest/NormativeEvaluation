# NEEC outside blind review, run r1: the comparison (Session 82, ledger S64)

`compare_outside.py` applied `PREREG.md` (the results repository's `neec-outside-review/r1/`; copy `NEEC_OutsideReview_Prereg_s80.md`)
sections 2 to 7 and 9 as registered. Every table is in `compare_outside_output.txt` (harness-checked, byte for byte); this record
reads it. **No score, reading, flag or file of the standing was changed, and Jev set no verdict.** Adjudication is Session 83's.

## 1. What was compared, and what differs from the registration

- **Reader.** 696 of 696 calls answered and valid under the schema's rules (nothing missing, nothing imputed): 667 first
  readings and CCO-PTF-CIP-SZH's 29 repeats. One model for the run, `nvidia/nemotron-3-ultra-550b-a55b`.
- **Deviation 1, host (decision 81.1).** The registration names OpenRouter; the owner chose NVIDIA's own API
  (`integrate.api.nvidia.com/v1`) before any call. Same model, kit, runner (md5 `7d952ac4`) and rules; `PROVIDER_NOTE.md`. The
  result files do not show whether the host honoured `seed` and `reasoning`; the run was on one host, so r1 is not split.
- **Deviation 2, Jev in windows (D63; ledger I11).** TypeSafe's API refused 105 of 294 units as too long (`max_tokens_exceeded`).
  They were re-read in windows under the rule fixed before the first windowed call (`DEVIATION_D63.md`; runner changed, new md5 in
  that file). Section 4 below reports them apart.
- **Where the registration is silent, five readings, each reported both ways or stated** (decision 82.1; listed in the script's
  header): R1 NEEC's clause status R (out of reach, 160 clauses) is outside the four-way map: clause agreement is given with R
  excluded (primary) and with R counted as agreeing with short or not_shown; R2 "closed-book units" both by the kit's mode (373) and
  by the reader's own `closed_book` flag (572); R3 Jev compared pass by pass and on clauses stable across passes; R4 moot left out of
  Jev comparisons; R5 a "closed-book source" is a clause whose source field says so.
- Inputs checked against section 1: corpus md5 `4a1a26af`, snapshot `ab3dbc90`, blocks `dfb3d898` (a mismatch exits 1; negative control).
  NEEC without the owner's decisions differs from NEEC in exactly the eight owner-decided cells.

## 2. Verdict agreement (section 3)

| Set (first readings) | n | agree | rate | reader up | reader down |
|---|---|---|---|---|---|
| All | 667 | 490 | 73.5% | 93 (92 by 0.5, 1 by 1.0) | 84 (all 0.5) |
| Group 1 (CCO-PTF-CIP-SZH) | 29 | 21 | 72.4% | 1 | 7 |
| Group 2 (PE, INT, NSD, DG) | 116 | 86 | 74.1% | 14 | 16 |
| Group 3 (close calls) | 135 | 72 | 53.3% | 36 | 27 |
| Group 4 (calibration) | 387 | 311 | 80.4% | 42 | 34 |
| Kit closed-book / sources | 373 / 294 | 261 / 229 | 70.0% / 77.9% | | |
| Reader closed_book true / false | 572 / 95 | 414 / 76 | 72.4% / 80.0% | | |

Against NEEC without the owner's decisions: 496 of 667 (74.4%); group 1 rises to 23 of 29 (79.3%). By system the rate runs from
58.6% (Doughnut Economics, ten up) to 82.8% (Status Quo, Market Socialism); by criterion from 47.8% (C5.3) to 91.3% (C2.3, C3.6).
The group 3 gap is expected: those are the units NEEC marked as close calls. Disagreements in groups 1 and 2, unit by unit, are in
the output (table 3e).

**The eight owner-decided units.** The reader read seven of the eight at 0.5 where the owner's decisions put them at 1.0 (the
exception is CCO C3.2, where it reads 1.0, the same as NEEC with decision 58.1 and above NEEC without it). It agrees with NEEC
without the owner's decisions on those seven. Stage B (the argument for the owner's reading shown): the reader held 0.5 on six
and CCO C3.2's 1.0, and moved one, Ostrom-Style Commons C3.4, from 0.5 to 1.0 (clause 4 cleared).

## 3. Clause agreement, the lean and the repeat (sections 3, 4, 5)

- **Clauses.** NEEC records clause statuses for 496 of the 667 units (all 496 have the v2.0 clause count); 171 are "not
  recorded". Over 1,208 clauses (R excluded) the reader's status equals NEEC's on 678, **56.1%**; with R counted as short or not_shown,
  834 of 1,368 (61.0%). Every clause equal in 211 of 496 units (42.5%). The reader is stricter on NEEC's clears (NEEC cleared and the
  reader short or not shown on 134 of 290) and more generous on NEEC's not_shown (reader short on 260 of 671, cleared on 82).
  Clause agreement is lowest in the calibration set (52.3%) and highest in group 2 (61.6%).
- **Lean** (reader minus NEEC; 95% bootstrap interval on the difference from the calibration lean, 10,000 resamples, seed 80).
  Calibration (387 units) **+0.012**. CCO-PTF-CIP-SZH **-0.103**, difference -0.115, interval [-0.205, -0.027], **excludes 0**; against
  NEEC without the owner's decisions -0.034, difference -0.046, [-0.132, +0.038], does not. The eight owner-decided units: -0.438,
  difference -0.449, [-0.527, -0.316], excludes 0; without the decisions +0.051, [-0.027, +0.184], does not. Of the other four of
  the top five, **Nordic Social Democracy** is +0.103, difference +0.092, [+0.000, +0.185]: the lower bound is zero to three places,
  a marginal finding (the reader clears seven NSD criteria NEEC holds at 0.5: C2.5, C2.6, C3.3, C3.4, C4.1, C4.6, C5.1); Degrowth
  -0.063, Participatory Economics -0.081 and Integral -0.029 do not exclude 0. For Session 83: the CCO-PTF-CIP-SZH finding comes
  from the owner-decided cells, not from the other 25.
- **Repeat.** CCO-PTF-CIP-SZH's 29 units read twice: verdicts agree on 27 of 29 (93.1%; C2.2 0.5 then 1.0, C5.1 0.0 then 0.5);
  clause statuses on 60 of 75 clauses (80.0%), every clause equal in 18 of 29 units.

## 4. Jev (section 6), whole-pack and windowed apart

| | Whole-pack (189 units, 486 clauses) | Windowed, D63 (105 units, 314 clauses) |
|---|---|---|
| Passes agree | 478 of 486 (98.4%) | 313 of 314 (99.7%) |
| Jev not_shown (pass 1) | 80.7% | 77.7% |
| Jev with the reader (stable) | 38.6% | 49.4% |
| Jev with NEEC (stable, R and moot out) | 56.3% | 74.2% |
| reader = Jev, against NEEC | 37 clauses | 14 clauses |
| Jev = NEEC, against the reader | 108 | 57 |
| reader = NEEC, against Jev | 113 | 40 |
| all three agree | 120 | 107 |

- The expected pattern holds: of the reader's 47 whole-pack clears resting on a closed-book source, Jev says not_shown on 45 (11 windowed:
  9). Where the reader cleared on the pack, Jev agreed on 32 of 55.
- **Windows.** The prediction that windowed units lean toward not_shown is **not seen in the aggregate** (77.7% against 80.7%), but the
  two sets are different criteria, so this is not like for like; a fact spread across files may still have been missed. Sixteen
  clause-passes in nine units carry a recorded window conflict (CN C2.1, C3.6, C4.6; QA C2.4; SG C3.6, C4.6; SQ C2.6, C3.6, C4.6),
  listed in table 6c.
- Table 6d lists, per unit and clause, the 51 clauses where Jev and the reader agree against NEEC: these are read first in adjudication.

## 5. The standing, three ways (section 7)

| | First | Second | Third | CCO-PTF-CIP-SZH |
|---|---|---|---|---|
| NEEC (Session 79) | CCO-PTF-CIP-SZH 17.5 | PE 17.0 | Integral 16.0 | 17.5, rank 1 |
| NEEC without the owner's decisions | PE 16.5 | NSD, CCO, INT 15.5 | | 15.5, rank 2 (tied) |
| The reader's verdicts (nothing missing; the common-criteria totals equal them) | **Nordic Social Democracy 18.5** | Integral, UBS 15.5 | | 14.5, rank 7 |

First place **changes** under the reader's verdicts (to Nordic Social Democracy, 18.5 against 15.5 in NEEC, from a reader that
clears seven NSD criteria NEEC holds at 0.5). Seven tiers change (Fully Automated Luxury Communism, Participatory Economics,
Georgism, Mutual Credit, Doughnut Economics, Universal Basic Services, China); Participatory Economics falls to Partially Adequate
on four 0.0 verdicts. CCO-PTF-CIP-SZH is Potentially Adequate at 14.5 with two 0.0 verdicts (C4.3, C5.1). The reader's standing is
one model's reading without a record, disagreeing with NEEC on 26.5% of units; it is evidence for adjudication, not a rival
standing.

## 6. What the output does not do

It does not decide any disagreement, does not use Jev as a verdict, and does not publish or change a score. The 171 units without
a NEEC clause record are compared on verdicts only. The outside result on every CCO-PTF-CIP-SZH unit and every owner-decided unit
is published in the Report and Paper whatever Session 83 decides (plan, section 6; PREREG section 8).
