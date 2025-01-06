from typing import Union


class Calculator:

    def _validate_input(self, x: Union[int, float], y: Union[int, float]) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers or floats")

    def _validate_operation(self, operation: str) -> None:
        valid_operations = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

        if operation not in valid_operations:
            raise ValueError("Invalid operation")

    def _calculate(
        self, x: Union[int, float], y: Union[int, float], operation: str
    ) -> Union[int, float]:
        try:
            self._validate_input(x, y)
            self._validate_operation(operation)
            if operation == "/":
                if y == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
            if operation == "+":
                return x + y
            elif operation == "-":
                return x - y
            elif operation == "*":
                return x * y
            elif operation == "/":
                return x / y
        except (TypeError, ZeroDivisionError, ValueError) as e:
            print(f"Error: {e}")
            return None

    def calculate(
        self, x: Union[int, float], y: Union[int, float], operation: str
    ) -> Union[int, float]:
        return self._calculate(x, y, operation)


if __name__ == "__main__":
    calculator = Calculator()

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calculator.calculate(x, y, operation)

    if result is not None:
        print(f"Result: {result}")
