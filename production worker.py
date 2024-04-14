from employee import Employee
def __init__(self, name, emp_number< shift, hourly_pay_rate):
    # Cronstructor method to initialize ProductionWorker attributes
    super().__init__(name, emp_number)
    self.__shift = shift
    self.__hourly_pay_rate = hourly_pay_rate

    # Method to set the shift number
    def set_shift(self, shift):
        self.__shift = shift

    # Method to set the hourly pay rate
    