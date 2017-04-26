# Author: Jorge Rodriguez
# Date: February 21, 2017
# Exercise 9

# Constants for tax percentage
COUNTY_SALES_TAX = .025
STATE_SALES_TAX = .05


def main():
    sales = float(input('Enter your total monthly sales: '))
    calc_sales_tax(sales)


def calc_sales_tax(sales):
    county_sales_tax = sales * COUNTY_SALES_TAX
    print("County sales tax of {} is {}".format(sales, county_sales_tax))

    state_sales_tax = sales * STATE_SALES_TAX
    print("State sales tax of {} is {}".format(sales, state_sales_tax))

    total_sales_tax = state_sales_tax + county_sales_tax
    print("Total sales tax of {} is {}".format(sales, total_sales_tax))

main()