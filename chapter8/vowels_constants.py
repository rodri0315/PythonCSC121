# Author: Jorge Rodriguez
# Date: April 2, 2017
# Lab Vowels and Constants


# main
def main():
    #Get string from user
    user_input = input('Enter a string: ')

#     Report the vowels and constants.
    print('That string has {} vowels and {} contants.'.format(num_vowels(user_input), num_constants(user_input)))

def num_vowels(string):

    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize a counter
    vowel_count = 0

    # Count the vowels in s
    for ch in string:
        if ch.lower() in vowels:
            vowel_count += 1

    # return the vowel count
    return vowel_count

def num_constants(string):

    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize a counter
    constant_count = 0

    # Count the vowels in s
    for ch in string:
        if ch.isalpha() and ch.lower() not in vowels:
            constant_count += 1

    # return the vowel count
    return constant_count

# call main
main()


