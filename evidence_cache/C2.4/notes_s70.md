# C2.4 clauses 1 and 3: turnout and trust survey (cached Session 70)

## Clause 1: participation (turnout)

Cached: `idea_voter_turnout_codebook.pdf` (International IDEA, fetched 2026-10-18), which documents the Voter Turnout
Database's methodology (turnout as a share of registered voters, and separately of voting-age population; national
presidential and parliamentary elections since 1945). The database's own country-filtered data view
(idea.int/data-tools/data/voter-turnout) is a client-rendered page; no static export endpoint was found this session
(`/export` paths tried all returned 301 or 404; see session transcript). Search found the United States' 2024
election turnout (64.47% of registered voters, or 59.17% of voting-age population, in two different database views;
which view the criterion's measure intends is not resolved here) but no figures for China, Singapore or Qatar.

China holds no direct national election of this kind (the National People's Congress is chosen by indirect,
tiered election), so clause 1 may need the measurement text's alternative ("where the system takes its binding
decisions otherwise, participation in those processes"); Qatar's Shura Council elections (two-thirds elected since
2021) and Singapore's general elections are both in scope and should be in the IDEA database once a session can
query it directly (through a browser, or by locating the site's data API token as C2.1's note describes for a
similar block).

## Clause 3: responsiveness (external efficacy)

The OECD Survey on Drivers of Trust in Public Institutions is the named source. Search (2026-10-18) found that the
United States has not been among the survey's participating countries in at least its 2024 and 2026 rounds (both
cover only OECD and partner-country respondents who opted in), and oecd.org itself refused this session's container
(HTTP 403, consistent with STATE.md's existing note on the OECD national-accounts page). China, Singapore and Qatar
are not OECD members and were not found as partner-country participants either. If this holds up, clause 3 may be
"not shown" for all four configured economies on the OECD series, and the criterion's "or the equivalent European
Social Survey item" fallback does not reach non-European countries either -- a finding worth session 75's attention,
since it could mean clause 3 is structurally unmeasurable for this unit's entire configured-economy set, not merely
unmeasured so far. This session did not confirm the finding against the OECD's own participant list (the site
refused the fetch); session 75 should verify directly, e.g. by requesting the OECD Trust Survey 2024/2026 country
list through an alternate route (a mirror, or a search of its published country notes, several of which were found
reachable individually even though the index page was not).
