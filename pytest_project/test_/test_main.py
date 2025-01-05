import pytest
from src.main import Calculator

class TestCalculator:
    @pytest.mark.parametrize("x, y, res", [
        (1, 2, 0.5),
        (5, -1, -5),
    ])
    def test_divide(self, x, y, res):
        calculator = Calculator()
        assert calculator.divide(x, y) == res

    @pytest.mark.parametrize("x, y, res", [
        (1, 2, 3),
        (5, -1, 4),
    ])
    def test_add(self, x, y, res):
        calculator = Calculator()
        assert calculator.add(x, y) == res

    @pytest.mark.parametrize("x, y, res", [
        (1, 2, -1),
        (5, -1, 6),
    ])
    def test_subtract(self, x, y, res):
        calculator = Calculator()
        assert calculator.subtract(x, y) == res

    @pytest.mark.parametrize("x, y, res", [
        (1, 2, 2),
        (5, -1, -5),
    ])
    def test_multiply(self, x, y, res):
        calculator = Calculator()
        assert calculator.multiply(x, y) == res
