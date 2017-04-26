# Author: Jorge Rodriguez
# Date: April 18, 2017
# Information Class, assignment


# Init class
class Information:
    # init method to initialize the attributes
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    # set methods sets the the name, address and phone number
    def set_name(self, name):
        self.__name = name

    # get methods returns the name, address and phone number
    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number


# Initialize 3 instances of the class Information
contact_1 = Information('Jorge Rodriguez', 'Carrboro, NC', '919-923-3333')
contact_2 = Information('Abel Rodriguez', 'Rhode Island, RI', '402-555-1234')
contact_3 = Information('Elizabeth Gaona', 'Mexico City, Mx', '011-52-55-51265476')

# print the information from our instances
print(f"Name: {contact_1.get_name()}")
print(f"Address: {contact_1.get_address()}")
print(f"Phone number: {contact_1.get_phone_number()}")
print("------------------")
print(f"Name: {contact_2.get_name()}")
print(f"Address: {contact_2.get_address()}")
print(f"Phone number: {contact_2.get_phone_number()}")
print("------------------")
print(f"Name: {contact_3.get_name()}")
print(f"Address: {contact_3.get_address()}")
print(f"Phone number: {contact_3.get_phone_number()}")
