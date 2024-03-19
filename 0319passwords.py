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
    valid = False  # change to true if all condions are met
    while not valid:
        valid = True  # we will change to false if ANY requirement not met
        print("""Password Requirements:\n
            Between 8 to 20 characters long.\n
            Contains at least one uppercase letter.\n
            Contains at least one lowercase letter.\n
            Includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*\n""")

        password = input("Please enter a valid password: ")
        length = len(password)
        if 8 <= length <= 20:
            continue
        else:
            valid = False
            print("Please make sure your password is beween 8 to 20 characters long")

        is_upper = False  # change to true if found
        # for loop stepping through characters in password. Look for an upper case.

        has_symbol = False
        symbol = ['!', '@', '#']
        for s in symbol:
            for c in password:
                if s == c:
                    has_symbol == True
        if has_symbol == False:
            print("Please make sure your password includes at least one symbol from the set: !@#$%&*")
            valid = False
            continue
        


main()
