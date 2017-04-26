# course: csc121
# exercise: 2) Sales Prediction
# date: 01/29/17
# author(name): Jorge Rodriguez
# description: Get the projected total sales
# program will take input, process a calculation and display the output of the calculation

# assign input from user to total_sales variable
# input() function reads input from the keyboard
# float() function Converts the value to a float
total_sales = float(input('Enter the projected sales: '))
# Calculate profit as 23% of total sales.
profit = total_sales * .23
# output(display) the profit
print('The profit is $', format(profit, ',.2f'))

# The following print method is a variant, may be helpful when displaying multiple values
# print("According to your of {1:6,.2f}, the profit is ${0:6,.2f}".format(profit, total_sales))
