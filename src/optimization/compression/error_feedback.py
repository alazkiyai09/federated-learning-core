"""Lazy error-feedback loader."""


def load_error_feedback():
    from src.optimization.compression.legacy.compression.error_feedback import ErrorFeedback

    return ErrorFeedback
