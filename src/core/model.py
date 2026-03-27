"""Shared model description."""


def model_blueprint() -> dict:
    return {"type": "mlp", "layers": [30, 64, 32, 2]}
