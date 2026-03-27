"""Lazy quantization loader."""


def load_quantizers():
    from src.optimization.compression.legacy.compression.quantizers import quantize_8bit, quantize_4bit

    return {"quantize_8bit": quantize_8bit, "quantize_4bit": quantize_4bit}
