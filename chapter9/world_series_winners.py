# Author: Jorge Rodriguez
# Date: April 11, 2017
# Exercise 7 World Series Winners


def main():
    start = 1903
    # Create first dictionary team:number of times won
    team_dict = {}
    # Create second dictionary year:name_of_team
    year_team_name = {}
    # create a list to keep count of teams that have already won in previous years
    team_list = []
    # Read file WorldSeries.txt and fill the two Dictionaries
    with open('WorldSeries.txt', 'r') as file:
        # Loop through file to check how many times team has won the World Series
        for line in file:
            # Loop through every line and add key(year) and the value(line'Team')
            year_team_name[start] = line
            # add one to variable start to keep count of years
            start += 1
            # Check if team already exists in the team_list
            if line in team_list:
                # add a value of 1 if team is already in the team_list
                team_dict[line] += 1
            else:
                # Add the team to the team_list to keep record of teams
                team_list.append(line)
                # Add a value of 1 to start count of the many times a team has won
                team_dict[line] = 1

    # Ask user a year in the range of 1903 - 2009
    print("Choose a year between 1903 and 2009: ")
    year = int(input())

    # Print Name of team that won that year and how many times the team has won it
    if year == 1904 or year == 1994:
        print("In this year the World Series was not played")
    elif year > 2009 or year < 1903:
        print("Either your input is incorrect or we do not have a record of the year you entered.")
        main()
    else:
        # Print the year and team that won the year chosen by the user
        print("In the year {} the {} won the World Series".format(year, year_team_name.get(year, 'Team')))
        # get the number of times a team has won according to the year chosen
        ws_wins = team_dict.get(year_team_name.get(year, 'Team'))
        # Print to user the team and the number times the team has won a World Series
        print("The {} has won the World Series {} time(s)".format(year_team_name.get(year, 'Team'), ws_wins))

# Call main
main()
