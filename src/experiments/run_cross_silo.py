"""Cross-silo federation experiment smoke runner."""

from __future__ import annotations

from src.scenarios.cross_silo.bank_simulation import describe_bank_simulation
from src.scenarios.cross_silo.federation_metrics import tracked_metrics


def run() -> dict[str, object]:
    simulation = describe_bank_simulation()
    return {
        "experiment": "cross_silo",
        "simulation": simulation,
        "tracked_metrics": tracked_metrics(),
    }
