# In this assignment, you will write a Python program that accomplishes the following tasks:
# Accept five names from the user.
# Store these names in a list.
# Sort the list using the Bubble Sort algorithm. 
# Finally, reverse the sorted list using a Python list method. 

# Requirements:
# Your program should prompt the user to enter five names.
# Use a loop to accept each name and append it to a list.
# Implement the Bubble Sort algorithm to sort the list of names in ascending order.
# Print the sorted list.
# After sorting, use a Python list method to reverse the order of the list.
# Print the final reversed list to the console.

# Informing user
print("\nI'm going to ask you for five names one at a time!")

# Initialize a list of names
names = []

# Obtaing names and putting them into the list
for i in range(0, 5):
    name = input("\nPlease enter a nane: ")
    names.append (name)
    continue

# Flag to track if a swap has occurred
swapped = True

# make all names lower case

for i in range (0,len(names)):
    names[i] = names[i].lower()

print(names)

# Continue looping until no swaps occur
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print(names)

# Reverse the list
names.reverse()

# Print the reversed list
print(names)