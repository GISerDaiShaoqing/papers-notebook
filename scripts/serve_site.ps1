$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $repoRoot "app\.venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) {
    throw "App virtual environment not found. See app/README.md to create it."
}

Push-Location $repoRoot
try {
    & $python "scripts\prepare_site.py"
    if ($LASTEXITCODE -ne 0) {
        throw "Could not prepare the website source files."
    }
    & $python -m mkdocs serve --config-file "mkdocs.yml" --dev-addr "127.0.0.1:8000"
    if ($LASTEXITCODE -ne 0) {
        throw "MkDocs server stopped with exit code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
