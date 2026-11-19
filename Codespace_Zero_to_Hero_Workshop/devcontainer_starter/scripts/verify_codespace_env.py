#!/usr/bin/env python3
"""
DM2026 Codespaces Environment & Workshop Readiness Gate (Neuro-Symbolic Verifier)
=================================================================================
Deterministic verification script for both:
  1. Runtime Codespace Container checks (CPU, RAM, Disk, Python, Packages, Git Remote)
  2. Workshop Curriculum Integrity checks (--audit-workshop)
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path


def check_runtime_env() -> dict:
    """Inspect container hardware, Python version, packages, and Git remote."""
    cpu_count = os.cpu_count() or 0
    disk_usage = shutil.disk_usage("/")
    disk_total_gb = round(disk_usage.total / (1024 ** 3), 2)
    disk_free_gb = round(disk_usage.free / (1024 ** 3), 2)

    mem_total_gb = None
    meminfo = Path("/proc/meminfo")
    if meminfo.exists():
        for line in meminfo.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("MemTotal:"):
                kb = int(line.split()[1])
                mem_total_gb = round(kb / (1024 ** 2), 2)
                break

    required_pkgs = ["numpy", "matplotlib", "pytest", "jupyterlab"]
    pkg_status = {}
    for pkg in required_pkgs:
        try:
            mod = importlib.import_module(pkg if pkg != "jupyterlab" else "jupyterlab")
            pkg_status[pkg] = getattr(mod, "__version__", "installed")
        except ImportError:
            pkg_status[pkg] = "MISSING"

    git_remote = "unknown"
    try:
        res = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if res.returncode == 0:
            git_remote = res.stdout.strip()
    except Exception:
        pass

    is_codespace = os.environ.get("CODESPACES", "false").lower() == "true"
    codespace_name = os.environ.get("CODESPACE_NAME", "local-host")

    os_pretty_name = platform.platform()
    os_release = Path("/etc/os-release")
    if os_release.exists():
        for line in os_release.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("PRETTY_NAME="):
                os_pretty_name = line.split("=", 1)[1].strip().strip('"')
                break

    cwd_str = str(Path.cwd().resolve())
    persistent_volume_safe = (
        cwd_str.startswith("/workspaces/DM2026") if is_codespace else True
    )

    report = {
        "os": platform.system(),
        "os_pretty_name": os_pretty_name,
        "python": platform.python_version(),
        "is_codespace": is_codespace,
        "codespace_name": codespace_name,
        "cwd": cwd_str,
        "persistent_volume_safe": persistent_volume_safe,
        "cpu_cores": cpu_count,
        "ram_gb": mem_total_gb,
        "disk_total_gb": disk_total_gb,
        "disk_free_gb": disk_free_gb,
        "git_remote": git_remote,
        "packages": pkg_status,
    }
    return report


def audit_workshop(workshop_dir: Path) -> tuple[bool, dict]:
    """Deterministic L.A.W. / Golden Baseline audit on the 7 workshop books."""
    expected_files = [
        "README.md",
        "01_5W1H_5Why_and_Study5_DeepDive.md",
        "02_Top10_Codespace_Playbooks.md",
        "03_Labs_01_to_14_Zero_to_Cloud_IDE.md",
        "04_Labs_15_to_28_DM2026_and_Hero_Capstones.md",
        "05_Instructor_90min_Stage_Script.md",
        "06_Student_QuickRef_and_Rubric.md",
    ]
    file_stats = {}
    total_bytes = 0
    missing = []
    placeholders_found = []
    all_text = []

    placeholder_patterns = [
        r"\[在此貼入",
        r"\[insert here\]",
        r"TODO:",
        r"TBD",
    ]

    for fname in expected_files:
        fpath = workshop_dir / fname
        if not fpath.exists():
            missing.append(fname)
            continue
        content = fpath.read_text(encoding="utf-8")
        size = fpath.stat().st_size
        total_bytes += size
        file_stats[fname] = size
        all_text.append(content)
        for pat in placeholder_patterns:
            if re.search(pat, content, re.IGNORECASE):
                placeholders_found.append(f"{fname}:{pat}")

    combined = "\n".join(all_text)
    labs_found = sorted(set(re.findall(r"##\s+Lab\s+(\d{2})[：:]", combined)))
    pbs_found = sorted(set(re.findall(r"\bPB-(\d{2})\b", combined)))

    passed = (
        len(missing) == 0
        and total_bytes >= 80000
        and len(placeholders_found) == 0
        and len(labs_found) >= 28
        and len(pbs_found) >= 10
    )

    summary = {
        "passed": passed,
        "total_bytes": total_bytes,
        "missing_files": missing,
        "file_bytes": file_stats,
        "labs_count": len(labs_found),
        "labs_found": labs_found,
        "playbooks_count": len(pbs_found),
        "playbooks_found": pbs_found,
        "placeholders_found": placeholders_found,
    }
    return passed, summary


def main() -> int:
    parser = argparse.ArgumentParser(description="DM2026 Codespaces & Workshop Gate")
    parser.add_argument(
        "--audit-workshop",
        type=Path,
        default=None,
        help="Path to DM2026_Codespace_Zero_to_Hero_Workshop directory",
    )
    args = parser.parse_args()

    if args.audit_workshop:
        passed, summary = audit_workshop(args.audit_workshop)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if passed else 1

    report = check_runtime_env()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
