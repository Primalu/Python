'''
    Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
    Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
    Ensure proper capitalization: Use the title function to make sure the first letter is capitalized before storing into the list.
    Create a Sorted List: Once all titles are collected, save them to a new list named sorted. This list should contain the titles in alphabetical order.
    Display the Titles: Use a for loop to print each title from the sorted list on a separate line.
    Test Your Program: Ensure that your program runs correctly and meets all the requirements.
    Upload to GitHub: Once tested, upload your program to GitHub.
    Submit Your Work: Submit the link to your GitHub repository on Canvas.
'''

def main():    
    user_book_list = [] # Setting up list var
    print("We'll be asking for 10 different book titles one at a time, then sorting them alphabetically.") # Background info for user
    while len(user_book_list) != 10: # Looping 10 times for every book title
        book_title = input("Please enter a book title: ") # Get user input
        user_book_list.append(book_title.title())  # Capitalize the first letter of each word and append to list
    sorted_book_list = sorted(user_book_list)  # Sort the list alphabetically
    print("Your list of books in alphabetical order is: ") # Setting up the coming list
    for title in sorted_book_list: # Looping for every title
        print(title) # Printing each title

main() # Calling the whole program