from __future__ import annotations

import json
import platform
import subprocess
from datetime import UTC, datetime
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = ROOT / "admin_panel.log"


def run_command(command: list[str]) -> tuple[int, str]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (completed.stdout or "") + (completed.stderr or "")
    return completed.returncode, output.strip()


def git_info() -> dict[str, str]:
    branch_code, branch = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    commit_code, commit = run_command(["git", "rev-parse", "HEAD"])
    status_code, status = run_command(["git", "status", "--short"])
    return {
        "branch": branch if branch_code == 0 else "unknown",
        "commit": commit[:12] if commit_code == 0 else "unknown",
        "dirty": "yes" if status_code == 0 and bool(status) else "no",
    }


def system_info() -> dict[str, str]:
    return {
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "machine": platform.machine(),
    }


def check_suite() -> dict[str, dict[str, str | int]]:
    checks: dict[str, list[str]] = {
        "format": ["make", "format"],
        "lint": ["make", "lint"],
        "typecheck": ["make", "typecheck"],
        "tests": ["make", "tests"],
    }
    results: dict[str, dict[str, str | int]] = {}
    for name, cmd in checks.items():
        code, output = run_command(cmd)
        results[name] = {"exit_code": code, "output": output[-5000:]}
    return results


def append_log(message: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as file:
        file.write(f"[{datetime.now(UTC).isoformat()}] {message}\n")


st.set_page_config(page_title="AZV Admin Panel", layout="wide")
st.title("AZV Admin Panel")

left, right = st.columns(2)

with left:
    st.subheader("System")
    st.json(system_info())

    st.subheader("Git")
    st.json(git_info())

with right:
    st.subheader("Quick Actions")
    if st.button("Run full verification"):
        append_log("Running full verification stack.")
        with st.spinner("Running checks..."):
            results = check_suite()
        st.session_state["last_results"] = results

    if st.button("Create project ZIP"):
        zip_name = ROOT / "dist" / "openai-agents-python-admin-bundle.zip"
        zip_name.parent.mkdir(parents=True, exist_ok=True)
        code, output = run_command(
            [
                "python",
                "-m",
                "zipfile",
                "-c",
                str(zip_name),
                ".",
            ]
        )
        append_log(f"ZIP build exit code {code}.")
        st.write({"exit_code": code, "zip": str(zip_name), "output": output[-500:]})

st.subheader("Verification Results")
if "last_results" in st.session_state:
    for check_name, data in st.session_state["last_results"].items():
        st.markdown(f"### {check_name}")
        st.write(f"Exit code: {data['exit_code']}")
        st.code(str(data["output"]))
else:
    st.info("No checks run yet.")

st.subheader("Admin Log")
if LOG_PATH.exists():
    st.code(LOG_PATH.read_text(encoding="utf-8")[-5000:])
else:
    st.info("No log entries yet.")

st.subheader("Export")
snapshot = {
    "system": system_info(),
    "git": git_info(),
}
st.download_button(
    "Download status JSON",
    data=json.dumps(snapshot, indent=2),
    file_name="admin_panel_status.json",
    mime="application/json",
)
