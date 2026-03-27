"""Pure-python aggregation helpers."""

from __future__ import annotations

from collections.abc import Mapping


def weighted_average(updates: list[tuple[Mapping[str, float], int]]) -> dict[str, float]:
    total = sum(weight for _, weight in updates)
    if total <= 0:
        return {}
    keys = set().union(*(payload.keys() for payload, _ in updates))
    aggregated: dict[str, float] = {}
    for key in keys:
        aggregated[key] = sum(payload.get(key, 0.0) * weight for payload, weight in updates) / total
    return aggregated
