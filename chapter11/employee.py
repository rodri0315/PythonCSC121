# Author: Jorge Rodriguez
# Date: April 25, 2017
# Employee and ProductionWorker Class, assignment


class Employee:
    # init method to initialize the attributes
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # set methods to set the name, number
    # Mutator for the __name attribute
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # get methods return the person's name, address and phone
    # Accessor for the name attribute
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


# ProductionWorker Class
class ProductionWorker(Employee):
    # init method to initialize the attributes
    def __init__(self, name, number, shift, pay_rate):
        # Initialize specialized attributes
        self.__shift = shift
        self.__pay_rate = pay_rate

        # call superclass __init__ method
        Employee.__init__(self, name, number)

    # set methods
    # Mutator for the __shift attribute
    def set_shift(self, shift):
        self.__shift = shift

    # Mutator for the __pay_rate attribute
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Get methods to return shift and pay_rate
    # Accessor for the shift attribute
    def set_shift(self):
        return self.__shift

    # Accessor for the pay_rate attribute
    def set_pay_rate(self):
        return self.__pay_rate
