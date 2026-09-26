"""session_check.py - one-command session-start verification (Session 44).

Run from the repository root with the values the latest handoff's "start here" section gives:
  python3 session_check.py --tag s44 --files 258 --digest <md5> --handoff NEEC_Project_Handoff_44.md
Checks: HEAD equals origin/main; tags s34..<tag> exist and <tag> points at HEAD; the tracked-file count;
the digest over every tracked file except the handoff; the harness reproduces its captured output byte
for byte; the latest Actions run on main; the Simulation's and Research Hub's HEADs (reported, not judged).
Needs git and network access; it is a session tool, not a harness check. Prints one line per check.
"""
import argparse
import hashlib
import json
import subprocess
import sys
import urllib.request

REPO = "BetterToBest/NormativeEvaluation"
SIM_PIN = "5a7a7b1"
HUB_PIN = "8e8a6ba"


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--files", type=int, required=True)
    ap.add_argument("--digest", required=True)
    ap.add_argument("--handoff", required=True)
    a = ap.parse_args()
    ok = True

    def line(label, good, detail=""):
        nonlocal ok
        ok &= good
        print(f"{'PASS' if good else 'FAIL'}  {label}{': ' + detail if detail else ''}")

    subprocess.run(["git", "fetch", "-q", "--tags", "origin"], check=True)
    head = git("rev-parse", "HEAD")
    line("HEAD equals origin/main", head == git("rev-parse", "origin/main"), head[:7])
    last = int(a.tag.lstrip("s"))
    tags = set(git("tag").split())
    want = {f"s{n}" for n in range(34, last + 1)}
    line(f"tags s34..{a.tag}", want <= tags, "missing " + ", ".join(sorted(want - tags)) if want - tags else "")
    if a.tag in tags:
        line(f"{a.tag} points at HEAD", git("rev-list", "-n", "1", a.tag) == head)
    files = [f for f in git("ls-files").split("\n") if f]
    line("tracked files", len(files) == a.files, f"{len(files)} (expected {a.files})")
    h = hashlib.md5()
    for f in sorted(files):
        if f != a.handoff:
            h.update(f.encode() + b"\0" + hashlib.md5(open(f, "rb").read()).digest())
    line("digest", h.hexdigest() == a.digest, h.hexdigest())
    out = subprocess.run([sys.executable, "run_all_checks.py"], capture_output=True).stdout
    same = out == open("run_all_checks_output.txt", "rb").read()
    summary = [ln for ln in out.decode().splitlines() if ln.startswith("SUMMARY")]
    line("harness byte-identical", same, summary[0] if summary else "no SUMMARY line")
    try:
        url = f"https://api.github.com/repos/{REPO}/actions/runs?branch=main&per_page=1"
        req = urllib.request.Request(url, headers={"User-Agent": "neec-session-check"})
        r = json.load(urllib.request.urlopen(req, timeout=20))["workflow_runs"][0]
        line("latest Actions run on main", r["conclusion"] == "success",
             f"run {r['run_number']} at {r['head_sha'][:7]}: {r['status']}/{r['conclusion']}")
    except Exception as e:  # network may be restricted; report, don't fail the session
        print(f"NOTE  Actions not checked ({type(e).__name__})")
    for name, pin in (("compassionism-simulation", SIM_PIN), ("research-hub", HUB_PIN)):
        try:
            sha = git("ls-remote", f"https://github.com/BetterToBest/{name}", "HEAD")[:7]
            print(f"{'INFO' if sha == pin else 'NOTE'}  {name} HEAD {sha}" + ("" if sha == pin else f" (pin {pin})"))
        except Exception as e:
            print(f"NOTE  {name} not checked ({type(e).__name__})")
    print("ALL PASS" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
