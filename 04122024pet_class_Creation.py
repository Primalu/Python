
'''
    Create the Pet Class:
        Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
        Implement get and set methods for each of these attributes.
        Add a method called print_details that prints the details of the pet.
    Create Instances:

    Create three objects of the Pet class with different kinds, breeds, and names.

    Call the print_details method for each object that you created
    Demonstrate a Special Method or Function:

    Choose one of the following and demonstrate its use with the Pet class instances:
        __name__: Display the name of the class.
        type(): Show the class used to instantiate a pet object.
        __module__: Return the module name in which the Pet class is defined.
        __bases__: Display the base classes of the Pet class (if any).
        getattr(): Use it to access an attribute of a Pet instance.
        isinstance(): Check if an instance is of the Pet class.
'''


# Class definition for a Person


class Pet:
    # Initializer with private variables
    def __init__(self, kind, breed, name):
        self.__kind = kind                              # Private variable for name
        self.__breed = breed                        # Private variable for address
        self.__name = name                                # Private variable for age

    # Method to get student's info as a formatted string
    def get_info(self):
        return f"{self.__kind} {self.__breed}, {self.__name}"


    # Getters
    def get_name(self):
        return self.__kind

    def get_address(self):
        return self.__breed

    def get_age(self):
        return self.__name

    # Setters
    def set_name(self, kind):
        self.__kind = kind

    def set_address(self, breed):
        self.__breed = breed

    def set_age(self, name):
        self.__name = name


        # Setting Display function
    def print_details(self):
            print("Name:", self.__name)
            print("Type:", self.__kind)
            print("Breed:", self.__breed)


def main():
    #Instance #1
    Bella = Pet("Dog", "German Shepard", "Bella")
    print("\n")
    Bella.print_details()

    #Instance #2
    Kiwi = Pet("Cat", "Tortoiseshell", "Kiwi")
    print("\n")
    Kiwi.print_details()

    #Instance #3
    Ari = Pet("Bird", "Parakeet", "Ari")
    print("\n")
    Ari.print_details()

    print("\n\nClass name:", Pet.__name__)

main() # Calling main

