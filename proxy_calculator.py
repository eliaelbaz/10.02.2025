from calculator import Calculator

class ProxyCalculator:
    """Proxy calculator that restricts advanced features for free users."""

    def __init__(self, is_premium=False):
        self.calculator = Calculator()
        self.is_premium = is_premium

    def add(self, a, b):
        return self.calculator.add(a, b)

    def sub(self, a, b):
        return self.calculator.sub(a, b)

    def mul(self, a, b):
        return self.calculator.mul(a, b) if self.is_premium else "Denied."

    def div(self, a, b):
        return self.calculator.div(a, b) if self.is_premium else "Denied."

    def power(self, a, b):
        return self.calculator.power(a, b) if self.is_premium else "Denied."
