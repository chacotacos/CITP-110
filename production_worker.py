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
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # Method to get the shift number
    def get_shift(self):
        return self.__shift

    # Method to get the hourly pay rate
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    # Path: production_worker.py
    