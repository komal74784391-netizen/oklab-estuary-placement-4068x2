"""Run the greedy placement solver on a configured estuary grid."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import yaml

from src.placement.greedy import greedy_placement


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    site = cfg["sites"][0]
    n = site["grid_rows"] * site["grid_cols"]
    similarity = np.random.rand(n, n)
    similarity = similarity @ similarity.T
    selected = greedy_placement(n, cfg["budget"], lambda i, s: similarity[i].mean())
    print("selected", selected)


if __name__ == "__main__":
    main()
