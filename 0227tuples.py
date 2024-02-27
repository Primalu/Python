'''
creating and useing a tuple
'''

def main(): # Using a tuple to display class programming class information
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    for classes in programming_classes:
        print(classes, end = " ")

    print(f"\nThere are : {len(programming_classes)} programming classes you can take at MCC!")

main()