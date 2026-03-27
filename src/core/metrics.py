"""Common metric labels for FL experiments."""


def supported_metrics() -> list[str]:
    return ["accuracy", "auc", "auprc", "convergence_round", "communication_cost"]
