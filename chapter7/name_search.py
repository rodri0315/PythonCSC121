# Author: Jorge Rodriguez
# Date: March 28, 2017
# Name search

boy_names = []
girl_names = []

def main():
    # receive list of boy names from file
    input_file = open("BoyNames.txt", "r")

    # check user answers against correct answers
    list_names = input_file.readlines()

    # Clean up the entries by removing new line chars
    for i in range(len(list_names)):
        list_names[i] = list_names[i].rstrip('\n')
        # append/add name read to the boys list
        boy_names.append(list_names[i])

    input_file.close()

    # receive list of names from file
    input_file2 = open("GirlNames.txt", "r")

    # check user answers against correct answers
    list_names2 = input_file2.readlines()

    for i in range(len(list_names2)):
        list_names2[i] = list_names2[i].rstrip('\n')
        # append/add name read to girl list
        girl_names.append(list_names2[i])

    input_file2.close()

    # merge lists to find names
    complete_list = boy_names + girl_names
    # Show user instructions
    print("(See if a (girls/boys)name was among the most popular from 2000-2009)")
    # get input from user
    user_input = str(input("\tEnter the name(s): "))
    # Ask user if they want to enter a second name
    answer = str(input("\tDo you want to enter another name? 'y'(Yes) or press 'enter'"))
    # If user wants to enter a second name ask for name
    if answer == 'y':
        user_input2 = str(input("\tEnter the name: "))
        # The simple way to search for a string in a list is just to use 'if string in list'
        if user_input2 in complete_list:
            # print second name to user
            print(f"We found the name {user_input2}")
        else:
            print(f"Name {user_input2} not found!")

    if user_input in complete_list:
        # print the fist name if found!
        print(f"We found the name {user_input}")
        print("Name(s) found!")
    # Print statement if name is not found
    else:
        print(f"Name {user_input} not found!")

# Run main
main()