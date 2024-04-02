"""
    creating our first class
"""

# Class definition for a Student


class Student:
    # Initializer with private variables
    def __init__(self, first_name, last_name, studentID, year):
        self.__first_name = first_name  # Private variable for first name
        self.__last_name = last_name    # Private variable for last name
        self.__studentID = studentID    # Private variable for student ID
        self.__year = year              # Private variable for academic year

     # Method to get student's info as a formatted string
    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, ID: {self.__studentID}, Year: {self.__year}"

      # Getter for first_name
    def get_first_name(self):
        return self.__first_name

    # Getter for last_name
    def get_last_name(self):
        return self.__last_name

    # Getter for studentID
    def get_studentID(self):
        return self.__studentID

    # Getter for year
    def get_year(self):
        return self.__year

    # Setter for first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Setter for last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Setter for studentID
    def set_studentID(self, studentID):
        self.__studentID = studentID

    # Setter for year
    def set_year(self, year):
        self.__year = year


def main():
    student1 = Student("John", "Doe", "123456", "Sophomore")
    student2 = Student("Jane", "Smith", "789012", "Freshman")

    print("\n\n\n\n")
    print(student1.get_info())
    print(student2.get_info())
    print("\n\n\n\n")

    student2.set_first_name("Buffy")
    student2.set_last_name("Summers")
    student2.set_studentID("123666")
    print(student2.get_first_name())


main()
