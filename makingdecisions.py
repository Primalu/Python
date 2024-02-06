# To do: Drive, Vote, alcohol, senior discount (65)

#Obtaing user age
age = float(input("\nPlease enter how old you where at your last birthday: "))

#If Driving
if age >= 16:
    print("\nYou are old enough to drive.")
else:
    print("You are not old enough to drive.")

# If Voting
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# If Alcohol
if age >= 21:
    print("You can buy alcohol legally.")
else:
    print("You cannot buy alcohol legally.")

# If Senior
if age >= 65:
    print("You are eligible for the senior discount.")
else:
    print("You are not eligible for the senior discount.")
