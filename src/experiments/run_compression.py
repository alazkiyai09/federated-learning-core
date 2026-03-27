"""Compression experiment smoke runner."""

from __future__ import annotations

from src.optimization.compression.benchmarks import supported_compression_methods


def run() -> dict[str, object]:
    methods = supported_compression_methods()
    return {
        "experiment": "compression",
        "supported_methods": methods,
        "num_methods": len(methods),
    }
