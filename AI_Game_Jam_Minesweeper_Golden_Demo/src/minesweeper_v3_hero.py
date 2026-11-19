"""
minesweeper_v3_hero.py — V3 Refactored Discrete Mathematics Minesweeper Engine (Golden Demo)
=============================================================================================
Connects ALL core Discrete Math Labs (W04 Lab1 – W13 Lab9):
  - Lab 1–2 (Grid & Matrices): Cartesian product Q = Z_H x Z_W, row-isolated List Comprehension.
  - Lab 3 (Set Theory): Collision-free mine placement via rng.sample -> |M| == num_mines, O(1) membership.
  - Lab 4 (Binary Relations): 8-neighbor relation R_8 with strict closed-interval boundary guard.
  - Lab 5 (Combinatorics & Probability): Exact C(HW, M) state space & first-click/remaining safety probability.
  - Lab 6–8 (Graph Components, BFS/DFS Flood Fill & Big-O): Iterative deque BFS with Mark-on-Enqueue -> O(V+E).
  - Lab 9 (Finite State Machine): GameState(Enum) with strict absorbing sinks (WON / LOST).
"""

from __future__ import annotations

import math
import random
from collections import deque
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple


class GameState(Enum):
    INIT = "INIT"
    PLAYING = "PLAYING"
    WON = "WON"
    LOST = "LOST"


EMOJI_DIGITS: Dict[int, str] = {
    0: "🟩",
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣",
}


class MinesweeperHeroEngine:
    """Production-grade Discrete Math Minesweeper engine verified for 100x scaling."""

    DIRECTIONS_8: Tuple[Tuple[int, int], ...] = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    )

    def __init__(self, rows: int = 9, cols: int = 9, num_mines: int = 10, seed: Optional[int] = 42) -> None:
        if rows <= 0 or cols <= 0:
            raise ValueError("Grid dimensions must be positive integers.")
        if not (0 <= num_mines < rows * cols):
            raise ValueError("num_mines must satisfy 0 <= num_mines < rows * cols.")

        self.rows: int = rows
        self.cols: int = cols
        self.num_mines: int = num_mines
        self.rng = random.Random(seed)

        self.state: GameState = GameState.INIT
        self.mines: Set[Tuple[int, int]] = set()
        # List comprehension guarantees independent row list objects (eliminates [[0]*cols]*rows aliasing)
        self.logic_board: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
        self.visible_board: List[List[str]] = [["🔲" for _ in range(cols)] for _ in range(rows)]
        self.revealed: Set[Tuple[int, int]] = set()
        self.flagged: Set[Tuple[int, int]] = set()
        self.steps_log: List[Dict[str, object]] = []

        self._place_mines()
        self._compute_neighbor_counts()
        self.state = GameState.PLAYING

    def is_valid(self, r: int, c: int) -> bool:
        """Closed-interval boundary guard preventing Python negative-index wraparound."""
        return 0 <= r < self.rows and 0 <= c < self.cols

    def get_neighbors(self, r: int, c: int) -> List[Tuple[int, int]]:
        """Lab 4: 8-neighbor binary relation R_8 restricted to valid Cartesian coordinates Q."""
        return [(r + dr, c + dc) for dr, dc in self.DIRECTIONS_8 if self.is_valid(r + dr, c + dc)]

    def _place_mines(self, exclude: Optional[Tuple[int, int]] = None) -> None:
        """Lab 3: Collision-free subset M subset Q with |M| == num_mines in O(HW) time."""
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols) if (r, c) != exclude]
        self.mines = set(self.rng.sample(all_cells, self.num_mines))

    def _compute_neighbor_counts(self) -> None:
        """Lab 2 & Lab 4: Populate logic_board (-1 for mines, 0..8 for adjacent mine count)."""
        self.logic_board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r, c in self.mines:
            self.logic_board[r][c] = -1
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.mines:
                    continue
                self.logic_board[r][c] = sum(
                    1 for nr, nc in self.get_neighbors(r, c) if (nr, nc) in self.mines
                )

    def total_board_combinations(self) -> int:
        """Lab 5: Total sample space cardinality C(H*W, M)."""
        return math.comb(self.rows * self.cols, self.num_mines)

    def current_unflagged_mine_probability(self) -> float:
        """Lab 5: Conditional probability of hitting a mine on a random unrevealed/unflagged cell."""
        unknown_cells = (self.rows * self.cols) - len(self.revealed) - len(self.flagged)
        remaining_mines = max(0, self.num_mines - len(self.flagged))
        if unknown_cells <= 0:
            return 0.0
        return min(1.0, remaining_mines / unknown_cells)

    def zero_connected_components(self) -> List[Set[Tuple[int, int]]]:
        """Lab 6: Partition all zero-value safe cells into 8-connected components via BFS."""
        visited: Set[Tuple[int, int]] = set()
        components: List[Set[Tuple[int, int]]] = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.logic_board[r][c] == 0 and (r, c) not in visited:
                    comp: Set[Tuple[int, int]] = set()
                    q: deque[Tuple[int, int]] = deque([(r, c)])
                    visited.add((r, c))
                    while q:
                        cr, cc = q.popleft()
                        comp.add((cr, cc))
                        for nr, nc in self.get_neighbors(cr, cc):
                            if self.logic_board[nr][nc] == 0 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
                    components.append(comp)
        return components

    def toggle_flag(self, r: int, c: int) -> bool:
        """Lab 9: Only allowed in PLAYING state; WON/LOST are strict absorbing states."""
        if self.state != GameState.PLAYING or not self.is_valid(r, c) or (r, c) in self.revealed:
            return False
        if (r, c) in self.flagged:
            self.flagged.remove((r, c))
            self.visible_board[r][c] = "🔲"
        else:
            self.flagged.add((r, c))
            self.visible_board[r][c] = "🚩"
        return True

    def reveal(self, r: int, c: int, use_bfs: bool = True) -> Tuple[GameState, int]:
        """
        Lab 7–9: Iterative Flood Fill (BFS deque or explicit DFS stack) with Mark-on-Enqueue.
        Complexity: Strictly O(|V| + |E|) = O(H*W), immune to RecursionError at 100x100+.
        """
        if self.state != GameState.PLAYING:
            return self.state, 0
        if not self.is_valid(r, c) or (r, c) in self.flagged or (r, c) in self.revealed:
            return self.state, 0

        if (r, c) in self.mines:
            self.state = GameState.LOST
            for mr, mc in self.mines:
                self.visible_board[mr][mc] = "💣"
            self.visible_board[r][c] = "💥"
            self.steps_log.append({"action": "reveal", "pos": (r, c), "result": "BOOM", "opened": 0})
            return self.state, 0

        opened = 0
        frontier = deque([(r, c)]) if use_bfs else [(r, c)]
        seen_local: Set[Tuple[int, int]] = {(r, c)}  # Mark-on-Enqueue invariant

        while frontier:
            cr, cc = frontier.popleft() if use_bfs else frontier.pop()
            if (cr, cc) in self.revealed or (cr, cc) in self.flagged or (cr, cc) in self.mines:
                continue
            self.revealed.add((cr, cc))
            val = self.logic_board[cr][cc]
            self.visible_board[cr][cc] = EMOJI_DIGITS.get(val, str(val))
            opened += 1
            if val == 0:
                for nr, nc in self.get_neighbors(cr, cc):
                    if (nr, nc) not in self.revealed and (nr, nc) not in seen_local:
                        seen_local.add((nr, nc))
                        frontier.append((nr, nc))

        safe_total = self.rows * self.cols - self.num_mines
        if len(self.revealed) == safe_total:
            self.state = GameState.WON
        self.steps_log.append({"action": "reveal", "pos": (r, c), "result": self.state.value, "opened": opened})
        return self.state, opened

    def render_emoji(self) -> str:
        header = "   " + " ".join(f"{c:>2}" for c in range(self.cols))
        lines = [header]
        for r in range(self.rows):
            lines.append(f"{r:>2} " + " ".join(self.visible_board[r]))
        return "\n".join(lines)
