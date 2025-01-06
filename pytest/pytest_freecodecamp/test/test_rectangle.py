import pytest


def test_area(my_rectangle):
    assert my_rectangle.area() == 200

#  pytest test/test_rectangle.py

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60

# pytest test/test_rectangle.py::test_perimeter

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle


