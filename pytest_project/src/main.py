from typing import Union


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        return x + y

    def subtract(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        return x - y

    def multiply(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers or floats")    
        return x * y


if __name__ == "__main__":
    calculator = Calculator()
