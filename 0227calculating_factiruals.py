'''
Your task is to write a Python program using a recursive function to calculate the factorial
of a number. A recursive function is a function that calls itself to solve a problem.

Start by defining a function named factorial that takes one parameter,
n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case. The base case for
our recursion will be when n is 1 or 0, because the factorial of 1 and 0 is 1.
For the recursive step, if n is greater than 1, the function should 
return n multiplied by a call to itself with n-1.
Create a main function. Inside this function, prompt the user to enter 
a non-negative integer. Use the int() function to convert the input to an integer.
Call the factorial function from your main function with the user's input as its 
argument, and print the result in a format like "The factorial of n is result.".
Finally, call your main function to run the program.
Upload to GitHub and submit your link to hand in the progam
'''

# Does factorial caululations
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else: 
        return n * factorial(n - 1)

# Getting userinput and displaying output, calls factorial
def main():
    user_Input = int(input("Please enter a non-negative integer: "))
    result = factorial(user_Input)
    print(f"The factorial of {user_Input} is {result}")

# Calling main
main()