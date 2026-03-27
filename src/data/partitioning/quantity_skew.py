"""Lazy quantity skew partition loader."""


def load_quantity_skew_partition():
    from src.data.partitioning.legacy.strategies.quantity_skew import quantity_skew_partition

    return quantity_skew_partition
