# Chapter 3 Assignment
# Author: Jorge Rodriguez
# Date: February 7, 2017

# Hot Dog Cookout Calculator

# Hot dogs and buns packages as constants variables
WINNIES_PACK = 10
BUNS_PACK = 8

# Ask user of num_of_people attending the cookout party and number each of hot dogs hot_gods_given given to each person
num_of_people = int(input('How many people will attend to your cookout party? :'))
hot_dogs_given = int(input('How many hot dogs is each person getting? '))

# Calculations
hot_dogs_needed = int(num_of_people * hot_dogs_given)
print('You need to make ' + repr(hot_dogs_needed) + ' hot dogs!\n')

# Logic for packages needed
# Get the result of how many packs are needed by using // (floor division) instead of / (true division)
# This will get number of packs without the remaining
hot_dog_pack_needed = hot_dogs_needed // WINNIES_PACK
buns_pack_needed = hot_dogs_needed // BUNS_PACK
# multiply (floored)packs by the number of items in them and check if that is enough for the hot dogs and buns needed
if hot_dog_pack_needed * WINNIES_PACK < hot_dogs_needed:
    hot_dog_pack_needed += 1
    # print('Not enough Hot dogs')
    # print('Adding a pack!...')
if buns_pack_needed * BUNS_PACK < hot_dogs_needed:
    buns_pack_needed += 1
    # print('Not enough buns')
    # print('Adding a pack!...')

# Use remainder operator to get the remainder hot dogs and buns left.
hot_dog_remainder = hot_dogs_needed % WINNIES_PACK
buns_remainder = hot_dogs_needed % BUNS_PACK

# Display results to user
# min number of packages of hot dogs and buns required
# min number of hot dogs and buns that will be left over
print('You will need ' + repr(hot_dog_pack_needed) + ' packs of hot dogs.')
print('You will have ' + repr(hot_dog_remainder) + ' hot dogs left over')
print('You will need ' + repr(buns_pack_needed) + ' packs of hot dog buns.')
print('You will have ' + repr(buns_remainder) + ' hot dog buns left over')