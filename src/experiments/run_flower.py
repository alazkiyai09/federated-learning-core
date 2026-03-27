"""Flower training-surface smoke runner."""

from __future__ import annotations

from src.training.flower.main import describe_training_stack


def run() -> dict[str, object]:
    stack = describe_training_stack()
    return {
        "experiment": "flower_training",
        "entrypoint": stack.get("entrypoint"),
        "strategies": stack.get("strategies", []),
    }
