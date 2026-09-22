#!/usr/bin/env python3
"""
step1c_retrofit.py
===================
NEEC Step 1c: retrofits the 13 pre-existing systems (Report Systems 1-12 +
Integral, Paper Appendix E) from legacy C1.2/C1.5 to the v2 structure
(C1.2a, C1.2b, narrowed C1.5) specified in Paper Section 12.3 / Appendix H.7v2.

METHOD: Per Section 12.5, this is "a re-review of each system's existing
evidence against the new criterion boundaries" -- NOT new research. Every
score below is derived from the ALREADY-PUBLISHED rationale text for that
system's legacy C1.2, C1.5, and (where relevant, e.g. for Gini figures)
C4.4, quoted or closely paraphrased in the RATIONALE strings below, and
checked against Appendix H.7v2's own anchor examples (Market Socialism,
Degrowth, Integral, UBI, Nordic, CCO-PTF are all pre-anchored there).

Each score carries a short RATIONALE and a CONFIDENCE flag:
  'anchored'    - directly matches an existing H.7v2 worked anchor
  'direct'      - follows straightforwardly from already-published text
  'inferential' - defensible but reasons somewhat beyond directly-quoted
                  figures; flagged for independent re-check
  'contestable' - genuinely close call, explicitly flagged for disagreement,
                  consistent with this project's disclosure norms (cf.
                  Georgism's C4.3, Mutual Credit/LETS's C4.3/C5.2)

Run: python3 step1c_retrofit.py
"""
import importlib.util

spec = importlib.util.spec_from_file_location("baseline", "baseline_weighting_script.py")
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)

OLD_SCORES = baseline.SCORES
OLD_PUBLISHED = baseline.PUBLISHED

# ---------------------------------------------------------------------------
# RETROFIT: new C1.2a / C1.2b / C1.5(narrowed) scores, with rationale summary
# and confidence tag, for each of the 13 systems. C1.1/C1.3/C1.4 and all of
# D2-D5 are UNCHANGED (Step 1c's scope is Domain 1's wealth criteria only,
# per Paper Section 12).
# ---------------------------------------------------------------------------
RETROFIT = {
    'Status Quo Market Capitalism': {
        'C1.2a': (0.5, 'direct',
            "Homeownership + retirement accounts are real, functioning accumulation "
            "vehicles (legacy C1.2's own cited mechanisms) but reach only a share of "
            "the population at $60k+/20yr scale -- bottom-50% median is $3,200 "
            "(legacy C1.2's own figure)."),
        'C1.2b': (0.0, 'anchored',
            "Gini 0.85 (legacy C1.5's own figure; H.7v2's own explicit 0.0 anchor "
            "case for this exact criterion) -- no structural prevention mechanism."),
        'C1.5p': (0.5, 'direct',
            "60% have any pathway (legacy C1.5's own figure), access-breadth "
            "component carried forward unchanged; below the >=80% threshold."),
    },
    'Nordic Social Democracy': {
        'C1.2a': (1.0, 'inferential',
            "Pension systems + homeownership programs + savings incentives (legacy "
            "C1.5's own cited mechanisms) are robust, multi-decade institutional "
            "vehicles; legacy C1.2's 0.5 concern ('falls short of universal access') "
            "was about BREADTH/DISTRIBUTION, now C1.5'/C1.2b's job, not about "
            "mechanism adequacy for engaged participants. Less directly evidenced "
            "than the Market Socialism/CCO-PTF 1.0 cases (no specific $ figure in "
            "the existing text) -- flagged as somewhat inferential."),
        'C1.2b': (0.5, 'direct',
            "Wealth Gini 0.65-0.75 (legacy C1.2's own figure, and H.7v2's own "
            "explicit discussion of this exact figure) -- meaningful reduction vs. "
            "unregulated capitalism's 0.85 via real redistributive policy, not "
            "confirmed under 0.35."),
        'C1.5p': (1.0, 'anchored',
            "H.7v2's own explicit worked example: 'the same qualitative-tolerance "
            "judgment call already documented in H.7's own C1.5 entry above carries "
            "over unchanged, since it was never about the Gini clause.'"),
    },
    'Centrally Planned Socialism': {
        'C1.2a': (0.0, 'direct',
            "'No mechanisms for individual wealth building beyond minimal personal "
            "property' (legacy C1.2's own text) -- explicit absence, no named "
            "collective vehicle (distinguishes from Degrowth/ParEcon's 0.5 cases)."),
        'C1.2b': (0.5, 'contestable',
            "Abolition of private capital markets implies very low MEASURED "
            "monetary wealth Gini -- but C4.4's own already-published rationale "
            "explicitly documents 'concentrated economic power' via the nomenklatura "
            "elite (privileged access to goods/housing/travel outside formal "
            "markets). Revised down from an initial 1.0 read to 0.5 to honestly "
            "reflect this tension: extremely compressed FORMAL wealth distribution, "
            "but real, documented DE FACTO privilege concentration a narrow "
            "wealth-Gini reading would miss. Flagged as a genuinely close call."),
        'C1.5p': (0.0, 'direct',
            "Follows C1.2a=0.0: no accumulation mechanism exists for individuals, "
            "so there is nothing for access-breadth to apply to (established "
            "Georgism/Mutual-Credit pattern)."),
    },
    'Market Socialism': {
        'C1.2a': (1.0, 'anchored',
            "Appendix H.8a's own worked example: 'Cooperative membership provides "
            "ownership stake and wealth accumulation... members accumulate "
            "substantial wealth through capital accounts' -- evidence speaks almost "
            "entirely to the buffer-building question."),
        'C1.2b': (0.5, 'anchored',
            "Appendix H.8a's own worked example: 'cooperative systems: Gini "
            "0.40-0.50' -- real progress attributable to distributed ownership, not "
            "confirmed under 0.35. Also matches C4.4's own text: 'Wealth Gini in "
            "cooperative networks is substantially lower... but' not quantified "
            "under threshold."),
        'C1.5p': (0.5, 'direct',
            "Legacy C1.5 text is pure access-breadth reasoning already ('Members "
            "have wealth access, but require cooperative membership... Not truly "
            "universal') -- unchanged by narrowing."),
    },
    'Libertarian Minarchism': {
        'C1.2a': (0.0, 'direct',
            "'Those born poor cannot accumulate initial capital' (legacy C1.2's own "
            "text) -- no baseline mechanism for the majority."),
        'C1.2b': (0.0, 'direct',
            "'Wealth concentration accelerates without redistributive mechanisms' "
            "(legacy C1.5's own text) -- explicit opposite of prevention."),
        'C1.5p': (0.0, 'direct',
            "'Only those born with capital have genuine wealth-building access' "
            "(legacy C1.5's own text) -- narrowest access case in the corpus."),
    },
    'MMT + Job Guarantee': {
        'C1.2a': (0.5, 'direct',
            "'No specific wealth-building mechanisms beyond traditional markets' "
            "(legacy C1.2's own text) -- same underlying mechanism as Status Quo "
            "Capitalism, just with more stable income to engage it."),
        'C1.2b': (0.0, 'contestable',
            "No wealth tax, cap, or targeted capture mechanism in the design; "
            "concentration among capital owners is untouched. C4.4's own 0.5 score "
            "('reduces capital power by providing an exit option... however it "
            "concentrates power in the federal government') is about "
            "bargaining/political power via the job-guarantee exit option, not a "
            "policy targeting wealth-Gini specifically -- this evaluation reads that "
            "as insufficient for C1.2b's structural-prevention threshold, but "
            "discloses this explicitly as the single most consequential close call "
            "in this retrofit (see note below: this is the only tier-crossing case)."),
        'C1.5p': (0.5, 'inferential',
            "Legacy C1.5=1.0 conflated 'universal EMPLOYMENT/income access' with "
            "'universal WEALTH-BUILDING-MECHANISM access' -- but the underlying "
            "accumulation mechanism is explicitly the same traditional-market one "
            "Status Quo Capitalism has (reaching ~60% per that system's own C1.5), "
            "just with guaranteed income improving the ability to engage it. Scored "
            "more conservatively under the narrowed criterion's stricter focus on "
            "mechanism-access specifically, not income access."),
    },
    'Universal Basic Income': {
        'C1.2a': (0.0, 'anchored',
            "THE canonical 0.0 anchor case, cited repeatedly throughout this "
            "project (Georgism, Mutual Credit/LETS both invoke this precedent): "
            "'Provides income but no wealth-building mechanisms... maintains "
            "wealth-excluded underclass despite income provision.'"),
        'C1.2b': (0.0, 'direct',
            "C4.4's own already-published rationale: 'Provides income but not "
            "economic power. Ownership, wealth, capital remain concentrated. UBI "
            "recipients remain subordinate to capital owners despite income "
            "provision.' No mechanism targets wealth concentration."),
        'C1.5p': (0.0, 'anchored',
            "Follows C1.2a=0.0, matching this system's own canonical role as the "
            "precedent case for this exact pattern throughout the project."),
    },
    'Degrowth Economics': {
        'C1.2a': (0.5, 'anchored',
            "H.7v2's own explicit worked anchor FOR THIS EXACT SYSTEM: "
            "'Commons-based wealth (community land trusts, cooperatives) provides "
            "collective security... illustrating the 0.5 band well.'"),
        'C1.2b': (1.0, 'direct',
            "C4.4's own already-published rationale explicitly names 'wealth caps' "
            "as a mechanism: 'Decentralization, wealth caps, cooperative ownership, "
            "democratic governance. Systematically distributes rather than "
            "concentrates power.' Explicit structural cap = clean 1.0 anchor case."),
        'C1.5p': (0.5, 'direct',
            "Legacy C1.5 text ('universal access to resources... but personal "
            "wealth accumulation is limited by design') is access-breadth reasoning "
            "already -- unchanged by narrowing."),
    },
    'Stakeholder Capitalism': {
        'C1.2a': (0.5, 'direct',
            "Stock options / profit-sharing (legacy C1.2's own cited mechanisms) "
            "are real but explicitly 'incremental' and 'expand slightly' -- modest, "
            "not a robust vehicle, matching the same traditional-market pattern as "
            "Status Quo Capitalism."),
        'C1.2b': (0.0, 'direct',
            "C4.4's own already-published rationale: 'One-share-one-vote maintains "
            "wealth-based power concentration... Token stakeholder voice doesn't "
            "challenge fundamental plutocratic control.' No structural cap."),
        'C1.5p': (0.5, 'direct',
            "Legacy C1.5's access-breadth component ('slightly broader wealth "
            "access through expanded stock ownership programs') carried forward, "
            "unchanged in substance."),
    },
    'Fully Automated Luxury Communism': {
        'C1.2a': (0.0, 'direct',
            "'Abundance makes individual wealth accumulation LESS RELEVANT... "
            "unclear if collective abundance equals personal wealth-building "
            "access' (legacy C1.2's own text) -- no named mechanism of any kind, "
            "unlike Degrowth/ParEcon's identified (if imperfect) collective "
            "institutions."),
        'C1.2b': (0.0, 'direct',
            "REVISED from an initial 0.5 (theoretical 'abundance reduces scarcity-"
            "driven concentration' read) after cross-checking C4.4's own "
            "already-published rationale, which is explicitly negative: 'Who "
            "owns/controls the machines is a central question left unresolved. Risk "
            "of technocratic elite (engineers, AI specialists) concentrating "
            "power.' The published evidence leans toward unresolved risk, not "
            "structural prevention -- scored to match that existing finding rather "
            "than override it with a new theoretical argument."),
        'C1.5p': (0.0, 'direct',
            "Follows C1.2a=0.0: 'universal access to abundant goods and services' "
            "is consumption access, not access to an asset-growth mechanism."),
    },
    'Participatory Economics': {
        'C1.2a': (0.5, 'anchored',
            "'No private capital accumulation by design. However, participatory "
            "planning could enable collective wealth-building through community "
            "investment councils' (legacy C1.2's own text) -- a genuinely "
            "collectively-held mechanism, matching H.7v2's own stated distinguishing "
            "logic for the 0.5 band ('collectively-rather-than-individually held') "
            "rather than the 0.0 band (which requires NO mechanism of any kind). "
            "NOTE: an earlier pass in this analysis scored this 0.0 by analogy to "
            "Centrally Planned Socialism; reconsidered and revised to 0.5 for "
            "consistency with H.7v2's own stated Degrowth-anchor logic, since "
            "'community investment councils' is a named collective mechanism, "
            "unlike Centrally Planned Socialism's flat absence."),
        'C1.2b': (1.0, 'anchored',
            "C4.4's own already-published rationale, about as clean an anchor as "
            "exists: 'No concentrated wealth, no capital owners, no managerial "
            "hierarchy.' Comprehensive elimination of private capital ownership."),
        'C1.5p': (0.5, 'direct',
            "Legacy C1.5's own text: 'Participatory councils provide UNIVERSAL "
            "economic input but not wealth accumulation in the traditional sense.' "
            "Access to the (moderate-efficacy, per C1.2a) collective mechanism is "
            "explicitly universal by design (all are council members), balanced "
            "against C1.2a's own finding that the mechanism's asset-growth power is "
            "only partial -- scored to avoid double-counting universality when the "
            "underlying mechanism itself is not a full 1.0."),
    },
    'CCO-PTF-CIP-SZH': {
        'C1.2a': (1.0, 'anchored',
            "Legacy C1.2's own text states the NEEC C1.2a threshold figure "
            "verbatim: 'The median household accumulates $70,000+ over 20 years "
            "through acre equity appreciation plus CCO surplus savings.' Cleanest "
            "possible 1.0 case in the corpus."),
        'C1.2b': (1.0, 'direct',
            "C4.4's own already-published rationale states the C1.2b threshold "
            "figure directly: 'Wealth Gini projected <0.35.'"),
        'C1.5p': (0.5, 'direct',
            "Legacy C1.5's own hedge carried forward unchanged: 'projected 80%+ "
            "participation... depends on implementation completeness... nearly "
            "universal but not absolute' -- projected/modeled, not measured, "
            "consistent with this system's own general Critical-Assessment caveat "
            "about modeling vs. real-world validation."),
    },
    'Integral': {
        'C1.2a': (0.0, 'anchored',
            "H.7v2's own explicit anchor citation for this exact system: ITC "
            "credits 'dissolve...like an energy cycle, not a currency' -- cannot "
            "function as anyone's buffer."),
        'C1.2b': (1.0, 'anchored',
            "H.7v2's own explicit anchor citation for this exact system, cited as "
            "'close to the strongest possible C1.2b answer in the corpus': ITC "
            "'cannot be traded, saved, speculated on, accumulated, or converted "
            "into influence.'"),
        'C1.5p': (0.0, 'anchored',
            "Follows C1.2a=0.0: no value-storage function of any kind exists to "
            "have access to, matching the same pattern this system's own case "
            "originally motivated (Paper Section 12.1)."),
    },
}

ALL_CRITS_25 = [f'C{d}.{i}' for d in range(1, 6) for i in range(1, 6)]
D2_D5_CRITS = [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]

def build_new_scores():
    """Returns dict: system -> {26-criterion score dict}"""
    new_scores = {}
    for sys, old_crit in OLD_SCORES.items():
        rf = RETROFIT[sys]
        new = {}
        new['C1.1'] = old_crit['C1.1']
        new['C1.2a'] = rf['C1.2a'][0]
        new['C1.2b'] = rf['C1.2b'][0]
        new['C1.3'] = old_crit['C1.3']
        new['C1.4'] = old_crit['C1.4']
        new['C1.5'] = rf['C1.5p'][0]
        for c in D2_D5_CRITS:
            new[c] = old_crit[c]
        new_scores[sys] = new
    return new_scores

D1_CRITS_NEW = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5']
ALL_CRITS_NEW = D1_CRITS_NEW + D2_D5_CRITS

def tier(fails):
    if fails < 3:
        return 'Potentially Adequate'
    elif fails <= 5:
        return 'Partially Adequate'
    return 'Structurally Inadequate'

def main():
    new_scores = build_new_scores()
    print("=" * 128)
    print(f"{'System':<36}{'OldD1/5':>9}{'NewD1/6':>9}{'OldTot/25':>11}{'NewTot/26':>11}"
          f"{'OldPct':>8}{'NewPct':>8}{'OldFail':>8}{'NewFail':>8}  OldTier -> NewTier")
    print("=" * 128)

    results = []
    for sys in OLD_SCORES.keys():
        old_c = OLD_SCORES[sys]
        new_c = new_scores[sys]

        old_d1 = sum(old_c[f'C1.{i}'] for i in range(1, 6))
        new_d1 = sum(new_c[c] for c in D1_CRITS_NEW)

        old_total = OLD_PUBLISHED[sys]['Total']
        new_total = round(new_d1 + sum(new_c[c] for c in D2_D5_CRITS), 4)

        # cross-check: new_total should equal old_total - old_d1 + new_d1
        expected_new_total = round(old_total - old_d1 + new_d1, 4)
        assert abs(new_total - expected_new_total) < 1e-9, f"MISMATCH for {sys}: {new_total} vs {expected_new_total}"

        old_fail = sum(1 for c in ALL_CRITS_25 if old_c[c] == 0.0)
        new_fail = sum(1 for c in ALL_CRITS_NEW if new_c[c] == 0.0)

        old_pct = round(old_total / 25 * 100)
        new_pct = round(new_total / 26 * 100)

        old_tier = tier(old_fail)
        new_tier = tier(new_fail)
        tier_flag = "  <<< TIER CHANGE" if old_tier != new_tier else ""

        print(f"{sys:<36}{old_d1:>9.1f}{new_d1:>9.1f}{old_total:>11.1f}{new_total:>11.1f}"
              f"{old_pct:>7}%{new_pct:>7}%{old_fail:>8}{new_fail:>8}  {old_tier} -> {new_tier}{tier_flag}")

        results.append(dict(system=sys, old_d1=old_d1, new_d1=new_d1, old_total=old_total,
                             new_total=new_total, old_pct=old_pct, new_pct=new_pct,
                             old_fail=old_fail, new_fail=new_fail, old_tier=old_tier, new_tier=new_tier))

    print("\n" + "=" * 128)
    print("TIER CHANGES:")
    changed = [r for r in results if r['old_tier'] != r['new_tier']]
    if not changed:
        print("  (none)")
    for r in changed:
        print(f"  {r['system']}: {r['old_tier']} ({r['old_fail']} failures) -> {r['new_tier']} ({r['new_fail']} failures)")

    print("\n" + "=" * 128)
    print("FULL RANKING UNDER NEW 26-CRITERION STRUCTURE (all 13 retrofitted systems,")
    print("descending by new percentage) -- for reference; Georgism (52%) and Mutual")
    print("Credit/LETS (56%) are already on this structure and can be merged in by eye:")
    print("=" * 128)
    for r in sorted(results, key=lambda r: -r['new_total']):
        print(f"  {r['system']:<36} {r['new_total']:>6.1f}/26 ({r['new_pct']:>3}%)  "
              f"{r['new_fail']:>2} failures  {r['new_tier']}")

    return results, new_scores

if __name__ == '__main__':
    main()
