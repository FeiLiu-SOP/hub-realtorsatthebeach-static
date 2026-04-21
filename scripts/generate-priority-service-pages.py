from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CITIES = [
    ("irvine", "ca", "Irvine", "CA"),
    ("san-jose", "ca", "San Jose", "CA"),
    ("san-francisco", "ca", "San Francisco", "CA"),
    ("san-diego", "ca", "San Diego", "CA"),
    ("los-angeles", "ca", "Los Angeles", "CA"),
    ("anaheim", "ca", "Anaheim", "CA"),
    ("seattle", "wa", "Seattle", "WA"),
    ("santa-ana", "ca", "Santa Ana", "CA"),
    ("long-beach", "ca", "Long Beach", "CA"),
    ("chula-vista", "ca", "Chula Vista", "CA"),
    ("boston", "ma", "Boston", "MA"),
    ("honolulu", "hi", "Honolulu", "HI"),
    ("oakland", "ca", "Oakland", "CA"),
    ("jersey-city", "nj", "Jersey City", "NJ"),
    ("riverside", "ca", "Riverside", "CA"),
    ("washington", "dc", "Washington", "DC"),
    ("miami", "fl", "Miami", "FL"),
    ("gilbert", "az", "Gilbert", "AZ"),
    ("reno", "nv", "Reno", "NV"),
    ("naples", "fl", "Naples", "FL"),
]

SERVICES = [
    {
        "path": "water-damage",
        "title": "Water Damage & Mold Remediation",
        "desc": "Emergency water extraction, moisture control, and mold-risk mitigation protocols for structural asset preservation.",
    },
    {
        "path": "siding",
        "title": "Siding & Cladding Repair",
        "desc": "Exterior envelope stabilization, siding retrofit, and cladding integrity work for weather-exposed properties.",
    },
    {
        "path": "plumbing",
        "title": "Plumbing Services",
        "desc": "Rapid-response leak isolation, pipe safety repair, and system hardening for critical residential infrastructure.",
    },
]


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | {city}, {state} | Realtors At The Beach</title>
  <meta name="robots" content="index,follow">
  <meta name="description" content="{title} service area coverage for {city}, {state}. National Property Protection Network emergency dispatch and structural mitigation workflow.">
</head>
<body style="font-family:verdana,sans-serif; max-width:46rem; margin:2rem auto; padding:0 1rem;">
  <p><a href="/">← Home</a></p>
  <h1 style="color:#CC0000;">{title} — {city}, {state}</h1>
  <p>{desc}</p>
  <p><strong>Dispatch status:</strong> Priority routing enabled for {city}, {state} within the National Property Protection Network matrix.</p>
  <p><strong>Emergency line:</strong> <a href="tel:+16074009375">+1 (607) 400-9375</a> (24/7)</p>
  <hr>
  <p style="font-size:12px;color:#444;">Related service tunnels:
    <a href="/water-damage/{slug}/">Water Damage</a> |
    <a href="/siding/{slug}/">Siding</a> |
    <a href="/plumbing/{slug}/">Plumbing</a>
  </p>
</body>
</html>
"""


def main() -> None:
    created = 0
    for city_slug, state_slug, city_name, state in CITIES:
        slug = f"{city_slug}-{state_slug}"
        for svc in SERVICES:
            out_dir = ROOT / svc["path"] / slug
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file = out_dir / "index.html"
            out_file.write_text(
                HTML_TEMPLATE.format(
                    title=svc["title"],
                    city=city_name,
                    state=state,
                    desc=svc["desc"],
                    slug=slug,
                ),
                encoding="utf-8",
            )
            created += 1

    print(f"Generated {created} city service pages.")


if __name__ == "__main__":
    main()

