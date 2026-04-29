#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOTSTRAP_DIR="$ROOT_DIR/bootstrap"
VENV_DIR="$ROOT_DIR/.venv"

printf "[OpenAZV] Bootstrapping local environment...\n"
command -v python3 >/dev/null || { echo "python3 is required"; exit 1; }
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install -r "$BOOTSTRAP_DIR/requirements-starter.txt"

printf "[OpenAZV] Installed starter dependencies.\n"
printf "[OpenAZV] Next: configure .env from .env.example and run your runtime entrypoint.\n"
