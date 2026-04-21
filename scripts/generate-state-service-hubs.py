from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STATES = [
    ("alabama", "Alabama", "AL"),
    ("alaska", "Alaska", "AK"),
    ("arizona", "Arizona", "AZ"),
    ("arkansas", "Arkansas", "AR"),
    ("california", "California", "CA"),
    ("colorado", "Colorado", "CO"),
    ("connecticut", "Connecticut", "CT"),
    ("delaware", "Delaware", "DE"),
    ("florida", "Florida", "FL"),
    ("georgia", "Georgia", "GA"),
    ("hawaii", "Hawaii", "HI"),
    ("idaho", "Idaho", "ID"),
    ("illinois", "Illinois", "IL"),
    ("indiana", "Indiana", "IN"),
    ("iowa", "Iowa", "IA"),
    ("kansas", "Kansas", "KS"),
    ("kentucky", "Kentucky", "KY"),
    ("louisiana", "Louisiana", "LA"),
    ("maine", "Maine", "ME"),
    ("maryland", "Maryland", "MD"),
    ("massachusetts", "Massachusetts", "MA"),
    ("michigan", "Michigan", "MI"),
    ("minnesota", "Minnesota", "MN"),
    ("mississippi", "Mississippi", "MS"),
    ("missouri", "Missouri", "MO"),
    ("montana", "Montana", "MT"),
    ("nebraska", "Nebraska", "NE"),
    ("nevada", "Nevada", "NV"),
    ("new-hampshire", "New Hampshire", "NH"),
    ("new-jersey", "New Jersey", "NJ"),
    ("new-mexico", "New Mexico", "NM"),
    ("new-york", "New York", "NY"),
    ("north-carolina", "North Carolina", "NC"),
    ("north-dakota", "North Dakota", "ND"),
    ("ohio", "Ohio", "OH"),
    ("oklahoma", "Oklahoma", "OK"),
    ("oregon", "Oregon", "OR"),
    ("pennsylvania", "Pennsylvania", "PA"),
    ("rhode-island", "Rhode Island", "RI"),
    ("south-carolina", "South Carolina", "SC"),
    ("south-dakota", "South Dakota", "SD"),
    ("tennessee", "Tennessee", "TN"),
    ("texas", "Texas", "TX"),
    ("utah", "Utah", "UT"),
    ("vermont", "Vermont", "VT"),
    ("virginia", "Virginia", "VA"),
    ("washington", "Washington", "WA"),
    ("west-virginia", "West Virginia", "WV"),
    ("wisconsin", "Wisconsin", "WI"),
    ("wyoming", "Wyoming", "WY"),
]

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{state_name} Service Hub | National Asset Preservation</title>
  <meta name="robots" content="index,follow">
  <meta name="description" content="{state_name} service hub for asset preservation dispatch coverage: water mitigation, siding integrity, and pipe safety response routing.">
</head>
<body style="font-family:verdana,sans-serif; max-width:46rem; margin:2rem auto; padding:0 1rem;">
  <p><a href="/">← Home</a></p>
  <h1 style="color:#0b2d5c;">{state_name} Service Hub</h1>
  <p>This index consolidates statewide operational coverage for <b>Asset Preservation</b> and structural risk mitigation.</p>
  <ul>
    <li><a href="/water-damage/">Water &amp; Flood Mitigation</a></li>
    <li><a href="/siding/">Siding &amp; Cladding Integrity</a></li>
    <li><a href="/plumbing/">Master Plumbing &amp; Pipe Safety</a></li>
  </ul>
  <p><strong>Emergency line:</strong> <a href="tel:+16074009375">+1 (607) 400-9375</a> (24/7)</p>
  <hr>
  <p style="font-size:12px;color:#475569;">
    Note: City-specific tunnels (e.g. <code>/water-damage/[city]-{abbr_lower}/</code>) are available for priority routing where applicable.
  </p>
</body>
</html>
"""


def main() -> None:
    base = ROOT / "service-hub"
    created = 0
    for slug, name, abbr in STATES:
        out_dir = base / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(
            HTML.format(state_name=name, abbr_lower=abbr.lower()),
            encoding="utf-8",
        )
        created += 1
    print(f"Generated {created} state hub pages.")


if __name__ == "__main__":
    main()

