from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    subprocess.run([
        "uv",
        "run",
        "streamlit",
        "run",
        str(root / "tools" / "admin_panel" / "app.py"),
    ], cwd=root, check=False)


if __name__ == "__main__":
    main()
