# federated-learning-core

Federated learning training framework split out of `fl-security-research`.

This repo consolidates the original FL foundation projects into one structure:

- `src/algorithms/` for FedAvg and strategy metadata
- `src/data/partitioning/` for IID and non-IID partitioning
- `src/training/flower/` for Flower-based orchestration
- `src/optimization/` for compression and personalization
- `src/scenarios/` for cross-silo and vertical FL
- `src/privacy/dp_sgd/` for differential privacy components

Original project implementations are preserved under the new package layout, especially in `legacy/` folders where the source tree needed to remain intact.

## Legacy Sources Merged

- `fedavg_from_scratch`
- `non_iid_partitioner`
- `flower_fraud_detection`
- `communication_efficient_fl`
- `cross_silo_bank_fl`
- `vertical_fraud_detection`
- `personalized_fl_fraud`
- `dp_federated_learning`

## Quick Start

```bash
pip install -r requirements.txt
pytest -q tests/test_public_surfaces.py
```
