class Calculator:
    def sum(self, x: int | float, y: int | float) -> int | float:
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("Both arguments must be numeric")
        return x + y

    def divide(self, x: int | float, y: int | float) -> int | float:
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("Both arguments must be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y


if __name__ == "__main__":
    calculator = Calculator()
