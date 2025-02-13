from calculator import Calculator

class FreeCalculator:
    def __init__(self, calculator):
        self.calculator = calculator

    def add(self, a, b):
        return self.calculator.add(a, b)

    def sub(self, a, b):
        return self.calculator.sub(a, b)

    def mul(self, a, b):
        raise Exception("Multiplication is not available in the free calculator.")

    def div(self, a, b):
        raise Exception("Division is not available in the free calculator.")

    def power(self, a, b):
        raise Exception("Power operation is not available in the free calculator.")
