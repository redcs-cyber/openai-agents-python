$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

uv run pyinstaller --noconfirm --onefile --name azv-admin-panel-launcher scripts/windows_launcher.py
Write-Host "Executable created under dist/azv-admin-panel-launcher.exe"
