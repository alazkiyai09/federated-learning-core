"""Flower strategy metadata."""


def available_strategies() -> list[str]:
    return ["fedavg", "fedprox", "fedadam"]
