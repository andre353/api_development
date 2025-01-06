from typing import Union


class Calculator:

    def _validate_input(self, x: Union[int, float], y: Union[int, float]) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        self._validate_input(x, y)
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        self._validate_input(x, y)
        return x + y

    def subtract(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        self._validate_input(x, y)
        return x - y

    def multiply(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        self._validate_input(x, y)
        return x * y


if __name__ == "__main__":
    calculator = Calculator()







