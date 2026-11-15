import numpy as np

from src.placement.coverage import coverage


def test_coverage_empty():
    sim = np.ones((4, 4))
    assert coverage(sim, []) == 0.0
