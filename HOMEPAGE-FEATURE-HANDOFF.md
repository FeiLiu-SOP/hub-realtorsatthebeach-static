# Homepage Feature Handoff (Execution Record + Full Capability Spec)

This document summarizes:
- Work items requested in recent sessions and their completion status.
- All active capabilities currently present on `real/index.html`.
- Data dependencies, deployment requirements, and maintenance workflow.

## 1) Completed Requests (Recent Sessions)

### A. Value Protection Calculator (initial build, then removed from homepage)
- Implemented previously on homepage with Zillow-style panel and CSV-based value logic.
- Later removed completely per instruction: no HTML block, no calculator CSS, no calculator JS execution remains on homepage.
- Current status: **Not active on homepage**.

### B. Zillow city value data pipeline
- Added Zillow City ZHVI source ingestion flow.
- Added script: `real/scripts/build-city-home-values.ps1`.
- Script behavior:
  - Reads Zillow source CSV: `real/data/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`.
  - Detects latest date column automatically.
  - Exports normalized city dataset:
    - `city`
    - `state`
    - `median_home_value`
  - Output file: `real/data/city-home-values.csv`.
- Current status: **Active and working**.

### C. Live Dispatch Registry module (homepage middle section)
- Added to homepage as native HTML block + CSS + vanilla JS (no framework).
- Randomized service log generation with city/state from `city-home-values.csv`.
- Auto-scrolling log stream.
- Registry sync interval randomized (currently 2–5 minutes).
- Visual style refactored to requested “bureaucratic credibility” presentation.
- Semantic wording updated:
  - `SUCCESS:` -> `STATUS: CONFIRMED`
  - `RESOLVED:` -> `SERVICE COMPLETED`
- Current status: **Active**.

### D. National Asset Preservation Service Matrix (before footer)
- Added 50-state service index section with native `<a>` links.
- Added Priority Service Areas block with 20 high-value major cities.
- Each priority city includes native `<a>` links for three service tunnels:
  - `/water-damage/[city]-[state]/`
  - `/siding/[city]-[state]/`
  - `/plumbing/[city]-[state]/`
- No JS-based navigation rendering for these SEO links.
- Current status: **Active**.

## 2) Current Homepage Capabilities (`real/index.html`)

## 2.1 Static Core Layout
- Legacy table-based homepage layout retained.
- Main hero and service cards remain in place.
- Sidebar keeps featured profile and emergency dispatch card.

## 2.2 Live Dispatch Registry (Active)

### Visual spec (current)
- Container background: `#F8FAFC`.
- Primary text color: `#1E293B`.
- Title bar: white background with gray metadata text.
- Title left indicator: animated green pulse dot.
- Typography in registry module: `Georgia, serif`.

### Runtime behavior
- JS reads `./data/city-home-values.csv`.
- Initializes with seeded history lines for immediate stream density.
- Continues appending random records with randomized cadence.
- Metadata line updates each cycle:
  - `Registry sync: next update in ~[2-5] min`
- If CSV fetch fails, registry enters local simulation mode (fallback city/state).

### Log templates currently used
- `[Timestamp] - STATUS: CONFIRMED - Water Mitigation Unit dispatched to [City], [State].`
- `[Timestamp] - ACTIVE: Siding Integrity Audit in progress - [City], [State].`
- `[Timestamp] - SERVICE COMPLETED: Emergency Pipe Safety repair completed - [City], [State].`

## 2.3 National Asset Preservation Service Matrix (Active)

### State index block
- 50 state-level native links under State Service Index.
- Label format currently: `[State] Service Hub` (Texas line includes “Division Service Hub” wording).

### Priority Service Areas block
- 20 city cards (high-value major city list) with three direct tunnel links each.
- Link format is static/native `<a>`, crawlable without JS.

## 3) Data Files and Their Roles

- `real/data/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`
  - Zillow source time series (city-level ZHVI).
- `real/data/city-home-values.csv`
  - Normalized runtime feed for homepage modules.
  - Current header:
    - `"city","state","median_home_value"`
- `real/scripts/build-city-home-values.ps1`
  - Rebuilds normalized feed from Zillow source.

## 4) Rebuild Workflow (When Zillow Data Updates)

From workspace root:

`powershell -NoProfile -ExecutionPolicy Bypass -File ".\real\scripts\build-city-home-values.ps1"`

Expected output:
- Rewrites `real/data/city-home-values.csv`.
- Prints row count and latest date column used.

## 4.1 Dynamic Sitemap "Blood Sync" Workflow (New)

Primary command (regenerate sitemap-index + service sitemaps):

`powershell -NoProfile -ExecutionPolicy Bypass -File ".\real\scripts\sync-seo-blood.ps1"`

Optional full sync (also rebuild city-home-values first):

`powershell -NoProfile -ExecutionPolicy Bypass -File ".\real\scripts\sync-seo-blood.ps1" -RebuildCityValues`

Generated outputs:
- `real/sitemap-index.xml`
- `real/sitemap-water-damage.xml`
- `real/sitemap-siding.xml`
- `real/sitemap-plumbing.xml`

Priority policy now enforced by generator:
- L2 (`/national-service-coverage/`) => `priority=1.0`
- L3 (`/service-hub/[state]/`) => `priority=1.0`
- L4 (`/[service]/[city-state]/`) => `priority=0.8`

## 5) Deployment Requirements (for full feature activation)

Minimum required files for current homepage features:
- `real/index.html`
- `real/data/city-home-values.csv`

Recommended to include for maintainability:
- `real/data/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`
- `real/scripts/build-city-home-values.ps1`

Important runtime note:
- If opened via `file://`, browser fetch restrictions may block CSV reads.
- Deploy on an HTTP(S) static host so registry data feed resolves correctly.

## 6) Current Scope Boundary

The following are **not** auto-generated yet by current code:
- Physical page files for every state hub URL.
- Physical city detail pages for every `/water-damage/[city]-[state]/`, `/siding/[city]-[state]/`, `/plumbing/[city]-[state]/` link.

These links are already present and crawlable as static anchors, but destination page generation is a separate build task if required.

