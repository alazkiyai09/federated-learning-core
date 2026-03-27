"""Lazy Flower server loader."""


def load_flower_server():
    from src.training.flower.legacy.server import get_strategy, start_server_with_strategy

    return {"get_strategy": get_strategy, "start_server_with_strategy": start_server_with_strategy}
