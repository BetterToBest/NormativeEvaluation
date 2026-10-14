# NEEC Rescoring Pass — Record, Stage 2, Group 2.2: C1.2a Wealth Building for Resilience (class M)

**Session 53 · 2026-10-14 · Scorer and engineer: Claude · Owner: Duke Johnson**
**Status: scratch (protocol 10.1). Parts (a) and (b) and group 2.1 are `NEEC_Rescoring_s37.md` to
`NEEC_Rescoring_s51.md`; this record edits none of them.** No corpus file, score or scoring document changes until the
pass ends. Its changes are then applied by generator with pinned inputs and restated in place (protocol 10.2, 10.3;
decisions D12, D14), and until then the published totals stand, provisional as `README.md` says. Decisions taken here
are Claude's under the owner's delegation (Handoff 35, section 2); each is recorded with its reasons, and the owner may
reverse any of them.
**Reproduce:** `python3 rescoring_s53.py` (harness check 102). It is the first group written on the shared module
(`pass_common.py`, decision 52.5): the script holds the 23 readings and the group's own checks, and the module computes
the consequences cumulatively with every part before it. It recomputes every 2019-dollar figure below from the series
it holds, checks the simulation runs' captured output by digest and every figure quoted from it, and checks that this
record contains its generated tables verbatim. The runs themselves: `node cco_c12a_checks_s53.js path/to/harness.js
path/to/index.html` on a clone of `BetterToBest/compassionism-simulation` at `5a7a7b1`; the harness does not rerun the
JavaScript, as with Sessions 38, 40 and 51.

---

## 1. What this group is

The consequence triage (`triage_s52.py`, decision 52.7) put C1.2a first among the criteria still to read: 23 units, six
of them able to change an adequacy tier on their own, the most of any criterion. C1.2a is class M: v2.0 restated its
bar (codes K6, R2; `NEEC_Criteria_v2_s45.md`, section 4). The Pass Threshold keeps its figure, $60,000 over 20 years for
70%+ of participants, and now states its price basis: constant 2019 US dollars at purchasing-power parity, deflated by
the national consumer price index and converted at the World Bank's 2019 PPP factor for private consumption. The
Requirement's $70,000 becomes $60,000, so the two agree, and the Cultural/Geographic Adaptation field is removed (its
middle-income bar of 150–200% of a year's household expenses is gone). For class M every unit is re-checked clause by
clause against Appendix V in the D28 form (section 7 of the criteria record): the four published 1.0s, the nine 0.5s
and the ten 0.0s.

**Outcome.** No entry clears C1.2a on v2.0's text. **Five units fall:** Nordic Social Democracy, Market Socialism,
CCO-PTF-CIP-SZH and Singapore from 1.0 to 0.5, and MMT + Job Guarantee from 0.5 to 0.0 (a correction). **One rises:**
Libertarian Minarchism, from 0.0 to 0.5 (a correction). Seventeen hold. Net −2.0 points; MMT gains a failure and
Libertarian Minarchism loses one; **no tier changes.** CCO-PTF-CIP-SZH keeps first place, 15.5 to 15.0; Participatory
Economics and Integral share second at 14.5. The finding that moves most units is the reading of the clause itself
(reading 3.1): the threshold asks that 70% of participants reach the figure, not that the median participant does,
and no national survey, and no source of any design, shows that. The design's own model shows it, on a saving rule
(reading 3.4).

## 2. How a clause is recorded, and the rule

As in part (a), section 2: the clause is cleared, short, not shown, out of reach or moot. A published 1.0 stands only
if the clause is cleared (D28, protocol 2.3); otherwise it becomes 0.5, and a clause-level gap never makes 0.0 (D28(f)).
C1.2a has one clause, so the R4 audit's A codes do not arise.

**Decision 53.2 (the form for units below 1.0).** Until now the pass re-estimated only published 1.0s, so its rule could
say "never 0.0". A class M re-read also re-reads 0.5s and 0.0s, which may rise or fall. *Decision:* such a unit is 1.0
if the clause is cleared; 0.0 only where one of protocol 2.1's whole-criterion conditions holds (no structural
mechanism addresses the criterion; the system excludes the concern; or the best evidence is far below the bar with no
credible pathway under the system's own logic), stated in the record as the unit's reason and never with the clause
cleared; and 0.5 otherwise. `pass_common.py` checks exactly this (`check_rule`); for any group with no 0.0 it prints
the rule as before, and its self-test still rebuilds group 2.1's tables verbatim. *Alternatives:* leave units below
1.0 untouched (rejected: class M asks that every unit be re-checked, section 7 of the criteria record); or let a short
clause make 0.0 (rejected: D28(f)). The dominance line now counts rises and 0.0s; for the earlier parts, all of whose
units were published 1.0s, it prints what it printed.

## 3. Decisions and readings (under the delegation)

**3.1 What the clause asks (decision 53.1).** "≥$60,000 median net-wealth accumulation over 20 years for 70%+ of
participants" joins a median to a share, and the corpus read it two ways. Status Quo's published 0.5 read it as a share:
"reaching well under the 70%-of-participants threshold at the $60,000+/20-year scale". Nordic Social Democracy's,
Market Socialism's and Singapore's 1.0s read it as the median of those who use the vehicles, leaving breadth to C1.5.
*Decision:* at least 70% of participants each accumulate $60,000 or more over 20 years; the median is reported beside
it. Reasons: (i) the protocol, not the scorer, says who the participants are (3.2): everyone who lives and works in a
configured economy, the economy-wide population for a mechanism, the population its sources serve for a comprehensive
system; (ii) the Paper calibrated the figure so that the United States does not meet it: "Median U.S. household wealth
is $121,700 (2019), but bottom 50% hold only ~$3,200. The $70,000 threshold represents substantial improvement for
lower-wealth households" (Paper v1.4, C1.2, Threshold Justification), which only the share reading preserves; (iii)
the 1.0 band says "reaching most participants". *Alternative, flagged:* the engaged-participants reading (the
Requirement's "for participants who engage with whatever wealth-building mechanism the system provides"; breadth to
C1.5). On it Status Quo, Nordic Social Democracy, Singapore and Qatar would be 1.0; each carries the flag. It would make
the bar one the United States meets, against the Paper's own calibration.

**3.2 Where 20 years' accumulation is not reported.** National surveys report the stock of net worth, not 20 years'
change in it. A stock is a lifetime's accumulation plus inheritance, so it overstates 20 years' accumulation: a share of
participants holding the figure is an upper bound on the share accumulating it. Where the upper bound is short, the
clause is short; where it clears, the clause is not thereby shown. Mid-career households (head aged 45 to 54) are
reported beside all households, as the nearest to 20 years of accumulation.

**3.3 The price basis.** Every figure is converted as v2.0's measurement field states: local currency (or US dollars at
the market rate, converted back to local currency at that year's official rate) deflated to 2019 by the national CPI,
then divided by the World Bank's 2019 PPP conversion factor for private consumption (WDI series PA.NUS.PRVT.PP,
FP.CPI.TOTL, PA.NUS.FCRF, retrieved 2026-10-14). The United States is the numeraire. US CPI-U for 2025 is the mean of
its eleven published months (October 2025 was not collected). Qatar's 2025 CPI is not yet published, so its 2024 index
is used. The figures, recomputed by the script: the bar is $75,557 in 2025 dollars and $71,510 in 2023 dollars; Norway's
bar is NOK 734,447 in 2024 prices.

**3.4 CCO-PTF-CIP-SZH on its published model (reading 3.10 of group 2.1).** The design's published 1.0 rests on the
papers' "$70,000+ over 20 years". The model at the pin frozen for v2.0 (`5a7a7b1`, v4.20; decision 52.9) computes the
quantity, so the model governs (group 2.1, reading 3.2). The runs (section 5) measure each agent's net worth at year 20
less its net worth at adoption, in 2019 dollars (the engine's dollars are 2023's, from BLS CES and CPS 2023; the
reference run holds prices constant). In the reference run 76.6% of agents accumulate the figure, every seed at 70% or
more, against 41.4% in the matched Baseline: the design's mechanisms add 35 points. But the engine adds each year's wage
income less the basket's cost to wealth (`a.wealth+=annualWageUSD-costUSD` in `runYear()`), so an agent saves every
dollar above its basket, and agents keep 47.2% of 20 years' cash income as net worth. The US personal saving rate was
3.4% to 5.6% in 2022–2025 (BEA; FRED series PSAVERT). Acre equity, the design's own vehicle, adds under one point to
the share. Protocol 2.1 puts at 0.5 a performance that "holds only under favourable or untested conditions"; a figure
that rests on households saving about half their income is such a performance. The engine's documentation at the pin
states that the papers' $82,000 median wealth is not produced by the engine (CONTRIBUTING.md, NEEC note 1), so the
rationale's figure has no published model behind it. *Decision:* the clause is not shown and the unit is 0.5, flagged
toward 1.0, since the engine's own figure clears in every seed. *Alternative:* credit the engine's figure as the design's
projection (1.0). Rejected because the clearance belongs to the saving rule rather than to a vehicle of the design's.
The Adverse Environment, which C1.2a does not require, gives 46.6%. For version 2.1: a version of the model with a
sourced consumption rule that still shows 70% at the figure would clear the clause (section 8).

**3.5 The configured national economies.** *Status Quo* (United States): in the 2025 Survey of Consumer Finances 66.3%
of families hold $60,000 (2019) or more, and 71.6% of those whose head is 45 to 54, before subtracting what they held at
the start: short, and 0.5 as before; the rationale's bottom-half figure is replaced by the survey the measure names.
*Nordic Social Democracy:* no figure in the published rationale. Statistics Norway's register data for 2024 put the
30th percentile of household net wealth at NOK 390,300 ($31,885 at 2019 PPP) and the 40th at NOK 1,131,000, so between
60% and 70% of households hold the figure, and 15.8% hold negative net wealth. The register excludes pension wealth:
that is the largest caveat, since Nordic retirement saving is largely collective. Sweden publishes no household wealth
statistics. Short on the one Nordic register that publishes the distribution: 0.5. *Singapore:* UBS's median of
$96,434 at end-2025 is $100,395 at 2019 PPP, above the bar; but the scoring document's own estimate is that about 75%
of the population has a genuine vehicle, Work Permit holders (about a fifth of the population) having none, and no
published distribution shows 70% of everyone who lives and works there at the figure: not shown, 0.5. *Qatar:* short,
0.5, as published; the UBS median ($116,897 at 2019 PPP) remains unreconciled with a population most of whose members
are migrant workers. *China:* UBS's median of $27,273 at end-2022 is $43,071 at 2019 PPP, below the bar; v2.0 removed
the middle-income adjustment on which the published rationale judged the magnitude likely to clear, so its flag toward
1.0 is removed; 0.5 as published. *Centrally Planned Socialism:* 0.0, as published; its savings deposits did not survive
1992.

**3.6 Two corrections (decision 53.3).** The re-read applies one reading to every entry of the same kind
(protocol 2.3(e)), and two published scores do not:
- **Libertarian Minarchism, 0.0 → 0.5.** Its own markets are its accumulation vehicles, the ones Status Quo's,
  Stakeholder Capitalism's and China's units credit at 0.5. The published 0.0 rested on reach ("those born poor cannot
  accumulate initial capital"), which is the 0.5 band's partial coverage, not 2.1's absence of a mechanism. Flagged
  toward 0.0.
- **MMT + Job Guarantee, 0.5 → 0.0.** A mechanism since decision D17. Its published 0.5 credited "traditional markets",
  the host economy's vehicles, which the reach rule (protocol 3.2, D28(c)) does not credit to a mechanism; the Job
  Guarantee itself pays a wage and holds no asset. Income without an accumulation vehicle is the 0.0 band's own
  description ("income or consumption only", Appendix H.7v2), as for Universal Basic Income and Georgism's dividend.
  Flagged toward 0.5.

*Alternative:* hold both as published. Rejected: a re-check clause by clause that leaves two units inconsistent with the
reading applied to their peers is not a re-check. Each changes a failure count by one; neither changes a tier.

**3.7 The other units.** Market Socialism's 1.0 rests on qualitative evidence ("members accumulate substantial wealth"),
which does not show the share: 0.5, not shown. Degrowth's and Participatory Economics' collectively held vehicles,
Sovereign Wealth Fund Statism's collective corpus, Stakeholder Capitalism's market vehicles and Islamic finance's
profit-sharing accounts stay 0.5; Islamic finance's flag toward 1.0 is removed, because reach alone does not show the
figure and the figure the host economy produces is not the mechanism's. Universal Basic Income, Integral (the band's
anchors), Fully Automated Luxury Communism, Georgism, Mutual Credit/LETS, Doughnut Economics, Universal Basic Services
and Ostrom-style commons stay 0.0, each on its stated reason; Doughnut Economics' and Ostrom's flags toward 0.5 and
Sovereign Wealth Fund Statism's toward 0.0 stand.

## 4. The units

### 4.1 Summary (generated)

| Entry | Published | Clause | Verdict | Flag |
|---|---:|---|---:|---|
| SQ | 0.5 | short | 0.5 | toward 1.0 on the engaged-participants reading (reading 3.1): the median accumulation of those who use the economy's accumulation vehicles, with breadth left to C1.5 |
| NSD | 1.0 | short | 0.5 | toward 1.0 on the engaged-participants reading (reading 3.1): the median accumulation of those who use the economy's accumulation vehicles, with breadth left to C1.5 |
| CPS | 0.0 | short | 0.0 |  |
| MS | 1.0 | not shown | 0.5 |  |
| LM | 0.0 | not shown | 0.5 | toward 0.0, the published reading |
| MMT | 0.5 | out of reach | 0.0 | toward 0.5, the published reading |
| UBI | 0.0 | out of reach | 0.0 |  |
| DG | 0.5 | not shown | 0.5 |  |
| SC | 0.5 | short | 0.5 |  |
| FALC | 0.0 | short | 0.0 |  |
| PE | 0.5 | not shown | 0.5 |  |
| CCO | 1.0 | not shown | 0.5 | toward 1.0: the engine's own figure clears the bar in every seed |
| INT | 0.0 | short | 0.0 |  |
| GEO | 0.0 | out of reach | 0.0 |  |
| MC | 0.0 | short | 0.0 |  |
| DE | 0.0 | short | 0.0 |  |
| UBS | 0.0 | out of reach | 0.0 |  |
| SWF | 0.5 | short | 0.5 |  |
| CN | 0.5 | short | 0.5 |  |
| SG | 1.0 | not shown | 0.5 | toward 1.0 on the engaged-participants reading (reading 3.1): the median accumulation of those who use the economy's accumulation vehicles, with breadth left to C1.5 |
| QA | 0.5 | short | 0.5 | toward 1.0 on the engaged-participants reading (reading 3.1): the median accumulation of those who use the economy's accumulation vehicles, with breadth left to C1.5 |
| IF | 0.5 | not shown | 0.5 |  |
| OS | 0.0 | short | 0.0 |  |

### 4.2 Clause by clause (generated)

#### SQ C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | on v2.0's price basis the bar is $75,557 in 2025 dollars; in the 2025 Survey of Consumer Finances 66.3% of US families hold net worth at or above it, a lifetime stock that overstates 20 years' accumulation, so fewer than 70% reach the figure; the 30th percentile is $43,835 and the median $171,606 (2019 dollars); among families whose head is 45 to 54, about 20 to 30 years into working life, 71.6% hold the bar's figure, before subtracting what they held at the start (reading 3.5); homeownership and retirement accounts are genuine vehicles, so the unit is 0.5, not 0.0 | Federal Reserve Board, 2025 Survey of Consumer Finances, summary extract SCFP2025.csv in scfp2025excel.zip (md5 c938318c), 2025 dollars, weighted, all five implicates; BLS CPI-U, US city average (CUUR0000SA0; FRED CPIAUCNS), annual averages 2019 and 2023, 2025 the mean of its eleven published months; Report v1.6, System 1, C1.2a |

*Note:* the published rationale's bottom-half figure (~$3,200, from the Paper's calibration of 2019) is replaced by the 2025 survey's distribution, which v2.0's measure names; the verdict is unchanged.

#### NSD C1.2a Wealth Building for Resilience: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | no figure in the published rationale, which credited the vehicles for those who use them and left breadth to C1.5; on Norway's register data for 2024 the bar is NOK 734,447, and the 30th percentile of household net wealth is NOK 390,300 ($31,885 in 2019 dollars at PPP) while the 40th is NOK 1,131,000 ($92,396): between 60% and 70% of households hold the bar's figure, and 15.8% hold negative net wealth; the register excludes pension wealth, so collective and public pension entitlements are not counted (reading 3.5) | Statistics Norway, Income and wealth statistics for households 2024, Table 4 (StatBank 10318, deciles of net wealth) and Table 3 (10315); students excluded, pension wealth not included; World Bank WDI, PPP conversion factor for private consumption 2019 (PA.NUS.PRVT.PP), CPI (FP.CPI.TOTL) and official exchange rate (PA.NUS.FCRF), retrieved 2026-10-14; Report v1.6, System 2, C1.2a |

*Note:* published 1.0 read in the D28 form: the clause is short on the one Nordic register that publishes the distribution, so the unit falls to 0.5; Sweden publishes no household wealth statistics, and no Nordic source located shows 70% of households at the figure.

#### CPS C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | no accumulation vehicle beyond minimal personal property; the savings-bank deposits households did hold were frozen and then erased by the price liberalisation of 1992, so the historical record shows no buffer that survived; far below the bar for any share of participants | Report v1.6, System 3, C1.2a; NEEC_Step1c_Retrofit_C1_2ab_C1_5.md, System 3 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion, and the historical record, collapse included (protocol 4.1), shows no credible pathway under the system's own logic.

#### MS C1.2a Wealth Building for Resilience: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | the rationale's evidence is qualitative: Mondragón members 'accumulate substantial wealth through capital accounts and profit distribution'; no source the unit cites states an accumulation figure, or the share of participants whose capital accounts and other net worth reach $60,000 (2019 dollars) over 20 years; a genuine, individually held vehicle, not shown at the bar for 70% of participants | Report v1.6, System 4, C1.2a; Paper v1.4, Appendix H.8a |

*Note:* published 1.0 read in the D28 form (silence is not clearance, protocol 2.3(b)): the unit falls to 0.5; it is the 1.0 band's anchor example, which the anchors line reports.

#### LM C1.2a Wealth Building for Resilience: 0.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | the system's own markets are its accumulation vehicles (property, ownership of enterprises, private saving), the same vehicles Status Quo Market Capitalism's unit credits at 0.5; the published 0.0 rested on their reach ('those born poor cannot accumulate initial capital'), which is the 0.5 band's partial coverage, not the absence of a mechanism; no source shows 70% of participants at the bar | Report v1.6, System 5, C1.2a; NEEC_Step1c_Retrofit_C1_2ab_C1_5.md, System 5 |

*Note:* a correction (reading 3.6): a reach shortfall is a 0.5 under protocol 2.1, as for Status Quo, Stakeholder Capitalism and China; one failure fewer, no tier change.

#### MMT C1.2a Wealth Building for Resilience: 0.5 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | out of reach | the Job Guarantee pays a wage and benefits; it holds no asset for its participants; the published 0.5 credited 'traditional markets', the host economy's vehicles, which the reach rule does not credit to a mechanism (protocol 3.2, D28(c)); generalised over the economy, the mechanism governs income, not accumulation | Report v1.6, System 6, C1.2a; NEEC_Step1c_Retrofit_C1_2ab_C1_5.md, System 6; SCORING_PROTOCOL.md 3.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: income only, the 0.0 band's own description (Appendix H.7v2).

*Note:* a correction (reading 3.6): income without an accumulation vehicle is the 0.0 band, as for Universal Basic Income and Georgism's dividend; one failure more, no tier change.

#### UBI C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | out of reach | an income transfer; no accumulation vehicle; the 0.0 band's own anchor case | Report v1.6, System 7, C1.2a; Paper v1.4, Appendix H.7v2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: income only (the band's anchor).

#### DG C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | community land trusts and cooperatives give real, collectively held security; individual accumulation is discouraged by design, and no source states a household figure; the 0.5 band's anchor case | Report v1.6, System 8, C1.2a; Paper v1.4, Appendix H.7v2 |

#### SC C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | the vehicles are Status Quo's (homeownership, retirement accounts) with incremental stock options and profit-sharing; on the 2025 Survey of Consumer Finances 66.3% of families hold the bar's figure, short of 70%, and no source shows the reform raising it | Report v1.6, System 9, C1.2a; Federal Reserve Board, 2025 Survey of Consumer Finances, summary extract SCFP2025.csv in scfp2025excel.zip (md5 c938318c), 2025 dollars, weighted, all five implicates |

#### FALC C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | no vehicle of any kind, individual or collective, is specified; 'abundance makes accumulation less relevant' describes consumption access, not a buffer | Report v1.6, System 10, C1.2a; NEEC_Step1c_Retrofit_C1_2ab_C1_5.md, System 10 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion.

#### PE C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | no private accumulation; named community investment councils can build collective wealth; no figure or household buffer is stated; the 0.5 band's collectively held case | Report v1.6, System 11, C1.2a; NEEC_Step1c_Retrofit_C1_2ab_C1_5.md, System 11 |

#### CCO C1.2a Wealth Building for Resilience: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | on the design's published model at v4.20 (500 seeds, the reference settings, prices constant), 76.6% of agents accumulate $60,000 or more in 2019 dollars over 20 years (77.4% with acre equity), 500 of 500 seeds at 70% or more, median $382,005, against 41.4% in the matched Baseline; but the engine adds wage income less the basket's cost to wealth, so an agent saves every dollar above its basket, and agents keep 47.2% of 20 years' cash income as net worth, more than five times the US personal saving rate of 3.4% to 5.6% (2022-2025); acre equity adds little; in the Adverse Environment 46.6% reach the figure; the rationale's $70,000+ is the papers', and the engine's documentation states that the papers' wealth figure is not produced by the engine (reading 3.4) | Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); cco_c12a_checks_s53_output.txt; the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), NEEC note 1; Report v1.6, System 12, C1.2a |

*Note:* published 1.0 read in the D28 form: the projection holds only under the engine's saving rule, a favourable and untested condition (protocol 2.1, 0.5), so the clause is not shown; for version 2.1, a version of the model with a sourced consumption rule that still shows 70% at the bar would clear it.

#### INT C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | Integral Time Credits cannot be saved or accumulated by design; no other vehicle; the 0.0 band's anchor case | Report v1.6, System 13, C1.2a; Paper v1.4, Appendix E |

*0.0 (protocol 2.1):* the system excludes accumulation by design (the band's anchor).

#### GEO C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | out of reach | the citizen's dividend is an annual pass-through of land rent, income rather than a held corpus; lower taxes on income and capital raise saving capacity in the host economy, which the reach rule does not credit | NEEC_Georgism_LVT_scoring_scratch.md, C1.2a; SCORING_PROTOCOL.md 3.2 |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: the mechanism's payment is income only.

#### MC C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | credit balances are claims on other members in a non-convertible unit, capped and in some designs subject to demurrage; no store of value usable as a buffer, for any participant | NEEC_MutualCredit_LETS_scoring_scratch.md, C1.2a |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: the instrument has no accumulation function by design.

#### DE C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | the framework names the categories of wealth and cites others' vehicles as compatible, but adopts none as its own; no implementation reviewed established an accumulation vehicle | NEEC_DoughnutEconomics_scoring_scratch.md, C1.2a |

*0.0 (protocol 2.1):* no structural mechanism of the system's own addresses the criterion (the published flag toward 0.5 stands).

#### UBS C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | out of reach | in-kind services, among them zero-rent social housing, reduce expenses but create no asset, deed or account | NEEC_UniversalBasicServices_scoring_scratch.md, C1.2a |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: services, not assets.

#### SWF C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | a large, growing, professionally invested corpus held collectively; no individual holds a titled or severable claim, so no household's net worth includes it; the 0.5 band's collectively held case | NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.2a |

*Note:* the published flag toward 0.0 stands.

#### CN C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | UBS's median wealth per adult, $27,273 at end-2022, is $43,071 in 2019 dollars at PPP, under the bar, so fewer than half of adults hold the figure; v2.0 removes the middle-income adjustment on which the published rationale judged the magnitude likely to clear; homeownership near 90% is a genuine, individually titled vehicle, impaired by falling prices and restricted rural land rights | NEEC_StateCapitalism_China_scoring_scratch.md, C1.2a; World Bank WDI, PPP conversion factor for private consumption 2019 (PA.NUS.PRVT.PP), CPI (FP.CPI.TOTL) and official exchange rate (PA.NUS.FCRF), retrieved 2026-10-14 |

*Note:* the published flag toward 1.0, a magnitude-first reading of the adjusted bar, is removed: the adjustment no longer exists and the median is below the bar.

#### SG C1.2a Wealth Building for Resilience: 1.0 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | UBS's median wealth per adult, $96,434 at end-2025, is $100,395 in 2019 dollars at PPP, above the bar; but the clause asks for 70% of participants, and the scoring document estimates that about 75% of the population has a genuine vehicle, Work Permit holders (about a fifth) having none; no published distribution shows 70% of all who live and work in the economy at the figure, and 20-year accumulation, lease decay aside, is not reported | NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.2a; World Bank WDI, PPP conversion factor for private consumption 2019 (PA.NUS.PRVT.PP), CPI (FP.CPI.TOTL) and official exchange rate (PA.NUS.FCRF), retrieved 2026-10-14 |

*Note:* published 1.0 read in the D28 form: the median alone does not show the 70% clause, so the unit falls to 0.5.

#### QA C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | for citizens a generous vehicle (free plots, near-interest-free housing loans, a pension); UBS's median wealth per adult, $95,499, is $116,897 in 2019 dollars at PPP, a figure the scoring document could not reconcile with the wage structure; citizens are 9% to 13% of residents, migrant workers have no pension and restricted ownership, and well under half of residents have a vehicle reaching the figure | NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.2a; World Bank WDI, PPP conversion factor for private consumption 2019 (PA.NUS.PRVT.PP), CPI (FP.CPI.TOTL) and official exchange rate (PA.NUS.FCRF), retrieved 2026-10-14 |

#### IF C1.2a Wealth Building for Resilience: 0.5 → 0.5

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | not shown | profit-sharing investment accounts are a genuine, individually held, accumulating vehicle; returns are smoothed to market benchmarks, so accumulation is indistinguishable from bank saving in the host economy, which the reach rule does not credit; nothing shows 70% of participants at the bar through the mechanism | NEEC_IslamicFinance_scoring_scratch.md, C1.2a; SCORING_PROTOCOL.md 3.2 |

*Note:* the published flag toward 1.0 (PSIAs treated as reaching most participants) is removed: reach alone does not show the bar's figure, and the figure the host economy produces is not the mechanism's.

#### OS C1.2a Wealth Building for Resilience: 0.0 → 0.0

| # | Clause (v2.0) | Status | Estimate | Source |
|---:|---|---|---|---|
| 1 | ≥$60,000 median net-wealth accumulation over 20 years for 70%+ of participants, in constant 2019 US dollars at purchasing-power parity | short | a member's claim on the commons is a use-right, non-severable and extinguished on exit; no individual balance grows; no case reports household accumulation of the bar's order | NEEC_Ostrom_Commons_scoring_scratch.md, C1.2a |

*0.0 (protocol 2.1):* no structural mechanism addresses the criterion: use-rights, not assets (the published flag toward 0.5 stands).

## 5. The simulation runs (from `cco_c12a_checks_s53_output.txt`)

`node cco_c12a_checks_s53.js` on `harness.js` (md5 `fe6fa4a3`) and `index.html` (md5 `c333b632`) at `5a7a7b1`; 500
seeds, 500 agents, 20 years. The runner reproduces `runScenario()`'s year-20 median wealth and wealth poverty on every
seed of the four scenarios before any figure is read. Accumulation is year-20 net worth less net worth at adoption,
deflated by the headline inflation rate where there is one, in 2019 dollars.

| Scenario | Net worth read as | Share accumulating >=$60,000 | Seeds at 70% or more | Median accumulation | 30th percentile | Saving share of cash income |
|---|---|---:|---:|---:|---:|---:|
| Reference (Full Integration), 0% | wealth (the engine's figure) | 76.6% | 500 of 500 | $382,005 | $141,971 | 47.2% |
| Reference (Full Integration), 0% | wealth + acre equity | 77.4% | 500 of 500 | $394,581 | $151,839 |  |
| Baseline, matched (0%) | wealth (the engine's figure) | 41.4% | 0 of 500 | -$11,325 | -$30,577 | 20.0% |
| Baseline, matched (0%) | wealth + acre equity | 41.4% | 0 of 500 | -$11,325 | -$30,577 |  |
| Adverse Environment, 2% | wealth (the engine's figure) | 46.6% | 0 of 500 | $35,418 | -$21,788 | 29.2% |
| Adverse Environment, 2% | wealth + acre equity | 47.9% | 0 of 500 | $46,211 | -$19,393 |  |
| Baseline, matched to Adverse (2%) | wealth (the engine's figure) | 13.6% | 0 of 500 | -$27,030 | -$50,336 | 2.3% |
| Baseline, matched to Adverse (2%) | wealth + acre equity | 13.6% | 0 of 500 | -$27,030 | -$50,336 |  |

## 6. What parts (a), (b) and groups 2.1 and 2.2 change (generated)

| Entry | Published (rank) | After group 2.1 (rank) | After group 2.2 (rank) | Change here | Failures | Tier |
|---|---:|---:|---:|---:|---:|---|
| CCO | 24.5 (1) | 15.5 (1) | 15.0 (1) | -0.5 | 0 | Potentially Adequate |
| PE | 20.5 (2) | 14.5 (2) | 14.5 (2) | 0.0 | 1 | Potentially Adequate |
| NSD | 19.5 (3) | 13.5 (4) | 13.0 (5) | -0.5 | 2 | Potentially Adequate |
| INT | 19.5 (3) | 14.5 (2) | 14.5 (2) | 0.0 | 3 | Partially Adequate |
| DG | 19.0 (5) | 13.5 (4) | 13.5 (4) | 0.0 | 2 | Potentially Adequate |
| MS | 16.5 (6) | 13.5 (4) | 13.0 (5) | -0.5 | 2 | Potentially Adequate |
| MMT | 15.5 (7) | 11.5 (13) | 11.0 (14) | -0.5 | 4 | Partially Adequate |
| UBI | 14.5 (8) | 11.0 (15) | 11.0 (14) | 0.0 | 7 | Structurally Inadequate |
| MC | 14.5 (8) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| OS | 14.5 (8) | 13.0 (7) | 13.0 (5) | 0.0 | 3 | Partially Adequate |
| SWF | 14.0 (11) | 12.5 (8) | 12.5 (8) | 0.0 | 3 | Partially Adequate |
| SG | 14.0 (11) | 12.0 (11) | 11.5 (12) | -0.5 | 4 | Partially Adequate |
| GEO | 13.5 (13) | 12.5 (8) | 12.5 (8) | 0.0 | 2 | Potentially Adequate |
| UBS | 13.5 (13) | 12.0 (11) | 12.0 (11) | 0.0 | 3 | Partially Adequate |
| IF | 13.5 (13) | 11.5 (13) | 11.5 (12) | 0.0 | 5 | Partially Adequate |
| FALC | 13.0 (16) | 9.5 (16) | 9.5 (16) | 0.0 | 10 | Structurally Inadequate |
| DE | 11.5 (17) | 9.0 (19) | 9.0 (19) | 0.0 | 8 | Structurally Inadequate |
| SQ | 10.5 (18) | 9.5 (16) | 9.5 (16) | 0.0 | 9 | Structurally Inadequate |
| CPS | 10.0 (19) | 7.5 (22) | 7.5 (22) | 0.0 | 12 | Structurally Inadequate |
| SC | 10.0 (19) | 8.5 (20) | 8.5 (20) | 0.0 | 9 | Structurally Inadequate |
| CN | 10.0 (19) | 9.5 (16) | 9.5 (16) | 0.0 | 8 | Structurally Inadequate |
| QA | 9.0 (22) | 8.0 (21) | 8.0 (21) | 0.0 | 10 | Structurally Inadequate |
| LM | 8.0 (23) | 6.0 (23) | 6.5 (23) | 0.5 | 14 | Structurally Inadequate |

After this group the corpus has 20 dominance pairs against 21 after group 2.1 (new: none; lost: MMT>SC), and its frontier holds 14 entries against 14 (SQ, NSD, MS, LM, UBI, DG, FALC, PE, CCO, INT, MC, SWF, IF, OS). First place: CCO, 15.5 after group 2.1, 15.0 now, ahead of PE, INT at 14.5. Across the pass so far 175 units have been re-estimated, each counted once: 16 are at 1.0, 149 at 0.5 and 10 at 0.0; against their published scores 141 fell, 1 rose and 33 are unchanged (net -70.0 points).

The score ledger, part by part:

| Entry | Published | (a) | (b1) | (b2) | (b3) | (b4) | (b5) | (b6) | (b7) | 48.3 | (b8) | (b9) | (2.1) | (2.2) | Now | Re-estimated | At 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCO | 24.5 | -0.5 | -1.5 | -0.5 | -0.5 | -0.5 | -0.5 | -1.0 | -0.5 | -0.5 | -0.5 | -1.0 | -1.5 | -0.5 | 15.0 | 21 | 19 |
| PE | 20.5 |  | -1.5 | -0.5 | -0.5 | -1.5 |  | -0.5 | -0.5 |  | -0.5 | -0.5 |  |  | 14.5 | 14 | 13 |
| NSD | 19.5 | -2.5 | -1.0 | -0.5 | -0.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  | -0.5 | 13.0 | 14 | 13 |
| INT | 19.5 | -0.5 | -1.0 | -0.5 |  | -1.0 | -0.5 | -1.0 | -0.5 |  |  |  |  |  | 14.5 | 13 | 10 |
| DG | 19.0 |  | -1.5 | -0.5 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -1.0 |  |  |  | 13.5 | 12 | 12 |
| MS | 16.5 | -1.0 | -1.5 | -0.5 | -0.5 |  |  |  | 0.5 |  |  |  |  | -0.5 | 13.0 | 9 | 7 |
| MMT | 15.5 | -1.5 | -1.0 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  | -0.5 | 11.0 | 9 | 8 |
| UBI | 14.5 | -1.5 | -0.5 | -0.5 | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 11.0 | 9 | 7 |
| MC | 14.5 |  | -1.0 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  | 12.5 | 6 | 4 |
| OS | 14.5 | -0.5 |  |  |  |  | -0.5 | -0.5 |  |  |  |  |  |  | 13.0 | 5 | 3 |
| SWF | 14.0 |  |  | -0.5 |  |  | -0.5 | -0.5 |  |  |  |  |  |  | 12.5 | 5 | 4 |
| SG | 14.0 | -1.0 | -0.5 | -0.5 |  |  |  |  |  |  |  |  |  | -0.5 | 11.5 | 5 | 5 |
| GEO | 13.5 | -0.5 |  |  |  |  | -0.5 |  |  |  |  |  |  |  | 12.5 | 3 | 2 |
| UBS | 13.5 |  | -0.5 | -0.5 |  |  | -0.5 |  |  |  |  |  |  |  | 12.0 | 5 | 3 |
| IF | 13.5 | -1.0 |  |  |  |  | -0.5 |  |  |  |  | -0.5 |  |  | 11.5 | 5 | 5 |
| FALC | 13.0 | -0.5 | -0.5 |  | -0.5 | -1.0 |  | -0.5 | -0.5 |  |  |  |  |  | 9.5 | 9 | 7 |
| DE | 11.5 | -0.5 | -0.5 |  |  |  | -0.5 | -0.5 | -0.5 |  |  |  |  |  | 9.0 | 6 | 5 |
| SQ | 10.5 | -0.5 |  |  |  | -0.5 |  |  |  |  |  |  |  |  | 9.5 | 4 | 3 |
| CPS | 10.0 | -1.5 |  |  | -0.5 |  |  |  |  |  | -0.5 |  |  |  | 7.5 | 6 | 5 |
| SC | 10.0 |  | -1.0 |  |  |  |  |  |  |  |  | -0.5 |  |  | 8.5 | 4 | 4 |
| CN | 10.0 |  |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 9.5 | 2 | 2 |
| QA | 9.0 | -0.5 |  | -0.5 |  |  |  |  |  |  |  |  |  |  | 8.0 | 3 | 3 |
| LM | 8.0 | -1.5 |  |  |  |  |  |  |  |  |  | -0.5 |  | 0.5 | 6.5 | 6 | 5 |

Anchor examples citing a unit the pass moves: C1.1's 1.0 example, NSD (part (b3)); C1.2a's 1.0 example, MS (part (2.2)); C1.2b's 1.0 example, CCO (part (2.1)); C1.4's 1.0 example, CCO (part (2.1)); C2.1's 1.0 example, UBI (part (a)); C2.3's 1.0 example, DG (part (b1)); C2.4's 1.0 example, PE (part (b1)); C2.5's 1.0 example, CCO (part (b5)); C3.1's 1.0 example, UBI (part (b2)); C3.2's 1.0 example, PE (part (b4)); C3.5's 1.0 example, CCO (part (b6)); C4.1's 1.0 example, DG (part (b6)); C4.2's 1.0 example, PE (part (b7)); C4.3's 1.0 example, CCO (part (b8)); C5.1's 1.0 example, MS (part (b2)); C5.2's 1.0 example, CCO (part (b9)); C5.4's 1.0 example, CCO (part (b9)); C5.5's 1.0 example, PE (part (b9)). Bands whose example the pass moves and which no corpus unit then scores at their value: C1.1's 1.0, C1.2a's 1.0, C2.1's 1.0, C2.3's 1.0, C2.4's 1.0, C3.1's 1.0, C3.5's 1.0, C4.1's 1.0, C4.2's 1.0, C4.3's 1.0.

## 7. Corrections found (not polish)

1. **Libertarian Minarchism's and MMT + Job Guarantee's C1.2a** (reading 3.6).
2. **CCO-PTF-CIP-SZH's C1.2a rationale** states the papers' "$70,000+ over 20 years" as the system's figure; the
   design's published model does not produce it, and its documentation says the papers' wealth figure is not the
   engine's (reading 3.4). Report v2.0 gives the model's figure with the saving rule beside it.
3. **Status Quo's C1.2a rationale** gives the bottom half's wealth (~$3,200) as the evidence; Report v2.0 gives the 2025
   Survey of Consumer Finances' share at the figure (66.3%).
4. **Anchor examples.** C1.2a's 1.0 example, Market Socialism, falls to 0.5, and no corpus unit is then at 1.0 on
   C1.2a: the band is left with no corpus example. When the pass is applied, the band keeps its description, drops its
   example and records the change in `source.corrections`, as part (b3)'s reading 3.5 set for C1.1; that no scored
   system clears the criterion is a finding Report v2.0 and Paper v2.0 state.

## 8. Notes for the simulation's maintainers (the owner's project; not NEEC corrections)

- The engine's agents consume their basket and save the rest (47.2% of cash income over 20 years in the reference run).
  Wealth levels, and the share accumulating $60,000, rest on that rule. A sourced consumption rule would let the model's
  wealth figures stand as projections.
- Acre equity is credited in full to `acreEquity` while the liquid share of its appreciation is also added to wealth
  (`PTH_APPR_CONSERVE` false, logged at v4.16); counting both overstates net worth slightly. The runs report wealth
  alone and wealth with acre equity.

## 9. Disclosure

CCO-PTF-CIP-SZH is the owner's design. It falls from 1.0 to 0.5 here on a reading of its own published model, and its
flag records that the engine's figure clears the bar. Three other published 1.0s fall on the same reading of the
clause, so the design keeps first place, at 15.0 on the 26 published criteria, ahead of Participatory Economics and
Integral at 14.5. The reading of the clause (3.1) was chosen before any unit's outcome was computed, from the
protocol's population rule and the Paper's calibration; its alternative is recorded and would raise four entries, the
design not among them, since the design's own figure, under any reading, rests on the saving rule.

## 10. What remains

- **Next group from the triage** (rerun after this group, `triage_s52_output.txt`), and the evidence cache (W5) before
  the first class I group.
- **For the criteria record's next amendment:** decisions 53.1 to 53.3, with 52.11 and 52.12, in one run of the chain.
- **For Report v2.0:** section 7's corrections; the empty 1.0 band of C1.2a.

## 11. What this record does not show

National surveys report wealth held, not 20 years' accumulation (reading 3.2), and only the United States and Norway
publish the distribution the clause needs; for Singapore, Qatar and China the medians are UBS estimates, at market
exchange rates, converted here. Norway's register leaves out pension wealth. "Not shown" means that no evidence was
located, not that the clause fails. The model's figures are the model's: 500 single-adult agents, prices an input, and
a saving rule this record does not alter. The interpretation check (decisions 50.1 to 50.4) was not run; reading 3.1 is
the kind of reading it exists for, and it is optional. The record is one scorer's re-estimation; whether its calls
reproduce is what the replication programme tests.
