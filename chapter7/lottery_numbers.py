# Author: Jorge Rodriguez
# Date: March 26, 2017
# Lab Lottery numbers

import random

MAX_NUMBERS = 7     # Max number of digits
START_COUNT = 0     # Start of random number
STOP_COUNT = 9      # End of random number
rand_numbers_list = []  # create an empty list

# Create main function


def main():
    # loop MAX_NUMBERS
    for i in range(MAX_NUMBERS):
        # Append each time a random number in range from start to stop to the list
        rand_numbers_list.append(random.randint(START_COUNT, STOP_COUNT))

    # create a count variable
    count = 1
    # Loop through each number in the list and print each number
    for number in rand_numbers_list:
        # Print results from list with an added count of each number
        print("Lottery #{} is {}".format(count, number))
        # increment count by one
        count += 1
# Call main func
main()


