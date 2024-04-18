'''
Set Up Your Python Environment: Create a diary folder for this assignment, you will upload the whole file to GitHub when you are done. 
Create a New Python File: Name this file personal_diary.py.
Writing the Code:
Create this in a main function
Prompt the user to enter the current date and time, then a diary entry.
Open or create a file named diary.txt in append mode using open().
Write the user-provided date, time, and diary entry into the file. Ensure each entry is separated from the others by writing a blank line after entering the date/time line and the entry line. 
Close the file using the close() method.
Comments and Documentation: Add comments to your code explaining its functionality.
Testing the Program: Run personal_diary.py three times, each time entering a different diary entry along with the date and time. Check diary.txt to ensure entries are recorded correctly.
Submission: Submit both your personal_diary.py file and the diary.txt file containing your entries. 
'''

'''
    Track mileage for work
    Calculate reimbursement based on mileage_rate
    store in external file

'''


milage_rate = .52


def open_file():
    try:
        # Open the file in read mode
        directory = open('mileage.txt', 'r')
        # we can read and write (append)
        content = directory.read()
        print(content)
        directory.close()  # Always close the file
        return (content)
    except FileNotFoundError:
        print("File not found.")

    except IOError:
        print("We created this file for you, it did not exist or was empty.")

    except Exception as e:
        print("An error occurred:", e)


def add_values(my_values):
    date = input("What is today's date: ")
    destination = input("Where did you go? ")
    total_miles = input("What were the total miles for this trip? ")
    entry = date + ", " + destination + ", " + total_miles + "\n"
    record = open('mileage.txt', 'a')
    record.write(entry)
    record.close()


def main():
    # Trying to open a file and handle exceptions
    values = open_file()
    print(f"The contents of the file are: {values}")
    add_values(values)


main()
