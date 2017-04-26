# Author: Jorge Rodriguez
# Date: April 23, 2017
# Customer demo Lab

from chapter11 import person_cust_class

# Get some customer information
name = input('Name: ')
address = input('Address: ')
phone = input('Phone: ')
customer_number = input('Customer number: ')
mail = input('Include in mailing list? (y/n): ')

# Determine True or False for mailing list.
if mail.lower() == 'y':
    mailing_list = True
else:
    mailing_list = False

# Create an instance of the Customer class.
my_customer = person_cust_class.Customer(name, address, phone, customer_number, mailing_list)


# Display the object's data
print("Customer's Information")
print("----------------------")
print("Name: ", my_customer.get_name())
print("Address: ", my_customer.get_address())
print("Phone: ", my_customer.get_phone())
print("Customer number: ", my_customer.get_customer_number())
print("Mailing List: ", my_customer.get_mailing_list())