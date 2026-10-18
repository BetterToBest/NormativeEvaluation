# C2.3 clause 2: time-use series (cached Session 70)

The measure names the OECD Time Use Database, HETUS (Eurostat's Harmonised European Time Use Surveys) and the
American Time Use Survey (ATUS). This session found:

- `bls.gov` (the ATUS's own host) refused the container (HTTP 403), consistent with STATE.md's existing note that
  the BLS API refuses this container's requests.
- `stats.oecd.org` (the OECD's legacy statistics portal, where the Time Use Database was hosted) returned the
  portal's shell page (HTTP 200, 174 KB) rather than a queryable table; the OECD migrated most datasets to a newer
  SDMX-based Data Explorer during 2024, and this session did not locate the Time Use Database's dataset identifier
  in the new system.
- Eurostat (`ec.europa.eu/eurostat`, which hosts HETUS) is reachable (HTTP 200) but covers only EU member states --
  none of the four configured economies (United States, China, Singapore, Qatar) are EU members, so HETUS cannot
  supply this clause for this unit regardless of access.

No data was cached for this clause. A future session should try the OECD's SDMX REST API directly
(`sdmx.oecd.org/public/rest/data/...`, not attempted this session) for the United States' time-use figures, and
should expect no OECD or HETUS coverage at all for China, Singapore or Qatar -- none of the three publishes to
either database on a comparable basis, so this clause may be "not shown" for three of the four configured economies
on structural grounds, independent of this session's access.
