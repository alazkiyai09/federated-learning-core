"""Shared dataset metadata helpers."""


def dataset_contract() -> dict:
    return {
        "task": "binary_fraud_detection",
        "expected_input_dim": 30,
        "default_split": {"train": 0.7, "val": 0.15, "test": 0.15},
    }
