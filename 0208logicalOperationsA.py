# In this exercise, you will practice using logical operators (and, or, not) in Python. 
# Your task is to create a program that prompts the user for two integer inputs and 
# then demonstrates the use of these operators.

# Obtaing the numbers
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Commands / Checks
# and Statemnt #1
if num1 > 0 and num2 > 0:
    print("Both numbers are greater than 0: True")
elif num1 < 0 or num2 < 0:
    print("Both numbers are greater than 0: False")
# and Statemnt #2
if num1 > 100 and num2 > 100:
    print("Both numbers are greater than 100: True")
elif num1 < 100 or num2 < 100:
    print("Both numbers are greater than 100: False")

# or Statement #1
if num1 % 2 == 0 or num2 % 2 == 0:
    print("Either number is even?: True")
elif num1 % 2 != 0 or num2 % 2 != 0:
    print("Either number is even?: False")
# or statemnt #2
if num1 < 100 or num2 < 100:
    print("Either number is less than 100?: True")
elif num1 > 100 or num2 > 100:
    print("Either number is less than 100?: False")


# not statemnt #1
if not num1 == num2:
    print("num1 is not equal to num2: True")
else:
    print("num1 is not equal to num2: Flase")
# not Statment #2
if not num1 == 0:
    print("num1 is not 0: True")
else:
    print("num1 is not 0: False")
