"""
benchmark_and_verify.py — /goal2 Compiled Python Stress Benchmark & 300-DPI Chart Generator
==========================================================================================
Empirically measures V1 (Buggy AI Prototype) vs. V3 (Discrete Math Hero Engine):
  1. Scaling Benchmark across 9x9 (81), 30x30 (900), 60x60 (3,600), and 100x100 (10,000 cells, 123x larger than 9x9).
  2. Membership & Collision Benchmark: O(N^2) list membership vs. O(1) Hash-Set lookup.
  3. Flood Fill Survival Benchmark: V1 unbounded recursive DFS crashes (RecursionError) vs. V3 deque BFS.
  4. Equivalence Verification: Iterative BFS vs. Explicit Stack DFS on identical seed=42 reveal identical sets.
  5. Outputs benchmarks/benchmark_results.json and 300-DPI dual-panel chart assets/complexity_v1_vs_v3.png.
"""

from __future__ import annotations

import json
import random
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from minesweeper_v1_buggy import MinesweeperV1Buggy
from minesweeper_v3_hero import GameState, MinesweeperHeroEngine


def bench_lookup_scaling() -> list[dict]:
    """Compare O(M * Q) list membership vs O(Q) hash set membership across board sizes."""
    configs = [
        {"label": "9x9 (81)", "rows": 9, "cols": 9, "mines": 15},
        {"label": "30x30 (900)", "rows": 30, "cols": 30, "mines": 200},
        {"label": "60x60 (3,600)", "rows": 60, "cols": 60, "mines": 900},
        {"label": "100x100 (10,000)", "rows": 100, "cols": 100, "mines": 2500},
    ]
    results = []
    for cfg in configs:
        r, c, m = cfg["rows"], cfg["cols"], cfg["mines"]
        v1 = MinesweeperV1Buggy(r, c, m, seed=42)
        v3 = MinesweeperHeroEngine(r, c, m, seed=42)
        queries = [(i, j) for i in range(r) for j in range(c)]

        # Run 10 repeats for sub-ms precision
        repeats = 10
        t0 = time.perf_counter()
        for _ in range(repeats):
            _ = sum(1 for q in queries if q in v1.mines_list)
        v1_ms = ((time.perf_counter() - t0) / repeats) * 1000.0

        t0 = time.perf_counter()
        for _ in range(repeats):
            _ = sum(1 for q in queries if q in v3.mines)
        v3_ms = ((time.perf_counter() - t0) / repeats) * 1000.0

        speedup = round(v1_ms / max(v3_ms, 1e-6), 2)
        results.append(
            {
                "label": cfg["label"],
                "cells": r * c,
                "mines": m,
                "v1_list_scan_ms": round(v1_ms, 4),
                "v3_set_hash_ms": round(v3_ms, 4),
                "speedup_x": speedup,
            }
        )
    return results


def bench_flood_fill_survival() -> list[dict]:
    """Compare V1 recursive DFS vs V3 iterative deque BFS on empty grids (worst-case depth)."""
    sizes = [9, 30, 60, 100]
    results = []
    for n in sizes:
        v1 = MinesweeperV1Buggy(n, n, 0, seed=42)
        v1_status = "OK"
        v1_opened = 0
        t0 = time.perf_counter()
        try:
            v1_opened = v1.reveal_recursive_unsafe(0, 0)
            v1_ms = round((time.perf_counter() - t0) * 1000.0, 4)
        except RecursionError:
            v1_status = "CRASH_RecursionError"
            v1_ms = None

        v3 = MinesweeperHeroEngine(n, n, 0, seed=42)
        t0 = time.perf_counter()
        state, v3_opened = v3.reveal(0, 0, use_bfs=True)
        v3_ms = round((time.perf_counter() - t0) * 1000.0, 4)

        results.append(
            {
                "grid": f"{n}x{n}",
                "cells": n * n,
                "v1_status": v1_status,
                "v1_opened": v1_opened,
                "v1_ms": v1_ms,
                "v3_status": f"OK_{state.value}",
                "v3_opened": v3_opened,
                "v3_ms": v3_ms,
            }
        )
    return results


def verify_invariants() -> dict:
    """Verify structural invariants & BFS vs DFS exact equivalence on seed=42."""
    v1 = MinesweeperV1Buggy(9, 9, 10, seed=42)
    v1.logic_board[0][0] = 99
    v1_shallow_aliasing_bug = v1.logic_board[1][0] == 99

    v3_bfs = MinesweeperHeroEngine(9, 9, 10, seed=42)
    v3_dfs = MinesweeperHeroEngine(9, 9, 10, seed=42)

    # Check aliasing eliminated
    v3_bfs.logic_board[0][0] = v3_bfs.logic_board[0][0]
    row_ids_unique = len({id(row) for row in v3_bfs.logic_board}) == 9

    # Find first zero cell to test flood fill equivalence
    zero_cell = next(
        (r, c) for r in range(9) for c in range(9) if v3_bfs.logic_board[r][c] == 0
    )
    st_bfs, cnt_bfs = v3_bfs.reveal(*zero_cell, use_bfs=True)
    st_dfs, cnt_dfs = v3_dfs.reveal(*zero_cell, use_bfs=False)
    bfs_dfs_equivalent = (st_bfs == st_dfs) and (cnt_bfs == cnt_dfs) and (v3_bfs.revealed == v3_dfs.revealed)

    # Check FSM absorbing state (LOST blocks further clicks)
    mine_cell = next(iter(v3_bfs.mines))
    st_lost, _ = v3_bfs.reveal(*mine_cell)
    revealed_at_loss = len(v3_bfs.revealed)
    safe_unrevealed = next(
        (r, c)
        for r in range(9)
        for c in range(9)
        if (r, c) not in v3_bfs.mines and (r, c) not in v3_bfs.revealed
    )
    st_after, opened_after = v3_bfs.reveal(*safe_unrevealed)
    fsm_absorbing_ok = (
        st_lost == GameState.LOST
        and st_after == GameState.LOST
        and opened_after == 0
        and len(v3_bfs.revealed) == revealed_at_loss
    )

    return {
        "v1_shallow_aliasing_bug_reproduced": v1_shallow_aliasing_bug,
        "v3_row_ids_unique": row_ids_unique,
        "v3_mines_exact_cardinality": len(v3_bfs.mines) == 10,
        "v3_zero_cell_tested": list(zero_cell),
        "v3_flood_fill_opened": cnt_bfs,
        "v3_bfs_dfs_exact_equivalent": bfs_dfs_equivalent,
        "v3_fsm_absorbing_state_locked": fsm_absorbing_ok,
        "v3_9x9_10mines_combinations": v3_bfs.total_board_combinations(),
        "v3_9x9_first_click_safety_pct": round((81 - 10) / 81 * 100.0, 2),
    }


def generate_chart(lookup_data: list[dict], flood_data: list[dict], out_path: Path) -> None:
    """Generate clean 300-DPI dual-panel comparative engineering chart."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "figure.facecolor": "#0f172a",
            "axes.facecolor": "#1e293b",
            "axes.edgecolor": "#475569",
            "axes.labelcolor": "#e2e8f0",
            "text.color": "#f8fafc",
            "xtick.color": "#cbd5e1",
            "ytick.color": "#cbd5e1",
            "grid.color": "#334155",
        }
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4), dpi=300)

    # Panel 1: Lookup Scaling (V1 O(N*M) List vs V3 O(N) Set Hash)
    cells = [d["cells"] for d in lookup_data]
    v1_ms = [d["v1_list_scan_ms"] for d in lookup_data]
    v3_ms = [d["v3_set_hash_ms"] for d in lookup_data]
    labels = [d["label"].split()[0] for d in lookup_data]

    ax1.plot(cells, v1_ms, marker="o", linewidth=2.6, color="#f43f5e", label="V1 List Scan O(N*M)")
    ax1.plot(cells, v3_ms, marker="s", linewidth=2.6, color="#10b981", label="V3 Hash Set O(N)")
    ax1.set_yscale("log")
    ax1.set_title("Mine Membership Query Scaling (Log Scale)", fontsize=12.5, fontweight="bold", pad=12)
    ax1.set_xlabel("Grid Size (Total Cells = H x W)", fontsize=10.5)
    ax1.set_ylabel("Query Time (ms, log scale)", fontsize=10.5)
    ax1.set_xticks(cells)
    ax1.set_xticklabels(labels, rotation=12)
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper left", frameon=True, facecolor="#0f172a", edgecolor="#475569")

    # Annotate 100x100 speedup
    last = lookup_data[-1]
    ax1.annotate(
        f"{last['speedup_x']}x Faster\n({last['v1_list_scan_ms']}ms -> {last['v3_set_hash_ms']}ms)",
        xy=(last["cells"], last["v3_set_hash_ms"]),
        xytext=(last["cells"] * 0.32, last["v1_list_scan_ms"] * 0.028),
        arrowprops=dict(arrowstyle="->", color="#22d3ee", lw=1.6),
        fontsize=9.5,
        fontweight="bold",
        color="#22d3ee",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#0f172a", edgecolor="#22d3ee", lw=1.0),
    )

    # Panel 2: Flood Fill 100x Scaling Survival (V1 Recursive Crash vs V3 Iterative BFS)
    f_labels = [d["grid"] for d in flood_data]
    x = list(range(len(f_labels)))
    v3_flood_ms = [d["v3_ms"] for d in flood_data]
    v1_flood_vals = [d["v1_ms"] if d["v1_ms"] is not None else max(v3_flood_ms) * 1.35 for d in flood_data]

    bars1 = ax2.bar([i - 0.18 for i in x], v1_flood_vals, width=0.35, color="#f43f5e", alpha=0.85, label="V1 Recursive DFS")
    bars2 = ax2.bar([i + 0.18 for i in x], v3_flood_ms, width=0.35, color="#22d3ee", alpha=0.92, label="V3 Iterative BFS (deque)")

    for i, d in enumerate(flood_data):
        if d["v1_status"] != "OK":
            ax2.text(
                i - 0.18,
                v1_flood_vals[i] * 1.03,
                "CRASH\n(RecursionError)",
                ha="center",
                va="bottom",
                fontsize=7.8,
                fontweight="bold",
                color="#fda4af",
            )
        ax2.text(
            i + 0.18,
            v3_flood_ms[i] + max(v3_flood_ms) * 0.02,
            f"{v3_flood_ms[i]:.2f}ms",
            ha="center",
            va="bottom",
            fontsize=8.2,
            fontweight="bold",
            color="#a5f3fc",
        )

    ax2.set_title("100x Flood Fill Survival: RecursionError vs Iterative O(V+E)", fontsize=12.5, fontweight="bold", pad=12)
    ax2.set_xlabel("Empty Grid Dimensions (H x W)", fontsize=10.5)
    ax2.set_ylabel("Execution Time (ms)", fontsize=10.5)
    ax2.set_xticks(x)
    ax2.set_xticklabels(f_labels)
    ax2.set_ylim(0, max(v1_flood_vals) * 1.28)
    ax2.grid(True, axis="y", linestyle="--", alpha=0.5)
    ax2.legend(loc="upper left", frameon=True, facecolor="#0f172a", edgecolor="#475569")

    fig.suptitle(
        "DM2026 Golden Demo — Prompt Evolution V1 -> V3 & 100x Scaling Benchmark",
        fontsize=14.5,
        fontweight="bold",
        color="#f8fafc",
        y=0.98,
    )
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(out_path, dpi=300)
    plt.close(fig)


def main() -> int:
    lookup = bench_lookup_scaling()
    flood = bench_flood_fill_survival()
    invariants = verify_invariants()

    payload = {
        "lookup_scaling": lookup,
        "flood_fill_survival": flood,
        "invariants": invariants,
    }

    bench_path = ROOT / "benchmarks" / "benchmark_results.json"
    bench_path.parent.mkdir(parents=True, exist_ok=True)
    bench_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    chart_path = ROOT / "assets" / "complexity_v1_vs_v3.png"
    generate_chart(lookup, flood, chart_path)

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"Chart written to: {chart_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
