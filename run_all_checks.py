#!/usr/bin/env python3
"""
run_all_checks.py -- NEEC single entry point for reproducibility checks
=======================================================================
Version 50 (Session 80). Runs every verification and analysis script on file
and confirms that each still reproduces its captured output BYTE FOR BYTE.
Three scripts written before Session 20 had no captured output; theirs was
first captured in Session 20 (verify_ubs, verify_new_systems, step1c_retrofit).
Version 0 (Session 20) ran 18 checks; version 1 (Session 25) ran 27. Version 2
adds decision D12 (Session 26): the generator that restates the comparative
claims of the three Session 21-23 scoring documents on the canonical corpus,
the generator that narrows their entry verifiers, the three narrowed entry
verifiers, the comparative-claims verifier, and a negative control in which
that verifier must reject the documents as they stood before D12. The Session
21-25 scripts now run against the Session 25 snapshots of those documents and
verifiers (see below): 34 checks. Version 3 (Session 27) adds the first
scripts of the reproducibility kit (decision D3): build_criteria.py, which
generates criteria.json from Paper v1.4 and checks every anchor example against
the published scores; build_summary_blocks.py, which stages the 23 summary
blocks (D3(a)); neec_entry.py, the generic entry verifier, run three ways (the
corpus inventory of the D13 measure, one entry with its D9 peer matrix, and its
self-test); and a negative control in which neec_entry.py must reject the
staged blocks against the Session 20 corpus, which lacks three of their
systems: 40 checks. Version 4 (Session 28) adds decisions D16 to D19:
stage_blocks_s28.py, which applies D17 and D18(a) to the staged blocks and
asserts that nothing else changes; neec_entry.py on the Session 28 blocks (the
D13 inventory after D16 to D18); and audit_claims_s28.py, the claim register
of the eight scoring documents not audited before (222 claims, each phrase
located and each computable verdict and replacement fact asserted on the
canonical corpus): 43 checks. Version 5 (Session 29) adds the D14 landing:
d14_landing_s29.py, the one generator that restates the eleven scoring
documents from their Session 26 snapshots and embeds their summary blocks;
verify_comparative_claims.py, generalised to all eleven documents (the Session
28 claim register, the restated phrases and their facts, the D13 measure from
the blocks in the documents, the blocks themselves); a negative control in
which it must reject the Session 26 texts; and neec_entry.py run on the
documents themselves: 47 checks. Every earlier check that reads one of those
documents now reads its Session 26 snapshot, and the Session 26 claims
verifier runs from its own snapshot. Version 6 (Session 30) adds decision D22:
verify_doughnut.py, reconstructed from the Doughnut Economics Verification
section; restate_s30.py, which restates that section; the Session 30 claims
verifier and a negative control in which it must reject the section as the
D14 pass left it. It adds candidate mode and the corpus file (D23): the corpus
file's builder, neec_entry.py's candidate self-test, and a negative control in
which a canonical entry is rejected as a candidate. And it adds the first blind
replication kit (D24): its builder, which regenerates the kit's blind protocol,
corpus and brief byte for byte, and the maintainers' baseline, the original
Ostrom-style commons governance entry validated as a candidate against the
kit's corpus: 56 checks. The D14 generator and the Session 29 claims verifier
now run against the Doughnut Economics document as the D14 pass left it, and
the D14 generator against the Session 29 neec_entry.py, which it pins.
Version 7 (Session 32) adds the first pilot replication's return (decision D2,
protocol 11.4-11.5): the replication's block validated as a candidate against
the kit's corpus, as the replicator was asked to validate it;
compare_replication.py, the criterion-level comparison of a blind replication,
run three ways (its self-test in a kit's layout; the comparison of the pilot's
replication with the original entry, which also checks the replication
record's generated tables and attribution table; and a negative control in
which it must refuse to run beside the canonical script); and
d18b_reexpression_s32.py, which computes decision D18(b)'s re-expression of
the Ostrom-style commons governance register, and decision D26 taken with it,
without changing any file: 61 checks.
Version 8 (Session 33) applies decisions D18(b) and D26 (the first pilot's consequences; confirmed by the
project owner): insert_session33.py writes the canonical scripts with Ostrom-style commons governance's C3.2
at 0.5 from their Session 32 snapshots; the Session 33 canonical script, CSV builder and corpus file are run
on the new corpus; verify_insertion_s33.py asserts that one cell changed and what follows from it;
restate_s33.py restates seven scoring documents from their Session 32 snapshots; the Session 33 claims
verifier runs on them, with a negative control in which it must reject the Session 32 documents; and
neec_entry.py reads the Session 33 blocks and verify_doughnut.py runs on the Session 33 corpus. Every
version 7 check now runs against the Session 32 files (see below), marked [Session 32 state] where that
changes its inputs. Version 8 also makes the harness runnable on a claude.ai Project, which cannot hold an
empty file: an expected-empty stream is written as EMPTY rather than read from a file, the refusal check
compares the refusal message on stderr (an uncaught exception also exits 1 with empty stdout, so exit
status and stdout alone could not tell a refusal from a crash), and a missing reference file fails its
check instead of stopping the run: 71 checks.
Version 9 (Session 34) adds Appendix A.4 on the Session 33 corpus: run_a4_full_rerun_33.py, which is
run_a4_full_rerun_23.py with its corpus-specific assertions re-derived (Ostrom-Style Commons Governance now
ties Mutual Credit / LETS and Universal Basic Income at 14.5), and a negative control in which it must
reject the Session 32 corpus, failing exactly its seven re-derived checks with an empty standard error (a
failure, not a crash). The two checks follow the 71 of version 8, whose numbering is unchanged:
run_a4_full_rerun_23.py keeps running against the Session 32 corpus it was written for. Version 9 also
regenerates README.md, the repository's landing page, with build_readme.py, whose score table, tier counts
and check count are computed from neec_scores.csv and from this harness (and the protocol's version from
SCORING_PROTOCOL.md's header), and compares it byte for byte with the committed copy, so the landing page
cannot drift from the data: 74 checks.
Version 10 (Session 35) adds revision R4's audit: r4_audit_s35.py, which audits every corpus 1.0 resting on
a multi-clause Pass Threshold clause by clause (167 units, 542 clause codes, each coded phrase located in its
rationale), computes decision D28 and the two rules it was weighed against, compares the quoted thresholds in
criteria.json and in two scoring documents with the definitions, and checks that the decision record
(NEEC_R4_MultiClause_Audit_s35.md) contains its generated tables verbatim. It changes no file: 75 checks.
Version 11 (Session 36) adds scoring protocol v2.0-draft.5 and what came with it: build_criteria.py, which now
corrects criteria.json after transcribing it (every anchor threshold becomes its definition's Pass Threshold,
decision D28(g); C3.2's bands carry decision D26, revision R3); build_replication_kit.py's self-test of
revision R8 on the protocol in force, which builds no kit; and verify_protocol_s36.py, which asserts the
protocol's own statements about the corpus, its archetype table, its decision register and its Appendix B,
with a negative control in which it must reject draft.4. Protocol draft.4, criteria.json and build_criteria.py
as they stood in Session 35 are pinned as *_s35_snapshot.* files: every check written before Session 36 that
reads one of them (the Session 27 criteria build, the Session 28 staging, the first replication kit, and the
Session 35 audit, which compares the uncorrected anchors with the definitions) reads the snapshot, so the
first kit still rebuilds byte for byte with the revised builder: 79 checks. Version 12 (Session 37) adds
rescoring_s37.py, part (a) of the rescoring pass (decisions D28, D29, D31): the 33 stated-shortfall 1.0s
re-estimated clause by clause, their consequences computed without changing any corpus file, and the
record NEEC_Rescoring_s37.md checked against its generated tables: 80 checks. Version 13 (Session 38) adds
rescoring_s38.py, the first group of part (b): the 29 part (b) units on the five criteria whose readings part (a)
fixed (C3.4, C5.3, C2.4, C1.3, C2.3), their consequences computed cumulatively with part (a), the pinned
Compassionism Simulation runs of cco_simulation_checks_s38.js checked by engine digest (the simulation's source is
not in this directory, so the JavaScript itself is not rerun here), and the record NEEC_Rescoring_s38.md checked
against its generated tables: 81 checks. Version 14 (Session 39) adds
rescoring_s39.py, the second group of part (b): C5.1's second clause tested in full on its eleven 1.0s outside
D28's population and C3.1's five part (b) units, with every departure from the audit's codes listed and asserted,
their consequences computed cumulatively with parts (a) and (b1), the anchor examples the pass moves counted, and
the record NEEC_Rescoring_s39.md checked against its generated tables: 82 checks.
Version 15 (Session 40) adds
rescoring_s40.py, the third group of part (b): C1.1's nine part (b) units, whose stress clause the audit coded silent,
with CCO-PTF-CIP-SZH's base clause tested against the design's own published model, the pinned Compassionism
Simulation runs of cco_simulation_checks_s40.js checked by both engine digests (harness.js and index.html; the
JavaScript itself is not rerun here), their consequences computed cumulatively with parts (a), (b1) and (b2), and the
record NEEC_Rescoring_s40.md checked against its generated tables: 83 checks.
Version 16 (Session 41) adds
rescoring_s41.py, the fourth group of part (b): the eleven part (b) units of C1.4, C2.1 and C3.2, with no departure
from the audit's A codes and the two clauses left not estimated each asserted to sit in a unit another clause decides,
their consequences computed cumulatively with parts (a) to (b3), the criteria the pass so far leaves with no 1.0
found and asserted, and the record NEEC_Rescoring_s41.md checked against its generated tables: 84 checks.
Version 17 (Session 42) adds
rescoring_s42.py, the fifth group of part (b): C2.5's ten part (b) units, with the one departure from the audit's A
codes listed and asserted, the audit's five out-of-reach codes confirmed, the four clauses left not estimated each
asserted to sit in a unit another clause decides, their consequences computed cumulatively with parts (a) to (b4),
and the record NEEC_Rescoring_s42.md checked against its generated tables: 85 checks.
Version 18 (Session 43) adds
rescoring_s43.py, the sixth group of part (b): the ten part (b) units of C3.5 and C4.1, with no departure from
the audit's A codes, the audit's four out-of-reach codes confirmed, the four clauses left not estimated each
asserted to sit in a unit another clause decides, a flag outside the group that rests on a unit it moves
asserted, their consequences computed cumulatively with parts (a) to (b5), and the record
NEEC_Rescoring_s43.md checked against its generated tables: 86 checks.
Version 19 (Session 44) adds
criteria_review_s44.py, the evidence tables of the criteria review (NEEC_Criteria_Review_s44.md): the implicit
norm weights under equal criterion weighting, the quantities scored in more than one Pass Threshold located verbatim,
their corpus agreement, and the Requirement figures that differ from a Pass Threshold; no file changed: 87 checks.
Version 20 (Session 45) adds the v2.0 criteria (NEEC_Criteria_v2_s45.md: Package A of the review, and Package B,
adopted by the owner, 28 criteria): build_criteria.py version 2, which builds criteria.json (neec-criteria/2.0)
from the pinned Session 44 criteria and the record's Appendix V, asserts seven rules (one figure per quantity,
no Requirement figure outside its threshold, no dated threshold, no US-only measure, verbatim clauses, anchors
equal to thresholds, the 28-criterion structure) and regenerates the protocol as draft.6; its self-test, in which
each rule must reject a planted violation; and criteria_v2_s45.py, the record's evidence tables. criteria.json,
build_criteria.py, SCORING_PROTOCOL.md and criteria_schema.json as they stood at tag s44 are pinned as
*_s44_snapshot.* files: every check written in Sessions 36 to 44 that reads one of them reads the snapshot and is
marked [Session 44 state]; the first replication kit's check reads the schema snapshot, which is byte-identical to
the schema it was built with. build_readme.py now also reads criteria.json. 90 checks.
Version 21 (Session 46) carries decision 46.1, Package C, adopted by the owner in part: C2.6 gains two clauses
(consent to medical treatment; compulsion prescribed by law, time-limited and open to judicial review) and C4.6
Harm Internalization is added, 29 criteria. The record is amended in place and tag s45 keeps its prior state, so
the three Session 45 checks now run build_criteria.py version 2.1, which regenerates the protocol as draft.7, and
criteria_v2_s45.py on the amended record; the two build captures are recaptured as build_criteria_s46_output.txt
and build_criteria_s46_selftest_output.txt (the Session 45 captures are at tag s45), and
criteria_v2_s45_output.txt is recaptured under its own name. No check is added or removed: 90 checks.
Version 22 (Session 47) carries decision 47.1, C4.6's clause 3 bar (World Justice Project sub-factor 6.2, 0.77,
the upper quartile of its 2025 edition), amended in place in the record, tag s46 keeping its prior state: the
build check runs build_criteria.py version 2.2, which regenerates the protocol as draft.8, and its capture is
renamed build_criteria_s47_output.txt (the self-test's capture is unchanged); criteria_v2_s45.py gains section 5,
which reads wjp_rol_sf62_2012_2025.csv (sub-factor 6.2 for every edition, extracted from the Project's 2025 data
file) and asserts the bar and every figure the record states. It adds rescoring_s47.py, part (b)'s seventh group
and the first on the v2.0 clauses: the ten part (b) units of C4.2 and C4.4, with part (a)'s three units of those
criteria re-read, each v2.0 clause mapped to the Session 44 clause the audit coded, the audit's A codes carried on
verbatim clauses and listed on restated ones, their consequences computed cumulatively with parts (a) to (b6), and
the record NEEC_Rescoring_s47.md checked against its generated tables. It reads the v2.0 criteria.json and the
pinned criteria_s44_snapshot.json side by side, so it is not pinned: 91 checks.
Version 23 (Session 48) carries decisions 48.1 to 48.3, amended in place in the record, tag s47 keeping its prior
state: 48.3 defines C4.4 clause 1's measure and moves C4.4 from class D to class M. The build check runs
build_criteria.py version 2.3, which regenerates the protocol as draft.9, and its capture is renamed
build_criteria_s48_output.txt; criteria_v2_s45.py counts the classes anew and asserts China's and Qatar's WJP series
(48.1). rescoring_s47.py asserts C4.4's Session 47 class, so check 91 now reads criteria.json as it stood at tag
s47, pinned byte-identical as criteria_s47_snapshot.json and copied in under the canonical name. It adds
rescoring_s48.py: C4.4's six units in the pass re-read on 48.3's measure (part (b7)'s records superseded),
Nordic Social Democracy's clause 1 bound computed from its published inputs, the consequences with parts (a) to
(b7), and the score ledger (every entry's published total, each part's change, its total now; the published totals
checked against neec_scores.csv), with NEEC_Rescoring_s48.md checked against its generated tables: 92 checks.
Version 24 (Session 49) adds the public site (decisions 49.1 to 49.10, from the site package prepared in a chat
session, NEEC_Site_Package_s49.md): build_site.py --check, which rebuilds docs/ in its own temporary directory from
criteria.json, the corpus, the record, Paper v1.4, the A.4 weighting script, the WJP extract, the issue forms and
site/, compares the result with docs/ file by file, and prints one line, which the harness also shows. Its inputs
keep their subdirectories, so a check's files may now name paths in subdirectories. A negative control, in which
the copied docs/index.html is replaced by docs/404.html, must fail with exit 1. Decisions 49.1 to 49.13 are
recorded in NEEC_Criteria_v2_s45.md, whose md5 criteria.json carries, so the build check's capture is renamed
build_criteria_s49_output.txt and recaptured; nothing else in criteria.json or the protocol changes. It adds
rescoring_s49.py, part (b)'s eighth group: the nine part (b) units of C4.3 and C4.5 on the v2.0 clauses,
CCO-PTF-CIP-SZH's C4.3 re-checked as class M on the same readings, part (a)'s three C4.5 units re-read, Nordic Social
Democracy's C4.3 computed from the Eurostat figures the script holds, the consequences cumulatively with parts (a)
to (b7) and decision 48.3, and the score ledger, with NEEC_Rescoring_s49.md checked against its generated tables:
95 checks. Version 25 (Session 50) adds the automated interpretation check (decisions 50.1 to 50.5, from the Jev
pilot package prepared in a chat session, NEEC_Jev_Pilot_Package_s50.md): jev_pilot_check.py, which reads the pilot's
recorded requests and responses (no network call), checks each state against its source and compares the answers with
the pass's clause statuses, its summary line shown. Decisions 50.1 to 50.7 are recorded in NEEC_Criteria_v2_s45.md,
so the build check's capture is renamed build_criteria_s50_output.txt and recaptured; nothing else in criteria.json
or the protocol changes. It adds rescoring_s50.py, part (b)'s ninth and last group: the eight part (b) units of C5.2,
C5.4 and C5.5 on the v2.0 clauses, part (a)'s two C5.2 units re-read, Status Quo's C5.2 re-checked as class M, Nordic
Social Democracy's C5.4 clause 2 from the ISSP 2016 figures it holds, the consequences cumulatively with parts (a) to
(b8) and decision 48.3, and the score ledger, with NEEC_Rescoring_s50.md checked against its generated tables; and
jev_s50_check.py, the interpretation check run on that group, which rebuilds every recorded request from its sources
and compares the recorded answers with the pass's statuses, its summary line shown: 98 checks. Version 26 (Session 51)
adds rescoring_s51.py, stage 2's first group: CCO-PTF-CIP-SZH's units that rest on the design's own modelling, read on
its published model at v4.20 (the pin moves from cd0ceec to 5a7a7b1): a scan of every published 1.0's rationale, the
five units it finds that the pass had not re-estimated, the design's C1.1 re-checked as class I on the Societal Poverty
Line, the design's other re-estimated units against v4.20, the consequences cumulatively with parts (a) and (b) and
decision 48.3, and the score ledger, with NEEC_Rescoring_s51.md checked against its generated tables and against the
tables of the simulation runs, whose captured output (cco_simulation_checks_s51_output.txt) it checks by digest; the
JavaScript itself is not rerun here, as with Sessions 38 and 40: 99 checks. Version 27 (Session 52)
adds pass_common.py, the pass's shared module (decision 52.5), checked by its --selftest, which rebuilds group 2.1's
consequences table, ledger, dominance line and anchors line from the parts before it and compares them verbatim with
the script's own; and triage_s52.py, the consequence triage (decision 52.7): 101 checks. Version 28 (Session 53) adds
rescoring_s53.py, stage 2's group 2.2 and the first written on the shared module: all 23 units of C1.2a re-read as
class M on v2.0's price basis, every 2019-dollar figure recomputed from the series it holds, the design's unit on its
published model through the captured output of cco_c12a_checks_s53.js, checked by digest, and the consequences
cumulatively with every part before it, with NEEC_Rescoring_s53.md checked against its generated tables; the Session 52
checks now load group 2.2 as a part of the pass: 102 checks. Version 29 (Session 54) adds rescoring_s54.py, stage 2's
group 2.3: the 20 units of C1.3 not yet re-estimated, re-read as class M on v2.0's two clauses, the figures the readings
derive recomputed, the design's unit on its published model through the captured output of cco_c13_checks_s54.js,
checked by digest, and the consequences cumulatively with every part before it, with NEEC_Rescoring_s54.md checked
against its generated tables; the Session 52 checks now load group 2.3 as a part of the pass: 103 checks. Version 30
(Session 56) adds rescoring_s56.py, stage 2's group 2.4 and the first class I group: the 20 units of C3.5 not yet
re-estimated, read on the indicators v2.0 names, every file the session added to the evidence cache checked by digest
and every passage quoted from it found there, clause 4 recomputed from the IMF rows, and the consequences cumulatively
with every part before it, with NEEC_Rescoring_s56.md checked against its generated tables; the Session 52 checks now
load group 2.4 as a part of the pass: 104 checks. Version 31 (Session 57) adds rescoring_s57.py, stage 2's group 2.5:
CCO-PTF-CIP-SZH's nine simulation units re-read on the design's published model at v5.6.0 (the pin moves from 5a7a7b1
to d10ed6e, decision 57.3), through the captured output of cco_sim_v56_checks_s57.js, checked by digest, whose own checks
reproduce the v5.6 release's published figures; the reopening conditions evaluated; the consequences cumulatively with
every part before it, with NEEC_Rescoring_s57.md checked against its generated tables. pass_common.py's dominance line
names a shared first place as shared (no earlier group had one), and its self-test allows a part whose units a later part
has all superseded; the Session 52 checks now load group 2.5 as a part of the pass: 105 checks. Version 32 (Session 58)
adds rescoring_s58.py, stage 2's group 2.6: the 16 units of C5.2 not yet re-estimated, re-read as class M on v2.0's five
clauses under the scope "each shown feasible by precedent or component evidence", the stage counts and spans the
readings derive recomputed, the clauses not estimated each tied to the clause that fixes its verdict, and the
consequences cumulatively with every part before it, with NEEC_Rescoring_s58.md checked against its generated tables;
it also checks owner_s58.py, the owner's decision 58.1 applied as a part of the pass of its own (CCO-PTF-CIP-SZH's C3.2
restored to 1.0), against the captured simulation output by digest; the Session 52 checks now load both as parts of
the pass: 106 checks. Version 33 (Session 60) adds rescoring_s60.py, stage 2's
group 2.7, the second class I group: the 20 units of C1.4 not yet re-estimated, read on the measure v2.0 names (each
clause a level in each of three displacement scenarios), every file of the evidence cache the readings use checked by
digest and every passage quoted from it found there, each published rationale located where the cache's index puts it,
and the consequences cumulatively with every part before it, with NEEC_Rescoring_s60.md checked against its generated
tables; the Session 52 checks now load group 2.7 as a part of the pass: 107 checks. Version 34 (Session 61) adds rescoring_s61.py,
stage 2's group 2.8: the 16 units of C4.3 not yet re-estimated, re-read as class M on the measure v2.0 names (the gap
between the median household incomes of the least and most advantaged groups on each declared axis), the three files
the group added to the evidence cache checked by digest and every passage quoted found there, every gap the readings
quote recomputed from them, each published rationale located, and the consequences cumulatively with every part before
it, with NEEC_Rescoring_s61.md checked against its generated tables; the Session 52 checks now load group 2.8 as a part
of the pass: 108 checks. Version 35 (Session 63) adds rescoring_s63.py,
stage 2's group 2.9, the third class I group: the 16 units of C3.1 not yet re-estimated, read on the measure v2.0 names
(days to the first increased payment, social benefits against the fall in real GDP, and the ILO's coverage), the ten
data files the group added to the evidence cache (and Session 62's index) checked by digest and every passage quoted found
there, every figure the readings quote recomputed from them, each published rationale located and compared with the
index, and the consequences cumulatively with every part before it, with NEEC_Rescoring_s63.md checked against its
generated tables; the Session 52 checks now load group 2.9 as a part of the pass: 109 checks. Version 36 (Session 64) adds
rescoring_s64.py, stage 2's group 2.10: the 16 units of C4.2 not yet re-estimated, re-read as class M on the four clauses
v2.0 names (consumption-based carbon, the Red List Index, footprint against biocapacity, the downscaled boundaries), the
two data files the group added to the evidence cache checked by digest and the rows quoted found there, every rate and index
change the readings quote recomputed from them, each published rationale located, and the consequences cumulatively with
every part before it, with NEEC_Rescoring_s64.md checked against its generated tables; the Session 52 checks now load group
2.10 as a part of the pass: 110 checks. Version 37 (Session 65) adds
rescoring_s65.py, the accelerated groups (decision 65.1): the remaining nine criteria (C4.1, C4.4, C3.4, C4.5, C2.5, C1.1,
C2.1, C2.4, C2.3) read in one script and one record, and the three new criteria (C2.6, C3.6, C4.6; 69 units) scored, with the
data files the groups added to the evidence cache checked by digest, every figure the readings quote recomputed from them,
each published rationale located, the consequences cumulatively with every part before it, and NEEC_Rescoring_s65.md compared
byte for byte with the record the script generates; the Session 52 checks now load it as a part of the pass; and apply_pass_s65.py,
stage 3's generator, checked against the three v2 files it writes (the corpus on the 29 criteria, the scores CSV and the site's
blocks): 112 checks. Version 38 (Session 68) adds build_evidence.py --check (decision 68.1): the 23 per-system evidence reports
and their index (evidence/), generated from the pass, the corpus, the blocks and the scoring documents, with every score,
every unit's verdict and every total checked against the corpus and the blocks, every link to a data file or to a document by
line checked to exist, and every file compared byte for byte with what the script generates, and a negative control in which
it must reject an evidence/ whose Status Quo report is another system's: 114 checks. build_site.py's inputs now include
evidence/, which the site's system pages link. Version 39 (Session 69) adds blind_review.py --selftest (ledger D52 to D54):
the blind re-read's shared module, proved on synthetic fixtures (compare_unit's agree/revise rule: a changed clause status
or verdict is a revision, a reworded estimate or source alone is not) and on one real unit of each of the three Sonnet-read
parts ((2.9) C3.1, (2.10) C4.2, (2.11) C1.1), whose blind_view() the check proves discloses no verdict, clause status,
estimate or source: 115 checks. No score or published file changed; the module applies nothing on its own. Version 40
(Session 70) adds evidence_cache_s70.py: the ten files cached for the shortcuts, by digest: 116 checks. Version 41
(Session 71) adds evidence_cache_s71.py (the nine files the blind re-read of C4.5 and C3.4 cached, by digest) and
blind_s71.py (the 24 blind readings, their comparison with part (2.11), the record's reconciliations, the
consequences on the 29 criteria and NEEC_BlindReview_s71.md's tables): 118 checks. No published file changed. Version
42 (Session 72) adds evidence_cache_s72.py (the eight files the blind re-read of C4.1 cached, by digest) and
blind_s72.py (the 23 blind readings of C4.1, their comparison with parts (2.11) and (b6), the reconciliation, the
consequences on the 29 criteria with Session 71's and NEEC_BlindReview_s72.md's tables): 120 checks. No published
file changed. Version 43 (Session 73) adds evidence_cache_s73.py (the ten files the blind re-read of C4.4 and C4.2
cached, by digest) and blind_s73.py (the 33 blind readings of C4.4 and C4.2, their comparison with parts (2.11) and
(2.10), the three reconciliations, the consequences on the 29 criteria with Sessions 71's and 72's and
NEEC_BlindReview_s73.md's tables): 122 checks. No published file changed. Version 44 (Session 74) adds
evidence_cache_s74.py (the three files the blind re-read of C1.1 and C3.1 cached, by digest) and blind_s74.py (the 30
blind readings of C1.1 and C3.1 and Nordic Social Democracy's C1.1, their comparison with parts (2.11), (2.9) and
(b3), the reconciliation, the consequences on the 29 criteria with Sessions 71's to 73's and NEEC_BlindReview_s74.md's
tables): 124 checks. No published file changed. Version 45 (Session 75) adds evidence_cache_s75.py (the ten files
the blind re-read of C2.1, C2.4, C2.3 and C2.5 cached, by digest) and blind_s75.py (the 18 first readings of C2.1,
C2.4 and C2.3 for the configured economies and the 23 blind readings of C2.5, their comparison with parts (2.11),
(b5) and (a), the reconciliation, the consequences on the 29 criteria with Sessions 71's to 74's and
NEEC_BlindReview_s75.md's tables): 126 checks. No published file changed. Version 46 (Session 76) adds
evidence_cache_s76.py (the 16 passages the blind re-read of C2.6, C3.6 and C4.6 cached from the designs' own texts, by
digest) and blind_s76.py (the 51 blind readings of the 17 designs and mechanisms on C2.6, C3.6 and C4.6, their
comparison with part (2.11), the consequences on the 29 criteria with Sessions 71's to 75's and
NEEC_BlindReview_s76.md's tables): 128 checks. No published file changed. Version 47 (Session 77) adds
evidence_cache_s77.py (the 21 files the blind re-read of C2.6, C3.6 and C4.6 for the configured economies cached, by
digest) and blind_s77.py (the 18 blind readings of the six configured economies on C2.6, C3.6 and C4.6, their
comparison with part (2.11), the consequences on the 29 criteria with Sessions 71's to 76's and
NEEC_BlindReview_s77.md's tables): 130 checks. No published file changed. Version 48 (Session 78) adds
final_pass.py --selftest (the seven blind groups' final readings laid over the pass) and apply_final_s78.py --check, which
writes the v2 files from them (ledger S61), with a negative control; the Session 65 files are kept as
neec_corpus_v2_s65_snapshot.json and its two companions, which apply_pass_s65.py and the blind scripts now read, so their
captured outputs change only in the file names; build_evidence.py and build_site.py check the regenerated files: 133 checks.
Version 49 (Session 79) adds apply_owner_s79.py --check, which writes the v2 files with the owner's decisions 79.1 to 79.4
(owner_s79.py, laid over the final readings by final_pass.owner_state()), with a negative control; apply_final_s78.py's
files are kept as neec_corpus_v2_s78_snapshot.json and its two companions; final_pass.py --selftest also checks the owner's
layer; build_evidence.py and build_site.py check the regenerated files: 135 checks.
Version 50 (Session 80) adds the outside blind review's kit (decisions 79.6, 79.8, 80.2 to 80.6): outside_kit.py --check
(outside_kit/ is exactly what the generator builds from the criteria, the protocol, the corpus's names and kinds, the
screened evidence cache and the cached design texts in outside_kit_sources/, each verified by md5), with a negative
control; outside_kit_check.py, which builds every prompt the runner would send and finds no leak, with a negative control
that plants one leak of each of seven kinds and shows each caught; and outside_review_runner.py --selftest: 140 checks.

HOW EACH CHECK RUNS. A check copies exactly the files its script needs into
a fresh temporary directory (under the names the script expects), runs the
script there, and compares its standard output (and, where a check names
one, its standard error), and any file it writes, with the captured copy on
file. EMPTY stands for an expected-empty stream, so no empty file is needed. Nothing in this directory is modified.

HISTORICAL SCRIPTS STAY UNEDITED. A verification script written before an
insertion pass makes claims about the corpus as it stood then (for example,
"the canonical corpus holds exactly 17 systems"). Rather than rewrite those
records, each one runs against the corpus it was written for:
  * the Session 16 corpus (17 systems): the pinned, byte-identical snapshot
    neec_weighting_robustness_analysis_v2_s16_snapshot.py, copied in under
    the canonical file name;
  * the Session 15 corpus (15 systems): a read-only view generated here from
    that snapshot, minus the two systems Session 16 inserted. The view narrows
    only SCORES and PUBLISHED and re-exports everything else unchanged. Helpers
    that read corpus data on their own (verify_transcription, dominates,
    run_full_report) therefore still see the snapshot's 17 systems; the 15
    shared vectors are identical there, so every lookup by name agrees.
  * the Session 20 corpus (20 systems): the pinned, byte-identical snapshots
    neec_weighting_robustness_analysis_v2_s20_snapshot.py,
    neec_scores_csv_builder_v2_s20_snapshot.py and neec_scores_s20_snapshot.csv
    (pinned in Session 25), copied in under the canonical file names. The
    Session 20 scripts and the Session 21-23 verifiers run against these.
  * the Session 25 documents and verifiers (pinned in Session 26, before
    decision D12 restated the three Session 21-23 scoring documents and
    narrowed their entry verifiers): *_s25_snapshot.md, verify_*_s25_snapshot.py
    and verify_*_output_s25_snapshot.txt, byte-identical copies, copied in
    under the canonical file names. The Session 21-25 scripts run against these.
  * the Session 26 documents and claims verifier (pinned in Session 29, before
    the D14 pass restated the eleven scoring documents): *_s26_snapshot.md and
    verify_comparative_claims_s26_snapshot.py, byte-identical copies, copied in
    under the canonical file names. The Session 16-28 scripts that read those
    documents run against these.
  * the Session 29 Doughnut Economics document, claims verifier and entry
    verifier (pinned in Session 30, before decision D22 and candidate mode):
    NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md,
    verify_comparative_claims_s29_snapshot.py and neec_entry_s29_snapshot.py,
    byte-identical copies, copied in under the canonical file names. The
    Session 29 scripts run against these where they depend on them.
  * the Session 32 corpus, documents and claims verifier (pinned in Session 33,
    before decisions D18(b) and D26): neec_weighting_robustness_analysis_v2,
    neec_scores_csv_builder_v2 and verify_comparative_claims (*_s32_snapshot.py),
    neec_scores_s32_snapshot.csv, neec_corpus_s32_snapshot.json, and the seven
    scoring documents restate_s33.py restates (*_s32_snapshot.md), byte-identical
    copies, copied in under the canonical file names. Every version 7 check runs
    against these.
  * the Session 35 protocol and criteria (pinned in Session 36, before protocol draft.5 and the
    correction of criteria.json): SCORING_PROTOCOL_s35_snapshot.md, criteria_s35_snapshot.json and
    build_criteria_s35_snapshot.py, byte-identical copies, copied in under the canonical file names. Every
    check written before Session 36 that reads one of them runs against these.
New insertion passes should pin their own snapshot the same way. Once the
project lives in a Git repository, a tag can replace the snapshot files.

Usage:   python3 run_all_checks.py
Exit status is 0 only if every check that runs passes. A check is skipped
(not failed) only when an external tool it needs, such as Node.js, is
absent.
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CANON = "neec_weighting_robustness_analysis_v2.py"
S16 = "neec_weighting_robustness_analysis_v2_s16_snapshot.py"
BASELINE = "baseline_weighting_script.py"
BUILDER = "neec_scores_csv_builder_v2.py"
S20 = "neec_weighting_robustness_analysis_v2_s20_snapshot.py"
S20_BUILDER = "neec_scores_csv_builder_v2_s20_snapshot.py"
S20_CSV = "neec_scores_s20_snapshot.csv"
PENDING = {  # Session 21-23 verifiers and the scratch documents they check
    "verify_qatar.py": "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
    "verify_islamicfinance.py": "NEEC_IslamicFinance_scoring_scratch.md",
    "verify_ostrom.py": "NEEC_Ostrom_Commons_scoring_scratch.md",
}
PENDING_FILES = {k: k for pair in PENDING.items() for k in pair}
QA_DOC, IF_DOC, OS_DOC = (PENDING[v] for v in ("verify_qatar.py", "verify_islamicfinance.py", "verify_ostrom.py"))
# Session 25 snapshots (pinned in Session 26): canonical name -> snapshot file.
S25 = {n: n[:-3] + "_s25_snapshot" + n[-3:] for n in PENDING_FILES}
S25_OUT = {o: o[:-4] + "_s25_snapshot.txt"
           for o in ("verify_qatar_output.txt", "verify_islamicfinance_output.txt", "verify_ostrom_output.txt")}
# Inputs of the Session 27 kit: the summary-block generator reads these documents and verifiers.
KIT_BLOCK_INPUTS = ("build_summary_blocks.py", "neec_entry.py", CANON, "neec_scores.csv",
                    "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                    "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
                    "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                    "NEEC_StateCapitalism_China_scoring_scratch.md", "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                    QA_DOC, IF_DOC, OS_DOC, "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md", "NEEC_Paper_v1_4.md",
                    "verify_china.py", "verify_singapore.py", "verify_qatar.py", "verify_islamicfinance.py",
                    "verify_ostrom.py")
KIT_ENTRY_INPUTS = ("neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s27.json")
# Session 28: decisions D16-D19 (staging) and the claim register of the eight unaudited documents.
S28_STAGE_INPUTS = ("stage_blocks_s28.py", "neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s27.json",
                    "SCORING_PROTOCOL.md")
S28_DOCS = ("NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
            "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
            "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "NEEC_StateCapitalism_China_scoring_scratch.md",
            "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md")
S28_AUDIT_INPUTS = ("audit_claims_s28.py", "neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s28.json") + S28_DOCS
# Inputs of verify_comparative_claims.py (Session 26).
CLAIMS_INPUTS = (CANON, "verify_comparative_claims.py", QA_DOC, IF_DOC, OS_DOC,
                 "verify_qatar.py", "verify_islamicfinance.py", "verify_ostrom.py",
                 "verify_singapore.py", "verify_china.py",
                 "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                 "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
                 "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                 "NEEC_StateCapitalism_China_scoring_scratch.md", "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                 "NEEC_Report_v1_6.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md")
# Session 29: the D14 landing. The eleven scoring documents and their Session 26 snapshots.
ELEVEN = S28_DOCS + (QA_DOC, IF_DOC, OS_DOC)
S26 = {d: d[:-3] + "_s26_snapshot.md" for d in ELEVEN}
S26_CLAIMS = "verify_comparative_claims_s26_snapshot.py"
D14_INPUTS = ("d14_landing_s29.py", "summary_blocks_s28.json", "neec_entry.py", CANON, "neec_scores.csv")
CLAIMS29_INPUTS = (CANON, "neec_scores.csv", "neec_entry.py", "audit_claims_s28.py", "summary_blocks_s28.json",
                   "d14_landing_s29.py", "verify_comparative_claims.py", "verify_qatar.py", "verify_islamicfinance.py",
                   "verify_ostrom.py", "verify_singapore.py", "verify_china.py") + ELEVEN
# Session 30: D22, candidate mode and the corpus file (D23), the first blind replication kit (D24).
DE_DOC = "NEEC_DoughnutEconomics_scoring_scratch.md"
DE_S29 = "NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md"
ENTRY_S29 = "neec_entry_s29_snapshot.py"
S29_CLAIMS = "verify_comparative_claims_s29_snapshot.py"
CLAIMS30_INPUTS = CLAIMS29_INPUTS + ("restate_s30.py", "verify_doughnut.py")
ENTRY30 = ("neec_entry.py", CANON, "neec_scores.csv", "neec_corpus.json")
KIT_INPUTS = ("build_replication_kit.py", "SCORING_PROTOCOL.md", "criteria.json", "criteria_schema.json",
              "summary_block_schema.json", "neec_entry.py", "neec_corpus.json", "build_corpus_file.py")
KIT = "out/neec_replication_kit_OS/"
# Session 32: the first pilot replication's return.
REPL_DOC = "NEEC_OstromCommons_replication_scoring.md"
REPL_RECORD = "NEEC_OstromCommons_replication_record.md"
KIT_LAYOUT = {"compare_replication.py": "compare_replication.py", "neec_entry.py": "neec_entry.py",
              "neec_corpus.json": "replication_kit_OS_neec_corpus.json"}
VIEW15 = "@view15"   # generated file (see VIEW15_SOURCE)
EMPTY = "@empty"     # an expected-empty stream: a claude.ai Project cannot hold an empty file
# Session 33: decisions D18(b) and D26. The files they change, and their Session 32 snapshots.
S33_DOCS = (OS_DOC, QA_DOC, IF_DOC, "NEEC_MutualCredit_LETS_scoring_scratch.md",
            "NEEC_UniversalBasicServices_scoring_scratch.md", "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
            "NEEC_StateCapitalism_Singapore_scoring_scratch.md")
S32 = {n: n[:-3] + "_s32_snapshot.py" for n in (CANON, BUILDER, "verify_comparative_claims.py")}
S32.update({d: d[:-3] + "_s32_snapshot.md" for d in S33_DOCS})
S32.update({"neec_scores.csv": "neec_scores_s32_snapshot.csv", "neec_corpus.json": "neec_corpus_s32_snapshot.json"})
# Session 36: protocol draft.5 and the corrected criteria.json. The files they replace, pinned as they stood in
# Session 35. The protocol (draft.4, Session 30) and criteria.json (Session 27) did not change between Session 32
# and Session 35, so these snapshots are also the Session 32 state that pin32() gives the version 7 checks.
S35 = {"SCORING_PROTOCOL.md": "SCORING_PROTOCOL_s35_snapshot.md", "criteria.json": "criteria_s35_snapshot.json",
       "build_criteria.py": "build_criteria_s35_snapshot.py"}
# Session 45: the v2.0 criteria. The files they replace, pinned as they stood at tag s44. criteria_schema.json did
# not change between Session 27 and Session 44, so its snapshot is also the state every earlier check read.
S44 = {n: n.rsplit(".", 1)[0] + "_s44_snapshot." + n.rsplit(".", 1)[1]
       for n in ("criteria.json", "build_criteria.py", "SCORING_PROTOCOL.md", "criteria_schema.json")}

VIEW15_SOURCE = '''"""Derived view generated by run_all_checks.py: the pinned Session 16 snapshot
minus the two systems Session 16 inserted, i.e. the 15-system corpus data that
the Session 10-15 scripts were written against. Read-only; not a canonical file."""
import importlib.util as _u
_spec = _u.spec_from_file_location("_neec_s16", "neec_weighting_robustness_analysis_v2_s16_snapshot.py")
_m = _u.module_from_spec(_spec)
_spec.loader.exec_module(_m)
_DROP = ("Doughnut Economics", "Universal Basic Services")
# Re-export the snapshot's public names unchanged, then narrow the two corpus tables.
globals().update({_k: _v for _k, _v in vars(_m).items()
                  if not _k.startswith("_") and _k not in ("SCORES", "PUBLISHED")})
SCORES = {k: v for k, v in _m.SCORES.items() if k not in _DROP}
PUBLISHED = {k: v for k, v in _m.PUBLISHED.items() if k not in _DROP}
'''

# The Session 20 insertion verifier's inputs, with the Session 20 corpus under the canonical names.
S20_INPUTS = {CANON: S20, S16: S16, BASELINE: BASELINE,
               "neec_scores_csv_builder_v2.py": S20_BUILDER,
               "neec_scores_csv_builder_v2_s16_snapshot.py": "neec_scores_csv_builder_v2_s16_snapshot.py",
               "neec_scores.csv": S20_CSV,
               "neec_scores_s16_snapshot.csv": "neec_scores_s16_snapshot.csv",
               "insert_session20.py": "insert_session20.py",
               "verify_swf.py": "verify_swf.py", "verify_china.py": "verify_china.py",
               "verify_singapore.py": "verify_singapore.py"}

# Each check: name, command, files {name in temp dir: source file here or VIEW15},
# stdout (captured file to match, or None), outputs {file written: reference file here},
# and optionally expect_exit (default 0; a negative control expects 1).
V7_CHECKS = [
    # --- the Session 32 state (23 systems; version 7's current corpus) ---
    dict(name="Canonical script, current corpus (23 systems, full report)",
         cmd=["python", CANON], files={CANON: CANON, BASELINE: BASELINE},
         stdout="session25_v2script_output.txt"),
    dict(name="CSV builder regenerates neec_scores.csv (23 systems)",
         cmd=["python", BUILDER], files={CANON: CANON, BUILDER: BUILDER},
         stdout="session25_csv_builder_output.txt",
         outputs={"neec_scores.csv": "neec_scores.csv"}),
    dict(name="Session 25 generator reproduces both canonical scripts from the Session 20 files",
         cmd=["python", "insert_session25.py", ".", "out"],
         files=dict(S25, **{k: k for k in (S20, S20_BUILDER, "insert_session25.py")}),
         stdout="session25_generator_output.txt",
         outputs={"out/" + CANON: CANON, "out/" + BUILDER: BUILDER}),
    dict(name="verify_insertion_s25.py (Session 25 insertion, current corpus; includes negative tests)",
         cmd=["python", "verify_insertion_s25.py"],
         files=dict(S25, **{k: k for k in (CANON, BUILDER, "neec_scores.csv", BASELINE, S20, S20_BUILDER,
                                                     S20_CSV, "insert_session25.py", "verify_insertion_s25.py")}),
         stdout="session25_verify_insertion_output.txt"),
    dict(name="run_a4_full_rerun_23.py (Appendix A.4, current corpus)",
         cmd=["python", "run_a4_full_rerun_23.py"],
         files={CANON: CANON, BASELINE: BASELINE, "run_a4_full_rerun_23.py": "run_a4_full_rerun_23.py"},
         stdout="a4_rerun_23_raw_output.txt"),
    dict(name="audit_claim_survival_s25.py (the Session 21-23 claims on the combined corpus)",
         cmd=["python", "audit_claim_survival_s25.py"],
         files=dict(S25, **S25_OUT, **{k: k for k in (S20, "audit_claim_survival_s25.py")}),
         stdout="session25_audit_output.txt"),
    # --- decision D12 (Session 26): restated documents, narrowed entry verifiers, current corpus ---
    dict(name="Session 26 generator restates the three scoring documents from their Session 25 snapshots",
         cmd=["python", "rewrite_session26.py", ".", "out"],
         files=dict({S25[d]: S25[d] for d in (QA_DOC, IF_DOC, OS_DOC)},
                    **{CANON: CANON, "rewrite_session26.py": "rewrite_session26.py"}),
         stdout="session26_rewrite_output.txt",
         outputs={"out/" + d: S26[d] for d in (QA_DOC, IF_DOC, OS_DOC)}),
    dict(name="Session 26 generator narrows the three entry verifiers from their Session 25 snapshots",
         cmd=["python", "narrow_verifiers_s26.py", ".", "out"],
         files=dict({S25[v]: S25[v] for v in PENDING}, **{"narrow_verifiers_s26.py": "narrow_verifiers_s26.py"}),
         stdout="session26_narrow_output.txt",
         outputs={"out/" + v: v for v in PENDING}),
    dict(name="verify_qatar.py (entry checks; current corpus, Session 26 document)",
         cmd=["python", "verify_qatar.py"],
         files={CANON: CANON, "verify_qatar.py": "verify_qatar.py", QA_DOC: S26[QA_DOC]},
         stdout="verify_qatar_output.txt"),
    dict(name="verify_islamicfinance.py (entry checks; current corpus, Session 26 document)",
         cmd=["python", "verify_islamicfinance.py"],
         files={CANON: CANON, "verify_islamicfinance.py": "verify_islamicfinance.py", IF_DOC: S26[IF_DOC]},
         stdout="verify_islamicfinance_output.txt"),
    dict(name="verify_ostrom.py (entry checks; current corpus, Session 26 document)",
         cmd=["python", "verify_ostrom.py"],
         files={CANON: CANON, "verify_ostrom.py": "verify_ostrom.py", OS_DOC: S26[OS_DOC]},
         stdout="verify_ostrom_output.txt"),
    dict(name="verify_comparative_claims.py as of Session 26 (snapshot; current corpus, Session 26 documents)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: S26.get(k, k) for k in CLAIMS_INPUTS}, **{"verify_comparative_claims.py": S26_CLAIMS}),
         stdout="session26_verify_claims_output.txt"),
    dict(name="verify_comparative_claims.py as of Session 26 rejects the Session 25 documents (negative control; exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: S26.get(k, k) for k in CLAIMS_INPUTS}, **{"verify_comparative_claims.py": S26_CLAIMS},
                    **{d: S25[d] for d in (QA_DOC, IF_DOC, OS_DOC)}),
         stdout="session26_verify_claims_negative_output.txt", expect_exit=1),
    # --- Session 27: the reproducibility kit (current corpus) ---
    dict(name="build_criteria.py generates criteria.json from Paper v1.4 and checks every anchor example",
         cmd=["python", "build_criteria.py"],
         files={k: k for k in ("build_criteria.py", "NEEC_Paper_v1_4.md", CANON)},
         stdout="build_criteria_output.txt", outputs={"criteria.json": "criteria.json"}),
    dict(name="build_summary_blocks.py stages the 23 summary blocks (D3(a))",
         cmd=["python", "build_summary_blocks.py"],
         files={k: S26.get(k, k) for k in KIT_BLOCK_INPUTS},
         stdout="build_summary_blocks_output.txt", outputs={"summary_blocks_s27.json": "summary_blocks_s27.json"}),
    dict(name="neec_entry.py validates the 23 staged blocks and prints the D13 inventory",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s27.json", "--corpus"],
         files={k: k for k in KIT_ENTRY_INPUTS}, stdout="neec_entry_corpus_output.txt"),
    dict(name="neec_entry.py, one entry with its D9 peer matrix (Ostrom-style commons governance)",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s27.json", "--entry", "OS"],
         files={k: k for k in KIT_ENTRY_INPUTS}, stdout="neec_entry_OS_output.txt"),
    dict(name="neec_entry.py self-test (Markdown round-trip; an altered vector is rejected)",
         cmd=["python", "neec_entry.py", "--selftest"],
         files={k: k for k in ("neec_entry.py", CANON, "neec_scores.csv")}, stdout="neec_entry_selftest_output.txt"),
    dict(name="neec_entry.py rejects the staged blocks against the Session 20 corpus (negative control; exit 1 expected)",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s27.json", "--corpus"],
         files={"neec_entry.py": "neec_entry.py", CANON: S20, "neec_scores.csv": S20_CSV,
                "summary_blocks_s27.json": "summary_blocks_s27.json"},
         stdout="neec_entry_negative_s20_output.txt", expect_exit=1),
    # --- Session 28: decisions D16-D19, and the claim register (current corpus) ---
    dict(name="stage_blocks_s28.py applies D17 and D18(a) to the staged blocks (nothing else changes)",
         cmd=["python", "stage_blocks_s28.py"], files={k: k for k in S28_STAGE_INPUTS},
         stdout="stage_blocks_s28_output.txt", outputs={"summary_blocks_s28.json": "summary_blocks_s28.json"}),
    dict(name="neec_entry.py validates the Session 28 blocks and prints the D13 inventory after D16-D18",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s28.json", "--corpus"],
         files={k: k for k in ("neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s28.json")},
         stdout="neec_entry_corpus_s28_output.txt"),
    dict(name="audit_claims_s28.py (the claim register of the eight documents not audited before; 222 claims)",
         cmd=["python", "audit_claims_s28.py"], files={k: S26.get(k, k) for k in S28_AUDIT_INPUTS},
         stdout="audit_claims_s28_output.txt"),
    # --- Session 29: the D14 landing (current corpus) ---
    dict(name="d14_landing_s29.py restates the eleven scoring documents from their Session 26 snapshots (D14; "
              "Doughnut Economics as the D14 pass left it)",
         cmd=["python", "d14_landing_s29.py", ".", "out"],
         files=dict({S26[d]: S26[d] for d in ELEVEN}, **{k: (ENTRY_S29 if k == "neec_entry.py" else k)
                                                          for k in D14_INPUTS}),
         stdout="d14_landing_s29_output.txt",
         outputs={"out/" + d: (DE_S29 if d == DE_DOC else d) for d in ELEVEN}),
    dict(name="verify_comparative_claims.py as of Session 29 (snapshot; the documents as the D14 pass left them)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: k for k in CLAIMS29_INPUTS}, **{"verify_comparative_claims.py": S29_CLAIMS, DE_DOC: DE_S29}),
         stdout="verify_claims_s29_output.txt"),
    dict(name="verify_comparative_claims.py as of Session 29 rejects the Session 26 documents (negative control; "
              "exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: k for k in CLAIMS29_INPUTS}, **{"verify_comparative_claims.py": S29_CLAIMS},
                    **{d: S26[d] for d in ELEVEN}),
         stdout="verify_claims_s29_negative_output.txt", expect_exit=1),
    dict(name="neec_entry.py reads the 23 summary blocks from the eleven documents and prints the D13 inventory",
         cmd=["python", "neec_entry.py"] + list(ELEVEN) + ["--corpus"],
         files=dict({k: k for k in ("neec_entry.py", CANON, "neec_scores.csv")}, **{d: d for d in ELEVEN}),
         stdout="neec_entry_documents_s29_output.txt"),
    # --- Session 30: D22, candidate mode and the corpus file (D23), the first blind replication kit (D24) ---
    dict(name="verify_doughnut.py (reconstructed in Session 30; the Doughnut Economics arithmetic and transcript)",
         cmd=["python", "verify_doughnut.py"],
         files={k: k for k in (CANON, "neec_scores.csv", "verify_doughnut.py", DE_DOC)},
         stdout="verify_doughnut_output.txt"),
    dict(name="restate_s30.py restates the Doughnut Economics Verification section from its Session 29 snapshot (D22)",
         cmd=["python", "restate_s30.py", ".", "out"],
         files={k: k for k in (DE_S29, "d14_landing_s29.py", "restate_s30.py")},
         stdout="restate_s30_output.txt", outputs={"out/" + DE_DOC: DE_DOC}),
    dict(name="verify_comparative_claims.py (Session 30: comparative claims in the eleven documents; current corpus)",
         cmd=["python", "verify_comparative_claims.py"], files={k: k for k in CLAIMS30_INPUTS},
         stdout="verify_claims_s30_output.txt"),
    dict(name="verify_comparative_claims.py rejects the Doughnut Economics document as the D14 pass left it "
              "(negative control; exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: k for k in CLAIMS30_INPUTS}, **{DE_DOC: DE_S29}),
         stdout="verify_claims_s30_negative_output.txt", expect_exit=1),
    dict(name="build_corpus_file.py writes neec_corpus.json from the canonical corpus and the eleven documents (D23)",
         cmd=["python", "build_corpus_file.py"],
         files=dict({k: k for k in ("build_corpus_file.py", "neec_entry.py", CANON, "neec_scores.csv")},
                    **{d: d for d in ELEVEN}),
         stdout="build_corpus_file_output.txt", outputs={"neec_corpus.json": "neec_corpus.json"}),
    dict(name="neec_entry.py candidate-mode self-test (a synthetic candidate; seven altered ones rejected)",
         cmd=["python", "neec_entry.py", "--selftest", "--candidate"], files={k: k for k in ENTRY30},
         stdout="neec_entry_selftest_candidate_output.txt"),
    dict(name="neec_entry.py --candidate rejects a canonical entry (negative control; exit 1 expected)",
         cmd=["python", "neec_entry.py", "--candidate", OS_DOC], files=dict({k: k for k in ENTRY30}, **{OS_DOC: OS_DOC}),
         stdout="neec_entry_candidate_negative_output.txt", expect_exit=1),
    dict(name="build_replication_kit.py OS builds the first blind replication kit (blind protocol, corpus, brief; "
              "leak scan; archive)",
         cmd=["python", "build_replication_kit.py", "OS", ".", "out"], files={k: k for k in KIT_INPUTS},
         stdout="build_replication_kit_OS_output.txt",
         outputs={KIT + "SCORING_PROTOCOL.md": "replication_kit_OS_SCORING_PROTOCOL.md",
                  KIT + "neec_corpus.json": "replication_kit_OS_neec_corpus.json",
                  KIT + "REPLICATION_BRIEF.md": "replication_kit_OS_REPLICATION_BRIEF.md"}),
    dict(name="pilot baseline: the original Ostrom entry validates as a candidate against the kit's corpus",
         cmd=["python", "neec_entry.py", "--candidate", OS_DOC],
         files={"neec_entry.py": "neec_entry.py", "neec_corpus.json": "replication_kit_OS_neec_corpus.json",
                OS_DOC: OS_DOC},
         stdout="neec_entry_candidate_OS_blind_output.txt"),
    # --- Session 32: the first pilot replication's return ---
    dict(name="compare_replication.py self-test in a kit's layout (synthetic replications; refusals; the statistics)",
         cmd=["python", "compare_replication.py", "--selftest"], files=dict(KIT_LAYOUT),
         stdout="compare_replication_selftest_output.txt"),
    dict(name="compare_replication.py: pilot 1, the replication against the original entry (protocol 11.4), "
              "and the replication record's tables and attributions (11.5)",
         cmd=["python", "compare_replication.py", OS_DOC, REPL_DOC, "--canonical-corpus", "neec_corpus_canonical.json",
              "--record", REPL_RECORD],
         files=dict(KIT_LAYOUT, **{"neec_corpus_canonical.json": "neec_corpus.json", OS_DOC: OS_DOC,
                                   REPL_DOC: REPL_DOC, REPL_RECORD: REPL_RECORD}),
         stdout="compare_replication_OS_pilot1_output.txt"),
    dict(name="the replication's block validates as a candidate against the kit's corpus, with its D9 peer matrix "
              "(the replicator's own check, re-run)",
         cmd=["python", "neec_entry.py", "--candidate", REPL_DOC],
         files={"neec_entry.py": "neec_entry.py", "neec_corpus.json": "replication_kit_OS_neec_corpus.json",
                REPL_DOC: REPL_DOC},
         stdout="neec_entry_candidate_OSR_output.txt"),
    dict(name="compare_replication.py refuses to run beside the canonical script (negative control; exit 1 expected)",
         cmd=["python", "compare_replication.py", "--selftest"], files=dict(KIT_LAYOUT, **{CANON: CANON}),
         stdout=EMPTY, stderr="compare_replication_canonical_refusal_stderr.txt", expect_exit=1),
    dict(name="d18b_reexpression_s32.py: decision D18(b), the Ostrom register re-expressed, and D26 with it "
              "(no file changes)",
         cmd=["python", "d18b_reexpression_s32.py"],
         files=dict({k: k for k in ENTRY30 + ("d18b_reexpression_s32.py", REPL_DOC)}, **{d: d for d in ELEVEN}),
         stdout="d18b_reexpression_s32_output.txt"),
    # --- Session 20 corpus (20 systems), via the pinned Session 20 snapshot ---
    dict(name="verify_ostrom.py as of Session 25 (Session 23; Session 20 corpus, Session 25 document)",
         cmd=["python", "verify_ostrom.py"],
         files={CANON: S20, "verify_ostrom.py": S25["verify_ostrom.py"],
                PENDING["verify_ostrom.py"]: S25[PENDING["verify_ostrom.py"]]},
         stdout=S25_OUT["verify_ostrom_output.txt"]),
    dict(name="verify_islamicfinance.py as of Session 25 (Session 22; Session 20 corpus, Session 25 document)",
         cmd=["python", "verify_islamicfinance.py"],
         files={CANON: S20, "verify_islamicfinance.py": S25["verify_islamicfinance.py"],
                PENDING["verify_islamicfinance.py"]: S25[PENDING["verify_islamicfinance.py"]]},
         stdout=S25_OUT["verify_islamicfinance_output.txt"]),
    dict(name="verify_qatar.py as of Session 25 (Session 21; Session 20 corpus, Session 25 document)",
         cmd=["python", "verify_qatar.py"],
         files={CANON: S20, "verify_qatar.py": S25["verify_qatar.py"],
                PENDING["verify_qatar.py"]: S25[PENDING["verify_qatar.py"]]},
         stdout=S25_OUT["verify_qatar_output.txt"]),
    dict(name="Session 20 canonical script (20 systems, full report)",
         cmd=["python", CANON], files={CANON: S20, BASELINE: BASELINE},
         stdout="session20_v2script_output.txt"),
    dict(name="Session 20 CSV builder regenerates the Session 20 CSV",
         cmd=["python", BUILDER], files={CANON: S20, BUILDER: S20_BUILDER},
         stdout="session20_csv_builder_output.txt",
         outputs={"neec_scores.csv": S20_CSV}),
    dict(name="Session 20 generator reproduces the Session 20 canonical files from the Session 16 files",
         cmd=["python", "insert_session20.py", ".", "out"],
         files={k: k for k in (S16, "neec_scores_csv_builder_v2_s16_snapshot.py", "insert_session20.py",
                               "verify_swf.py", "verify_china.py", "verify_singapore.py")},
         stdout=None,
         outputs={"out/" + CANON: S20, "out/" + BUILDER: S20_BUILDER}),
    dict(name="verify_insertion_s20.py (Session 20 insertion; Session 20 corpus)",
         cmd=["python", "verify_insertion_s20.py"],
         files=dict(S20_INPUTS, **{"verify_insertion_s20.py": "verify_insertion_s20.py"}),
         stdout="verify_insertion_s20_output.txt"),
    dict(name="run_a4_full_rerun_20.py (Appendix A.4; Session 20 corpus)",
         cmd=["python", "run_a4_full_rerun_20.py"],
         files={CANON: S20, BASELINE: BASELINE, "run_a4_full_rerun_20.py": "run_a4_full_rerun_20.py"},
         stdout="a4_rerun_20_raw_output.txt"),
    # --- Session 16 and earlier corpora ---
    dict(name="verify_singapore.py (Session 19; Session 16 corpus)",
         cmd=["python", "verify_singapore.py"],
         files={CANON: S16, "verify_singapore.py": "verify_singapore.py",
                "verify_swf.py": "verify_swf.py", "verify_china.py": "verify_china.py",
                "NEEC_StateCapitalism_Singapore_scoring_scratch.md":
                    S26["NEEC_StateCapitalism_Singapore_scoring_scratch.md"]},
         stdout="verify_singapore_output.txt"),
    dict(name="verify_china.py (Session 18; Session 16 corpus)",
         cmd=["python", "verify_china.py"],
         files={CANON: S16, "verify_china.py": "verify_china.py", "verify_swf.py": "verify_swf.py",
                "NEEC_StateCapitalism_China_scoring_scratch.md":
                    S26["NEEC_StateCapitalism_China_scoring_scratch.md"]},
         stdout="verify_china_output.txt"),
    dict(name="verify_swf.py (Session 17; Session 16 corpus)",
         cmd=["python", "verify_swf.py"],
         files={CANON: S16, "verify_swf.py": "verify_swf.py"},
         stdout="verify_swf_output.txt"),
    dict(name="Session 16 canonical script (17 systems, full report)",
         cmd=["python", CANON], files={CANON: S16, BASELINE: BASELINE},
         stdout="session16_v2script_output.txt"),
    dict(name="session16_full_analysis.py (Session 16 corpus)",
         cmd=["python", "session16_full_analysis.py"],
         files={CANON: S16, BASELINE: BASELINE,
                "session16_full_analysis.py": "session16_full_analysis.py"},
         stdout="session16_full_analysis_output.txt"),
    dict(name="regen_analysis_paper.py (Session 10; 15-system view, baseline absent as in the original run)",
         cmd=["python", "regen_analysis_paper.py"],
         files={CANON: VIEW15, S16: S16, "regen_analysis_paper.py": "regen_analysis_paper.py"},
         stdout="regen_verification_output_v16.txt"),
    dict(name="run_a4_full_rerun.py (Session 12 Appendix A.4 run; 15-system view)",
         cmd=["python", "run_a4_full_rerun.py"],
         files={CANON: VIEW15, S16: S16, "run_a4_full_rerun.py": "run_a4_full_rerun.py"},
         stdout="full_a4_rerun_raw_output.txt"),
    dict(name="verify_ubs.py (Session 15; 15-system view; output first captured in Session 20)",
         cmd=["python", "verify_ubs.py"],
         files={CANON: VIEW15, S16: S16, "verify_ubs.py": "verify_ubs.py"},
         stdout="verify_ubs_output.txt"),
    dict(name="verify_new_systems.py (Session 16; output first captured in Session 20)",
         cmd=["python", "verify_new_systems.py"],
         files={"verify_new_systems.py": "verify_new_systems.py"},
         stdout="verify_new_systems_output.txt"),
    dict(name="step1c_retrofit.py (Session 8; output first captured in Session 20)",
         cmd=["python", "step1c_retrofit.py"],
         files={"step1c_retrofit.py": "step1c_retrofit.py", BASELINE: BASELINE},
         stdout="step1c_retrofit_output.txt"),
    dict(name="neec_c14_crossvalidation.py (Appendix G Python reference) reproduces its CSV",
         cmd=["python", "neec_c14_crossvalidation.py"],
         files={"neec_c14_crossvalidation.py": "neec_c14_crossvalidation.py"}, stdout=None,
         outputs={"neec_c14_crossvalidation_run2_v4.1_results.csv":
                  "neec_c14_crossvalidation_run2_v4_1_results.csv"}),
    dict(name="neec_c14_v41_realjs_check.js (Appendix G, v4.1 source) reproduces its CSV",
         cmd=["node", "neec_c14_v41_realjs_check.js"],
         files={"neec_c14_v41_realjs_check.js": "neec_c14_v41_realjs_check.js"}, stdout=None,
         outputs={"neec_c14_v41_realjs_yearbyyear.csv": "neec_c14_v41_realjs_yearbyyear.csv"}),
    dict(name="neec_c14_v42_realjs_check.js (Appendix G, v4.2 source) reproduces its CSV",
         cmd=["node", "neec_c14_v42_realjs_check.js"],
         files={"neec_c14_v42_realjs_check.js": "neec_c14_v42_realjs_check.js"}, stdout=None,
         outputs={"neec_c14_v42_realjs_yearbyyear.csv": "neec_c14_v42_realjs_yearbyyear.csv"}),
]

CLAIMS33_INPUTS = CLAIMS30_INPUTS + ("restate_s33.py", "d18b_reexpression_s32.py")
S33_CHECKS = [
    # --- the current state: Session 33, decisions D18(b) and D26 ---
    dict(name="insert_session33.py writes both canonical scripts from their Session 32 snapshots (decision D26)",
         cmd=["python", "insert_session33.py", ".", "out"],
         files={k: k for k in (S32[CANON], S32[BUILDER], "insert_session33.py")},
         stdout="insert_session33_output.txt", outputs={"out/" + CANON: CANON, "out/" + BUILDER: BUILDER}),
    dict(name="Canonical script, current corpus (Session 33: 23 systems, full report)",
         cmd=["python", CANON], files={CANON: CANON, BASELINE: BASELINE}, stdout="session33_v2script_output.txt"),
    dict(name="CSV builder regenerates neec_scores.csv (Session 33)",
         cmd=["python", BUILDER], files={CANON: CANON, BUILDER: BUILDER},
         stdout="session33_csv_builder_output.txt", outputs={"neec_scores.csv": "neec_scores.csv"}),
    dict(name="verify_insertion_s33.py (one cell changed; CSV, corpus file and corpus consistent; negative tests)",
         cmd=["python", "verify_insertion_s33.py"],
         files={k: k for k in ("verify_insertion_s33.py", CANON, S32[CANON], "neec_scores.csv", S32["neec_scores.csv"],
                               "neec_corpus.json", S32["neec_corpus.json"])},
         stdout="verify_insertion_s33_output.txt"),
    dict(name="restate_s33.py restates seven scoring documents from their Session 32 snapshots (D18(b), D26)",
         cmd=["python", "restate_s33.py", ".", "out"],
         files=dict({S32[d]: S32[d] for d in S33_DOCS},
                    **{k: k for k in ("restate_s33.py", "d14_landing_s29.py", "d18b_reexpression_s32.py",
                                      "neec_entry.py", CANON, "neec_scores.csv")}),
         stdout="restate_s33_output.txt", outputs={"out/" + d: d for d in S33_DOCS}),
    dict(name="verify_comparative_claims.py (Session 33: comparative claims in the eleven documents; current corpus)",
         cmd=["python", "verify_comparative_claims.py"], files={k: k for k in CLAIMS33_INPUTS},
         stdout="verify_claims_s33_output.txt"),
    dict(name="verify_comparative_claims.py (Session 33) rejects the seven Session 32 documents (negative control; "
              "exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files={k: (S32[k] if k in S33_DOCS else k) for k in CLAIMS33_INPUTS},
         stdout="verify_claims_s33_negative_output.txt", expect_exit=1),
    dict(name="build_corpus_file.py writes neec_corpus.json from the Session 33 corpus and documents",
         cmd=["python", "build_corpus_file.py"],
         files=dict({k: k for k in ("build_corpus_file.py", "neec_entry.py", CANON, "neec_scores.csv")},
                    **{d: d for d in ELEVEN}),
         stdout="build_corpus_file_s33_output.txt", outputs={"neec_corpus.json": "neec_corpus.json"}),
    dict(name="neec_entry.py reads the 23 summary blocks from the eleven documents (Session 33) and prints the D13 "
              "inventory",
         cmd=["python", "neec_entry.py"] + list(ELEVEN) + ["--corpus"],
         files=dict({k: k for k in ("neec_entry.py", CANON, "neec_scores.csv")}, **{d: d for d in ELEVEN}),
         stdout="neec_entry_documents_s33_output.txt"),
    dict(name="verify_doughnut.py on the Session 33 corpus (the same captured output: D26 does not touch it)",
         cmd=["python", "verify_doughnut.py"],
         files={k: k for k in (CANON, "neec_scores.csv", "verify_doughnut.py", DE_DOC)},
         stdout="verify_doughnut_output.txt"),
]


# Session 34: Appendix A.4 on the Session 33 corpus (appended after the version 8 checks).
S34_CHECKS = [
    dict(name="run_a4_full_rerun_33.py (Appendix A.4, Session 33 corpus)",
         cmd=["python", "run_a4_full_rerun_33.py"],
         files={CANON: CANON, BASELINE: BASELINE, "run_a4_full_rerun_33.py": "run_a4_full_rerun_33.py"},
         stdout="a4_rerun_33_raw_output.txt"),
    dict(name="run_a4_full_rerun_33.py rejects the Session 32 corpus (negative control; exit 1 expected; its seven "
              "re-derived checks fail and nothing is written to stderr)",
         cmd=["python", "run_a4_full_rerun_33.py"],
         files={CANON: S32[CANON], BASELINE: BASELINE, "run_a4_full_rerun_33.py": "run_a4_full_rerun_33.py"},
         stdout="a4_rerun_33_negative_output.txt", stderr=EMPTY, expect_exit=1),
    dict(name="build_readme.py regenerates README.md from neec_scores.csv and this harness (the landing page "
              "cannot drift from the data)",
         cmd=["python", "build_readme.py"],
         files={k: k for k in ("build_readme.py", "neec_scores.csv", "run_all_checks.py", "SCORING_PROTOCOL.md",
                               "criteria.json")},
         stdout=None, outputs={"README.md": "README.md"}),
]


def pin32(chk):
    """A version 7 check, run against the Session 32 files: sources and reference outputs map to snapshots."""
    c = dict(chk)
    pin = {**S44, **S35, **S32}
    c["files"] = {dest: pin.get(src, src) for dest, src in chk["files"].items()}
    c["outputs"] = {prod: pin.get(ref, ref) for prod, ref in chk.get("outputs", {}).items()}
    if c["files"] != chk["files"] or c["outputs"] != chk.get("outputs", {}):
        c["name"] = chk["name"] + " [Session 32 state]"
    return c


def pin44(chk):
    """A Session 36-44 check, run against the files as they stood at tag s44 (sources and reference outputs)."""
    c = dict(chk)
    c["files"] = {dest: S44.get(src, src) for dest, src in chk["files"].items()}
    c["outputs"] = {prod: S44.get(ref, ref) for prod, ref in chk.get("outputs", {}).items()}
    if c["files"] != chk["files"] or c["outputs"] != chk.get("outputs", {}):
        c["name"] = chk["name"] + " [Session 44 state]"
    return c


# Session 35: revision R4's audit and decision D28 (appended after the version 9 checks).
S35_CHECKS = [
    dict(name="r4_audit_s35.py (revision R4: every corpus 1.0 on a multi-clause Pass Threshold, audited clause by "
              "clause; decision D28 and its bound; the record's tables; changes no file) [Session 35 state]",
         cmd=["python", "r4_audit_s35.py"],
         files={k: S35.get(k, k) for k in ("r4_audit_s35.py", "criteria.json", "neec_corpus.json", "neec_scores.csv",
                               "NEEC_Report_v1_6.md", "NEEC_R4_MultiClause_Audit_s35.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
                               "NEEC_IslamicFinance_scoring_scratch.md", "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="r4_audit_s35_output.txt", stderr=EMPTY),
]

# Session 36: protocol v2.0-draft.5, the corrected criteria.json, revision R8 (appended after the version 10 checks).
PROTO_DOCS = ("NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
              "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
              "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "NEEC_StateCapitalism_China_scoring_scratch.md",
              "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
              QA_DOC, IF_DOC, OS_DOC, REPL_DOC)
PROTO_INPUTS = ("verify_protocol_s36.py", "SCORING_PROTOCOL.md", "criteria.json", "neec_corpus.json", "neec_entry.py",
                "r4_audit_s35.py") + PROTO_DOCS
S36_CHECKS = [
    dict(name="build_criteria.py (Session 36) generates criteria.json and corrects it: every anchor threshold is its "
              "definition's Pass Threshold (D28(g)); C3.2's bands carry D26 (R3)",
         cmd=["python", "build_criteria.py"],
         files={k: k for k in ("build_criteria.py", "NEEC_Paper_v1_4.md", CANON)},
         stdout="build_criteria_s36_output.txt", outputs={"criteria.json": "criteria.json"}),
    dict(name="build_replication_kit.py --selftest-r8: revision R8 on protocol draft.5 (no kit built; the first kit's "
              "3.1 marker is one R8 refuses)",
         cmd=["python", "build_replication_kit.py", "--selftest-r8", "."],
         files={k: k for k in ("build_replication_kit.py", "SCORING_PROTOCOL.md", "SCORING_PROTOCOL_s35_snapshot.md")},
         stdout="build_replication_kit_r8_selftest_output.txt", stderr=EMPTY),
    dict(name="verify_protocol_s36.py: the protocol's statements about the corpus, its archetype table, register and "
              "Appendix B (draft.5)",
         cmd=["python", "verify_protocol_s36.py"], files={k: k for k in PROTO_INPUTS},
         stdout="verify_protocol_s36_output.txt", stderr=EMPTY),
    dict(name="verify_protocol_s36.py rejects protocol draft.4 (negative control; exit 1 expected; its stale "
              "statements fail and nothing is written to stderr)",
         cmd=["python", "verify_protocol_s36.py"],
         files=dict({k: k for k in PROTO_INPUTS}, **{"SCORING_PROTOCOL.md": S35["SCORING_PROTOCOL.md"]}),
         stdout="verify_protocol_s36_negative_output.txt", stderr=EMPTY, expect_exit=1),
]

# Session 37: the rescoring pass, part (a) (appended after the version 11 checks).
S37_CHECKS = [
    dict(name="rescoring_s37.py: rescoring pass part (a), the 33 stated-shortfall 1.0s re-estimated clause by clause "
              "(D28, D31); consequences computed, no corpus file changed",
         cmd=["python", "rescoring_s37.py"],
         files={k: k for k in ("rescoring_s37.py", "r4_audit_s35.py", "criteria.json", "neec_corpus.json",
                               "NEEC_Rescoring_s37.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s37_output.txt", stderr=EMPTY),
]

# Session 38: the rescoring pass, part (b), first group (appended after the version 12 checks).
S38_CHECKS = [
    dict(name="rescoring_s38.py: rescoring pass part (b), first group, the 29 units of C3.4, C5.3, C2.4, C1.3 and "
              "C2.3 re-estimated clause by clause (D28, D31); consequences with part (a), no corpus file changed",
         cmd=["python", "rescoring_s38.py"],
         files={k: k for k in ("rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py", "criteria.json",
                               "neec_corpus.json", "NEEC_Rescoring_s38.md", "cco_simulation_checks_s38_output.txt",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s38_output.txt", stderr=EMPTY),
]

# Session 39: the rescoring pass, part (b), second group (appended after the version 13 checks).
S39_CHECKS = [
    dict(name="rescoring_s39.py: rescoring pass part (b), second group, C5.1 clause 2 on 11 units and C3.1's 5 "
              "units re-estimated clause by clause (D28); consequences with parts (a) and (b1), no corpus file changed",
         cmd=["python", "rescoring_s39.py"],
         files={k: k for k in ("rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py",
                               "criteria.json", "neec_corpus.json", "NEEC_Rescoring_s39.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s39_output.txt", stderr=EMPTY),
]

# Session 40: the rescoring pass, part (b), third group (appended after the version 14 checks).
S40_CHECKS = [
    dict(name="rescoring_s40.py: rescoring pass part (b), third group, C1.1's 9 units re-estimated clause by clause "
              "(D28), CCO's against the design's pinned simulation; consequences with parts (a), (b1) and (b2), no "
              "corpus file changed",
         cmd=["python", "rescoring_s40.py"],
         files={k: k for k in ("rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py",
                               "r4_audit_s35.py", "criteria.json", "neec_corpus.json", "NEEC_Rescoring_s40.md",
                               "cco_simulation_checks_s40_output.txt",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s40_output.txt", stderr=EMPTY),
]

# Session 41: the rescoring pass, part (b), fourth group (appended after the version 15 checks).
S41_CHECKS = [
    dict(name="rescoring_s41.py: rescoring pass part (b), fourth group, the 11 units of C1.4, C2.1 and C3.2 "
              "re-estimated clause by clause (D28); consequences with parts (a) to (b3), no corpus file changed",
         cmd=["python", "rescoring_s41.py"],
         files={k: k for k in ("rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py",
                               "rescoring_s37.py", "r4_audit_s35.py", "criteria.json", "neec_corpus.json",
                               "NEEC_Rescoring_s41.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s41_output.txt", stderr=EMPTY),
]

# Session 42: the rescoring pass, part (b), fifth group (appended after the version 16 checks).
S42_CHECKS = [
    dict(name="rescoring_s42.py: rescoring pass part (b), fifth group, C2.5's 10 units re-estimated clause by "
              "clause (D28); consequences with parts (a) to (b4), no corpus file changed",
         cmd=["python", "rescoring_s42.py"],
         files={k: k for k in ("rescoring_s42.py", "rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py",
                               "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py", "criteria.json",
                               "neec_corpus.json", "NEEC_Rescoring_s42.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s42_output.txt", stderr=EMPTY),
]

# Session 43: the rescoring pass, part (b), sixth group (appended after the version 17 checks).
S43_CHECKS = [
    dict(name="rescoring_s43.py: rescoring pass part (b), sixth group, the 10 units of C3.5 and C4.1 re-estimated "
              "clause by clause (D28); consequences with parts (a) to (b5), no corpus file changed",
         cmd=["python", "rescoring_s43.py"],
         files={k: k for k in ("rescoring_s43.py", "rescoring_s42.py", "rescoring_s41.py", "rescoring_s40.py",
                               "rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py",
                               "criteria.json", "neec_corpus.json", "NEEC_Rescoring_s43.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s43_output.txt", stderr=EMPTY),
]

# Session 44: the criteria review's evidence tables (appended after the version 18 checks).
S44_CHECKS = [
    dict(name="criteria_review_s44.py: the criteria review's evidence tables (norm weights, quantities scored in more "
              "than one Pass Threshold, their corpus agreement, Requirement figures differing from a Pass Threshold)",
         cmd=["python", "criteria_review_s44.py"],
         files={k: k for k in ("criteria_review_s44.py", "criteria.json", "neec_corpus.json")},
         stdout="criteria_review_s44_output.txt", stderr=EMPTY),
]

# Session 45: the v2.0 criteria (appended after the version 19 checks).
V2_INPUTS = ("build_criteria.py", "criteria_s44_snapshot.json", "SCORING_PROTOCOL_s44_snapshot.md",
             "NEEC_Criteria_v2_s45.md")
S45_CHECKS = [
    dict(name="build_criteria.py (version 2.3) builds criteria.json v2.0, 29 criteria, from the pinned Session 44 "
              "criteria and the record's Appendix V, asserts rules A1-A7, and regenerates the protocol as draft.9",
         cmd=["python", "build_criteria.py"], files={k: k for k in V2_INPUTS},
         stdout="build_criteria_s50_output.txt", stderr=EMPTY,
         outputs={"criteria.json": "criteria.json", "SCORING_PROTOCOL.md": "SCORING_PROTOCOL.md"}),
    dict(name="build_criteria.py --selftest: each of rules A1-A7 rejects a planted violation, and the clean v2.0 "
              "document passes (negative control)",
         cmd=["python", "build_criteria.py", "--selftest"], files={k: k for k in V2_INPUTS},
         stdout="build_criteria_s46_selftest_output.txt", stderr=EMPTY),
    dict(name="criteria_v2_s45.py: the v2.0 record's evidence tables (figure scan, norm weights, units by revision "
              "class, registered quantities, C4.6's clause 3 bar from the World Justice Project's data)",
         cmd=["python", "criteria_v2_s45.py"],
         files={k: k for k in ("criteria_v2_s45.py", "criteria_s44_snapshot.json", "criteria.json",
                               "NEEC_Criteria_v2_s45.md", "neec_corpus.json", "wjp_rol_sf62_2012_2025.csv")},
         stdout="criteria_v2_s45_output.txt", stderr=EMPTY),
]

# Session 47: part (b)'s seventh group, on the v2.0 clauses (appended after the version 21 checks). It reads the
# v2.0 criteria.json for the clauses and criteria_s44_snapshot.json for the published structure. Since Session 48
# (decision 48.3 moved C4.4 to class M) it reads criteria.json as it stood at tag s47, criteria_s47_snapshot.json.
S47_CHECKS = [
    dict(name="rescoring_s47.py: rescoring pass part (b), seventh group, the 10 units of C4.2 and C4.4 on the v2.0 "
              "clauses, with part (a)'s 3 units of those criteria re-read (D28); consequences with parts (a) to (b6), "
              "no corpus file changed [Session 47 criteria]",
         cmd=["python", "rescoring_s47.py"],
         files={k: k for k in ("rescoring_s47.py", "rescoring_s43.py", "rescoring_s42.py", "rescoring_s41.py",
                               "rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py",
                               "r4_audit_s35.py", "criteria_s44_snapshot.json", "neec_corpus.json",
                               "NEEC_Rescoring_s47.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s47_output.txt", stderr=EMPTY),
]
S47_CHECKS[0]["files"]["criteria.json"] = "criteria_s47_snapshot.json"

# Session 48: C4.4 re-read on decision 48.3, and the score ledger (appended after the version 22 checks). It reads the
# v2.0 criteria.json (with 48.3) and criteria_s47_snapshot.json side by side, so it is not pinned.
S48_CHECKS = [
    dict(name="rescoring_s48.py: C4.4's six units in the pass re-read on decision 48.3's measure (D28), Nordic Social "
              "Democracy's clause 1 bound, consequences with parts (a) to (b7), and the score ledger; no corpus file "
              "changed",
         cmd=["python", "rescoring_s48.py"],
         files={k: k for k in ("rescoring_s48.py", "rescoring_s47.py", "rescoring_s43.py", "rescoring_s42.py",
                               "rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py",
                               "rescoring_s37.py", "r4_audit_s35.py", "criteria.json", "criteria_s47_snapshot.json",
                               "criteria_s44_snapshot.json", "neec_corpus.json", "neec_scores.csv",
                               "NEEC_Report_v1_6.md", "NEEC_Rescoring_s48.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s48_output.txt", stderr=EMPTY),
]


def tree(*roots):
    """Every file under the given directories here, each mapped to itself (the copy keeps the subdirectories)."""
    out = {}
    for root in roots:
        for r, _, fs in os.walk(os.path.join(HERE, root)):
            for f in fs:
                rel = os.path.relpath(os.path.join(r, f), HERE).replace(os.sep, "/")
                out[rel] = rel
    return dict(sorted(out.items()))


# Session 49: the public site (appended after the version 23 checks). build_site.py --check rebuilds docs/ in its own
# temporary directory from its inputs and site/, and compares the result with docs/, which is copied in whole.
S49_CHECKS = [
    dict(name="build_site.py --check: the public site docs/ equals what build_site.py generates from criteria.json, "
              "the corpus, the record, Paper v1.4, the A.4 weighting script, the WJP extract, the issue forms and "
              "site/ (decision 49.7)",
         cmd=["python", "build_site.py", "--check"],
         files={**{k: k for k in ("build_site.py", "criteria.json", "neec_corpus_v2.json", "neec_scores_v2.csv",
                                  "summary_blocks_v2.json", "NEEC_Criteria_v2_s45.md", "NEEC_Paper_v1_4.md",
                                  "wjp_rol_sf62_2012_2025.csv", "neec_weighting_robustness_analysis_v2.py")},
                **tree("site", "docs", "evidence", os.path.join(".github", "ISSUE_TEMPLATE"))},
         stdout="build_site_check_output.txt", stderr=EMPTY, show_stdout=True),
]
S49_CHECKS.append(dict(S49_CHECKS[0], files={**S49_CHECKS[0]["files"], "docs/index.html": "docs/404.html"},
                       name="build_site.py --check rejects a docs/ whose home page is replaced by another page "
                            "(negative control; exit 1 expected)",
                       stdout="build_site_check_negative_output.txt", expect_exit=1))

# Session 49: part (b)'s eighth group, C4.3 and C4.5 on the v2.0 clauses, cumulative with parts (a) to (b7) and
# decision 48.3 (appended after the site checks). It reads the v2.0 criteria.json, so it is not pinned.
S49_CHECKS.append(
    dict(name="rescoring_s49.py: rescoring pass part (b), eighth group, the 9 units of C4.3 and C4.5 on the v2.0 "
              "clauses, CCO-PTF-CIP-SZH's C4.3 re-checked as class M, and part (a)'s 3 units of C4.5 re-read (D28); "
              "Nordic Social Democracy's C4.3 from Eurostat; consequences with parts (a) to (b7) and 48.3, and the "
              "score ledger; no corpus file changed",
         cmd=["python", "rescoring_s49.py"],
         files={k: k for k in ("rescoring_s49.py", "rescoring_s48.py", "rescoring_s47.py", "rescoring_s43.py",
                               "rescoring_s42.py", "rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py",
                               "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py", "criteria.json",
                               "criteria_s47_snapshot.json", "criteria_s44_snapshot.json", "neec_corpus.json",
                               "neec_scores.csv", "NEEC_Report_v1_6.md", "NEEC_Rescoring_s49.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md", "NEEC_Georgism_LVT_scoring_scratch.md",
                               "NEEC_MutualCredit_LETS_scoring_scratch.md", "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s49_output.txt", stderr=EMPTY))

# Session 50: the Jev pilot of 2026-09-25, an automated interpretation check (decisions 50.1 to 50.5, from the
# package prepared in a chat session, NEEC_Jev_Pilot_Package_s50.md). jev_pilot_check.py reads the recorded requests
# and responses only (no network call) and the pass records of Sessions 37 to 48, so it takes their files.
S50_CHECKS = [
    dict(name="jev_pilot_check.py: the Jev pilot (jev-1.13.0), an automated interpretation check, not a replication: "
              "every recorded response present and pinned, every state equal to its source or a declared edit, and "
              "the comparison with the pass's clause statuses (decision 50.1)",
         cmd=["python", "jev_pilot_check.py"],
         files={**S48_CHECKS[0]["files"],
                **{k: k for k in ("jev_pilot_check.py", "jev_pilot_2026-09-25.json")}},
         stdout="jev_pilot_check_output.txt", stderr=EMPTY, show_summary=True),
]

# Session 50: part (b)'s ninth and last group, C5.2, C5.4 and C5.5 on the v2.0 clauses, cumulative with parts (a) to
# (b8) and decision 48.3, and the interpretation check run on it (decision 50.2). Both read the v2.0 criteria.json.
S50_FILES = {**S49_CHECKS[2]["files"], **{k: k for k in ("rescoring_s50.py", "NEEC_Rescoring_s50.md")}}
S50_CHECKS.append(
    dict(name="rescoring_s50.py: rescoring pass part (b), ninth and last group, the 8 units of C5.2, C5.4 and C5.5 on "
              "the v2.0 clauses, part (a)'s 2 units of C5.2 re-read, and Status Quo's C5.2 re-checked as class M "
              "(D28); Nordic Social Democracy's C5.4 from the ISSP 2016 figures; consequences with parts (a) to (b8) "
              "and 48.3, and the score ledger; no corpus file changed",
         cmd=["python", "rescoring_s50.py"], files=S50_FILES,
         stdout="rescoring_s50_output.txt", stderr=EMPTY))
S50_CHECKS.append(
    dict(name="jev_s50_check.py: the interpretation check on part (b)'s ninth group (jev-1.13.0, flag-only): every "
              "request rebuilt from its sources equals the recorded one, every located-evidence excerpt is in the "
              "unit's estimates, and each answer is compared with the pass's clause status (decisions 50.2 to 50.4)",
         cmd=["python", "jev_s50_check.py"],
         files={**S50_FILES, **{k: k for k in ("jev_s50_check.py", "jev_s50_2026-09-25.json", "jev_pilot_check.py",
                                               "NEEC_IslamicFinance_scoring_scratch.md",
                                               "NEEC_MutualCredit_LETS_scoring_scratch.md")}},
         stdout="jev_s50_check_output.txt", stderr=EMPTY, show_summary=True))

# Session 51: stage 2's first group, the design's modelled units on its published model at v4.20 (5a7a7b1), cumulative
# with parts (a) and (b) and decision 48.3. It reads the captured output of cco_simulation_checks_s51.js, not the
# JavaScript, which needs the simulation's source.
S51_FILES = {**S50_FILES, **{k: k for k in ("rescoring_s51.py", "NEEC_Rescoring_s51.md",
                                            "cco_simulation_checks_s51_output.txt")}}
S51_CHECKS = [
    dict(name="rescoring_s51.py: rescoring pass stage 2, group 2.1, CCO-PTF-CIP-SZH's units that rest on the design's "
              "own modelling on its published model at v4.20: a scan of every published 1.0, C1.2b, C1.4, C3.2, C3.3 and "
              "C5.3 re-read and C1.1 re-checked as class I (D28); the design's other re-estimated units against v4.20; "
              "the simulation runs' capture by digest; consequences with parts (a) and (b) and 48.3, and the score "
              "ledger; no corpus file changed",
         cmd=["python", "rescoring_s51.py"], files=S51_FILES,
         stdout="rescoring_s51_output.txt", stderr=EMPTY),
]

# Session 52: the shared pass module (decision 52.5) and the consequence triage (decision 52.7). Both read the pass
# cumulatively through group 2.1 and change no file and no score.
S52_FILES = {**S51_FILES, **{k: k for k in ("pass_common.py", "triage_s52.py", "neec_scores.csv")}}
S52_CHECKS = [
    dict(name="pass_common.py --selftest: the pass's shared module reproduces the pass's rules (tier, ranks, D28) and "
              "group 2.1's consequences table, ledger, dominance line and anchors line verbatim",
         cmd=["python", "pass_common.py", "--selftest"], files=S52_FILES,
         stdout="pass_common_selftest_output.txt", stderr=EMPTY),
    dict(name="triage_s52.py: the consequence triage (W6): which units not yet read could change a failure count, an "
              "adequacy tier or a rank on their own, the entries and criteria by that, the order of groups, the units "
              "that could change none",
         cmd=["python", "triage_s52.py"], files=S52_FILES,
         stdout="triage_s52_output.txt", stderr=EMPTY),
]

# Session 53: group 2.2, C1.2a re-read as class M, on the shared module. pass_common.PARTS now includes it, so the
# Session 52 checks load its files too. It reads the captured output of cco_c12a_checks_s53.js, not the JavaScript.
S53_FILES = {**S52_FILES, **{k: k for k in ("rescoring_s53.py", "NEEC_Rescoring_s53.md",
                                            "cco_c12a_checks_s53_output.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S53_FILES
S53_CHECKS = [
    dict(name="rescoring_s53.py: rescoring pass stage 2, group 2.2, C1.2a Wealth Building for Resilience re-read as "
              "class M (all 23 units): v2.0's price basis recomputed, the design's unit on its published model (the "
              "runs' capture by digest), the rule with 0.0 on a stated whole-criterion reason (53.2), consequences "
              "cumulatively with every part before it; no corpus file changed",
         cmd=["python", "rescoring_s53.py"], files=S53_FILES,
         stdout="rescoring_s53_output.txt", stderr=EMPTY),
]

# Session 54: group 2.3, C1.3 re-read as class M, on the shared module. pass_common.PARTS now includes it, so the
# Session 52 checks load its files too. It reads the captured output of cco_c13_checks_s54.js, not the JavaScript.
S54_FILES = {**S53_FILES, **{k: k for k in ("rescoring_s54.py", "NEEC_Rescoring_s54.md",
                                            "cco_c13_checks_s54_output.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S54_FILES
S54_CHECKS = [
    dict(name="rescoring_s54.py: rescoring pass stage 2, group 2.3, C1.3 Housing Security re-read as class M (the 20 "
              "units not yet re-estimated): the figures the readings derive recomputed, the design's unit on its "
              "published model (the runs' capture by digest), the rule with 0.0 on a stated whole-criterion reason "
              "(53.2), consequences cumulatively with every part before it; no corpus file changed",
         cmd=["python", "rescoring_s54.py"], files=S54_FILES,
         stdout="rescoring_s54_output.txt", stderr=EMPTY),
]

# Session 56: group 2.4, C3.5 read as class I, on the shared module. pass_common.PARTS now includes it, so the Session 52
# checks load its files too. It reads the sources the session added to the evidence cache, not the network.
S56_FILES = {**S54_FILES, **{k: k for k in ("rescoring_s56.py", "NEEC_Rescoring_s56.md")},
             **{"evidence_cache/C3.5/" + k: "evidence_cache/C3.5/" + k
                for k in ("imf_ffs_rows_s56.json", "gao_fy2024_govexec.txt", "cnao_rectification_2023.txt",
                          "cnao_rectification_2024.txt", "cnao_rectification_2025.txt", "riksrevisionen_ar2020.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S56_FILES
S56_CHECKS = [
    dict(name="rescoring_s56.py: rescoring pass stage 2, group 2.4, C3.5 Failure-Mode Transparency read as class I (the "
              "20 units not yet re-estimated): the sources added to the evidence cache by digest and every passage "
              "quoted, clause 4 recomputed from the IMF rows, the rule with 0.0 on a stated whole-criterion reason "
              "(53.2), consequences cumulatively with every part before it; no corpus file changed",
         cmd=["python", "rescoring_s56.py"], files=S56_FILES,
         stdout="rescoring_s56_output.txt", stderr=EMPTY),
]

# Session 57: group 2.5, CCO-PTF-CIP-SZH's simulation units re-read on the design's published model at v5.6.0 (d10ed6e;
# decision 57.3), on the shared module. pass_common.PARTS now includes it, so the Session 52 checks load its files too. It
# reads the captured output of cco_sim_v56_checks_s57.js, not the JavaScript, which needs the simulation's source.
S57_FILES = {**S56_FILES, **{k: k for k in ("rescoring_s57.py", "NEEC_Rescoring_s57.md",
                                            "cco_sim_v56_checks_s57_output.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S57_FILES
S57_CHECKS = [
    dict(name="rescoring_s57.py: rescoring pass stage 2, group 2.5, CCO-PTF-CIP-SZH's nine simulation units re-read on "
              "the design's published model at v5.6.0: the runs' capture by digest, the release's figures reproduced, "
              "every figure quoted found in it, the reopening conditions evaluated, the rule, consequences cumulatively "
              "with every part before it; no corpus file changed",
         cmd=["python", "rescoring_s57.py"], files=S57_FILES,
         stdout="rescoring_s57_output.txt", stderr=EMPTY),
]

# Session 58: the owner's decision 58.1 as part "58.1" (owner_s58.py) and group 2.6, C5.2 re-read as class M, on the
# shared module. pass_common.PARTS now includes both, so the Session 52 checks load their files too.
S58_FILES = {**S57_FILES, **{k: k for k in ("owner_s58.py", "rescoring_s58.py", "NEEC_Rescoring_s58.md")}}
for _c in S52_CHECKS:
    _c["files"] = S58_FILES
S58_CHECKS = [
    dict(name="rescoring_s58.py: rescoring pass stage 2, group 2.6, C5.2 Staged Transition Pathways re-read as class M "
              "(the 16 units not yet re-estimated): the precedents' stages and spans recomputed, the clauses not "
              "estimated tied to the clause fixing each verdict, the owner's part 58.1 checked against the runs' "
              "capture, the rule with 0.0 on a stated whole-criterion reason (53.2), consequences cumulatively with "
              "every part before it; no corpus file changed",
         cmd=["python", "rescoring_s58.py"], files=S58_FILES,
         stdout="rescoring_s58_output.txt", stderr=EMPTY),
]

# Session 60: group 2.7, C1.4 read as class I, on the shared module. pass_common.PARTS now includes it, so the Session 52
# checks load its files too. It reads the evidence cache Session 59 built and the two extracts Session 60 added, and the
# scoring documents the cache's index names, not the network.
S60_FILES = {**S58_FILES, **{k: k for k in ("rescoring_s60.py", "NEEC_Rescoring_s60.md", "NEEC_Report_v1_6.md",
                                            "NEEC_StateCapitalism_China_scoring_scratch.md",
                                            "NEEC_DoughnutEconomics_scoring_scratch.md",
                                            "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                                            "NEEC_MutualCredit_LETS_scoring_scratch.md",
                                            "NEEC_Ostrom_Commons_scoring_scratch.md",
                                            "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
                                            "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                                            "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                                            "NEEC_UniversalBasicServices_scoring_scratch.md")},
             **{"evidence_cache/C1.4/" + k: "evidence_cache/C1.4/" + k
                for k in ("index.json", "wb_pip_methods.txt", "wb_final_consumption.txt", "wb_final_consumption_kd.txt",
                          "wb_fce_kd_metadata.txt", "integral_wp_v01_extract.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S60_FILES
S60_CHECKS = [
    dict(name="rescoring_s60.py: rescoring pass stage 2, group 2.7, C1.4 Automation Resilience read as class I (the 20 "
              "units not yet re-estimated): the evidence cache's files by digest and every passage quoted, each "
              "published rationale located by the cache's index, the measure's reading (60.1), the rule with 0.0 on a "
              "stated whole-criterion reason (53.2), consequences cumulatively with every part before it; no corpus "
              "file changed",
         cmd=["python", "rescoring_s60.py"], files=S60_FILES,
         stdout="rescoring_s60_output.txt", stderr=EMPTY),
]

# Session 61: group 2.8, C4.3 re-read as class M, on the shared module. pass_common.PARTS now includes it, so the Session
# 52 checks load its files too. It reads the three files it added to the evidence cache and the scoring documents holding
# the units' rationales, not the network.
S61_FILES = {**S60_FILES, **{k: k for k in ("rescoring_s61.py", "NEEC_Rescoring_s61.md")},
             **{"evidence_cache/C4.3/" + k: "evidence_cache/C4.3/" + k
                for k in ("us_census_h05_extract.txt", "sg_ghs2025_table6_1.txt", "integral_wp_v01_c43_extract.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S61_FILES
S61_CHECKS = [
    dict(name="rescoring_s61.py: rescoring pass stage 2, group 2.8, C4.3 Group Equity re-read as class M (the 16 units "
              "not yet re-estimated): the evidence cache's files by digest and every passage quoted, every gap quoted "
              "recomputed from the cache, each published rationale located, the rule with 0.0 on a stated "
              "whole-criterion reason (53.2, 61.1), consequences cumulatively with every part before it; no corpus file "
              "changed",
         cmd=["python", "rescoring_s61.py"], files=S61_FILES,
         stdout="rescoring_s61_output.txt", stderr=EMPTY),
]

# Session 63: group 2.9, C3.1 read as class I, on the shared module. pass_common.PARTS now includes it, so the Session
# 52 checks load its files too. It reads the ten data files it added to the evidence cache, Session 62's index and the
# scoring documents holding the units' rationales, not the network.
S63_FILES = {**S61_FILES, **{k: k for k in ("rescoring_s63.py", "NEEC_Rescoring_s63.md",
                                             "NEEC_Georgism_LVT_scoring_scratch.md",
                                             "NEEC_MutualCredit_LETS_scoring_scratch.md")},
             **{"evidence_cache/C3.1/" + k: "evidence_cache/C3.1/" + k
                for k in ("index.json", "fred_benefits_annual.csv", "fred_realgdp_annual.csv",
                          "fred_benefits_monthly.csv", "fred_claims_weekly.csv", "sdg131_840.json", "sdg131_156.json",
                          "sdg131_702.json", "sdg131_634.json", "sdg131_578.json", "cares_act_wikipedia_lead.txt")}}
for _c in S52_CHECKS:
    _c["files"] = S63_FILES
S63_CHECKS = [
    dict(name="rescoring_s63.py: rescoring pass stage 2, group 2.9, C3.1 Crisis Response Capacity read as class I (the "
              "16 units not yet re-estimated): the evidence cache's data files by digest and every passage quoted, every "
              "figure quoted recomputed from the cache, each published rationale located and unchanged since the "
              "cache's index, the rule with 0.0 on a stated whole-criterion reason (53.2, 63.1), consequences "
              "cumulatively with every part before it; no corpus file changed",
         cmd=["python", "rescoring_s63.py"], files=S63_FILES,
         stdout="rescoring_s63_output.txt", stderr=EMPTY),
]

# Session 64: group 2.10, C4.2 read as class M, on the shared module. pass_common.PARTS now includes it, so the Session
# 52 checks load its files too. It reads the two data files it added to the evidence cache and the scoring documents
# holding the units' rationales, not the network.
S64_FILES = {**S63_FILES, **{k: k for k in ("rescoring_s64.py", "NEEC_Rescoring_s64.md")},
             **{"evidence_cache/C4.2/" + k: "evidence_cache/C4.2/" + k
                for k in ("owid_gcb_consumption_co2.csv", "owid_iucn_red_list_index.csv")}}
for _c in S52_CHECKS:
    _c["files"] = S64_FILES
S64_CHECKS = [
    dict(name="rescoring_s64.py: rescoring pass stage 2, group 2.10, C4.2 Ecological Compliance re-read as class M (the "
              "16 units not yet re-estimated): the evidence cache's two data files by digest and the rows quoted, every "
              "rate and index change quoted recomputed from the cache, each published rationale located, the rule with "
              "0.0 on a stated whole-criterion reason (53.2, 64.2), consequences cumulatively with every part before "
              "it; no corpus file changed",
         cmd=["python", "rescoring_s64.py"], files=S64_FILES,
         stdout="rescoring_s64_output.txt", stderr=EMPTY),
]

# Session 65: the accelerated groups, one script (rescoring_s65.py), on the shared module. pass_common.PARTS includes it, so the
# Session 52 checks load its files too. It reads the data files it added to the evidence cache (C1.1, C2.6, C3.6, C4.1, C4.4),
# the scoring documents holding the units' rationales and wjp_rol_sf62_2012_2025.csv, not the network.
S65_FILES = {**S64_FILES, **{k: k for k in ("rescoring_s65.py", "NEEC_Rescoring_s65.md", "wjp_rol_sf62_2012_2025.csv")},
             **{"evidence_cache/" + k: "evidence_cache/" + k
                for k in ("C4.1/imf_weo_gross_debt_pct_gdp.json", "C4.1/wb_gross_savings_pct_gni.json",
                          "C4.1/wb_consumption_fixed_capital_pct_gni.json", "C4.4/owid_vdem_regimes_of_the_world.csv",
                          "C1.1/wb_societal_poverty_rate.json", "C2.6/owid_freedom_house_civil_liberties_rating.csv",
                          "C3.6/pwt1001_selected_economies.csv")}}
for _c in S52_CHECKS:
    _c["files"] = S65_FILES
S65_CHECKS = [
    dict(name="rescoring_s65.py: rescoring pass stage 2, the accelerated groups (C4.1, C4.4, C3.4, C4.5, C2.5, C1.1, C2.1, "
              "C2.4, C2.3: the 128 units not yet re-estimated, and the three new criteria C2.6, C3.6, C4.6: 69 units): the "
              "evidence cache's data files by digest, every figure quoted recomputed from them, each published rationale "
              "located, the rule with 0.0 on a stated whole-criterion reason (53.2), consequences cumulatively with every "
              "part before it, and the record compared byte for byte with the one the script generates; no corpus file "
              "changed",
         cmd=["python", "rescoring_s65.py"], files=S65_FILES,
         stdout="rescoring_s65_output.txt", stderr=EMPTY),
]

# Session 65, stage 3: the generator that applies the pass. It reads neec_corpus.json (the published vectors the pass was computed
# against), the pass's parts through pass_common.py, summary_blocks_s28.json and the record, and checks the three v2 files it wrote.
S65B_FILES = {**S65_FILES, **{k: k for k in ("apply_pass_s65.py", "neec_corpus_v2_s65_snapshot.json",
                                             "neec_scores_v2_s65_snapshot.csv", "summary_blocks_v2_s65_snapshot.json",
                                             "summary_blocks_s28.json")}}
S65_CHECKS.append(
    dict(name="apply_pass_s65.py --check: stage 3, the generator that applies the rescoring pass: the 23 entries on the 29 "
              "criteria (neec_corpus_v2_s65_snapshot.json), their totals, domain sums, failures and tiers "
              "(neec_scores_v2_s65_snapshot.csv) and the site's blocks (summary_blocks_v2_s65_snapshot.json), kept as the "
              "Session 65 files, equal what the pass produces from the published vectors; the 26 "
              "criteria's final scores are the pass's final state; each total on the 29 is the pass's total on the 26 plus "
              "the three new units; the record's table on the 29 shows the same totals and ranks; no published file changed",
         cmd=["python", "apply_pass_s65.py", "--check"], files=S65B_FILES,
         stdout="apply_pass_s65_output.txt", stderr=EMPTY))

# Session 68: the per-system evidence reports (decision 68.1). build_evidence.py --check rebuilds the 24 files of evidence/ in
# memory from the pass (through pass_common.py), the v2 corpus, scores and blocks, criteria.json, the scoring documents and records
# and the evidence cache, and compares them with evidence/, which is copied in whole.
S68_FILES = {**S65B_FILES, **{k: k for k in ("build_evidence.py", "site/config.json")},
             **{f: f for f in sorted(os.listdir(HERE)) if f.startswith("NEEC_Rescoring_s") and f.endswith(".md")},
             **tree("evidence_cache", "evidence")}
S68_CHECKS = [
    dict(name="build_evidence.py --check: the 23 per-system evidence reports and their index (evidence/) equal what the script "
              "generates from the rescoring pass, the v2 corpus, scores and blocks and the scoring documents: 667 criterion "
              "sections (the pass's units with their clause readings and sources, the held cells with their published "
              "rationale), each score and each unit's verdict equal to the corpus, each total equal to the blocks', every link "
              "to a data file in evidence_cache/ or to a document by line pointing at a file that exists; no score changed",
         cmd=["python", "build_evidence.py", "--check"], files=S68_FILES,
         stdout="build_evidence_output.txt", stderr=EMPTY),
]
S68_CHECKS.append(dict(S68_CHECKS[0], files={**S68_FILES, "evidence/sq.md": "evidence/cn.md"},
                       name="build_evidence.py --check rejects an evidence/ whose Status Quo report is replaced by another "
                            "system's (negative control; exit 1 expected)",
                       stdout="build_evidence_check_negative_output.txt", expect_exit=1))

# Session 69: the blind re-read's shared module (ledger D52 to D54), before the Report and Paper v2.0. blind_review.py
# --selftest proves compare_unit's agree/revise rule on synthetic fixtures (clause-status and verdict changes only; a
# reworded estimate or source alone is not a revision) and that blind_view(), what a blind-review session is shown before
# it records its own reading, discloses no verdict, clause status, estimate or source of the prior, Sonnet-read unit.
S69_FILES = {**S68_FILES, "blind_review.py": "blind_review.py"}
S69_CHECKS = [
    dict(name="blind_review.py --selftest: compare_unit agrees only when every clause status and the verdict match; "
              "blind_view exposes no verdict, status, estimate or source for a real unit of each Sonnet-read part "
              "((2.9) C3.1, (2.10) C4.2, (2.11) C1.1)",
         cmd=["python", "blind_review.py", "--selftest"], files=S69_FILES,
         stdout="blind_review_selftest_output.txt", stderr=EMPTY),
]

# Session 70: evidence caches for the shortcuts (ledger S53), before the blind re-read proper (Sessions 71-77).
# evidence_cache_s70.py (default, no args) verifies by digest the ten files this session cached: the WHR 2026
# statistical appendix (C2.1), the IDEA turnout codebook (C2.4), two US CFR sections on quarantine/judicial review
# and the Easterly and Fischer (1995) NBER working paper (C2.6, C3.6), four WHO GHO mortality queries (C4.6), and
# the 17 designs' and mechanisms' source index. It makes no reading and changes no score; each gap left for a later
# session is named in evidence_cache/C2.1/notes_s70.md, C2.3/notes_s70.md, C2.4/notes_s70.md,
# C2.6/law_in_force_notes_s70.md and C4.6/notes_s70.md (prose, not digest-checked).
S70_FILES = {**S69_FILES, "evidence_cache_s70.py": "evidence_cache_s70.py",
             **{"evidence_cache/" + k: "evidence_cache/" + k
                for k in ("designs_index_s70.json", "C2.1/whr26_statistical_appendix.pdf",
                          "C2.4/idea_voter_turnout_codebook.pdf", "C2.6/us_cfr_42_70.14.html",
                          "C2.6/us_cfr_42_71.37.html", "C3.6/easterly_fischer_1995_nber_w4735.pdf",
                          "C4.6/SDGAIRBOD.json", "C4.6/SDGWSHBOD.json", "C4.6/SDGPOISON.json", "C4.6/air42.json")}}
S70_CHECKS = [
    dict(name="evidence_cache_s70.py: the ten files Session 70 cached for the shortcuts (STATE.md, 'Next work' item "
              "0; ledger S53) verify by digest against their live sources",
         cmd=["python", "evidence_cache_s70.py"], files=S70_FILES,
         stdout="evidence_cache_s70_output.txt", stderr=EMPTY),
]

# Session 71: the blind re-read of C4.5 and C3.4 (ledger S54; decisions 69.1, 69.2), the first group of stage 3b.
# evidence_cache_s71.py verifies by digest the nine files the group cached (Penn World Table labour shares, the US
# national-income components, natural-resource rents, the SDG labour shares, Sweden's 43 b, Hahnel and Wright, the
# Research Hub at 8e8a6ba, Integral's white paper, CPI-U and the federal funds rate). blind_s71.py checks the 24 blind
# readings (complete, D28 and decision 53.2's 0.0 rule), recomputes every figure they quote from the cache, compares
# them with part (2.11)'s readings (blind_review.compare_group), applies the record's three reconciliations, checks
# that no CCO-PTF-CIP-SZH verdict changes, computes the consequences on the 29 criteria and each flag's, and confirms
# NEEC_BlindReview_s71.md carries every table it generates. Nothing is applied: ledger S61 applies the final readings.
S71_CACHE = ("C4.5/pwt1001_labsh_selected_economies.csv", "C4.5/fred_us_national_income_components.csv",
             "C4.5/wb_natural_resource_rents_pct_gdp.json", "C4.5/un_sdg_10_4_1_labour_share.json",
             "C4.5/se_lag_1997_238_43b.txt", "C4.5/hahnel_wright_2016_extract.txt",
             "C4.5/research_hub_8e8a6ba_cco_extract.txt", "C4.5/sources_s71.md",
             "C3.4/integral_wp_v01_c34_extract.txt", "C3.4/fred_cpi_fedfunds_2019_2023.csv", "C3.4/sources_s71.md")
S71_FILES = {**S70_FILES, "evidence_cache_s71.py": "evidence_cache_s71.py", "blind_s71.py": "blind_s71.py",
             "NEEC_BlindReview_s71.md": "NEEC_BlindReview_s71.md", "neec_corpus_v2.json": "neec_corpus_v2.json",
             "neec_scores_v2.csv": "neec_scores_v2.csv",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S71_CACHE}}
S71_CHECKS = [
    dict(name="evidence_cache_s71.py: the nine files Session 71 cached for the blind re-read of C4.5 and C3.4 "
              "(ledger S54) verify by digest",
         cmd=["python", "evidence_cache_s71.py"], files=S71_FILES,
         stdout="evidence_cache_s71_output.txt", stderr=EMPTY),
    dict(name="blind_s71.py: the blind re-read of C4.5 (17 units) and C3.4 (7 units) against part (2.11): readings "
              "complete and on D28 and decision 53.2, figures recomputed from the cache, the comparison, the three "
              "reconciliations, no CCO-PTF-CIP-SZH verdict change, consequences and flag effects, and "
              "NEEC_BlindReview_s71.md carrying every generated table",
         cmd=["python", "blind_s71.py"], files=S71_FILES,
         stdout="blind_s71_output.txt", stderr=EMPTY),
]

# Session 72: the blind re-read of C4.1 (ledger S55; decisions 69.1, 69.2), on v2.0's two clauses: part (2.11)'s 15
# units and part (b6)'s 8 designs. evidence_cache_s72.py verifies by digest the eight files the group cached (US net
# saving and GNI, adjusted net savings, Ofer (1990), the "400 days" programme, the Libertarian Party platform, Hahnel
# and Wright, Integral's white paper, the Research Hub at 8e8a6ba). blind_s72.py checks the 23 blind readings
# (complete, D28 and decision 53.2's 0.0 rule), recomputes every figure they quote from the cache, compares them with
# the prior parts (blind_review.compare_group), checks that no CCO-PTF-CIP-SZH verdict changes, computes the
# consequences on the 29 criteria alone and with blind_s71.FINAL, and each flag's, and confirms
# NEEC_BlindReview_s72.md carries every table it generates. Nothing is applied: ledger S61 applies the final readings.
S72_CACHE = ("C4.1/imf_weo_gross_debt_pct_gdp.json", "C4.1/wb_gross_savings_pct_gni.json",
             "C4.1/wb_consumption_fixed_capital_pct_gni.json", "C4.1/fred_us_net_saving_gni.csv",
             "C4.1/wb_adjusted_net_savings_pct_gni.json", "C4.1/ofer_1990_extract.txt",
             "C4.1/programme_400_days_1990_extract.txt", "C4.1/lp_platform_extract.txt",
             "C4.1/hahnel_wright_2016_c41_extract.txt", "C4.1/integral_wp_v01_c41_extract.txt",
             "C4.1/research_hub_8e8a6ba_c41_extract.txt", "C4.1/sources_s72.md")
S72_FILES = {**S71_FILES, "evidence_cache_s72.py": "evidence_cache_s72.py", "blind_s72.py": "blind_s72.py",
             "NEEC_BlindReview_s72.md": "NEEC_BlindReview_s72.md",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S72_CACHE}}
S72_CHECKS = [
    dict(name="evidence_cache_s72.py: the eight files Session 72 cached for the blind re-read of C4.1 (ledger S55) "
              "verify by digest",
         cmd=["python", "evidence_cache_s72.py"], files=S72_FILES,
         stdout="evidence_cache_s72_output.txt", stderr=EMPTY),
    dict(name="blind_s72.py: the blind re-read of C4.1 (23 units) against parts (2.11) and (b6), on v2.0's two "
              "clauses: readings complete and on D28 and decision 53.2, figures recomputed from the cache, the "
              "comparison, the reconciliation, no CCO-PTF-CIP-SZH verdict change, consequences with Session 71's and "
              "flag effects, and NEEC_BlindReview_s72.md carrying every generated table",
         cmd=["python", "blind_s72.py"], files=S72_FILES,
         stdout="blind_s72_output.txt", stderr=EMPTY),
]

# Session 73: the blind re-read of C4.4 and C4.2 (ledger S56; decisions 69.1, 69.2): part (2.11)'s 17 C4.4 units and
# part (2.10)'s 16 C4.2 units, on v2.0's clauses. evidence_cache_s73.py verifies by digest the ten files the group
# cached (WDI self-employment, BLS government payrolls, V-Dem for the Soviet years; the Red List Index unrounded,
# Fanning et al. (2022) and O'Neill et al. (2018) boundary data, the Soviet territories' CO2, the Libertarian Party
# platform's environment passage). blind_s73.py checks the 33 blind readings (complete, D28 and decision 53.2's 0.0
# rule), recomputes every figure they quote from the cache, compares them with the prior parts
# (blind_review.compare_group), applies the record's three reconciliations, checks that no CCO-PTF-CIP-SZH verdict
# changes, computes the consequences on the 29 criteria alone and with blind_s71.FINAL and blind_s72.FINAL, and each
# flag's, and confirms NEEC_BlindReview_s73.md carries every table it generates. Nothing is applied: ledger S61
# applies the final readings.
S73_CACHE = ("C4.4/wb_self_employment_pct.json", "C4.4/fred_us_government_payrolls.csv",
             "C4.4/owid_vdem_regimes_russia_1917_1992.csv", "C4.4/sources_s73.md",
             "C4.2/un_sdg_red_list_index.json", "C4.2/fanning_2022_biophysical_historical.csv",
             "C4.2/fanning_2022_biophysical_bau.csv", "C4.2/oneill_2018_biophysical.csv",
             "C4.2/owid_gcb_ussr_territorial_co2.csv", "C4.2/lp_platform_environment_extract.txt",
             "C4.2/sources_s73.md")
S73_FILES = {**S72_FILES, "evidence_cache_s73.py": "evidence_cache_s73.py", "blind_s73.py": "blind_s73.py",
             "NEEC_BlindReview_s73.md": "NEEC_BlindReview_s73.md",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S73_CACHE}}
S73_CHECKS = [
    dict(name="evidence_cache_s73.py: the ten files Session 73 cached for the blind re-read of C4.4 and C4.2 (ledger "
              "S56) verify by digest",
         cmd=["python", "evidence_cache_s73.py"], files=S73_FILES,
         stdout="evidence_cache_s73_output.txt", stderr=EMPTY),
    dict(name="blind_s73.py: the blind re-read of C4.4 (17 units) against part (2.11) and C4.2 (16 units) against "
              "part (2.10), on v2.0's clauses: readings complete and on D28 and decision 53.2, figures recomputed "
              "from the cache, the comparison, the three reconciliations, no CCO-PTF-CIP-SZH verdict change, "
              "consequences with Sessions 71's and 72's and flag effects, and NEEC_BlindReview_s73.md carrying every "
              "generated table",
         cmd=["python", "blind_s73.py"], files=S73_FILES,
         stdout="blind_s73_output.txt", stderr=EMPTY),
]

# Session 74: the blind re-read of C1.1 and C3.1 (ledger S57; decisions 69.1, 69.2): part (2.11)'s 14 C1.1 units and
# part (2.9)'s 16 C3.1 units, on v2.0's clauses, and Nordic Social Democracy's C1.1 (part (b3)) on the Nordic poverty
# finding. evidence_cache_s74.py verifies by digest the three files the group cached (the Societal Poverty Line from
# the PIP API, Integral's white paper on access to essentials, the Libertarian Party platform's income-security and
# bailout passages). blind_s74.py checks the 31 readings (complete, D28 and decision 53.2's 0.0 rule), recomputes
# every figure they quote from the cache, compares them with the prior parts (blind_review.compare_group), applies the
# record's reconciliation, checks that no CCO-PTF-CIP-SZH verdict changes and that no mechanism is at 0.0, computes
# the consequences on the 29 criteria alone and with blind_s71.FINAL to blind_s73.FINAL, and each flag's, and confirms
# NEEC_BlindReview_s74.md carries every table it generates. Nothing is applied: ledger S61 applies the final readings.
S74_CACHE = ("C1.1/wb_societal_poverty_rate.json", "C1.1/pip_societal_poverty_line.json",
             "C1.1/integral_wp_v01_c11_extract.txt", "C1.1/sources_s74.md",
             "C3.1/cares_act_wikipedia_lead.txt", "C3.1/eurostat_gov_esms.txt", "C3.1/fred_benefits_annual.csv",
             "C3.1/fred_benefits_monthly.csv", "C3.1/fred_claims_weekly.csv", "C3.1/fred_realgdp_annual.csv",
             "C3.1/imf_fiscal_db.txt", "C3.1/index.json", "C3.1/sdg131_156.json", "C3.1/sdg131_578.json",
             "C3.1/sdg131_634.json", "C3.1/sdg131_702.json", "C3.1/sdg131_840.json",
             "C3.1/un_sdg_131_metadata.txt", "C3.1/un_sna2008.txt", "C3.1/wb_final_consumption.txt",
             "C3.1/wb_sp_coverage.txt", "C3.1/lp_platform_c11_c31_extract.txt", "C3.1/sources_s74.md")
S74_FILES = {**S73_FILES, "evidence_cache_s74.py": "evidence_cache_s74.py", "blind_s74.py": "blind_s74.py",
             "NEEC_BlindReview_s74.md": "NEEC_BlindReview_s74.md",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S74_CACHE}}
S74_CHECKS = [
    dict(name="evidence_cache_s74.py: the three files Session 74 cached for the blind re-read of C1.1 and C3.1 "
              "(ledger S57) verify by digest",
         cmd=["python", "evidence_cache_s74.py"], files=S74_FILES,
         stdout="evidence_cache_s74_output.txt", stderr=EMPTY),
    dict(name="blind_s74.py: the blind re-read of C1.1 (14 units) against part (2.11) and C3.1 (16 units) against "
              "part (2.9), on v2.0's clauses, and Nordic Social Democracy's C1.1 against part (b3): readings complete "
              "and on D28 and decision 53.2, figures recomputed from the cache, the comparison, the reconciliation, no "
              "CCO-PTF-CIP-SZH verdict change, consequences with Sessions 71's to 73's and flag effects, and "
              "NEEC_BlindReview_s74.md carrying every generated table",
         cmd=["python", "blind_s74.py"], files=S74_FILES,
         stdout="blind_s74_output.txt", stderr=EMPTY),
]

# Session 75: the blind re-read of C2.1, C2.4, C2.3 (the six configured economies, clause 1 read for the first time,
# decision 65.2 having held it) and C2.5 (part (2.11)'s 13 units and part (b5)'s 10, on v2.0's clauses) (ledger S58;
# decisions 69.1, 69.2). evidence_cache_s75.py verifies by digest the ten files the group cached (the Gallup freedom
# share, IDEA's turnout export, the OECD Trust Survey's external-efficacy item and Time Use Database, EU-SILC's
# artistic-practice and meaning-of-life tables, the Qatar referendum entry, and CCO's, Integral's and the Libertarian
# Party's passages on exit). blind_s75.py checks the 41 readings (complete, D28 and decision 53.2's 0.0 rule),
# recomputes every figure they quote from the cache, compares them with the parts the pass holds, applies the record's
# reconciliation, checks that no CCO-PTF-CIP-SZH verdict changes and that no mechanism is at 0.0, computes the
# consequences on the 29 criteria alone and with blind_s71.FINAL to blind_s74.FINAL, and each flag's, and confirms
# NEEC_BlindReview_s75.md carries every table it generates. Nothing is applied: ledger S61 applies the final readings.
S75_CACHE = ("C2.1/notes_s70.md", "C2.1/whr26_statistical_appendix.pdf", "C2.1/whr_freedom_s75.json",
             "C2.1/sources_s75.md", "C2.3/notes_s70.md", "C2.3/eurostat_artistic_practice_s75.json",
             "C2.3/oecd_time_use_s75.json", "C2.3/eurostat_meaning_of_life_s75.json", "C2.3/sources_s75.md",
             "C2.4/notes_s70.md", "C2.4/idea_voter_turnout_codebook.pdf", "C2.4/idea_turnout_s75.json",
             "C2.4/oecd_trust_pe_ext_s75.json", "C2.4/idea_dt_qatar_2024_11_extract.txt", "C2.4/sources_s75.md",
             "C2.5/cco_research_hub_c25_extract.txt", "C2.5/integral_wp_v01_c25_extract.txt",
             "C2.5/lp_platform_c25_extract.txt", "C2.5/sources_s75.md")
S75_FILES = {**S74_FILES, "evidence_cache_s75.py": "evidence_cache_s75.py", "blind_s75.py": "blind_s75.py",
             "NEEC_BlindReview_s75.md": "NEEC_BlindReview_s75.md",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S75_CACHE}}
S75_CHECKS = [
    dict(name="evidence_cache_s75.py: the ten files Session 75 cached for the blind re-read of C2.1, C2.4, C2.3 and "
              "C2.5 (ledger S58) verify by digest",
         cmd=["python", "evidence_cache_s75.py"], files=S75_FILES,
         stdout="evidence_cache_s75_output.txt", stderr=EMPTY),
    dict(name="blind_s75.py: the first readings of C2.1, C2.4 and C2.3 for the six configured economies (18 units) and "
              "the blind re-read of C2.5 (23 units) against parts (2.11), (b5) and (a), on v2.0's clauses: readings "
              "complete and on D28 and decision 53.2, figures recomputed from the cache, the comparison, the "
              "reconciliation, no CCO-PTF-CIP-SZH verdict change, consequences with Sessions 71's to 74's and flag "
              "effects, and NEEC_BlindReview_s75.md carrying every generated table",
         cmd=["python", "blind_s75.py"], files=S75_FILES,
         stdout="blind_s75_output.txt", stderr=EMPTY),
]

# Session 76: the blind re-read of C2.6, C3.6 and C4.6 for the 17 designs and mechanisms (part (2.11)'s 51 units, which
# Session 65 scored on a stated rule) (ledger S59; decisions 69.1, 69.2). evidence_cache_s76.py verifies by digest the 16
# passages the group cached from the designs' own freely published texts. blind_s76.py checks the 51 readings
# (complete, D28, no mechanism at 0.0, no clause out of reach for a design), recomputes the market economies'
# productivity record they calibrate against, compares them with part (2.11) (rescoring_s65.NEW_UNITS), checks that no
# verdict differs and every clause revision has its stated reason, that no CCO-PTF-CIP-SZH verdict changes, computes
# the consequences on the 29 criteria with blind_s71.FINAL to blind_s75.FINAL and each flag's, and confirms
# NEEC_BlindReview_s76.md carries every table it generates. Nothing is applied: ledger S61 applies the final readings.
S76_CACHE = ("C2.6/lp_platform_c26_extract.txt", "C2.6/cco_research_hub_c26_extract.txt",
             "C2.6/integral_wp_v01_c26_extract.txt", "C2.6/pe_model_c26_extract.txt",
             "C2.6/ostrom_nobel_c26_extract.txt", "C2.6/levy_jg_wp902_c26_extract.txt",
             "C2.6/bien_definition_c26_extract.txt", "C2.6/george_progress_poverty_c26_extract.txt",
             "C2.6/sources_s76.md", "C2.6/owid_freedom_house_civil_liberties_rating.csv",
             "C2.6/law_in_force_notes_s70.md", "C2.6/us_cfr_42_70.14.html", "C2.6/us_cfr_42_71.37.html",
             "C3.6/cco_research_hub_c36_extract.txt", "C3.6/integral_wp_v01_c36_extract.txt",
             "C3.6/pe_model_c36_extract.txt", "C3.6/pwt1001_selected_economies.csv", "C3.6/sources_s76.md",
             "C3.6/easterly_fischer_1995_nber_w4735.pdf",
             "C4.6/lp_platform_c46_extract.txt", "C4.6/pe_model_c46_extract.txt",
             "C4.6/integral_wp_v01_c46_extract.txt", "C4.6/wef_metrics_c46_extract.txt",
             "C4.6/cco_research_hub_c46_extract.txt", "C4.6/sources_s76.md", "C4.6/SDGAIRBOD.json",
             "C4.6/SDGPOISON.json", "C4.6/SDGWSHBOD.json", "C4.6/air42.json", "C4.6/notes_s70.md")
S76_FILES = {**S75_FILES, "evidence_cache_s76.py": "evidence_cache_s76.py", "blind_s76.py": "blind_s76.py",
             "NEEC_BlindReview_s76.md": "NEEC_BlindReview_s76.md",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S76_CACHE}}
S76_CHECKS = [
    dict(name="evidence_cache_s76.py: the 16 passages Session 76 cached from the designs' own texts for the blind "
              "re-read of C2.6, C3.6 and C4.6 (ledger S59) verify by digest",
         cmd=["python", "evidence_cache_s76.py"], files=S76_FILES,
         stdout="evidence_cache_s76_output.txt", stderr=EMPTY),
    dict(name="blind_s76.py: the blind re-read of C2.6, C3.6 and C4.6 for the 17 designs and mechanisms (51 units) "
              "against part (2.11): readings complete and on D28, the market economies' record recomputed from the "
              "cache, the comparison (no verdict differs; each clause revision's reason), no CCO-PTF-CIP-SZH verdict "
              "change, consequences with Sessions 71's to 75's and flag effects, and NEEC_BlindReview_s76.md carrying "
              "every generated table",
         cmd=["python", "blind_s76.py"], files=S76_FILES,
         stdout="blind_s76_output.txt", stderr=EMPTY),
]

# Session 77: the blind re-read of C2.6, C3.6 and C4.6 for the six configured economies (part (2.11)'s 18 units)
# (ledger S60; decisions 69.1, 69.2). evidence_cache_s77.py verifies by digest the 21 files the group cached: Freedom
# House's and V-Dem's series and Freedom in the World 2026's pages, the law in force, Penn World Table 11.0, the
# Poverty and Inequality Platform, the transcription of Easterly and Fischer's tables, the OECD's GBD 2019 mortality
# dataset and the WHO's poisoning series. blind_s77.py checks the 18 readings (complete, D28), recomputes the figures
# they quote, compares them with part (2.11) (rescoring_s65.NEW_UNITS), checks the four C3.6 verdict differences and
# every revision's stated reason, computes the consequences on the 29 criteria with blind_s71.FINAL to blind_s76.FINAL
# and each flag's, and confirms NEEC_BlindReview_s77.md carries every table it generates. Nothing is applied: ledger
# S61 applies the final readings.
S77_CACHE = ("C2.6/cn_law_c26_extract.txt", "C2.6/dk_law_c26_extract.txt", "C2.6/fh_fiw2026_cl_f1_extract.txt",
             "C2.6/fi_law_c26_extract.txt", "C2.6/no_law_c26_extract.txt",
             "C2.6/owid_fh_civil_liberties_rating_su_s77.csv", "C2.6/owid_fh_civil_liberties_score_s77.csv",
             "C2.6/owid_vdem_civil_liberties_s77.csv", "C2.6/se_law_c26_extract.txt", "C2.6/sg_law_c26_extract.txt",
             "C2.6/su_law_c26_extract.txt", "C2.6/us_law_c26_extract.txt", "C3.6/easterly_fischer_1995_tables_s77.csv",
             "C3.6/pip_spl_selected_economies.csv", "C3.6/pwt110_selected_economies.csv", "C4.6/cn_law_c46_extract.txt",
             "C4.6/nordic_law_c46_extract.txt", "C4.6/oecd_exp_morsc_gbd2019_s77.csv",
             "C4.6/su_environment_c46_extract.txt", "C4.6/us_law_c46_extract.txt", "C4.6/who_gho_sdgpoison_s77.csv",
             "C2.6/sources_s77.md", "C3.6/sources_s77.md", "C4.6/sources_s77.md")
S77_FILES = {**S76_FILES, "evidence_cache_s77.py": "evidence_cache_s77.py", "blind_s77.py": "blind_s77.py",
             "NEEC_BlindReview_s77.md": "NEEC_BlindReview_s77.md",
             **{"evidence_cache/" + k: "evidence_cache/" + k for k in S77_CACHE}}
S77_CHECKS = [
    dict(name="evidence_cache_s77.py: the 21 files Session 77 cached for the blind re-read of C2.6, C3.6 and C4.6 for "
              "the configured economies (ledger S60) verify by digest",
         cmd=["python", "evidence_cache_s77.py"], files=S77_FILES,
         stdout="evidence_cache_s77_output.txt", stderr=EMPTY),
    dict(name="blind_s77.py: the blind re-read of C2.6, C3.6 and C4.6 for the six configured economies (18 units) "
              "against part (2.11): readings complete and on D28, figures recomputed from the cache, the comparison "
              "(four C3.6 verdicts differ; each revision's reason), consequences with Sessions 71's to 76's and flag "
              "effects, and NEEC_BlindReview_s77.md carrying every generated table",
         cmd=["python", "blind_s77.py"], files=S77_FILES,
         stdout="blind_s77_output.txt", stderr=EMPTY),
]

# Session 78 (ledger S61): the blind re-read's final readings applied. final_pass.py lays the seven groups' FINAL dictionaries over the
# pass; apply_final_s78.py writes the v2 files and the record from them. build_evidence.py and build_site.py (the checks of Sessions
# 68 and 49) now read these files, so their inputs are the real v2 files; the blind scripts and apply_pass_s65.py keep the Session 65
# snapshots (S65B_FILES).
S78_V2 = ("neec_corpus_v2.json", "neec_scores_v2.csv", "summary_blocks_v2.json")
# Session 79: apply_final_s78.py's three files are kept as the Session 78 snapshots; final_pass.py loads owner_s79.py
S78_SNAP = ("neec_corpus_v2_s78_snapshot.json", "neec_scores_v2_s78_snapshot.csv", "summary_blocks_v2_s78_snapshot.json")
S78_FILES = {**S77_FILES, **{k: k for k in ("final_pass.py", "apply_final_s78.py", "build_evidence.py", "NEEC_FinalApplication_s78.md",
                                            "site/config.json", "owner_s79.py") + S78_V2 + S78_SNAP}}
S78_CHECKS = [
    dict(name="final_pass.py --selftest: the seven blind groups' FINAL dictionaries (221 units: 24, 23, 33, 31, 41, 51, 18) load, "
              "overlap nowhere, replace the pass's reading of the same cell (the 26 published criteria's merged units and the 69 "
              "class N units), and each has one status per v2.0 clause and follows D28; the owner's layer of Session 79 (owner_s79.py) revises "
              "seven final units, one clause each, 0.5 to 1.0 by D28, each keeping its prior reading as its flag",
         cmd=["python", "final_pass.py", "--selftest"], files=S78_FILES,
         stdout="final_pass_selftest_output.txt", stderr=EMPTY),
    dict(name="apply_final_s78.py --check: stage 3b, the generator that applies the blind re-read: the 23 entries on the 29 "
              "criteria, their totals, failures and tiers and the site's blocks, kept from Session 79 as the Session 78 snapshots "
              "(neec_corpus_v2_s78_snapshot.json and its two companions), and the record (NEEC_FinalApplication_s78.md) equal "
              "what it produces; the corpus carries "
              "each unit's final verdict and differs from the Session 65 snapshot in exactly the 28 cells the groups changed "
              "(5, 2, 8, 3, 6, 0 and 4 by group); the tier changes are Universal Basic Income's and Sovereign Wealth Fund "
              "Statism's; Participatory Economics is first alone at 16.5; CCO-PTF-CIP-SZH's vector is unchanged",
         cmd=["python", "apply_final_s78.py", "--check"], files=S78_FILES,
         stdout="apply_final_s78_output.txt", stderr=EMPTY),
]
S78_CHECKS.append(dict(S78_CHECKS[1], files={**S78_FILES, "neec_corpus_v2_s78_snapshot.json": "neec_corpus_v2_s65_snapshot.json"},
                       name="apply_final_s78.py --check rejects a Session 78 corpus that is the Session 65 snapshot "
                            "(negative control; exit 1 expected)",
                       stdout="apply_final_s78_check_negative_output.txt", expect_exit=1))
for _c in S68_CHECKS:    # build_evidence.py --check reads the regenerated v2 files and the blind groups' final readings
    _c["files"] = {**S78_FILES, **{k: v for k, v in _c["files"].items() if k.startswith("evidence/")}}

# Session 79: the owner's decisions 79.1 to 79.4 (owner_s79.py), laid over the final readings by final_pass.owner_state() and
# written by apply_owner_s79.py into the v2 files; build_evidence.py and build_site.py read them (their files above).
S79_FILES = {**S78_FILES, **{k: k for k in ("apply_owner_s79.py", "NEEC_OwnerDecisions_s79.md")}}
S79_CHECKS = [
    dict(name="apply_owner_s79.py --check: the owner's decisions 79.1 to 79.4 applied: the v2 corpus, scores, blocks and "
              "NEEC_OwnerDecisions_s79.md equal what it produces; the corpus differs from the Session 78 snapshot in exactly "
              "seven cells, each 0.5 to 1.0 (CCO-PTF-CIP-SZH C1.2a, C2.5 and C3.4; Integral, Participatory Economics, Degrowth "
              "Economics and Ostrom-Style Commons Governance C3.4), each a close call toward 0.5; no tier changes; "
              "CCO-PTF-CIP-SZH first alone at 17.5, Participatory Economics 17.0; without the decisions, Participatory "
              "Economics first at 16.5",
         cmd=["python", "apply_owner_s79.py", "--check"], files=S79_FILES,
         stdout="apply_owner_s79_output.txt", stderr=EMPTY),
]
S79_CHECKS.append(dict(S79_CHECKS[0], files={**S79_FILES, "neec_corpus_v2.json": "neec_corpus_v2_s78_snapshot.json"},
                       name="apply_owner_s79.py --check rejects a neec_corpus_v2.json that is the Session 78 snapshot "
                            "(negative control; exit 1 expected)",
                       stdout="apply_owner_s79_check_negative_output.txt", expect_exit=1))
for _c in S68_CHECKS:    # build_evidence.py --check shows the owner's layer and links its record
    _c["files"] = {**_c["files"], **{k: k for k in ("NEEC_OwnerDecisions_s79.md", "apply_owner_s79.py")}}

# Session 80: the outside blind review's kit (outside_kit.py), its leak check (outside_kit_check.py) and the runner
# (outside_review_runner.py, which the leak check imports to build every prompt as the run will).
S80_FILES = {**tree("outside_kit", "outside_kit_sources", "evidence_cache"),
             **{k: k for k in ("outside_kit.py", "outside_kit_check.py", "outside_review_runner.py", "criteria.json",
                               "neec_corpus_v2.json", "summary_blocks_v2.json", "SCORING_PROTOCOL.md")}}
S80_CHECKS = [
    dict(name="outside_kit.py --check: the outside review's kit (outside_kit/: the instructions, the blind rules, 29 "
              "criteria with their worked examples removed, 23 system files, the source packs, the order of 696 calls, "
              "the eight stage B arguments, the schema and the manifest) is exactly what the generator builds; the "
              "cached design texts match their md5s",
         cmd=["python", "outside_kit.py", "--check"], files=S80_FILES,
         stdout="outside_kit_output.txt", stderr=EMPTY),
    dict(name="outside_kit.py --check rejects a kit with one criterion file swapped for another (negative control; "
              "exit 1 expected)",
         cmd=["python", "outside_kit.py", "--check"],
         files={**S80_FILES, "outside_kit/criteria/C1.1.md": "outside_kit/criteria/C1.2a.md"},
         stdout="outside_kit_negative_output.txt", stderr=EMPTY, expect_exit=1),
    dict(name="outside_kit_check.py: every blind prompt (696) and Jev state (294), built by the runner's own functions, "
              "holds no tier, record, session, owner, withheld marker, stage B text, other system's name, or verdict "
              "next to a criterion; each prompt carries its own criterion, system and pack",
         cmd=["python", "outside_kit_check.py"], files=S80_FILES,
         stdout="outside_kit_check_output.txt", stderr=EMPTY),
    dict(name="outside_kit_check.py --negative: one leak of each of seven kinds planted in a copy of the kit is caught, "
              "and only that kind",
         cmd=["python", "outside_kit_check.py", "--negative"], files=S80_FILES,
         stdout="outside_kit_check_negative_output.txt", stderr=EMPTY),
    dict(name="outside_review_runner.py --selftest: prompt assembly, the FINAL parser, the clause-rule validator, "
              "resume, the heartbeat, the stage B gate and the Jev request, offline",
         cmd=["python", "outside_review_runner.py", "--selftest"], files=S80_FILES,
         stdout="outside_review_runner_selftest_output.txt", stderr=EMPTY),
]

CHECKS = (S33_CHECKS + [pin32(c) for c in V7_CHECKS] + S34_CHECKS + S35_CHECKS
          + [pin44(c) for c in S36_CHECKS + S37_CHECKS + S38_CHECKS + S39_CHECKS + S40_CHECKS + S41_CHECKS
             + S42_CHECKS + S43_CHECKS + S44_CHECKS]
          + S45_CHECKS + S47_CHECKS + S48_CHECKS + S49_CHECKS + S50_CHECKS + S51_CHECKS + S52_CHECKS + S53_CHECKS
          + S54_CHECKS + S56_CHECKS + S57_CHECKS + S58_CHECKS + S60_CHECKS + S61_CHECKS + S63_CHECKS + S64_CHECKS
          + S65_CHECKS + S68_CHECKS + S69_CHECKS + S70_CHECKS + S71_CHECKS + S72_CHECKS + S73_CHECKS + S74_CHECKS
          + S75_CHECKS + S76_CHECKS + S77_CHECKS + S78_CHECKS + S79_CHECKS + S80_CHECKS)


def md5(data):
    return hashlib.md5(data).hexdigest()[:8]


def run_check(chk):
    exe = sys.executable if chk["cmd"][0] == "python" else shutil.which(chk["cmd"][0])
    if exe is None:
        return "SKIP", [f"{chk['cmd'][0]} not found on PATH"]
    notes = []
    with tempfile.TemporaryDirectory() as tmp:
        for dest, src in chk["files"].items():
            target = os.path.join(tmp, dest)
            if src == VIEW15:
                with open(target, "w", encoding="utf-8") as f:
                    f.write(VIEW15_SOURCE)
                continue
            if not os.path.isfile(os.path.join(HERE, src)):
                return "FAIL", [f"missing input file: {src}"]
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copy(os.path.join(HERE, src), target)
        proc = subprocess.run([exe] + chk["cmd"][1:], cwd=tmp, capture_output=True)
        expect = chk.get("expect_exit", 0)
        ok = proc.returncode == expect
        if not ok:
            tail = proc.stderr.decode("utf-8", "replace").strip().splitlines()[-1:] or [""]
            notes.append(f"exit status {proc.returncode}, expected {expect}: {tail[0][:120]}")
        elif expect:
            notes.append(f"exit status {proc.returncode}, as expected")
        if chk.get("show_stdout"):
            notes.append(proc.stdout.decode("utf-8", "replace").strip())
        if chk.get("show_summary"):
            notes += [ln for ln in proc.stdout.decode("utf-8", "replace").splitlines() if ln.startswith("SUMMARY")]
        for stream, got in (("stdout", proc.stdout), ("stderr", proc.stderr)):
            name = chk.get(stream)
            if not name:
                continue
            if name == EMPTY:
                ref, label = b"", "(empty)"
            elif not os.path.isfile(os.path.join(HERE, name)):
                ok = False
                notes.append(f"{stream}: missing reference file {name}")
                continue
            else:
                ref, label = open(os.path.join(HERE, name), "rb").read(), name
            same = got == ref
            ok = ok and same
            notes.append(f"{stream} {'==' if same else '!='} {label} (md5 {md5(ref)})")
        for produced, reference in chk.get("outputs", {}).items():
            p = os.path.join(tmp, produced)
            if not os.path.isfile(os.path.join(HERE, reference)):
                ok = False
                notes.append(f"missing reference file {reference}")
                continue
            ref = open(os.path.join(HERE, reference), "rb").read()
            same = os.path.isfile(p) and open(p, "rb").read() == ref
            ok = ok and same
            notes.append(f"{os.path.basename(produced)} {'==' if same else '!='} {reference} (md5 {md5(ref)})")
    return ("PASS" if ok else "FAIL"), notes


def main():
    print("=" * 92)
    print(f"run_all_checks.py -- {len(CHECKS)} reproducibility checks")
    print("=" * 92)
    tally = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    for i, chk in enumerate(CHECKS, 1):
        status, notes = run_check(chk)
        tally[status] += 1
        print(f"\n[{i:2d}] {status}  {chk['name']}")
        for n in notes:
            print(f"          {n}")
    print("\n" + "=" * 92)
    print(f"SUMMARY: {tally['PASS']} passed, {tally['FAIL']} failed, {tally['SKIP']} skipped "
          f"(of {len(CHECKS)}).")
    print("Not covered here: the realjs scripts' fidelity to index.html (the Compassionism")
    print("Simulation source, which is not in this directory), and the Report and Paper prose.")
    return 1 if tally["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
