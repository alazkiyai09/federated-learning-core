"""Lazy IID partition loader."""


def load_iid_partition():
    from src.data.partitioning.legacy.strategies.iid import iid_partition

    return iid_partition
