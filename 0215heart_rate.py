# Objective:
# Create a Python script to track heart rate readings taken at
# various times throughout the day and calculate the average heart rate.

# Requirements: Define Time Slots:
# Create a list named time_slots with different times of the
# day, such as "Morning", "Midday", "Afternoon", "Evening".

# User Input for Heart Rate:
# Use a loop to iterate over each time slot. For each time slot, 
# use the input() function to ask the user to enter their heart rate 
# (in beats per minute). Convert this input to an integer.

# Storing Heart Rate Data:
# Create an empty list named heart_rates. For each time slot, append a 
# sublist to heart_rates that contains the time slot and the corresponding heart rate.

# Calculate Average Heart Rate:
# Initialize a variable to keep track of the total heart rate. 
# Use a loop to add up the heart rate recorded at each time slot. 
# Calculate and print the average heart rate at the end.

# Sample Output:
# Enter your heart rate (in BPM) in the Morning: 70 Enter your heart rate (in BPM) at 
# Midday: 75 Enter your heart rate (in BPM) in the 
# Afternoon:  72 Enter your heart rate (in BPM) in the 
# Evening: 68 Average heart rate today: 71.25 BPM

# Defining Lists
test_times = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rate = []

# getting user imput
for time in test_times:
    bpm = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
    heart_rate.append([time, bpm])  

# Getting Avarage
total = 0
for hr in heart_rate:
    total += hr[1]
average = total / len(heart_rate)
# Printing Avg.
print(f"Your average BPM today is {average:.2f} BPM.")
