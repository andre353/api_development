import pytest
import source.shapes as shapes

@pytest.mark.parametrize('side_length, expected_area', [
    (5, 25),
    (10, 100),
    (15, 225),
])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize('side_length, expected_perimeter', [
    (shapes.Square(5), 20),
    (shapes.Square(10), 40),
    (shapes.Square(15), 60)
])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter    