"""Personalized FL experiment smoke runner."""

from __future__ import annotations

from src.optimization.personalization.fine_tuning import describe_fine_tuning
from src.optimization.personalization.meta_learning import describe_meta_learning


def run() -> dict[str, object]:
    return {
        "experiment": "personalization",
        "fine_tuning": describe_fine_tuning(),
        "meta_learning": describe_meta_learning(),
    }
