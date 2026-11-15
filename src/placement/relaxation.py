"""Convex relaxation of the placement objective."""
from __future__ import annotations

import numpy as np


def solve_relaxation(similarity: np.ndarray, budget: int, iters: int = 200, lr: float = 0.1) -> np.ndarray:
    n = similarity.shape[0]
    x = np.full(n, budget / n)
    for _ in range(iters):
        grad = similarity.sum(axis=1) - similarity @ x
        x = x + lr * grad
        x = np.maximum(x, 0.0)
        if x.sum() > 0:
            x = x / x.sum() * budget
    return np.minimum(x, 1.0)
