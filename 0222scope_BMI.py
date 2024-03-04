'''
Create a BMI calculator that takes a user's weight and height, calculates their BMI, 
and then categorizes their BMI into underweight, normal weight, overweight, or obese.

'''

# Defining global vars
WEIGHT = None
HEIGHT = None

# bmi function
def bmi_finding(WEIGHT, HEIGHT):
    WeightKG = WEIGHT * 0.453592
    HeightM = HEIGHT * 0.0254
    BMI = WeightKG / (HeightM * HeightM)
    print(f"Your BMI is: {BMI:.2f}")
    if BMI < 18.5:
        print("You are in the underweight category.")
    elif BMI < 24.9:
        print("You are in the normal weight category.")
    elif BMI < 29.9:
        print("You are in the overweight category.")
    else:
        print("You are in the obese category.")

# Error checking function
def error_checking():
    global WEIGHT, HEIGHT
    WEIGHT = input("Please enter your weight in pounds: ")
    HEIGHT = input("Please enter your height in inches: ")

    while not (WEIGHT.isnumeric() and HEIGHT.isnumeric()): # User only needs to reenter what was incorrect
        if not WEIGHT.isnumeric():
            print("Please make sure you are only using numbers for your weight (e.g '154')")
            WEIGHT = input("Please reenter your weight in pounds: ")
        if not HEIGHT.isnumeric():
            print("Please make sure you are only using numbers for your height (e.g '68')")
            HEIGHT = input("Please reenter your height in inches: ")

    bmi_finding(int(WEIGHT), int(HEIGHT)) 

# Starting the function, "Main"
error_checking()


'''
I found use of the gobal funtion from W3 Schools
https://www.w3schools.com/python/python_variables_global.asp
'''
