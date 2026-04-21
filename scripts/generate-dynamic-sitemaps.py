from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://realtorsatthebeach.com"
TODAY = date.today().isoformat()

SERVICES = [
    ("water-damage", "sitemap-water-damage.xml"),
    ("siding", "sitemap-siding.xml"),
    ("plumbing", "sitemap-plumbing.xml"),
]


@dataclass(frozen=True)
class UrlEntry:
    loc: str
    priority: str
    changefreq: str
    lastmod: str = TODAY


def to_url(path: str) -> str:
    clean = "/" + path.strip("/")
    return f"{BASE_URL}{clean}/"


def is_city_node(path: Path) -> bool:
    # L4 city node: /{service}/{city-state}/index.html
    # Excludes service root and any non-city folders.
    return (
        path.is_dir()
        and path.name not in {"", ".", ".."}
        and (path / "index.html").exists()
    )


def collect_state_hubs() -> list[UrlEntry]:
    state_root = ROOT / "service-hub"
    if not state_root.exists():
        return []

    entries: list[UrlEntry] = []
    for child in sorted(state_root.iterdir(), key=lambda p: p.name):
        if child.is_dir() and (child / "index.html").exists():
            entries.append(
                UrlEntry(
                    loc=to_url(f"service-hub/{child.name}"),
                    priority="1.0",  # L3
                    changefreq="weekly",
                )
            )
    return entries


def collect_city_nodes(service: str) -> list[UrlEntry]:
    service_root = ROOT / service
    if not service_root.exists():
        return []

    entries: list[UrlEntry] = []
    for child in sorted(service_root.iterdir(), key=lambda p: p.name):
        if is_city_node(child):
            entries.append(
                UrlEntry(
                    loc=to_url(f"{service}/{child.name}"),
                    priority="0.8",  # L4
                    changefreq="weekly",
                )
            )
    return entries


def xml_urlset(entries: Iterable[UrlEntry]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for entry in entries:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{entry.loc}</loc>",
                f"    <lastmod>{entry.lastmod}</lastmod>",
                f"    <changefreq>{entry.changefreq}</changefreq>",
                f"    <priority>{entry.priority}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    lines.append("")
    return "\n".join(lines)


def xml_sitemap_index(items: list[tuple[str, str]]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for filename, loc in items:
        lines.extend(
            [
                "  <sitemap>",
                f"    <loc>{loc}</loc>",
                f"    <lastmod>{TODAY}</lastmod>",
                "  </sitemap>",
            ]
        )
    lines.append("</sitemapindex>")
    lines.append("")
    return "\n".join(lines)


def write_service_sitemap(service: str, filename: str, state_hubs: list[UrlEntry]) -> None:
    l2_and_l3 = [
        UrlEntry(loc=to_url("national-service-coverage"), priority="1.0", changefreq="daily"),  # L2
        *state_hubs,  # L3
    ]
    l4 = collect_city_nodes(service)
    content = xml_urlset([*l2_and_l3, *l4])
    (ROOT / filename).write_text(content, encoding="utf-8")


def main() -> None:
    state_hubs = collect_state_hubs()
    index_items: list[tuple[str, str]] = []

    for service, sitemap_file in SERVICES:
        write_service_sitemap(service, sitemap_file, state_hubs)
        index_items.append((sitemap_file, f"{BASE_URL}/{sitemap_file}"))

    sitemap_index = xml_sitemap_index(index_items)
    (ROOT / "sitemap-index.xml").write_text(sitemap_index, encoding="utf-8")

    print(
        "Generated sitemap-index.xml and service sitemaps: "
        + ", ".join(name for _, name in SERVICES)
    )


if __name__ == "__main__":
    main()

