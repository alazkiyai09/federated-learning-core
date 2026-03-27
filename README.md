# Federated Learning Core (`federated-learning-core`)

Core **federated learning framework** for cross-silo training, non-IID partitioning, communication optimization, personalization, and DP-SGD privacy experiments.

## Why This Repository

Federated learning systems need more than one algorithm. `federated-learning-core` offers composable surfaces for algorithm baselines, orchestration, partitioning strategies, and privacy controls.

## Core Features

- FedAvg aggregation surface and federated client/server wrappers
- Non-IID partitioning (Dirichlet, quantity skew, IID baselines)
- Flower-based orchestration modules
- Compression utilities for bandwidth-constrained FL
- Personalization and meta-learning scaffolds
- Differential privacy accounting/mechanism surfaces
- Experiment runners under `src/experiments`

## Project Structure

- `src/algorithms/`: FL algorithm wrappers and aggregators
- `src/data/partitioning/`: data partitioning strategies
- `src/training/flower/`: training stack and strategy metadata
- `src/optimization/`: compression and personalization
- `src/privacy/dp_sgd/`: privacy accounting and mechanisms
- `src/scenarios/`: cross-silo and vertical FL scenario modules
- `src/experiments/`: runnable experiment entrypoints

## Quick Start

```bash
pip install -r requirements.txt
pytest -q tests/test_public_surfaces.py
```

## Experiment Runners

- `src/experiments/run_fedavg.py`
- `src/experiments/run_flower.py`
- `src/experiments/run_compression.py`
- `src/experiments/run_cross_silo.py`
- `src/experiments/run_vertical.py`
- `src/experiments/run_personalization.py`
- `src/experiments/run_dp.py`

## SEO Keywords

federated learning framework, fedavg implementation, non iid partitioning, cross silo federated learning, differential privacy sgd, flower federated training, personalized federated learning
