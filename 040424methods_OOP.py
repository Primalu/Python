
'''
    Class Creation: Design a class named Person that includes the following data: name, address, age, and phone number.
    Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
    Creating Instances: Write a program that creates three instances (objects) of the Person class.
    Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.
'''


# Class definition for a Person


class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone_number):
        self.__name = name                              # Private variable for name
        self.__address = address                        # Private variable for address
        self.__age = age                                # Private variable for age
        self.__phone_number = phone_number              # Private variable for phone number

    # Method to get student's info as a formatted string
    def get_info(self):
        return f"{self.__name} {self.__address}, Age: {self.__age}, +(1): {self.__phone_number}"



    # Getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

        # Setting Display function
    def display_person_info(self):
            print("Name:", self.__name)
            print("Adress:", self.__address)
            print("Age:", self.__age, "years old.")
            print("Phone Number: +(1)", self.__phone_number)

def main():
    #Instance #1
    alvin = Person("Alvin", "Hollywood", "9", "213-112-2291")
    print("\n")
    alvin.display_person_info()

    #Instance #2
    simon = Person("Simon", "1544 North St. Andrews Place in Hollywood", "8", "213-199-1315")
    print("\n")
    simon.display_person_info()

    #Instance #3
    theodore = Person("Theodore", "Dave's House", "7", "213-208-1741")
    print("\n")
    theodore.display_person_info()


main() # Calling main

#I know the chipmunks are triplets but, it felt wrong to have them all the same age.
