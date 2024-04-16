
'''
Assignment Part 1: Defining Classes

File 1: Write an Employee class with the following attributes:
        Employee name
        Employee number

Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

        Shift number (integer: 1 for day, 2 for night)
        Hourly pay rate

Implement accessor and mutator methods (getters and setters) for each class.
Assignment Part 2: Implementing and Testing

Part 2: Write a script to:

        Create an instance of ProductionWorker.
        Prompt the user for each attribute's data.
        Store and then display the data using the object's methods.
'''


# Class definition for a Employee

class Employee:
        # Defing stats
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

        # Getters
    def get_employee_name(self):
        return self.employee_name
    
    def get_employee_number(self):
        return self.employee_number

        # Setters
    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number


# Class definition for a Production

class ProductionWorker(Employee):
        # Defing stats
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(employee_name, employee_number)
        self.shift_number = int(shift_number)
        self.hourly_pay_rate = hourly_pay_rate

        # Convert the shift number to day/night
        if self.shift_number == 1:
            self.shift = "day"
        elif self.shift_number == 2:
            self.shift = "night"
        else:
            self.shift = "unknown"

        # Getters
    def get_shift(self):
        return self.shift

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

        # Setters
    def set_shift_number(self, shift_number):
        self.shift_number = int(shift_number)
        
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

        # Converting the shift number into words
        if self.shift_number == 1:
            self.shift = "Day"
        elif self.shift_number == 2:
            self.shift = "Night"



def main():
        # Getting User Inputs
    print("Enter the following details of the Employee\n--------------------------------------------")
    employee_name = input("Enter Employee Name: ")
    employee_number = input("Enter Employee Number: ")
    hourly_pay_rate = input("Enter Pay Rate: ")
    shift_number = input("Enter Shift Number (1 for day shifts, 2 for night shifts): ")

        # Dealing with User Inputs
    worker = ProductionWorker(employee_name, employee_number, shift_number, hourly_pay_rate)

        # Displaying User Input
    print("\n-------------------------------------------------------\nDetails of Employee:\n-------------------------------------------------------")
    print("Name:", worker.get_employee_name())
    print("Employee Number:", worker.get_employee_number())
    print("Shift:", worker.get_shift())
    print("Pay Rate:", worker.get_hourly_pay_rate())


main()
