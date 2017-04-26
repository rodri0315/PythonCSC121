# Author: Jorge Rodriguez
# Date: February 27, 2017
# Exercise 15


# create main function to run program
def main():
    # Ask user to enter 5 test scores, save scores in variables
    test1 = int(input('Enter score for test 1: '))
    test2 = int(input('Enter score for test 2: '))
    test3 = int(input('Enter score for test 3: '))
    test4 = int(input('Enter score for test 4: '))
    test5 = int(input('Enter score for test 5: '))

    # save scores in array to be able to iterate through it
    test_scores = [test1, test2, test3, test4, test5]

    # print letter grade for each score
    # use function to print letter grade
    print_letter_grade(test_scores)

    # print average test score
    # save average in variable, get average using function
    average = calc_average(test1, test2, test3, test4, test5)
    # print output, use to decimal point
    print("The average test score is {0:.2f}".format(average))


# create functions
# calc_average function accepts five test scores as arguments, returns averages from test scores
def calc_average(test1, test2, test3, test4, test5):
    average_test_score = (test1 + test2 + test3 + test4 + test5) / 5
    return average_test_score


# determine_grade function should accept a test score as argument, returns letter grade
def determine_grade(average_grade):
    # Use if statement, check for grade and match letter grade according to grade scale.
    if average_grade > 100:
        # if average is over 100 print message to user and re run program.
        print("{} input is invalid only grades 0 to 100, try again...\n".format(average_grade))
        main()
    # Check grade is less than 100 and 90 or above.
    elif 90 <= average_grade <= 100:
        # assign letter grade to a variable
        grade = "A"
        # return letter grade
        return grade
    elif average_grade >= 80:
        grade = "B"
        return grade
    elif average_grade >= 70:
        grade = "C"
        return grade
    elif average_grade >= 60:
        grade = "D"
        return grade
    else:
        grade = "F"
        return grade


# function returns letter grade, takes an array as an argument to iterate through it and print letter grade.
def print_letter_grade(array):
    # initiate variable to count test number
    test_number = 0
    # iterate through each test and print letter grade
    for score in array:
        # save letter grade in variable, use function to get letter grade
        letter_grade = determine_grade(score)
        # increment test number by one each time
        test_number += 1
        # print output to user
        print("The grade for test {} is {}".format(test_number, letter_grade))

# call main
main()
