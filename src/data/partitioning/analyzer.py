"""Partitioning metadata."""


def describe_partitioners() -> dict:
    return {
        "strategies": ["iid", "dirichlet_label_skew", "quantity_skew", "feature_skew", "realistic_bank"],
        "source": "src/data/partitioning/legacy",
    }
