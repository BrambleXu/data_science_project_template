from src.fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(4) == 3
