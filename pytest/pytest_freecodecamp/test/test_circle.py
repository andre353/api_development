import math
import pytest
import source.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"Running {method.__name__}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Finished {method.__name__}")

# pytest -s test/test_circle.py
    def test_area(self):
        assert self.circle.area() == 314.1592653589793

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected   
# pytest -s test/test_circle.py::TestCircle::test_perimeter        