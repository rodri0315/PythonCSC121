# Chapter 5 Lab 2
# Author: Jorge Rodriguez
# Date: February 21, 2017

# constant of inches per foot
INCHES_PER_FOOT = 12

# main function
def main():
    # Get number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # convert feet to inches on the print statement
    print(feet, 'equals to', feet_to_inches(feet), 'inches.')

# the feet_to_inches function returns the conversion of the feet parameter to inches
def feet_to_inches(feet):
    # convert feet to inches
    inches = feet * INCHES_PER_FOOT
    return inches

# calls main function
main()

