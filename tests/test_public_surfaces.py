from src.algorithms.fedavg.aggregation import weighted_average
from src.data.partitioning.analyzer import describe_partitioners
from src.optimization.compression.benchmarks import supported_compression_methods
from src.training.flower.main import describe_training_stack


def test_weighted_average():
    result = weighted_average(
        [
            ({"w1": 1.0, "w2": 2.0}, 2),
            ({"w1": 4.0, "w2": 8.0}, 1),
        ]
    )
    assert result["w1"] == 2.0
    assert result["w2"] == 4.0


def test_partitioning_surface():
    info = describe_partitioners()
    assert "iid" in info["strategies"]
    assert "realistic_bank" in info["strategies"]


def test_compression_surface():
    methods = supported_compression_methods()
    assert "top_k" in methods
    assert "quantize_8bit" in methods


def test_training_surface():
    info = describe_training_stack()
    assert info["entrypoint"].endswith("main_legacy.py")
    assert "fedprox" in info["strategies"]
