# AZV Admin Panel

This Streamlit panel provides an operational dashboard for the repository.

## Start

```bash
scripts/start_admin_panel.sh
```

## Build Windows EXE launcher

Run from Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_windows_exe.ps1
```

The generated launcher executable will be written to `dist/`.
