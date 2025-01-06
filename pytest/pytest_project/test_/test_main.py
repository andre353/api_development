import pytest
from contextlib import nullcontext as does_not_raise
from src.main import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, 0, -5, pytest.raises(ZeroDivisionError)),
        ],
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            calculator = Calculator()
            assert calculator.divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (5, "-1", 4, pytest.raises(TypeError)),
        ],
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            calculator = Calculator()
            assert calculator.add(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, -1, does_not_raise()),
            (5, -1, 6, does_not_raise()),
            (5, "-1", 6, pytest.raises(TypeError)),
        ],
    )
    def test_subtract(self, x, y, res, expectation):
        with expectation:
            calculator = Calculator()
            assert calculator.subtract(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 2, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
        ],
    )
    def test_multiply(self, x, y, res, expectation):
        with expectation:
            calculator = Calculator()
            assert calculator.multiply(x, y) == res
