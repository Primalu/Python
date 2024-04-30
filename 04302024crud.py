"""
    CRUD application for creating an address book.
    This will have some problems in it. you may solve the problems 
    for extra credit:
    Does not allow for duplicate names to be properly handled
    Search searches the entire entry not a specific field


    🚨 Avoid project creep!


"""


def main_menu():
    # present menu
    # Check values 
    # return choice
    try:
        print("\nMain Menu - Customer Directory")
        print("1. Create new entry")
        print("2. Read and display by name")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Quit")
        choice = int(input("Please enter the number of your selection: "))
        if choice < 0 or choice > 5:
            print("That is out of range, please try again.")
            main_menu()
        else:
            return choice
    except ValueError:
        print("That is not a valid number. Please try again.")
        main_menu()
    except Exception as e:
        print(f"main_menu: {e}")

def check():
    # read file to list
    # if file not there create empty customer list
    # return customer list
    try:
        file = open("customer_directory.txt", "r")
        customer = file.readlines()
        for line in customer:
            print(line) # This was for test purposes!
        file.close()
        return customer
    except FileNotFoundError:
        print("That file does not exist. \n We will create a new file for you!")
        customer = []
        return customer
    except Exception as e:
        print(f"Check: {e}")
    

def save():
    # save the file
    print("Save")
    main()

def create():
    # create a new entry
    # call the save  function
    try:
        customer = check()
        print("\n Please enter the customer information: ")
        first_name = input("First name: ")
        last_name = input("Last Name: ")
        phone = input("Phone number: ")
        email = input("Email address: ")
        entry = {f"{first_name}, {last_name}, {phone}, {email}\n"}
        customer.append(entry)
        for line in customer:
            print(line)
    except Exception as e:
        print(f"Create: {e}")
    main()

def read():
    # will call the search function
    # will display the found record
    print("read")
    main()

def search():
    # called by - read, update, delete
    # returns - record, index
    print("Search")

def update():
    # updates a record
    # uses search function
    print("Update")
    main()

def delete():
    # calls search
    # verifies that it is the record to delete
    # deletes the record
    print("delete")
    main()



def main():
    choice = main_menu()
    try:
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            print("Goodbye!\n")
    except Exception as e:
        print(f"Main: {e}")

main()