"""
minesweeper_v1_buggy.py — Typical AI-Generated V1 Prototype (Intentionally Flawed for Math Defense)
==================================================================================================
Four real discrete-math defects commonly hallucinated by unguided LLM prompts:
  1. Shallow Copy Aliasing (Lab 2): `[[0] * cols] * rows` shares the exact same row list reference!
  2. O(N^2) List Lookup & Collision Risk (Lab 3 & Lab 8): Checking `if (r, c) not in mines_list` inside a loop.
  3. Unbounded Recursive DFS (Lab 7 & Lab 8): Hits Python's RecursionError when grid scales 10x–100x.
  4. Missing FSM Absorbing State Guard (Lab 9): Clicking after LOST or WON continues mutating the board!
"""

from __future__ import annotations

import random
from typing import List, Set, Tuple


class MinesweeperV1Buggy:
    """Deliberately flawed V1 AI prototype used in Prompt Evolution & 100x Stress Demo."""

    def __init__(self, rows: int = 9, cols: int = 9, num_mines: int = 10, seed: int = 42) -> None:
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.rng = random.Random(seed)
        # FLAW 1: Shallow copy aliasing! Mutating logic_board[0][0] mutates every row!
        self.logic_board: List[List[int]] = [[0] * cols] * rows
        self.mines_list: List[Tuple[int, int]] = []
        self.revealed: List[Tuple[int, int]] = []
        self.state: str = "PLAYING"

        self._place_mines_naive()

    def _place_mines_naive(self) -> None:
        # FLAW 2: List membership check `not in self.mines_list` is O(|M|) per step -> O(N^2) under high density
        while len(self.mines_list) < self.num_mines:
            r = self.rng.randint(0, self.rows - 1)
            c = self.rng.randint(0, self.cols - 1)
            if (r, c) not in self.mines_list:
                self.mines_list.append((r, c))

    def has_mine_slow(self, cell: Tuple[int, int]) -> bool:
        """O(|M|) linear scan instead of O(1) hash set lookup."""
        return cell in self.mines_list

    def reveal_recursive_unsafe(self, r: int, c: int, visited: Set[Tuple[int, int]] | None = None) -> int:
        """
        FLAW 3: Unbounded recursive DFS over an empty grid.
        On a 60x60 (3,600 cells) or 100x100 (10,000 cells) board, recursion depth exceeds sys.getrecursionlimit() (~1000)
        and crashes with RecursionError!
        FLAW 4: No check on `self.state != "PLAYING"` -> allows clicking after LOST/WON!
        """
        if visited is None:
            visited = set()
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return 0
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        if (r, c) in self.mines_list:
            self.state = "LOST"
            return 0
        self.revealed.append((r, c))
        opened = 1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                opened += self.reveal_recursive_unsafe(r + dr, c + dc, visited)
        return opened
