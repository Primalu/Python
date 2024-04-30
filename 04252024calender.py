'''
Requirements

        Your program must be contained within a main() function.
        Use the Python input() function to ask the user for their birth month (as an integer).
        Ensure your program can handle invalid inputs gracefully.
        Use Python's datetime module to find the current year.
        Generate and display the calendar for the user's birth month in the current year.
        Format the calendar output so it is easy to read and understand.

 Steps

        Start by importing the necessary modules: calendar and datetime.
        Create a main() function where your program's logic will reside.
        Inside main(), get the current year using datetime.datetime.now().year.
        Ask the user to enter their birth month and store it in a variable.
        Validate the user input to ensure it's an integer between 1 and 12.
        Use the Calendar module to generate the calendar for the given month and year.
        Print the calendar to the console in a readable format.
        Don't forget to call the main() function at the end of your script.
 
Tips and Hints

    Remember to handle cases where the user input might be invalid. For example, if the user inputs a string or a number outside the 1-12 range, your program should handle these gracefully.
    To align dates under the correct day of the week, use the calendar.month() function from the Calendar module.
    Keep your code organized and comments to make it easy to understand.
    Test your program with different inputs to ensure it's robust and handles all scenarios.
'''


# Start by importing the necessary modules: calendar and datetime
from datetime import datetime
import  calendar


def main(): # Create a main() function where your program's logic will reside.
    print("\n\n")
    try:
            # Inside main(), get the current year using datetime.datetime.now().year.
        curent_year = datetime.now().year 
            # Ask the user to enter their birth month and store it in a variable.
        birth_month = int(input("What Month were you born (as a number. May would be 5):  "))
            # Validate the user input to ensure it's an integer between 1 and 12.
        if not 1 <= birth_month <= 12:
            print("Enter a correct month!")
            main()
            # Use the Calendar module to generate the calendar for the given month and year.
        cal = calendar.TextCalendar(calendar.SUNDAY)
            # Print the calendar to the console in a readable format.
        print(f"{cal.formatmonth(curent_year, birth_month)}")
        
        

       
      
    except Exception as e:
        print(f"An Error has occurred:  {e}") 
        main()

# Don't forget to call the main() function at the end of your script.
main()
