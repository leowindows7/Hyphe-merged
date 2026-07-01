#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "apis-tester"
ENTRYPOINT = APP_DIR / "startTester.py"

if not ENTRYPOINT.exists():
    raise SystemExit(f"Could not find tester entry point at {ENTRYPOINT}")

cmd = [sys.executable, str(ENTRYPOINT)]
cmd.extend(sys.argv[1:])
raise SystemExit(subprocess.call(cmd, cwd=str(APP_DIR)))
