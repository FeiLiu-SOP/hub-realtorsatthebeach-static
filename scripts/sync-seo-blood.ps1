param(
  [switch]$RebuildCityValues
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootDir = Resolve-Path (Join-Path $scriptDir "..")

Write-Host "[SEO Sync] Root: $rootDir"

if ($RebuildCityValues) {
  Write-Host "[SEO Sync] Rebuilding city-home-values.csv ..."
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $scriptDir "build-city-home-values.ps1")
  if ($LASTEXITCODE -ne 0) {
    throw "build-city-home-values.ps1 failed with exit code $LASTEXITCODE"
  }
}

Write-Host "[SEO Sync] Regenerating dynamic sitemaps ..."
& python (Join-Path $scriptDir "generate-dynamic-sitemaps.py")
if ($LASTEXITCODE -ne 0) {
  throw "generate-dynamic-sitemaps.py failed with exit code $LASTEXITCODE"
}

Write-Host "[SEO Sync] Done."
Write-Host "Generated:"
Write-Host " - real/sitemap-index.xml"
Write-Host " - real/sitemap-water-damage.xml"
Write-Host " - real/sitemap-siding.xml"
Write-Host " - real/sitemap-plumbing.xml"

