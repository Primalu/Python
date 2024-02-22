'''
    The function should be named calculate_interest.
    It should take three parameters:
principal - The principal amount (the initial sum of money).
rate - The rate of interest (as a percentage).
time - The time the money is invested or borrowed for, in years.
Get the information from the customer, then call the function and pass the information in. 
The function should calculate the simple interest using the given formula and return the result.
'''


def calculate_interest():
    principal_amount, interest_rate, time = get_user_imputs()
    calculated_interest = (principal_amount * interest_rate * time) / 100
    print(f"The simple interest for a principal amount of ${principal_amount:,.2f} at an \ninterest rate of {interest_rate}% over a period of {time} years is: ${calculated_interest:,.2f}")


# Getting user imputs
def get_user_imputs():
    principal_amount = int(input("Enter the principal amount: "))
    interest_rate = int(input("Enter the interest rate as a whole number (5% would be 5): "))
    time = int(input("Enter the investment time in whole years: "))
    return principal_amount, interest_rate, time

# Calling intrest rate
calculate_interest()