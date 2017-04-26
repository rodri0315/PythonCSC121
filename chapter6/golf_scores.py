# Author: Jorge Rodriguez
# Date: March 21, 2017
# Exercise 10

# Programs saves dat entered by user, player's name and score.


def main():
    # get number of player records to create
    num_players = int(input("How many player's you want to add?"))

    # Open file for writing.
    players_file = open('golf.txt', 'w')

    # Get each player's data and write to golf.txt file
    for count in range(1, num_players +1 ):
        # Get data for a player
        print("Enter player's #{} data name and score ".format(count))
        name = input('Name: ')
        score = input('Score: ')
        # Write data as a record to the file
        players_file.write(name + '\n')
        players_file.write(score + '\n')

        # Display a blank line
        print()

    # Close file
    players_file.close()
    print("Player's records written to golf.txt")

# Call main
main()