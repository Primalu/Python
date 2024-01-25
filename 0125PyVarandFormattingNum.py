# Defining Variables
kg_val_1 = 2
kg_val_2 = 23
kg_val_3 = 59
kg_val_4 = 82
kg_val_5 = 28

# Conversion factor lb = kg * 2.20462
conversion_factor = 2.20462

# Calulations
lbs_val_1 = kg_val_1 / conversion_factor
lbs_val_2 = kg_val_2 / conversion_factor
lbs_val_3 = kg_val_3 / conversion_factor
lbs_val_4 = kg_val_4 / conversion_factor
lbs_val_5 = kg_val_5 / conversion_factor

# Output results
print(f"{kg_val_1} kilograms is equal to {lbs_val_1:.2f} pounds.")
print(f"{kg_val_2} kilograms is equal to {lbs_val_2:.2f} pounds.")
print(f"{kg_val_3} kilograms is equal to {lbs_val_3:.2f} pounds.")
print(f"{kg_val_4} kilograms is equal to {lbs_val_4:.2f} pounds.")
print(f"{kg_val_5} kilograms is equal to {lbs_val_5:.2f} pounds.")
