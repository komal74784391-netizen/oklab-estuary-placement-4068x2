"""Lazy greedy submodular maximisation for sensor placement."""
from __future__ import annotations

from typing import Callable, List


def greedy_placement(n: int, budget: int, marginal: Callable[[int, set], float]) -> List[int]:
    selected: List[int] = []
    current: set = set()
    while len(selected) < budget:
        best_idx, best_gain = None, float("-inf")
        for idx in range(n):
            if idx in current:
                continue
            gain = marginal(idx, current)
            if gain > best_gain:
                best_idx, best_gain = idx, gain
        if best_idx is None or best_gain <= 0:
            break
        selected.append(best_idx)
        current.add(best_idx)
    return selected
