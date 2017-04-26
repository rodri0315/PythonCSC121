# Author: Jorge Rodriguez
# Date: April 4, 2017

# define a main function
def main():
    # get string from user and convert to UPPERCASE
    user_input = input('Enter a 10 character phone number. \n(ex. 555-GET-FOOD): ').upper()

    # print phone number converted to digits only
    print(get_translation(user_input))

# method takes a string to convert to phone number digits
def get_translation(string):
    # create empty list to add filtered characters
    char_list = []

    # Loop will check each character from the string
    for ch in string:
        # if char is digit add it to list
        if ch.isdigit():
            char_list.append(ch)
        # if char is a dash, add it to list
        elif ch == '-':
            char_list.append('-')
        # depending the char will point to a diff number and add that number to the list
        elif ch.isalpha():
            if ch == 'A' or ch == 'B' or ch == 'C':
                char_list.append('2')
            if ch == 'D' or ch == 'E' or ch == 'F':
                char_list.append('3')
            if ch == 'G' or ch == 'H' or ch == 'I':
                char_list.append('4')
            if ch == 'J' or ch == 'K' or ch == 'L':
                char_list.append('5')
            if ch == 'M' or ch == 'N' or ch == 'O':
                char_list.append('6')
            if ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
                char_list.append('7')
            if ch == 'T' or ch == 'U' or ch == 'V':
                char_list.append('8')
            if ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
                char_list.append('9')
    # Join list to convert to string
    converted_string = ''.join(char_list)
    # return converted string
    return converted_string
# call main
main()