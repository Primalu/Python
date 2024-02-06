# To do: Accept a numeric grade from the user and display a letter grade.
# The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

# User inputs
grade = int(input("\nEnter the numeric grade: "))

# Setting Letter Grade Var.
letter_grade = "I"

# Convering to letter grade
if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
elif grade < 60:
    letter_grade = "F"
else:
    letter_grade = "Invalid Input" # Fail safe attempt, I don't know how you'd break it but.

# Print statment
print("The letter grade is:", letter_grade,"\n")
