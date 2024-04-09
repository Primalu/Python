
'''
        Define a Pet Class:
            Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
            Set a default value for pet_type as "Dog".
            Implement getter and setter methods for all properties.
            Include a class variable vet_name set to the name of your veterinary office.
            Add a method display_pet_info to print all details of the pet and owner.
        Create Pet Objects:
            Instantiate at least three pet objects with different details.
            Show the use of setter methods for at least one pet object.
        Implement Property Existence Check:
            Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
        Display Information:
            Use display_pet_info to print details for each pet.
            Show examples of check_property being used on various properties and pets.
'''

 # Class aka. Pattern
class Animals:
    # Class variable
    vet_office_name = "McHenry County Vet"
    vet_name = "Dr. Flutter"

        #Innit
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
        self.__pet_type = pet_type

        # Getter
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name

    def get_pet_type(self):
        return self.__pet_type

        #Getters
    def set_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # Function
    def display_pet_info(self):
        print("Owner:", self.__owner_first_name, self.__owner_last_name)
        print("Pet ID:", self.__pet_id)
        print("Pet Name:", self.__pet_name)
        print("Pet Type:", self.__pet_type)
        print("Veterinary:", Animals.vet_name)

# Checkin property (function name says it all really)
def check_property(pet, properties): # spelled dumb beacuse property is a base function and dont want conflicts
    if hasattr(pet, properties):
        print(f"The property '{properties}' exists in the pet's profile!")
    else:
        print(f"The property '{properties}' does not exist in the pet's profile.") # Period to display passive aggressiveism 

# Main function, also hold on animals details
def main():
    # Pet #1
    grahm_cracker = Animals("Grahm", "Cracker", '009234', "Grahm Jr.")
    print("\n\n")
    grahm_cracker.display_pet_info()
    check_property(grahm_cracker, "get_owner_last_name")
    check_property(grahm_cracker, "get_is_fixed")

    # Pet #2
    mc_fluffy = Animals("Margret", "Petsolot", '539024', "McFluffy Buttoms The Third", "Cat")
    print("\n\n")
    mc_fluffy.display_pet_info()
    check_property(mc_fluffy, "get_pet_id")
    check_property(mc_fluffy, "get_is_declawed") #Never declaw cats

    # Pet #3
    floofster = Animals("Andrew", "Alxel", '834751', "Floofster")
    print("\n\n")
    floofster.display_pet_info()
    check_property(floofster, "get_pet_type")
    check_property(floofster, "get_can_play_guitar")


main()

'''
Fun fact Meri, wanna know why guys have more unified sizing than girls? (feels relvent to this assinment)

War! No really, needed better sizing to mass produce for milltary uniform for our soldiers.
'''
