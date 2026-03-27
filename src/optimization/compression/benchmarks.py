"""Compression metadata."""


def supported_compression_methods() -> list[str]:
    return ["top_k", "random_k", "threshold", "quantize_8bit", "quantize_4bit", "error_feedback"]
