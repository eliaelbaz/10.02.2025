from proxy_calculator import ProxyCalculator
from template_method import TemplateMethod

if __name__ == "__main__":
    print("=== Free User ===")
    free_calc = ProxyCalculator(is_premium=False)
    print("Addition:", free_calc.add(5, 3))
    print("Subtraction:", free_calc.sub(10, 4))
    print("Multiplication:", free_calc.mul(5, 3))
    print("Division:", free_calc.div(10, 2))
    print("Power:", free_calc.power(2, 3))

    print("\n=== Premium User ===")
    premium_calc = ProxyCalculator(is_premium=True)
    print("Addition:", premium_calc.add(5, 3))
    print("Multiplication:", premium_calc.mul(5, 3))
    print("Division:", premium_calc.div(10, 2))
    print("Power:", premium_calc.power(2, 3))

    print("\n=== Input Validation ===")

    while True:
        user_number = TemplateMethod.get_valid_integer()
        print("Valid number:", user_number)
        break

    while True:
        user_email = TemplateMethod.get_valid_email()
        print("Valid email:", user_email)
        break

    print("\nProcess completed successfully.")
