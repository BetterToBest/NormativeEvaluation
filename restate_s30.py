#!/usr/bin/env python3
"""
restate_s30.py -- NEEC Session 30: decision D22, the Doughnut Economics Verification section
=============================================================================================
In Session 30 the project owner asked for verify_doughnut.py, the Session 14 script this entry's
Verification section describes, which was never added to the project files. It cannot be recovered;
verify_doughnut.py was reconstructed in Session 30 from that section (see its own header). Once a file
of that name is on file, the section's D14 wording -- "an ad hoc script (`verify_doughnut.py`) that is
not among the project files" -- no longer reads true, so decision D22 restates the section in place
(protocol 10.3), by generator, in two edits:

  DE-05  the Session 14 check is described without the claim that the script is not on file
         (this supersedes the D14 restatement of audit item DE-05);
  D22    the sentence that pointed to neec_entry.py "because the Session 14 script is not on file"
         says what the reconstruction is and does, and that the harness runs it and neec_entry.py.

Nothing else in the document changes: the transcript, the D14 restatement of DE-06 (asserted by the
claims verifier) and the summary block are untouched. The edits are applied by the D14 generator's own
edit function (d14_landing_s29.apply_edit, pinned by MD5): anchors match across any run of whitespace,
each exactly once, and the paragraph an edit lands in is re-wrapped at 76 columns. Every restated
phrase must occur exactly once in the output. The facts behind the phrases are asserted by
verify_comparative_claims.py (group [K]), which reads the phrases from this file, pinned by MD5.

Usage:   python3 restate_s30.py [INDIR] [OUTDIR]        (defaults: . and out)
Inputs (pinned by MD5): NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md (the document as the D14
pass left it) and d14_landing_s29.py. Writes NEEC_DoughnutEconomics_scoring_scratch.md into OUTDIR.
Prints file names only; deterministic.
"""
import contextlib
import hashlib
import importlib.util
import io
import os
import sys

DOC = "NEEC_DoughnutEconomics_scoring_scratch.md"
SNAPSHOT = ("NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md", "1c527415")
D14_GEN = ("d14_landing_s29.py", "6ed2d55c")

EDITS = []


def E(rids, start, end, new, claims):
    EDITS.append(dict(doc="DE", rids=list(rids), start=start, end=end, new=new, claims=list(claims), keep=False,
                      para=False, sub=None))


E(["DE-05"], "The 26-criterion score vector above was checked programmatically in Session",
  "for two things before this document was finalized:",
  "The 26-criterion score vector above was checked programmatically in Session 14, by an ad hoc script named "
  "`verify_doughnut.py`, for two things before this document was finalized:",
  ["by an ad hoc script named `verify_doughnut.py`, for two things before this document was finalized:"])
E(["D22"], "Because the Session 14 script is not on file,", "which the harness (`run_all_checks.py`) runs.",
  "The Session 14 script was not kept. The `verify_doughnut.py` now among the project files is a reconstruction, "
  "written in Session 30 from this section: it reads the vector from this document's criterion headings, repeats "
  "both checks, and reproduces the transcript above byte for byte. It also checks the vector against the canonical "
  "corpus, `neec_scores.csv` and this document's summary block, which `neec_entry.py` validates in full. The "
  "harness (`run_all_checks.py`) runs both.",
  ["The Session 14 script was not kept. The `verify_doughnut.py` now among the project files is a reconstruction, "
   "written in Session 30 from this section:"])
# The D14 wording of DE-05 that this pass removes (the claims verifier asserts that it is gone).
SUPERSEDED = {"DE-05": "by an ad hoc script (`verify_doughnut.py`) that is not among the project files,"}


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
    print("restate_s30.py -- decision D22: the Doughnut Economics Verification section, restated in place")
    print("=" * 96)
    text = pinned(indir, *SNAPSHOT).decode("utf-8")
    pinned(indir, *D14_GEN)
    spec = importlib.util.spec_from_file_location("d14_landing_s29", os.path.join(indir, D14_GEN[0]))
    D14 = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(D14)
    print(f"inputs: {SNAPSHOT[0]} (md5 {SNAPSHOT[1]}); edit function from {D14_GEN[0]} (md5 {D14_GEN[1]})")
    problems = []
    for e in EDITS:
        try:
            text = D14.apply_edit(text, e)
        except ValueError as err:
            problems.append(str(err))
    flat = D14.norm(text)
    for e in EDITS:
        for ph in e["claims"]:
            n = flat.count(D14.norm(ph))
            if n != 1:
                problems.append(f"{','.join(e['rids'])}: restated phrase occurs {n} times: {ph[:60]!r}")
    for rid, ph in SUPERSEDED.items():
        if D14.norm(ph) in flat:
            problems.append(f"{rid}: the D14 wording is still present")
    if problems:
        print("\nPROBLEMS (nothing written):")
        for p in problems:
            print(f"  - {p}")
        return 1
    for e in EDITS:
        print(f"  {','.join(e['rids']):6} applied; restated phrase occurs once: {e['claims'][0][:72]}...")
    print(f"  DE-05  the D14 wording is gone: {SUPERSEDED['DE-05'][:72]}")
    os.makedirs(outdir, exist_ok=True)
    data = text.encode("utf-8")
    with open(os.path.join(outdir, DOC), "wb") as f:
        f.write(data)
    print(f"\nwrote {DOC} (md5 {hashlib.md5(data).hexdigest()[:8]})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
