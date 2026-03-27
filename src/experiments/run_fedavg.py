"""Runnable FedAvg smoke experiment for the split FL core repository."""

from __future__ import annotations

from src.algorithms.fedavg.aggregation import weighted_average


def run() -> dict[str, object]:
    updates = [
        ({"w1": 0.8, "w2": 1.2}, 120),
        ({"w1": 1.0, "w2": 1.0}, 80),
        ({"w1": 1.2, "w2": 0.7}, 100),
    ]
    aggregated = weighted_average(updates)
    return {"experiment": "fedavg", "num_clients": len(updates), "aggregated": aggregated}
