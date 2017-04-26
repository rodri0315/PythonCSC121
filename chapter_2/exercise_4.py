# course: csc121
# exercise: 1
# date: 01/24/17
# author(name): Jorge Rodriguez
# description: program will calculate subtotal, sales tax, and grand total of the user's items

# Initiating a constant to 7%
TAX_PERCENTAGE = .07
# create variables to store user's input, prompt user to enter their sales of each item
item1 = float(input('Enter the price of the first item: $'))
item2 = float(input('Enter the price of the second item: $'))
item3 = float(input('Enter the price of the third item: $'))
item4 = float(input('Enter the price of the fourth item: $'))
item5 = float(input('Enter the price of the fifth item: $'))
# add all items and store in a subtotal variable
subtotal = (item1+item2+item3+item4+item5)
# get sales tax of 7%(.07) from subtotal
sales_tax = (subtotal * TAX_PERCENTAGE)
# get total from the sum of subtotal and sales_tax
total = subtotal + sales_tax
# output/print subtotal, sales_taz, and total to user, blank print method left on purpose to separate input from output
print("")
print("The subtotal of the sale is: $", format(subtotal, ',.2f'))
print("The amount of sales tax is: $", format(sales_tax, ',.2f'))
print("The total sale is: $", format(total, ',.2f'))
