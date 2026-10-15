# NEEC Rescoring Pass — Record, Stage 2, Group 2.10: C4.2 Ecological Compliance (class M)

**Session 64 · 2026-10-15 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b), groups 2.1 to 2.9 and part 58.1 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s63.md` and `owner_s58.py`; this record edits none of them.** No corpus file, score or scoring document
changes until the pass ends. Its changes are then applied by generator with pinned inputs and restated in place
(protocol 10.2, 10.3; decisions D12, D14), and until then the published totals stand, provisional as `README.md` says.
Decisions taken here are Claude's under the owner's delegation (Handoff 35, section 2; decision 57.2: only
CCO-PTF-CIP-SZH's score changes wait on the owner, and none is made here); each is recorded with its reasons, and the
owner may reverse any of them.
**Reproduce:** `python3 rescoring_s64.py` (harness check 110). It is written on the shared module (`pass_common.py`,
decision 52.5): the script holds the 16 readings and the group's own checks, and the module computes the consequences
cumulatively with every part before it. It checks the two data files this group added to the evidence cache
(`evidence_cache/C4.2/`) by digest, finds the rows quoted, recomputes every rate and index change the readings quote,
locates each unit's published rationale and checks that this record contains its generated tables verbatim. It reads no
network.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7), rerun after group 2.9, put C4.2 first among the criteria still
to read: 16 units in play, three of them able to change an adequacy tier on their own. C4.2 is class M: v2.0 restates its
bar and measure (K3, K4, R1, G3, S2). Its four clauses are consumption-based CO2 emissions falling at least 3.8% a year
(the rate of a 35% cut over 2019-2030, binding at any date), biodiversity neutral or positive (the IUCN Red List Index,
SDG indicator 15.5.1), the ecological footprint of consumption per person no greater than world biocapacity per person,
and no more than two of the four nationally downscaled planetary boundaries transgressed (`criteria.json`;
`NEEC_Criteria_v2_s45.md`). Part (b7) (`NEEC_Rescoring_s47.md`) read the seven published 1.0s, each to 0.5, and set the
readings this group applies to designs and mechanisms: a clause is shown only by a projection on the measure (its 3.3 and
3.4). This group reads the other 16: eight 0.5s and eight 0.0s, the four configured national economies (Status Quo,
China, Singapore, Qatar) and Nordic Social Democracy on the accounts v2.0 names.

**Outcome.** **Nothing moves.** All 16 hold: eight at 0.5 and eight at 0.0 (Status Quo, Libertarian Minarchism,
Stakeholder Capitalism, Sovereign Wealth Fund Statism, China, Singapore, Qatar, Islamic Finance). No unit clears all four
clauses, so none is 1.0, and C4.2 stays among the criteria no scored system clears. The accounts bear the published scores
out. The four configured economies fall short on carbon (the United States cuts consumption-based emissions 0.7% a year
over 2019-2023 against a bar of 3.8%; China, Qatar and, since 2019, Singapore raise them) and on biodiversity (their Red
List Index declines). **Nordic Social Democracy is the first unit in the pass to clear a C4.2 clause**: the index is
unchanged in Denmark, Finland, Norway and Sweden from 2015 to 2025; its carbon clause is short, since Denmark and Sweden
fall between 1.4% and 2.3% a year on every window and none of the four reaches the bar over ten years (reading 3.4). Six units are
flagged; two of the flags, Market Socialism toward 0.0 and Sovereign Wealth Fund Statism toward 0.5, could each change a
tier. No tier, rank or first place changes (CCO-PTF-CIP-SZH and Integral share 14.5).

## 2. How a clause is recorded, and the rule

As in groups 2.2 to 2.9 and decision 53.2: each clause is cleared, short, not shown, out of reach or moot. A unit is 1.0
only if every clause is cleared (D28, protocol 2.3); 0.0 only on one of protocol 2.1's whole-criterion conditions, stated
as the unit's reason and never with a clause cleared; 0.5 otherwise. A clause-level gap never makes 0.0 (D28(f)). "Not
shown" means that no estimate of the clause's quantity was located, not that the clause fails; "short" means the
evidence located falls below it. For a mechanism, a clause whose quantity it does not govern even when generalised is
out of reach, and the host economy's figure is not credited to it (protocol 3.2, D28(c)).

## 3. Decisions and readings (under the delegation)

**3.1 What the clauses ask, and what the measure counts (decision 64.1, a method choice).** (1) *The question.* Clause 1
is "a compound annual rate of change over the scoring window", but v2.0 names no window for a national economy.
Clause 2 asks that the Red List Index be non-declining over it. (2) *Interpretations.* (a) The window is the bar's own,
2019 to the latest year of the accounts (2023); (b) it is the latest ten years; (c) either window, reading the clause
short only where both fall short. (3) *Preponderance:* report all three of 2019 to 2023, 2013 to 2023 and 2007 to 2023
(the last where the accounts allow), and call a clause short only if the economy falls short on every window read, as
reading (c) does. The bar "binds at any date" (v2.0), so a rate reached on a window including 2020's fall is not
discounted, and it is not credited alone either. (4) *Applied:* the rate is the compound annual rate between the end
years of the window, on the Global Carbon Budget's consumption-based accounts as Our World in Data republishes them. The
bar is 3.84% a year (0.65 to the power of 1/11), the 3.8% v2.0 states. For clause 2 the window is 2015 to 2025, and the
index's two decimals are the resolution: a series unchanged at two decimals is non-declining; a series that falls by
0.01 is declining. The index covers the species occurring in the economy, not the pressure its consumption puts on
species elsewhere; v2.0 names it as the measure. *Reopening:* a window v2.0 or the criteria record's next amendment
fixes.

**3.2 0.0 and 0.5 on C4.2 (decision 64.2, a method choice, as decision 61.1 was for C4.3).** (1) *The question.* A class M
re-read may lower a 0.5 or raise a 0.0 (decision 53.2), so the line must be drawn the same way for every unit. C4.2's
0.0 band reads "relative or efficiency metrics substituting for absolute ones" and its 0.5 band "meaningful mitigation
exists but growth or consumption imperatives are not fully subordinated to ecological limits". (2) *Interpretations.*
(a) Any unit that has not shown a clause is 0.0; (b) any unit with some mitigation is 0.5; (c) protocol 2.1's three
conditions, read on C4.2's measure. (3) *Preponderance:* (c). The band texts describe and protocol 2.1 governs
(protocol 2.3(g)); (a) would make every design 0.0 by a test it cannot pass, the mirror of the test that cannot fail
which part (b1)'s reading 3.1 rejects. Read on C4.2, the conditions are: *no structural mechanism addresses the
criterion*; *the system excludes the concern* (its own logic rules out the constraint, or its funding depends on what the
criterion requires it to end); *far below the threshold with no credible pathway under the system's own logic* (a
rate far from the bar on the accounts with an account of why it stays so). (4) *Applied:* the eight published 0.0s each
meet one, and each is stated as the unit's reason; the eight 0.5s do not, and none is moved. A unit whose mechanism bears
on the criterion without fixing its direction (a transfer, a cooperative form, a local currency) is 0.5 with a flag,
not 0.0: the rule asks for a reason about the system, not for the absence of an estimate.

**3.3 The four configured economies (decision 64.3).** United States, China, Singapore and Qatar, on the accounts of 3.1
(sources in section 5).

| Economy | 2019-2023 | 2013-2023 | 2007-2023 | Red List Index 2015, 2025 |
|---|---:|---:|---:|---|
| United States | -0.7% | -0.4% | -1.1% | 0.83, 0.82 |
| China | +2.7% | +2.3% | +4.4% | 0.85, 0.83 |
| Singapore | +1.6% | -2.5% | +2.4% | 0.92, 0.89 |
| Qatar | +1.4% | +4.0% | +4.4% | 0.81, 0.78 |

The bar is a fall of 3.84% a year. *United States:* the only one of the four whose consumption-based emissions fall, at
about a fifth of the bar's rate on every window; Status Quo stays at 0.0 on the published account (efficiency gains offset
by scale, a growth imperative), which the accounts show as a fall that is the system's best case and no pathway to the
bar. *China:* rising on every window; the operative targets were relative and missed; the published flag toward 0.5
(deployment at scale, announced absolute targets) is kept. *Singapore:* the sign depends on the window (up since 2019,
down 2.5% a year over the decade), and neither reaches the bar; the published flag toward 0.5 is kept. *Qatar:* rising,
the highest per-capita emitter on the entry's figures. For each, the Red List Index declines. Clauses 3 and 4 are not
shown (3.8). Each holds at 0.0, a published score, on its stated reason.

**3.4 Nordic Social Democracy (decision 64.4).** Read on Denmark, Finland, Norway and Sweden, as part (b8) read it on
C4.3. *Clause 1* is short: the clause is for each economy the entry is read on, as in part (b8), and Denmark (-1.7% a year over 2019-2023, -1.4% over the
decade) and Sweden (-2.0%, -1.6%) fall well under the bar on every window; Finland (-4.3%) and Norway (-5.2%) reach it
on the window that includes 2020's fall and fall under it over ten years (-3.5%, -3.1%); Finland's -3.9% since 2007 is
just past the bar and Norway's -2.8% is not. Denmark and Sweden are short on every window read, so the family is short. *Clause 2* is
cleared: the index is 0.97, 0.98, 0.95 and 0.99 in 2015 and again in 2025, and unchanged since 2010 in all four. It is the
first C4.2 clause cleared by any unit in the pass. Clauses 3 and 4 are not shown (3.8). One clause cleared does not make
1.0 (D28), and the published account (leading renewable and environmental policy, consumption patterns and trade
embedding costs abroad, absolute reductions not achieved) is the 0.5 band's. Holds at 0.5. *Alternative weighed:* credit
the index as evidence that the Nordic economies are within ecological limits at home. Not adopted: the index counts the
species occurring in the country, so it cannot show the pressure of consumption that v2.0's requirement is "measured on
consumption" to capture.

**3.5 Designs and mechanisms at 0.5 (decision 64.5).** The 11 units that are not read on national accounts are designs,
mechanisms or a historical system; the seven at 0.5 (Centrally Planned Socialism, Market Socialism, Universal Basic Income, Georgism,
Mutual Credit, Universal Basic Services, Ostrom-style commons) show no clause by the part (b7) test, since none has a
projection of consumption-based emissions, of pressure on species and habitat, of the footprint or of the boundaries
under the system. Each holds at 0.5 on the mechanism or record its published account gives. Universal Basic Services'
Luxembourg precedent (road-transport CO2 down about 5.9%) is a sector's level once, a quantified finding of partial
reach, not a national rate. Ostrom-style commons: clauses 1 and 4 are out of reach by the mechanism's own scale (a global
test against a local commons, the scale limit stated by the mechanism's author); clause 3 is not shown, since the
sustained yield of a managed local resource, though well evidenced and the mechanism's definition of success, is not a
national footprint per person. *Flags* (toward 0.0, none moves a score): **Market Socialism**, since the entry itself
says market competition bounds how much a cooperative can sacrifice competitiveness for ecology, which is a growth
imperative left in place (it could change the entry's tier: two failures to three); **Universal Basic Income**, a
transfer's consumption effect with a carbon tax a funding choice the design does not fix; **Centrally Planned
Socialism**, the published account's own point that its lower footprint was not due to sustainability principles and
that limits were disregarded wherever growth was prioritised. Centrally Planned Socialism's and Universal Basic
Income's tiers cannot change.

**3.6 The 0.0s that are mechanisms (decision 64.6).** Libertarian Minarchism holds on the system's own logic (the state is
confined to protecting rights, ruling out the constraint on extraction and emission the criterion measures).
Stakeholder Capitalism holds as the band's own example (relative and efficiency metrics, net-zero pledges resting on
offsets). Islamic Finance holds: the instruments (green sukuk, a grant scheme, value-based intermediation) direct capital
to better projects and none constrains the total; the published entry did not flag it. Sovereign Wealth Fund Statism
holds: the mechanism's own funding is fossil-fuel extraction, which Norway expanded with 57 licences in 2026, and the
fund's exclusions govern what it holds, not the economy's emissions (part (b6), reading 3.6). **Flag, new:** Sovereign
Wealth Fund Statism toward 0.5, crediting the fund's own conduct (coal, tar-sands and oil-sands exclusions, a spending
rule) as partial mitigation and not crediting the host economy's extraction to the mechanism (protocol 3.2). It would
move the entry's failures from three to two, a better tier. It is flagged, not applied: the published reason, that the
mechanism's own funding depends on extraction, is about the mechanism and not the host economy, so protocol 3.2 does
not remove it.

**3.7 Flags.** Six, all kept as flags. Toward 0.0: Centrally Planned Socialism, Market Socialism, Universal Basic Income
(reading 3.5). Toward 0.5: Sovereign Wealth Fund Statism (3.6), China and Singapore (3.3, the published flags kept).
Market Socialism's and Sovereign Wealth Fund Statism's could each change a tier.

**3.8 Clauses 3 and 4 are not shown for any unit.** The footprint accounts of the Footprint Data Foundation and York
University are published through an API (data.footprintnetwork.org) that answered HTTP 403 to the container, and no open
republication was located (Our World in Data's footprint charts were tried under more than ten names, and its search returned none); the
nationally downscaled boundary accounts (O'Neill et al. 2018; Fanning et al. 2022) are published through the Leeds
Good Life site, not read here as a table. Clause 3 and clause 4 are therefore "not shown" for the four economies and the
Nordic countries, which is an absence of an estimate, not a finding that the clause fails; no verdict here rests on
either. *Reopening:* the footprint per person and the count of boundaries transgressed for the four economies and the
Nordic countries; a cleared clause 3 or 4 changes no score alone, since clauses 1 and 2 are short or not shown.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Carbon | Biodiversity | Footprint | Boundaries | Verdict | Flag |
|---|---:|---|---|---|---|---:|---|
| SQ | 0.0 | short | short | not shown | not shown | 0.0 |  |
| NSD | 0.5 | short | cleared | not shown | not shown | 0.5 |  |
| CPS | 0.5 | not shown | not shown | not shown | not shown | 0.5 | toward 0.0 |
| MS | 0.5 | not shown | not shown | not shown | not shown | 0.5 | toward 0.0 |
| LM | 0.0 | not shown | not shown | not shown | not shown | 0.0 |  |
| UBI | 0.5 | not shown | not shown | not shown | not shown | 0.5 | toward 0.0 |
| SC | 0.0 | not shown | not shown | not shown | not shown | 0.0 |  |
| GEO | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| MC | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| UBS | 0.5 | not shown | not shown | not shown | not shown | 0.5 |  |
| SWF | 0.0 | not shown | not shown | not shown | not shown | 0.0 | toward 0.5 |
| CN | 0.0 | short | short | not shown | not shown | 0.0 | toward 0.5 |
| SG | 0.0 | short | short | not shown | not shown | 0.0 | toward 0.5 |
| QA | 0.0 | short | short | not shown | not shown | 0.0 |  |
| IF | 0.0 | not shown | not shown | not shown | not shown | 0.0 |  |
| OS | 0.5 | out of reach | not shown | not shown | out of reach | 0.5 |  |

### 4.2 Clause by clause (generated)

#### SQ C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | short | United States, consumption-based CO2: -0.7% a year over 2019-2023, -0.4% over 2013-2023, -1.1% over 2007-2023; the bar is a fall of 3.8% a year (a 35% cut over 2019-2030); the world's rose +0.8% a year over 2019-2024 (reading 3.3) | Global Carbon Budget national consumption-based CO2 accounts (Friedlingstein et al.), as republished by Our World in Data, chart consumption-co2-emissions (evidence_cache/C4.2/owid_gcb_consumption_co2.csv, retrieved 2026-10-15); Report v1.6, SQ C4.2 |
| 2 | biodiversity neutral or positive | short | United States, Red List Index 0.83 in 2015, 0.82 in 2025: declining (reading 3.3) | IUCN Red List Index (the indicator SDG 15.5.1 reports), as republished by Our World in Data, chart red-list-index (evidence_cache/C4.2/owid_iucn_red_list_index.csv, retrieved 2026-10-15); Report v1.6, SQ C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | the ecological footprint of consumption per person against world biocapacity per person (National Footprint and Biocapacity Accounts) was not reachable: data.footprintnetwork.org's API answered HTTP 403 and no open republication was located, so the clause is not shown (reading 3.8) | Report v1.6, SQ C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | the nationally downscaled boundaries (O'Neill et al. 2018; Fanning et al. 2022) were not located as a table for this economy, so the count of boundaries transgressed is not shown (reading 3.8) | Report v1.6, SQ C4.2 |

*0.0 (protocol 2.1):* the best evidence shows performance far below the threshold with no credible pathway under the system's own logic (protocol 2.1): consumption-based emissions fell about a fifth of the bar's rate, and the published account (efficiency gains offset by scale, a growth imperative) is the 0.0 band's own description; a fall of this size is the system's best case, not a pathway to the bar.

*Note:* 0.0 holds.

#### NSD C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | short | consumption-based CO2, 2019-2023 and 2013-2023 (% a year): Denmark -1.7 and -1.4; Finland -4.3 and -3.5; Norway -5.2 and -3.1; Sweden -2.0 and -1.6; the bar is 3.8%: Finland and Norway reach it on the window that includes 2020's fall, none on the ten-year window, and Denmark and Sweden reach it on neither, so the economy-wide clause is short (reading 3.4) | Global Carbon Budget national consumption-based CO2 accounts (Friedlingstein et al.), as republished by Our World in Data, chart consumption-co2-emissions (evidence_cache/C4.2/owid_gcb_consumption_co2.csv, retrieved 2026-10-15); Report v1.6, NSD C4.2 |
| 2 | biodiversity neutral or positive | cleared | Red List Index, 2015 and 2025: Denmark 0.97 and 0.97; Finland 0.98 and 0.98; Norway 0.95 and 0.95; Sweden 0.99 and 0.99: unchanged in all four to the index's two decimals, so non-declining over the window (reading 3.4); the index covers the species occurring in the country, not the pressure its consumption puts on species elsewhere | IUCN Red List Index (the indicator SDG 15.5.1 reports), as republished by Our World in Data, chart red-list-index (evidence_cache/C4.2/owid_iucn_red_list_index.csv, retrieved 2026-10-15); Report v1.6, NSD C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | the ecological footprint of consumption per person against world biocapacity per person (National Footprint and Biocapacity Accounts) was not reachable: data.footprintnetwork.org's API answered HTTP 403 and no open republication was located, so the clause is not shown (reading 3.8) | Report v1.6, NSD C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | the nationally downscaled boundaries (O'Neill et al. 2018; Fanning et al. 2022) were not located as a table for this economy, so the count of boundaries transgressed is not shown (reading 3.8) | Report v1.6, NSD C4.2 |

*Note:* 0.5 holds: the published account (leading renewable and environmental policy, absolute reductions not achieved) is the 0.5 band's, and the measure bears it out for two of the four countries on one window; the only clause cleared in the group, and one clause cleared never makes 1.0 (reading 3.4).

#### CPS C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | no consumption-based account exists for the planned economies of the record (the accounts begin in 1990, after the Soviet system's end); no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, CPS C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3); the record's Aral Sea and pollution disasters are damage, not a level of the index | Report v1.6, CPS C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, CPS C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, CPS C4.2 |

*Flag (reading 3.5):* toward 0.0: weighting the published account (ecological limits disregarded wherever growth was prioritised) as the 0.0 band's growth imperative with no pathway under the system's own logic; the entry's 0.5 rests on lower per-capita consumption, which the entry itself says was not due to sustainability principles.

*Note:* 0.5 holds on the published account (reading 3.5); flagged.

#### MS C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, MS C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | Report v1.6, MS C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, MS C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, MS C4.2 |

*Flag (reading 3.5):* toward 0.0: weighting the entry's own limit, that market competition bounds how much a cooperative can sacrifice competitiveness for ecology, as a growth imperative the mechanism leaves in place; it could change the entry's tier.

*Note:* 0.5 holds: democratic control over firms is a mechanism that can subordinate profit to ecology and some cooperatives use it, and the entry records its limit, the 0.5 band's description (reading 3.5); flagged.

#### LM C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | no ecological constraint exists in the system's logic, so no rate is to be read; no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, LM C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | Report v1.6, LM C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, LM C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, LM C4.2 |

*0.0 (protocol 2.1):* the system excludes the criterion's concern (protocol 2.1): its own logic confines the state to protecting rights and rules out the regulatory constraint on extraction and emission that the criterion measures, as the published account says (externalities unaddressed, private property rights insufficient against a commons).

*Note:* 0.0 holds (reading 3.6).

#### UBI C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | a transfer raises household consumption; whether the emissions rise depends on what funds it and on complementary policy, as the entry says; no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, UBI C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | Report v1.6, UBI C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, UBI C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, UBI C4.2 |

*Flag (reading 3.5):* toward 0.0: weighting the transfer's consumption effect as a growth imperative with no ecological mechanism of its own, a carbon tax being a funding choice the design does not fix.

*Note:* 0.5 holds: the entry's two-sided account (consumption effect against a possible carbon-tax funding) is the 0.5 band's second description; a mechanism that bears on the criterion without fixing its direction (reading 3.5); flagged.

#### SC C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | ESG metrics report relative improvements (intensity) and net-zero pledges lean on offsets; no absolute rate attributable to the mechanism is located; no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, SC C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | Report v1.6, SC C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, SC C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, SC C4.2 |

*0.0 (protocol 2.1):* far below the threshold with no credible pathway under the system's own logic (protocol 2.1): relative and efficiency metrics substitute for absolute ones, the 0.0 band's own text, for which this unit is the band's example.

*Note:* 0.0 holds (reading 3.6).

#### GEO C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, GEO C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | Report v1.6, GEO C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, GEO C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | land-use taxation is linked to construction-land carbon-emission efficiency in a 30-province study and densification is an abatement lever, a channel for the land-system boundary; no downscaled count follows; no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, GEO C4.2 |

*Note:* 0.5 holds: an actively studied causal channel with no hard ecological ceiling, the 0.5 band (reading 3.5).

#### MC C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | Report v1.6, MC C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | Report v1.6, MC C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | Report v1.6, MC C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | Report v1.6, MC C4.2 |

*Note:* 0.5 holds: a consistent value for local exchange that structurally cannot fund long-distance supply chains, with no quantified effect and no ceiling (reading 3.5).

#### UBS C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | the closest precedent, Luxembourg's fare-free public transport (2020), cut road-transport CO2 by about 5.9% in a synthetic difference-in-differences study: a sector's level once, not a consumption-based annual rate for an economy; no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | NEEC_UniversalBasicServices_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | NEEC_UniversalBasicServices_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | NEEC_UniversalBasicServices_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | NEEC_UniversalBasicServices_scoring_scratch.md, C4.2 |

*Note:* 0.5 holds: a quantified, causally designed finding of partial reach (reading 3.5).

#### SWF C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | the exemplars' revenue is fossil-fuel extraction and Norway expanded licensing in 2026; the fund's exclusions govern what it holds, not the economy's emissions (part (b6), reading 3.6); no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2 |

*0.0 (protocol 2.1):* the system excludes the criterion's concern (protocol 2.1): the mechanism's own funding is continued fossil-fuel extraction, which the criterion constrains, so the mechanism depends on what the criterion requires it to end.

*Flag (reading 3.6):* toward 0.5: crediting the fund's own conduct (coal, tar-sands and oil-sands exclusions, a spending rule) as partial mitigation and not crediting the host economy's extraction to the mechanism (protocol 3.2); it could change the entry's tier.

*Note:* 0.0 holds (reading 3.6); flagged.

#### CN C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | short | China, consumption-based CO2: +2.7% a year over 2019-2023, +2.3% over 2013-2023, +4.4% over 2007-2023: rising; the bar is a fall of 3.8% a year (a 35% cut over 2019-2030) (reading 3.3) | Global Carbon Budget national consumption-based CO2 accounts (Friedlingstein et al.), as republished by Our World in Data, chart consumption-co2-emissions (evidence_cache/C4.2/owid_gcb_consumption_co2.csv, retrieved 2026-10-15); NEEC_StateCapitalism_China_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | short | China, Red List Index 0.85 in 2015, 0.83 in 2025: declining (reading 3.3) | IUCN Red List Index (the indicator SDG 15.5.1 reports), as republished by Our World in Data, chart red-list-index (evidence_cache/C4.2/owid_iucn_red_list_index.csv, retrieved 2026-10-15); NEEC_StateCapitalism_China_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | the ecological footprint of consumption per person against world biocapacity per person (National Footprint and Biocapacity Accounts) was not reachable: data.footprintnetwork.org's API answered HTTP 403 and no open republication was located, so the clause is not shown (reading 3.8) | NEEC_StateCapitalism_China_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | the nationally downscaled boundaries (O'Neill et al. 2018; Fanning et al. 2022) were not located as a table for this economy, so the count of boundaries transgressed is not shown (reading 3.8) | NEEC_StateCapitalism_China_scoring_scratch.md, C4.2 |

*0.0 (protocol 2.1):* far below the threshold with no credible pathway under the system's own logic (protocol 2.1): consumption-based emissions are rising, the operative targets have been relative (an intensity cut of 18% was targeted and about 12% achieved), and the index is falling.

*Flag (reading 3.3):* toward 0.5: the published flag kept: weighting the scale of renewable deployment and the announced absolute targets as a credible pathway.

*Note:* 0.0 holds; the published flag kept (reading 3.3).

#### SG C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | short | Singapore, consumption-based CO2: +1.6% a year over 2019-2023, -2.5% over 2013-2023, +2.4% over 2007-2023: the sign depends on the window, and neither reaches the bar of 3.8% (reading 3.3) | Global Carbon Budget national consumption-based CO2 accounts (Friedlingstein et al.), as republished by Our World in Data, chart consumption-co2-emissions (evidence_cache/C4.2/owid_gcb_consumption_co2.csv, retrieved 2026-10-15); NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | short | Singapore, Red List Index 0.92 in 2015, 0.89 in 2025: declining (reading 3.3) | IUCN Red List Index (the indicator SDG 15.5.1 reports), as republished by Our World in Data, chart red-list-index (evidence_cache/C4.2/owid_iucn_red_list_index.csv, retrieved 2026-10-15); NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | the ecological footprint of consumption per person against world biocapacity per person (National Footprint and Biocapacity Accounts) was not reachable: data.footprintnetwork.org's API answered HTTP 403 and no open republication was located, so the clause is not shown (reading 3.8) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | the nationally downscaled boundaries (O'Neill et al. 2018; Fanning et al. 2022) were not located as a table for this economy, so the count of boundaries transgressed is not shown (reading 3.8) | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2 |

*0.0 (protocol 2.1):* far below the threshold with no credible pathway under the system's own logic (protocol 2.1): consumption-based emissions are up since 2019 and the decade's fall is under the bar, the index is falling, and the 2030 target path rises on the entry's own account (Climate Action Tracker: highly insufficient).

*Flag (reading 3.3):* toward 0.5: the published flag kept: weighting the ten-year fall in consumption-based emissions and the carbon tax as a credible pathway.

*Note:* 0.0 holds; the published flag kept (reading 3.3).

#### QA C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | short | Qatar, consumption-based CO2: +1.4% a year over 2019-2023, +4.0% over 2013-2023, +4.4% over 2007-2023: rising; the bar is a fall of 3.8% a year (a 35% cut over 2019-2030) (reading 3.3) | Global Carbon Budget national consumption-based CO2 accounts (Friedlingstein et al.), as republished by Our World in Data, chart consumption-co2-emissions (evidence_cache/C4.2/owid_gcb_consumption_co2.csv, retrieved 2026-10-15); NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | short | Qatar, Red List Index 0.81 in 2015, 0.78 in 2025: declining (reading 3.3) | IUCN Red List Index (the indicator SDG 15.5.1 reports), as republished by Our World in Data, chart red-list-index (evidence_cache/C4.2/owid_iucn_red_list_index.csv, retrieved 2026-10-15); NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | the ecological footprint of consumption per person against world biocapacity per person (National Footprint and Biocapacity Accounts) was not reachable: data.footprintnetwork.org's API answered HTTP 403 and no open republication was located, so the clause is not shown (reading 3.8) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | the nationally downscaled boundaries (O'Neill et al. 2018; Fanning et al. 2022) were not located as a table for this economy, so the count of boundaries transgressed is not shown (reading 3.8) | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2 |

*0.0 (protocol 2.1):* far below the threshold with no credible pathway under the system's own logic (protocol 2.1): the highest per-capita emitter in the world on the entry's figures, consumption-based emissions rising, a rent system funded by hydrocarbon exports, no carbon price, and a pledge against an unpublished baseline.

*Note:* 0.0 holds (reading 3.3).

#### IF C4.2 Ecological Compliance: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | not shown | proceeds-use labels (green sukuk, a grant scheme, value-based intermediation) direct capital to better projects without a cap on the total; no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | NEEC_IslamicFinance_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3) | NEEC_IslamicFinance_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | no projection of the system's footprint per person against biocapacity is stated or located | NEEC_IslamicFinance_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | not shown | no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located | NEEC_IslamicFinance_scoring_scratch.md, C4.2 |

*0.0 (protocol 2.1):* far below the threshold with no credible pathway under the system's own logic (protocol 2.1): the mechanism's ecological instruments are allocative labels, none constrains the total, the 0.0 band's relative-for-absolute substitution that the corpus records against Stakeholder Capitalism.

*Note:* 0.0 holds; the published entry did not flag it (reading 3.6).

#### OS C4.2 Ecological Compliance: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | Consumption-based carbon emissions falling ≥3.8% a year | out of reach | a global test: Ostrom's own statement is that the design principles are for local commons of bounded scale, and a consumption-based national rate is outside the mechanism's reach; no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or located, so the rate is not shown (part (b7), reading 3.4) | NEEC_Ostrom_Commons_scoring_scratch.md, C4.2 |
| 2 | biodiversity neutral or positive | not shown | no projection of pressure on species and habitat under the system is stated or located (part (b7), reading 3.3); well-evidenced local yields are not the index | NEEC_Ostrom_Commons_scoring_scratch.md, C4.2 |
| 3 | resource extraction ≤ regeneration | not shown | sustained yield of a managed local resource is the mechanism's definition of success and is well evidenced, but it is not a national footprint per person against biocapacity | NEEC_Ostrom_Commons_scoring_scratch.md, C4.2 |
| 4 | no more than two of the four nationally downscaled planetary boundaries transgressed | out of reach | the nationally downscaled boundaries are a global test and a local commons governs one resource, so the count is outside the mechanism's reach | NEEC_Ostrom_Commons_scoring_scratch.md, C4.2 |

*Note:* 0.5 holds: the 0.5 band's meaningful mitigation, with two clauses out of reach by the mechanism's own scale (reading 3.5).

## 5. The sources added to the evidence cache

Written on 2026-10-15 by `evidence_cache_s64.py` (which holds each file's md5 and fetches with `--fetch`). Both files are
the rows of nine economies (China, Denmark, Finland, Norway, Qatar, Singapore, Sweden, the United States and the world)
from Our World in Data's open CSV for two charts. `owid_gcb_consumption_co2.csv` is its chart *consumption-co2-emissions*,
annual consumption-based CO2 emissions in tonnes, 1990 to 2023 (Norway from 2003; the world to 2024), from the Global
Carbon Budget. `owid_iucn_red_list_index.csv` is its chart *red-list-index*, the IUCN Red List Index by country, 1980 to
2025. Our World in Data is a republisher, not the original; the Global Carbon Budget's and the IUCN's own files were not
read. The rows and values are checked by digest and by the passages the script quotes.

## 6. What parts (a), (b), groups 2.1 to 2.9 and part 58.1 change (generated)

| Entry | Published (rank) | After group 2.9 (rank) | After group 2.10 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 14.5 (1) | 14.5 (1) | 0.0 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.0 (3) | 14.0 (3) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.5 (4) | 0.0 | 1 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (1) | 14.5 (1) | 0.0 | 2 | Potentially Adequate |
| DG | 19.0 (5) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.0 (5) | 13.0 (5) | 0.0 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.0 (14) | 11.0 (14) | 0.0 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 10.5 (15) | 10.5 (15) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (9) | 12.5 (9) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 13.0 (5) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (9) | 12.5 (9) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 4 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (11) | 11.5 (11) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.0 (18) | 9.0 (18) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 9.0 (18) | 9.0 (18) | 0.0 | 8 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.5 (21) | 8.5 (21) | 0.0 | 9 | Structurally Inadequate |
| LM | 8.0 (23) | 7.0 (23) | 7.0 (23) | 0.0 | 13 | Structurally Inadequate |

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | (2.3) | (2.4) | (2.5) | 58.1 | (2.6) | (2.7) | (2.8) | (2.9) | (2.10) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | -0.5 |  | -0.5 | 0.5 |  |  |  |  |  | 14.5 | 22 | 20 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | 14.0 | 17 | 16 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 |  | 0.5 |  |  |  |  |  |  |  | 13.5 | 17 | 16 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  |  | 14.5 | 17 | 14 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 13.0 | 16 | 16 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 13.0 | 16 | 14 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 11.0 | 11 | 9 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 10.5 | 14 | 11 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 13 | 10 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 13.0 | 12 | 10 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  |  | 13.0 | 12 | 8 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  | 11.5 | 11 | 10 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12.5 | 10 | 9 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  | 11.5 | 12 | 9 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 11.5 | 11 | 9 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 9.0 | 14 | 11 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.0 | 12 | 10 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | -0.5 | 0.5 |  | 9.5 | 10 | 6 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  | 7.5 | 11 | 8 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  |  | 0.5 |  |  |  |  |  |  |  | 9.0 | 10 | 8 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9.5 | 9 | 6 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  |  | 0.5 |  |  |  |  |  |  |  | 8.5 | 10 | 8 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 |  | 0.5 |  |  |  |  |  |  |  | 7.0 | 12 | 6 |

After this group the corpus has 17 dominance pairs against 17 after group 2.9 (new: none; lost: none), and its frontier holds 15 entries against 15 (SQ, NSD, CPS, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place is shared by CCO and INT at 14.5 (CCO 14.5, INT 14.5 after group 2.9), ahead of PE at 14.0. Across the pass so far 299 units have been re-estimated, each counted once: 18 are at 1.0, 244 at 0.5 and 37 at 0.0; against their published scores 149 fell, 8 rose and 142 are unchanged (net -70.5 points).

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.5)); C1.4's 1.0 example, CCO (part (2.5)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.1's 0.0 example, SQ (part (2.9)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C3.5's 0.0 example, LM (part (2.4)); C3.5's 0.0 example, SC (part (2.4)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.2's 0.0 example, INT (part (2.6)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C1.4's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

C4.2's published anchors: Participatory Economics at 1.0 (moved to 0.5 by part (b7)), Nordic Social Democracy at 0.5
(holds) and Stakeholder Capitalism at 0.0 (holds). After this group no corpus unit is at 1.0 on C4.2; stage 3's
restatement of the criterion's anchors drops the 1.0 band's example, as C1.1's, C1.2a's and C3.1's were dropped.

## 7. Corrections found (not polish)

No score is corrected: every published score holds, and the group changes no total, rank, failure count or tier.
Two findings for the criterion's wording:

1. **The Red List Index and the requirement.** Nordic Social Democracy is the first unit in the pass to clear a
   C4.2 clause, and the clause it clears (the Red List Index, domestic species) is the one that cannot show the
   consumption-based pressure the requirement names (reading 3.4). Report v2.0 and the criteria record's next amendment
   may state that clause 2 is measured on the economy's own species while the requirement is measured on consumption.
2. **The index's two-decimal resolution** makes "non-declining" a statement about changes of 0.01 or more (reading 3.1).

## 8. Disclosure

CCO-PTF-CIP-SZH is the owner's design. Its C4.2 unit was read in part (b7) and is not re-read; this group changes none of
its scores. First place stays shared at 14.5 by CCO-PTF-CIP-SZH and Integral; Integral's C4.2 unit was read in part (b7).
Every reading here was made before the consequences table was computed. The session ran on Sonnet 5.5, not on the Opus
5.5 at high that `STATE.md`'s routing assigns judgment groups; the owner may wish to have the readings that carry
judgment (the 0.0 and 0.5 method of reading 3.2, Market Socialism's and Sovereign Wealth Fund Statism's flags, and the
holds of the 0.0s) read again in an Opus session.

## 9. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`): C1.1 Poverty Elimination Capacity,
  class I (14 units in play), which needs its evidence cache first, in a Sonnet 5.5 session at medium; then C4.1, C2.1,
  C2.4, C2.3, C4.4, C4.5, C2.5 and C3.4.
- **`evidence_cache_s62.py`'s check [2]** compares the units in play *now* with its index, so it reports a failure once
  a group is part of the pass; its digest checks still pass. It is not a harness check and is not edited here.
- **For the criteria record's next amendment:** decision 64.1 (the windows for clause 1; the index's resolution).
- **For Report v2.0:** section 7's finding.
- **Sources a later session could add:** the Footprint Data Foundation's national accounts (footprint per person and
  biocapacity per person) for the four economies and the Nordic countries; the national boundary accounts of Fanning et
  al. (2022); the Global Carbon Budget's own file in place of Our World in Data's rows.

## 10. What this record does not show

Clause 1 is read from a republisher's rows of the Global Carbon Budget for 2023 as the latest year, and the window is a
choice (3.1), not v2.0's. The Red List Index is a domestic-species index at two decimals. Clauses 3 and 4 are shown
for no unit (3.8). "Not shown" means that no estimate was located, not that the clause fails. The interpretation check
(decisions 50.1 to 50.4) was not run; it is optional. The record is one scorer's re-estimation; whether its calls
reproduce is what the replication programme tests.
