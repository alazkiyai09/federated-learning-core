"""Training entrypoint metadata."""


def describe_training_stack() -> dict:
    return {
        "source": "src/training/flower/legacy",
        "entrypoint": "src/training/flower/main_legacy.py",
        "strategies": available_strategies(),
    }


def available_strategies() -> list[str]:
    return ["fedavg", "fedprox", "fedadam"]
