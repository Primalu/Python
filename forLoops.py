# Python Assignment: Find Numbers Divisible by 7
# In this assignment, you will write a Python program to identify
# and print all the numbers divisible by 7 that fall between 1 and 300.
# This task will help you practice using loops and conditional statements in Python.

# Settup
for i in range(1, 300):# Setting up the cycle to to run though the numbers
    if i%7 != 0: # Cheching the divisabily of 7
        continue # Telling it to countiune 
    print(i) # Printing the numbers divisable by 7.