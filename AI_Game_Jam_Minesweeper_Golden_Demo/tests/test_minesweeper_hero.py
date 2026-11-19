"""
test_minesweeper_hero.py — Automated Pytest Gate for DM2026 Minesweeper Golden Demo
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from minesweeper_v1_buggy import MinesweeperV1Buggy
from minesweeper_v3_hero import GameState, MinesweeperHeroEngine


def test_v1_demonstrates_shallow_copy_aliasing() -> None:
    v1 = MinesweeperV1Buggy(rows=5, cols=5, num_mines=3, seed=42)
    v1.logic_board[0][0] = 77
    assert v1.logic_board[4][0] == 77  # Demonstrates why V1 fails


def test_v3_row_isolation_and_exact_mine_cardinality() -> None:
    eng = MinesweeperHeroEngine(rows=9, cols=9, num_mines=10, seed=42)
    assert len({id(row) for row in eng.logic_board}) == 9
    assert len(eng.mines) == 10
    assert eng.total_board_combinations() == math.comb(81, 10)


def test_v3_negative_index_guard() -> None:
    eng = MinesweeperHeroEngine(rows=9, cols=9, num_mines=10, seed=42)
    assert eng.is_valid(-1, 0) is False
    assert eng.is_valid(0, -1) is False
    assert eng.is_valid(9, 0) is False
    assert eng.reveal(-1, -1) == (GameState.PLAYING, 0)
    neighbors_corner = eng.get_neighbors(0, 0)
    assert len(neighbors_corner) == 3
    assert all(0 <= r < 9 and 0 <= c < 9 for r, c in neighbors_corner)


def test_v3_bfs_dfs_equivalence_and_connected_components() -> None:
    bfs_eng = MinesweeperHeroEngine(rows=9, cols=9, num_mines=10, seed=42)
    dfs_eng = MinesweeperHeroEngine(rows=9, cols=9, num_mines=10, seed=42)
    zero_cell = next((r, c) for r in range(9) for c in range(9) if bfs_eng.logic_board[r][c] == 0)

    st_b, op_b = bfs_eng.reveal(*zero_cell, use_bfs=True)
    st_d, op_d = dfs_eng.reveal(*zero_cell, use_bfs=False)
    assert st_b == st_d == GameState.PLAYING
    assert op_b == op_d > 1
    assert bfs_eng.revealed == dfs_eng.revealed

    comps = bfs_eng.zero_connected_components()
    assert len(comps) >= 1
    assert any(zero_cell in comp for comp in comps)


def test_v3_100x_scale_survival_without_recursion_error() -> None:
    eng = MinesweeperHeroEngine(rows=100, cols=100, num_mines=0, seed=42)
    state, opened = eng.reveal(0, 0, use_bfs=True)
    assert state == GameState.WON
    assert opened == 10000
    assert len(eng.revealed) == 10000


def test_v3_fsm_absorbing_states_won_and_lost() -> None:
    # 1. Verify LOST absorbing state
    eng = MinesweeperHeroEngine(rows=9, cols=9, num_mines=10, seed=42)
    mine_r, mine_c = next(iter(eng.mines))
    state, _ = eng.reveal(mine_r, mine_c)
    assert state == GameState.LOST

    revealed_before = set(eng.revealed)
    safe_cell = next((r, c) for r in range(9) for c in range(9) if (r, c) not in eng.mines)
    assert eng.reveal(*safe_cell) == (GameState.LOST, 0)
    assert eng.toggle_flag(*safe_unrevealed(eng)) is False
    assert eng.revealed == revealed_before

    # 2. Verify WON absorbing state
    won_eng = MinesweeperHeroEngine(rows=3, cols=3, num_mines=0, seed=42)
    won_state, opened = won_eng.reveal(0, 0)
    assert won_state == GameState.WON
    assert opened == 9
    assert won_eng.reveal(1, 1) == (GameState.WON, 0)
    assert won_eng.toggle_flag(1, 1) is False


def safe_unrevealed(eng: MinesweeperHeroEngine) -> tuple[int, int]:
    return next(
        (r, c)
        for r in range(eng.rows)
        for c in range(eng.cols)
        if (r, c) not in eng.revealed
    )
