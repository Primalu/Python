'''
        Implement a custom exception class NotNumericError.
        Write a Python script that prompts the user to input a number.
        Use a try-except-else-finally block:
            The try block should contain the logic to check if the input is a number. (isnumeric() )
            The except block should catch the InvalidInputError and print an error message.
            The else block should print a confirmation message if the input is valid.
            The finally block should print a message indicating the end of the program's execution.
        Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered. (call the program again)
'''

# Error class InvalidInputError
class InvalidInputError(Exception):
    def __init__(self, message="Please make sure the number you enter is LESS than 10."):
        self.message = message
        super().__init__(self.message)

    # Error Message
    def __str__(self):
        return f'{self.message}'

# Error class NotNumericError
class NotNumericError(Exception):
    def __init__(self, message="Please make sure you enter a NUMBER that is less than 10."):
        self.message = message
        super().__init__(self.message)

    # Error Message
    def __str__(self):
        return f'{self.message}'


def main():
    try:
        # goal - create a custom error for if you get a float when you want an int
        while True:
            value = input("Please enter a number from 0 to 9: ")

            # Error Handling
            if not value.isnumeric():
                raise NotNumericError()

            value = int(value)

            if value > 9:
                raise InvalidInputError()

            print(f"Thank you, you entered {value}.")  # Correct Value
            break  # Exit the loop if input is valid

    except NotNumericError as e:
        print(f"error: {e}")
        main()  # Calling Main
    except InvalidInputError as e:
        print(f"error: {e}")
        main()  # Calling Main
    except Exception as e:
        print(f"The exception is: {e}")
        print("Please enter an integer between 0 and 9")
        main()  # Calling Main
    finally:
        print("Wonderfull!!!")


# Calling Main
main()
