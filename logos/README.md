# Space Force unit logo library

UNCLASSIFIED. Public units only. As of 22 Oct 2026.

Official emblem files for the USSPACECOM chain-of-command page. Every image here must be an
original file downloaded from an official public source (.mil sites, DAF Historical Support
Division, DVIDS). Nothing is redrawn, traced, cropped into a new design, or generated.

## Status
Sources: carson approved Wikipedia and Wikimedia Commons. Each row records the Commons file page,
the original (.mil, DVIDS or official account) source that Commons cites, and the official page.
The .mil sites refuse cloud traffic (Akamai "Access Denied"), so files come from Commons for now.

- 53 emblems picked on Commons. Only `ussf-emblem.png` is downloaded so far: Wikimedia rate-limits
  the cloud network. Run `python logos/fetch_logos.py` from a normal connection to fetch the rest.
- Not used: user-drawn or traced copies (Commons "own work" files and unofficial SVG versions).
- No usable official file found: CFSCC (original is on media.defense.gov), Space Delta 9,
  2nd Sustainment Sq, 15th C2 Sq, 15th ISR Sq. Ops centers are left as text labels.
- Rows marked "source unverified" cite only imgur or Facebook on Commons; check them against a
  .mil copy before use.

## Layout
- `logos/` (this folder) command, component and delta emblems (`delta-05.png` etc.)
- `logos/squadrons/` squadron emblems
- `manifest.csv` source URL, status and notes for each file

## Usage terms
- Department of the Air Force unit emblems: commercial reproduction requires the proponent unit
  commander's permission (DAFI 84-105, Chapter 3, as cited on DAF Lineage and Honors statements).
  Non-commercial training use is the intended use here; do not sell or imply endorsement.
- USSF emblem: do not stretch, distort, add or remove elements, or add effects; minimum 1 inch
  wide (trademark.af.mil). The USSF Seal is reserved for internal official use and is not used here.
- Army, Navy and Marine Corps insignia follow their own service trademark rules; check each
  service's trademark office before any non-training use.
- Lineage statements from non-AFHRA sources are unofficial.
