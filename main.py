from calculator import Calculator
from free_calculator import FreeCalculator
from input_templates import AgeInput, EmailInput

if __name__ == "__main__":
    full_calc = Calculator()
    free_calc = FreeCalculator(full_calc)

    print("Free Calculator Addition: 5 + 3 =", free_calc.add(5, 3))
    print("Free Calculator Subtraction: 10 - 4 =", free_calc.sub(10, 4))
    try:
        free_calc.mul(2, 3)
    except Exception as e:
        print("Free Calculator Multiplication:", e)

    age_input = AgeInput()
    age = age_input.get_input()
    print("Your age is:", age)

    email_input = EmailInput()
    email = email_input.get_input()
    print("Your email address is:", email)
