
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area of the rectangle is {area:.2f}")

# Prewarning Print
print("When inputting please put everything as just numbers")

# Getting user variables
house_budget = float(input("Enter your rent/mortgage budget: "))
utilities_budget = float(input("Enter your utilities budget: "))
groceries_budget = float(input("Enter your groceries budget: "))
transportation_budget = float(input("Enter your transportation budget: "))
health_care_budget = float(input("Enter your health care budget: "))
personal_care_budget = float(input("Enter your personal care budget: "))
clothing_budget = float(input("Enter your clothing budget: "))
debt_budget = float(input("Enter your debt budget: "))

# Total Budget Math
total_budget = house_budget + utilities_budget + groceries_budget + transportation_budget + health_care_budget + personal_care_budget + clothing_budget + debt_budget
print(total_budget)