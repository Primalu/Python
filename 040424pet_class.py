class Student:
    # Class variable
    school_name = "McHenry County College"

    def __init__(pets, owner_first_name, owner_last_name, pet_id, pet_name, pet_type):
        pets.__owner_first_name = owner_first_name
        pets.__owner_last_name = owner_last_name
        pets.__pet_id = pet_id
        pets.__pet_name = pet_name
        pets.__pet_type = pet_type

    # Getter and Setter for owner_first_name
    def get_owner_first_name(pets):
        return pets.__owner_first_name
    
    def get_owner_last_name(pets):
        return pets.__owner_last_name
        
    def get_pet_id(pets):
        return pets.__pet_id
    
    def get_pet_name(pets):
        return pets.__pet_name

    def get_pet_type(pets):
        return pets.__pet_type

    def set_first_name(pets, value):
        pets.__owner_first_name = value
    
    def set_owner_last_name(pets, value):
        pets.__owner_last_name = value

    def set_pet_id(pets, value):
        pets.__pet_id = value
    
    def set_pet_name(pets, value):
        pets.__pet_name = value

    def set_pet_type(pets, value):
        pets.__pet_type = value


    # Similarly, create getters and setters for last_name, pet_id, pet_name and pet_type

    def print_student_details(pets):
        print("Student Details:", vars(pets))
    
    def print_info(pets):
        print(pets.__owner_first_name + " " + pets.__owner_last_name)
        print(pets.__pet_id)
        print(pets.__pet_name)
    




def main():
    ducktor_quacks = Student("Meri", "Quacksalot", '009234', "Super Senior")
    print("\n\n\n")
    print(ducktor_quacks.get_first_name())
    print(ducktor_quacks.print_student_details())
    print(ducktor_quacks.print_info())

    print("\n\n\n")
    ducktor_quacks.set_pet_name("Ducktorate")
    print(ducktor_quacks.print_info())



main()