
# Getting the number they have to guess
import random

"""
    Working with modules, random and math
"""

# Defining main
def main():
    random_number = random.randint(1, 100) # Getting num
    while True:
        try: 
             guess = int(input("Guess a number between 1 and 100: "))
        except ValueError: # Error checking
            print("Please enter a valid number.")
            continue

        difference = abs(random_number - guess) # Setting a difference var to make the guessing easier
        if guess == random_number: # Correct Guess
            print(f"You did it! Your guess of {guess} was Correct!")
            break # Ending game, they guessed correctly after all
        elif difference <= 5: # Very close guess
            print(f"Your guess of {guess} is Very hot! (Very close)")
        elif difference <= 15: # Close guess
            print(f"Your guess of {guess} is Hot! (Close)")
        elif difference <= 25: # Far guess
            print(f"Your guess of {guess} is Cool (Far away)")
        elif difference > 25: # Very far guess
            print(f"Your guess of {guess} is Cold (Very far away)")

# Calling Main function
main()