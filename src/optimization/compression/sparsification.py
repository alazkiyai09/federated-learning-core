"""Lazy sparsification loader."""


def load_top_k_sparsify():
    from src.optimization.compression.legacy.compression.sparsifiers import top_k_sparsify

    return top_k_sparsify
