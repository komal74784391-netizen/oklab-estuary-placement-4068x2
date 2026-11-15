# Sparse sensor placement for estuarine soundscape mapping

Implementation of the placement solvers and coverage metrics described in
"Sparse sensor placement for estuarine soundscape mapping"
(*Ecological Informatics Letters*, 2022, DOI 10.1016/eil.2022.104873).

## Repository status

Released. Both the greedy solver and the convex relaxation, the coverage
metrics and the two estuary deployments used in the paper are included.

## Contents

- `src/placement/greedy.py` - lazy greedy submodular maximisation
- `src/placement/relaxation.py` - convex relaxation solver
- `src/placement/coverage.py` - soundscape coverage metrics
- `scripts/optimize_placement.py`
- `scripts/evaluate_coverage.py`
- `configs/estuary_sites.yaml`
- `tests/test_coverage.py`
