# This file defines the Employee class

class Employee:
    def __init__(self, name, emp_number):
        # Cunstructor method to initialaize the employee name and number
        self.__name = name
        self.__emp_number = emp_number

    # method to set the employee name
    def set_name(self, name):
        self.__name = name

    # method to set the employee number
    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    # method to get the employee name
    def get_name(self):
        return self.__name
    
    # method to get the employee number
    def get_emp_number(self):
        return self.__emp_number