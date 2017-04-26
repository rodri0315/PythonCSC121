# Author: Jorge Rodriguez
# Date: March 21, 2017
# Exercise 10


def main():

    # create a list of correct answers
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                       'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

    correct, incorrect = 0, 0
    incorrect_questions = []

    # receive list of user answers from file
    input_file = open("answers.txt", "r")

    # check user answers against correct answers
    user_answers = input_file.readlines()
    # clean up th entries by removing the new lines chars
    for i in range(20):
        user_answers[i] = user_answers[i].rstrip('\n')
    # check the answer against correct answer
    for index in range(20):
        if user_answers[index] == correct_answers[index]:
            # keeping a running total of correct answers
            correct += 1
        else:
            incorrect -= 1
            # keeping a running total of incorrect answers
            incorrect_questions.append(index + 1)
            # keeping a list of incorrect items

#     Determine pass or Fail
    if correct >= 15:
        print("You passed the exam!")
    else:
        print("You did not passed the exam")
    print(f"Correct: {str(correct)}")
    print(f"Incorrect: {str(incorrect)}")
    print(incorrect_questions)

main()
