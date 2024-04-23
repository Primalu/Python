'''
    Set Up Your Python Environment: Create a diary folder for this assignment, you will upload the whole file to GitHub when you are done. 
    Create a New Python File: Name this file personal_diary.py.
    Writing the Code:
        Create this in a main function
        Prompt the user to enter the current date and time, then a diary entry.
        Open or create a file named diary.txt in append mode using open(). ( use append not write)
        Write the user-provided date, time, and diary entry into the file. Ensure each entry is separated from the others by writing a blank line after entering the date/time line and the entry line. 
        Close the file using the close() method.
    Comments and Documentation: Add comments to your code explaining its functionality.
    Testing the Program: Run personal_diary.py three times, each time entering a different diary entry along with the date and time. Check diary.txt to ensure entries are recorded correctly.
    Submission: Submit both your personal_diary.py file and the diary.txt file containing your entries. 
'''
    #Opening the file
def open_file():
    try:
        # Open the file in read mode
        directory = open('diary.txt', 'r')
        # we can read and write (append)
        content = directory.read()
        print(content)
        directory.close()  # Always close the file
        return (content)
    except FileNotFoundError: # Unable to locate file
        print("File not found.")

    except IOError: # Creating new file
        print("We created this file for you, it did not exist or was empty.")

    except Exception as e: # Other error
        print("An error occurred:", e)

def add_values():
    date = input("What is today's date: ")                  # Getting User Date
    time = input("Whats the curent time? ")                 # Gettubg User Time
    diary_entry = input("Please enter you diary entry: ")   # Getting User Entry
    entry = date + ", " + time + ", " + diary_entry + "\n"  # User-friendly-ifiying
    record = open('diary.txt', 'a')                         # Open File
    record.append(entry)                                    # Add to file
    record.close()                                          # Close File


def main(): 
    values = open_file() # Open file
    print(f"The contents of the file are: {values}") # Showing contwnts of file
    add_values() # Adding to file


main()