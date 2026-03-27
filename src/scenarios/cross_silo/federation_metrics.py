"""Cross-silo metric metadata."""


def tracked_metrics() -> list[str]:
    return ["per_bank_auc", "global_auc", "fairness_gap"]
