# Author: Jorge Rodriguez
# Date: April 11, 2017
# State capitals Lab

# Constant for the number of questions asked to the user.
NUM_QUESTIONS = 5


def main():
    # Initialize the state_capitals dictionary
    state_caps = state_capital_dict()

    # Initialize a counter of correct responses start at 0
    correct = 0
    # Initialize a counter of incorrect responses start at 0
    incorrect = 0

    # Repeat five times -use for loop
    # Quiz the user.
    for count in range(NUM_QUESTIONS):
        # Get random entry from dictionary
        state, capital = state_caps.popitem()

        # Quiz the user.
        print(f'What is the capital of {state}? ')
        answer = input()

        # Is the user correct, convert to lower case to match answer
        if answer.lower() == capital.lower():
            correct += 1
            print('Correct!')
        else:
            incorrect += 1
            print('Incorrect.')

    # Display the results
    print(f'Correct responses {correct} out of {NUM_QUESTIONS}')
    print(f'Incorrect responses {incorrect} out of {NUM_QUESTIONS}')


# SUDOCODE
# Get a random entry from the dictionary get state and capital

#   Ask user to enter the answer of the capital of state chosen

#   If user answer is correct
#       add one to counter correct answer
#       print message to user of their correct answer
#   Else:
#         Add 1 to incorrect counter
#         Print message indicating incorrect answer

# Display results, number of correct and incorrect answer


# Initialize/Create a dictionary with states and capitals
def state_capital_dict():
    state_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                      'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                      'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                      'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
                      'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                      'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
                      'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
                      'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
                      'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
                      'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
                      'North Carolina': 'Raleigh',
                      'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
                      'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                      'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
                      'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                      'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    return state_capitals


# Call main
main()
