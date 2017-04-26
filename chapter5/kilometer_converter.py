# Chapter 5 Lab 1
# Author: Jorge Rodriguez
# Date: February 21, 2017

# save conversion number km to miles in constant
KM_TO_MILES = 0.6214

# main function gets distance in Km and calls show_miles function to display results

def main():
    # Get distance in Km from user
    km_dist = float(input('Enter your distance in Kilometers: '))

    # Display the Kilometer distance in miles to user
    show_miles(km_dist)

# the show_miles function converts the parameter Km to miles and display the result

def show_miles(km_dist):
    # calculate miles
    miles = km_dist * KM_TO_MILES
    # Display miles, used format function to round result up to 2 decimals
    print(km_dist, ' kilometers is equals to ', format(miles, '.2f'), 'miles.')

# this calls the main function
main()
