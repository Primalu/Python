# Defining Vars
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps= []

# Obtaing steps
total = 0
for day in week:
    day_steps = int(input(f"How many steps did you take on {day}:  "))
    steps.append(day_steps)
    total += day_steps

# Setting up results
index = 0
print("\n")

# Printing Days
for day in week:
    print(f"On {day} you took {steps[index]} steps")
    index += 1

# Printing Avg and Total
average = total / len(steps)
print(f"\nYou took a total of {total} steps")
print(f"You walked an average of {average:.1f} steps per day.")
