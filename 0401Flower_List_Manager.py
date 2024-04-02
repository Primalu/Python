'''
    Create a Main Function: Encapsulate your program within a main() function.
    User Input for Flower List: Prompt the user to enter names of flowers and store them in a list. Have them enter the word "done" when done, and check for it.
    Sorting and Searching: Sort the list, print on screen with a number next to the flower name, and allow the user to search for a specific flower. Print a message if the flower is found.
    Accessing a Specific Flower: Ask the user for a number to access the corresponding flower. Handle errors for invalid inputs. (Note, our printout starts at 1, list indexes start at 0, adjust accordingly.
    Exception Handling: Use try and except statements for ValueError and IndexError, and include a generic except statement.
    Upload to GitHub: Upload your completed script to your GitHub repository.
    Submission: Submit the GitHub repository link containing your script.
'''

def main():
    try:
        flower_list = []
        print("Please enter the names of flowers that you like. When done, please type 'done'.")

        # Obtaining user flowers
        while True:
            flower = input("Please enter a flower name: ")
            if flower == 'done':
                break
            else:
                flower_list.append(flower.title())

        # Sorting and Printing the Flower list
        flower_list = sorted(flower_list)  # Sort the list
        print("\nList of flowers entered:")
        for flowers in flower_list:  # Print on screen with a number next to the flower name 
            index = flower_list.index(flowers) + 1
            print(f"{index}. {flowers}")

        # Flower search, verbal
        search_flower = input("\nPlease enter the name of the flower you want to search for: ").title() #Putting everthing into title to make it eaiser to work with
        if search_flower in flower_list:
            print(f"The flower '{search_flower.title()}' is found in the list.")
        else:
            print(f"The flower '{search_flower.title()}' is not found in the list.")

        # Flower search, numarical
        flower_index = int(input("\nPlease enter the number corresponding to the flower you want to access: ")) # I expect most of the errors will arise from here
        if 1 <= flower_index <= len(flower_list):
            print(f"You've selected '{flower_list[flower_index - 1]}'.")
        else:
            print("Invalid input. Please enter a number within the range of the list.")


    # Error Handlings
    except ValueError:
        print("A ValueError occurred.")

    except IndexError:
        print("An IndexError occurred.")

    except Exception:
        print("An unexpected error has occurred.")


main() # Calling best boi main
