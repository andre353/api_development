import pytest
import source.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        if method.__name__ == "test_area":
            print("Running test_area")

    def teardown_method(self, method):
        if method.__name__ == "test_area":
            print("Finished test_area")

# pytest -s test/test_circle.py
    def test_area(self):
        circle = shapes.Circle(5)
        assert circle.area() == 78.53981633974483