from abc import ABC, abstractmethod

class InputTemplate(ABC):
    def get_input(self):
        while True:
            user_input = input(self.prompt_message())
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue
            try:
                value = self.convert_input(user_input)
            except ValueError:
                print("Invalid input format. Please try again.")
                continue
            if not self.validate(value):
                print("Input does not meet the requirements. Please try again.")
                continue
            return value

    @abstractmethod
    def prompt_message(self):
        """Return the message to prompt the user."""
        pass

    @abstractmethod
    def convert_input(self, user_input):
        """Convert the input from a string to the desired type."""
        pass

    @abstractmethod
    def validate(self, value):
        """Validate the converted input."""
        pass

class AgeInput(InputTemplate):
    def prompt_message(self):
        return "Enter your age (1-100): "

    def convert_input(self, user_input):
        return int(user_input)

    def validate(self, value):
        return 1 <= value <= 100

class EmailInput(InputTemplate):
    def prompt_message(self):
        return "Enter your email address: "

    def convert_input(self, user_input):
        return user_input.strip()

    def validate(self, value):
        parts = value.split('@')
        return len(parts) == 2 and all(parts)
