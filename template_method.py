class TemplateMethod:
    """Handles input validation using the Template Method pattern."""

    @staticmethod
    def get_valid_integer():
        """Receives an integer input between 1 and 100, ensuring it is valid."""
        while True:
            print("Enter your age:")
            user_input = input().strip()

            if not user_input.isdigit():
                print("Error: Input must be a number.")
                continue

            try:
                num = int(user_input)
                if 1 <= num <= 100:
                    return num
                else:
                    print("Error: Number must be between 1 and 100.")
            except ValueError:
                print("Error: Invalid number format.")

    @staticmethod
    def get_valid_email():
        """Receives a valid email input, ensuring it includes '@' with text before and after."""
        while True:
            print("Enter your email:")
            email = input().strip()

            if "@" not in email or email.startswith("@") or email.endswith("@"):
                print("Error: Email must contain '@' with text before and after.")
                continue

            return email
