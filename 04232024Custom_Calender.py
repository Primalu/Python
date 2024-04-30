'''
Assignment Objectives:

    Ask the user to input their birthday.
    Calculate the user's age in years, months, days, hours, and minutes.
    Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
    Display the results in a user-friendly format.
    Implement the solution inside a main() function.

Instructions:

Create a Python script that performs the following steps:

    Define a main() function where your program logic will reside.
    Use my start program from GitHub: startprogram 

    Links to an external site.
    You can view the classroom demonstration of how we got to the code at the top of the page.
    Comment explaining each line of the code
        Finish the code to get and display:
            months
            weeks
            days (done)
            years (done)
    Format and print the results in a clear, understandable manner.

Tips:

    To calculate the age in years, you might need to consider leap years. A simple approach is to divide the total number of days by 365.25.
    For months, first calculate the years, then use the remaining days to estimate the months.
    For weeks, calculate by dividing days by 7
    Use try-except blocks to handle any potential input errors.
'''


    # Import important detail
from datetime import datetime

    # Definging main
def main():
    print("\n\n") # Make readable
    try:
        today = datetime.today() # Get today
        birth_year = int(input("What year were you born?  ")) # Getting User Born Year
        month = int(input("What Month were you born (as a number. May would be 5)  ")) # Getting User Born Month
        day = int(input("What day of the month were you born?  ")) # Getting User Born Day
        birthday = datetime(birth_year, month, day) # Mathin their (user) birthing
       
        print("Your birthday is: ") # Prefrace birthday print
        birthday_output = birthday.strftime("%Y-%m-%d") # Birthday custom info 
        print(birthday_output) # Birthday custom info print

        delta = today - birthday # delta = Gregorian year. Aka no leap year, a year is 365.2425 days
        print(f'Difference is {delta.days} days') # How old in days user is
        delta_years = delta.days // 365.2425 # Finding out how old user is in years
        print(f'You are {delta_years} years old\n\n') # Printing user age in years
      
        # Error handling
    except Exception as e:
        print(f"An Error has occurred:  {e}")  # Telling the user the error
        main() # Calling main

    # Calling Main
main()