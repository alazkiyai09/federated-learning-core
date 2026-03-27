"""Vertical FL experiment smoke runner."""

from __future__ import annotations

from src.scenarios.vertical.psi import describe_psi
from src.scenarios.vertical.trainer import describe_vertical_trainer


def run() -> dict[str, object]:
    return {
        "experiment": "vertical_fl",
        "psi": describe_psi(),
        "trainer": describe_vertical_trainer(),
    }
