"""DP-SGD metadata."""


def describe_dp_mechanisms() -> dict:
    return {
        "source": "src/privacy/dp_sgd/legacy/dp_mechanisms",
        "components": ["gradient_clipper", "noise_addition", "privacy_accountant"],
    }
