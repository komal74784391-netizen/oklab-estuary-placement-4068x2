"""Evaluate coverage of a placement plan."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import yaml

from src.placement.coverage import coverage, redundancy


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    n = cfg["sites"][0]["grid_rows"] * cfg["sites"][0]["grid_cols"]
    similarity = np.random.rand(n, n)
    selected = list(range(cfg["budget"]))
    print("coverage", coverage(similarity, selected), "redundancy", redundancy(similarity, selected))


if __name__ == "__main__":
    main()
