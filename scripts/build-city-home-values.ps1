param(
  [Parameter(Mandatory = $false)]
  [string] $InputPath,

  [Parameter(Mandatory = $false)]
  [string] $OutputPath
)

$ErrorActionPreference = "Stop"

$defaultInput = ".\real\data\City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
$defaultOutput = ".\real\data\city-home-values.csv"

if ([string]::IsNullOrWhiteSpace($InputPath)) { $InputPath = $defaultInput }
if ([string]::IsNullOrWhiteSpace($OutputPath)) { $OutputPath = $defaultOutput }

$InputPath = (Resolve-Path -LiteralPath $InputPath).Path
if (-not [System.IO.Path]::IsPathRooted($OutputPath)) {
  $OutputPath = (Join-Path (Get-Location) $OutputPath)
}

if (-not (Test-Path -LiteralPath $InputPath)) {
  throw "Input CSV not found: $InputPath"
}

$rows = Import-Csv -LiteralPath $InputPath
if (-not $rows -or $rows.Count -lt 1) {
  throw "No rows parsed from input: $InputPath"
}

$props = $rows[0].PSObject.Properties.Name
$dateCols = $props | Where-Object { $_ -match '^\d{4}-\d{2}-\d{2}$' } | Sort-Object
if (-not $dateCols -or $dateCols.Count -lt 1) {
  throw "No date columns found in Zillow file."
}

$latestCol = $dateCols[-1]

$out = New-Object System.Collections.Generic.List[object]
$seen = @{}

foreach ($r in $rows) {
  $city = [string]$r.RegionName
  $state = [string]$r.State
  $regionType = [string]$r.RegionType
  if ([string]::IsNullOrWhiteSpace($city)) { continue }
  if ($regionType -and $regionType.ToLowerInvariant() -ne "city") { continue }

  $raw = $r.$latestCol
  if ([string]::IsNullOrWhiteSpace([string]$raw)) { continue }
  $val = 0.0
  if (-not [double]::TryParse([string]$raw, [ref]$val)) { continue }

  $key = $city.Trim().ToLowerInvariant()
  if ($seen.ContainsKey($key)) { continue }
  $seen[$key] = $true

  $out.Add([pscustomobject]@{
    city = $city.Trim()
    state = ("" + $state).Trim()
    median_home_value = [math]::Round($val)
  })
}

if ($out.Count -lt 1) {
  throw "No city values produced. Check RegionType/columns."
}

$targetDir = Split-Path -Parent $OutputPath
if (-not (Test-Path -LiteralPath $targetDir)) {
  New-Item -ItemType Directory -Path $targetDir | Out-Null
}

$out | Export-Csv -LiteralPath $OutputPath -NoTypeInformation
Write-Host "Wrote $($out.Count) rows to $OutputPath using latest column $latestCol"

