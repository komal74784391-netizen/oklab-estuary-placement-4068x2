"""Soundscape coverage metrics."""
from __future__ import annotations

import numpy as np


def coverage(similarity: np.ndarray, selected) -> float:
    idx = list(selected)
    if not idx:
        return 0.0
    return float(similarity[np.ix_(idx, range(similarity.shape[1]))].max(axis=0).mean())


def redundancy(similarity: np.ndarray, selected) -> float:
    idx = list(selected)
    if len(idx) < 2:
        return 0.0
    sub = similarity[np.ix_(idx, idx)]
    off_diag = sub.sum() - np.trace(sub)
    return float(off_diag / (len(idx) * (len(idx) - 1)))
