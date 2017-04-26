# Author: Jorge Rodriguez
# Date: April 23, 2017
# Person Customer Class Lab


class Person:
    # init method to initialize the attributes
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # set methods to set the name, address, and phone
    # Mutator for the __name attribute
    def set_name(self, name):
        self.__name = name

    # Mutator for the __address attribute
    def set_address(self, address):
        self.__address = address

    # Mutator for the __phone attribute
    def set_phone(self, phone):
        self.__phone = phone

    # get methods return the person's name, address and phone
    # Accessor for the name attribute
    def get_name(self):
        return self.__name

    # Accessor for the address attribute
    def get_address(self):
        return self.__address

    # Accessor for the phone attribute
    def get_phone(self):
        return self.__phone


# Customer Class
class Customer(Person):
    # init method to initialize the attributes
    def __init__(self, name, address, phone, customer_number, mailing_list):
        self.__customer_number = customer_number

        # Call superclass __init__ method
        Person.__init__(self, name, address, phone)

        # init the specialized attributes
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    # Mutator for the __customer_number attribute
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    # Mutator for the __mailing_list attribute
    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    # Accessor for the __customer_number attribute
    def get_customer_number(self):
        return self.__customer_number

    # Accessor for the __mailing_list attribute
    def get_mailing_list(self):
        return self.__mailing_list
