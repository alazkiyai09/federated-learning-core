"""Lazy loader for the preserved FedAvg client."""


def load_client():
    from src.algorithms.fedavg.legacy.client import FederatedClient

    return FederatedClient
