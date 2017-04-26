# Chapter 1 Assignment
# Author: Jorge Rodriguez
# Date: February 5, 2017

print('You will enter the length and width for two rectangles')
print('The program will tell you which rectangle has the greater area')
# get length and width of 2 rectangles
rect_length1 = float(input('Enter the length of the first rectangle: '))
rect_width1 = float(input('Enter the width of the first rectangle: '))
rect_length2 = float(input('Enter the length of the second rectangle: '))
rect_width2 = float(input('Enter the width of the first rectangle: '))
# calculate area of both rectangles
rect_area1 = rect_width1 * rect_length1
rect_area2 = rect_length2 * rect_width2
# compare which rectangle has the greater area

if rect_area1 > rect_area2:
    print('Your first rectangle has a greater area than your second rectangle')
elif rect_area1 < rect_area2:
    print("Your second rectangle had a greater area than your first rectangle")
else:
    print('Both rectangles had the same area!')
