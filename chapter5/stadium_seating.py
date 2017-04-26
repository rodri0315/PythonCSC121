# Author: Jorge Rodriguez
# Date: February 26, 2017
# Exercise 7


# define main function
def main():
    # Init variables depending on tickets class, get total tickets sold from user
    c_tickets = int(input('How many tickets of class C were sold?'))
    b_tickets = int(input('How many tickets of class B were sold?'))
    a_tickets = int(input('How many tickets of class A were sold?'))
    # save total addition of tickets cost in variable income
    # add functions and passing the correct matching parameter for each one to get total income
    income = class_a(a_tickets) + class_b(b_tickets) + class_c(c_tickets)
    # output total income to user, using format method to display income with commas and up to 2 decimal cents.
    print("Total income generated is ${0:,.2f}".format(income))


# declare functions to get cost of tickets depending on what class seats they are
# takes one parameter (tickets), function returns the cost of tickets depending on class seat.
def class_a(tickets):
    # declare variable cost equals tickets times cost of ticket
    cost = tickets * 20
    # return cost
    return cost


def class_b(tickets):
    cost = tickets * 15
    return cost


def class_c(tickets):
    cost = tickets * 15
    return cost

# calls main function to run program
main()


