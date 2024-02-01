# Prewarning Print
print("\n\nWhen inputting please put everything as just numbers!")

# Getting user variables
house_budget = float(input("\nPlease enter your rent/mortgage budget: "))
utilities_budget = float(input("Please enter your utilities budget: "))
groceries_budget = float(input("Please enter your groceries budget: "))
transportation_budget = float(input("Please enter your transportation budget: "))
health_care_budget = float(input("Please enter your health care budget: "))
personal_care_budget = float(input("Please enter your personal care budget: "))
clothing_budget = float(input("Please enter your clothing budget: "))
debt_budget = float(input("Please enter your debt budget: "))

# Total Budget Math
total_budget = house_budget + utilities_budget + groceries_budget + transportation_budget + health_care_budget + personal_care_budget + clothing_budget + debt_budget
print(f"\nYour total budget is {total_budget:.2f}")

# Budget Percentage math ((value/total value)*100%)
house_budget_percentage = (house_budget/total_budget) * 100
utilities_budget_percentage = (utilities_budget/total_budget) * 100
groceries_budget_percentage = (groceries_budget/total_budget) * 100
transportation_budget_percentage = (transportation_budget/total_budget) * 100
health_care_budget_percentage = (health_care_budget/total_budget) * 100
personal_care_budget_percentage = (personal_care_budget/total_budget) * 100
clothing_budget_percentage = (clothing_budget/total_budget) * 100
debt_budget_percentage = (debt_budget/total_budget) * 100

# Printing persentage breakdowns
print(f"\nYour rent/mortgage takes up {house_budget_percentage:.2f}% of your budget")
print(f"Your utilities takes up {utilities_budget_percentage:.2f}% of your budget")
print(f"Your groceries takes up {groceries_budget_percentage:.2f}% of your budget")
print(f"Your transportation takes up {transportation_budget_percentage:.2f}% of your budget")
print(f"Your health care takes up {health_care_budget_percentage:.2f}% of your budget")
print(f"Your personal care takes up {personal_care_budget_percentage:.2f}% of your budget")
print(f"Your clothing takes up {clothing_budget_percentage:.2f}% of your budget")
print(f"Your debt takes up {debt_budget_percentage:.2f}% of your budget")
