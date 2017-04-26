# Chapter 4 Lab Assignment
# Author: Jorge Rodriguez
# Date: February 12, 2017

# Bug Collector
# For each of 7 days
#     Input collected bugs for a day
#     Add bugs collected to total
# Display Total

# counter, set total number of bugs
total = 0

# set number of days for the week, could have used a while loop.
# WEEK_DAYS = 6

# Loop through WEEK_DAYS, start at 0 and ask user their input until WEEK_DAYS is 6
for day in range(1, 8):
    # Prompt user
    print('Enter the bugs collected on day', day, ':')
    # Input the number of bugs
    bugs = int(input())
    # add bugs to the total
    total += bugs

# Display total number of bugs
print('You collected a total of', total, 'bugs.')

