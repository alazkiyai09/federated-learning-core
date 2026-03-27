"""Runtime settings."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    name: str = os.getenv("FL_CORE_NAME", "federated-learning-core")
    default_clients: int = int(os.getenv("FL_DEFAULT_CLIENTS", "5"))
    default_rounds: int = int(os.getenv("FL_DEFAULT_ROUNDS", "10"))


settings = Settings()
