from employee import Employee

class ShiftSupervisor(Employee):
    def __init__(self, name, emp_number, annual_salary, annual_bonus):
        super().__init__(name, emp_number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary
    
    def get_annual_bonus(self):
        return self.__annual_bonus