class Calculator:
    def sum(self, x: int | float, y: int | float) -> int | float:
        return x + y

    def divide(self, x: int | float, y: int | float) -> int | float:
        return x / y


if __name__ == "__main__":
    calculator = Calculator()
