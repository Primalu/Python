'''
Create a BMI calculator that takes a user's weight and height, calculates their BMI, 
and then categorizes their BMI into underweight, normal weight, overweight, or obese.

'''

WEIGHT = int(input("Please enter your weight in pounds (in pound): "))
HEIGHT = int(input("Please enter your height in inches (in inches): "))

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
