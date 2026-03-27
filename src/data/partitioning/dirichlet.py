"""Lazy Dirichlet partition loader."""


def load_dirichlet_partition():
    from src.data.partitioning.legacy.strategies.label_skew import dirichlet_partition

    return dirichlet_partition
