"""Lazy Flower client loader."""


def load_flower_client():
    from src.training.flower.legacy.client import create_client

    return create_client
