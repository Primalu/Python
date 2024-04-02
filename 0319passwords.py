'''
Set up your program in a main() function
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.
'''


def main():
    while True:
        print("""\nPassword Requirements:
                Between 8 to 20 characters long.
                Contains at least one uppercase letter.
                Contains at least one lowercase letter.
                Includes at least one number.
                Includes at least one symbol from the set: !@#$%&*\n""")

        valid = False  # change to true if all conditions are met
        while not valid:
            valid = True  # we will change to false if ANY requirement not met

            # Checking Password Length
            password = input("Please enter a valid password: ")
            length = len(password)
            if not (8 <= length <= 20):
                print("Please make sure your password is between 8 to 20 characters long")
                valid = False
                continue

            # Checking Password Uppercase
            has_upper = False # Change to true if found
            for char in password:
                if char.isupper():
                    has_upper = True
                    break
            if not has_upper:
                print("Please make sure your password contains at least one uppercase letter")
                valid = False
                continue

            # Checking Password Lowercase
            has_lower = False
            for char in password:
                if char.islower():
                    has_lower = True
                    break
            if not has_lower:
                print("Please make sure your password contains at least one lowercase letter")
                valid = False
                continue

            # Checking Password Number
            has_num = False
            for char in password:
                if char.isnumeric():
                    has_num = True
                    break
            if not has_num:
                print("Please make sure your password includes at least one number")
                valid = False
                continue

            # Checking Password Symbol. Was having issues so I had IRL help with this section
            has_symbol = False
            symbols = set('!@#$%&*')
            for char in password:
                if char in symbols:
                    has_symbol = True
                    break
            if not has_symbol:
                print("Please make sure your password includes at least one symbol from the set: !@#$%&*")
                valid = False

        # Prompting the user to re-enter the password for confirmation
        while True:
            try:
                confirm_password = input("Please re-enter your password for confirmation: ")
                if confirm_password == password:
                    print("Password successfully confirmed!")
                    break
                else:
                    print("Passwords do not match. Please start over again.")
                    valid = False  # Resetting valid to False to start the user over agan
                    break
            except:
                print("An unexpected error has occurred") # Imma be honest, I dont know what error youd run into in this program.
                continue
        break

main()
