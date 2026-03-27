"""Lazy loader for the preserved FedAvg server."""


def load_server():
    from src.algorithms.fedavg.legacy.server import FederatedServer

    return FederatedServer
