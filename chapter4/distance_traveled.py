# Chapter 4 Assignment
# Author: Jorge Rodriguez
# Date: February 14, 2017

# get speed input from user and set it in variable
speed = int(input('What is the speed of the vehicle in mph? '))
# get hours input from user and save in variable
hours_traveled = int(input('How many hours has it traveled? '))

# Print header for output
print('Hour\t\t Distance Traveled')
print('________________________________')
# Iterate over the hours from users input, using range starting from 1
for hour in range(1, hours_traveled + 1):
    # get distance, multiply speed times hour in sequence
    distance = speed * hour
    # print results.
    print(hour, '\t\t\t\t', distance)

