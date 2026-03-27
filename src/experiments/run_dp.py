"""Differential privacy FL experiment smoke runner."""

from __future__ import annotations

from src.privacy.dp_sgd.accounting import describe_accounting
from src.privacy.dp_sgd.mechanisms import describe_dp_mechanisms


def run() -> dict[str, object]:
    return {
        "experiment": "dp_sgd",
        "accounting": describe_accounting(),
        "mechanisms": describe_dp_mechanisms(),
    }
