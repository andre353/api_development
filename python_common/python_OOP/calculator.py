class Calculator:

    def _validate_input(self, x: str, y: str,) -> None:
        if not x.isdigit() or not y.isdigit():
            raise TypeError("Оба числа должны быть числами.")
    def _validate_operation(self, operation: str) -> None:
        valid_operations = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

        if operation not in valid_operations:
            raise ValueError("Неверно введенная математическая операция.")

    def _calculate(
        self, x: str, y: str, operation: str
    ) -> float:
        try:
            self._validate_input(x, y)
            self._validate_operation(operation)
            x = int(x)
            y = int(y)
            6
            if operation == "/":
                if y == 0:
                    raise ZeroDivisionError("На ноль делить нельзя.")
            if operation == "+":
                return x + y
            elif operation == "-":
                return x - y
            elif operation == "*":
                return x * y
            elif operation == "/":
                return x / y
        except (TypeError, ZeroDivisionError, ValueError) as e:
            print(f"Ошибка: {e}")
            return None

    def calculate(
        self, x:int, y: int, operation: str
    ) -> int:
        return self._calculate(x, y, operation)


if __name__ == "__main__":
    calculator = Calculator()

    x = input("Введите первое число: ")
    y = input("Введите второе число: ")
    operation = input("Введите математическую операцию (+, -, *, /): ")

    result = calculator.calculate(x, y, operation)

    if result is not None:
        print(f"Результат: {result}")
