"""
Nancy Guan
DS2000
Final Project
November 14, 2024
european_football.py
"""
import csv
import matplotlib.pyplot as plt

# Set constants
# Create default lists of each team in each league
FILE = "top5_leagues_player.csv"
LEAGUE_COLUMN = 17
HEIGHT_COLUMN = 4
CLUB_COLUMN = 12
COLOR_CYCLE = ["dodgerblue", "lightsteelblue", "skyblue", "steelblue"]
PREM_TEAMS = ["Man City", "Chelsea", "Arsenal", "Liverpool", "Man Utd",
              "Tottenham", "Newcastle", "West Ham", "Leicester", "Aston Villa",
              "Wolves", "Southampton", "Brighton", "Everton", "Nottm Forest",
              "Brentford", "Leeds", "Crystal Palace", "Fulham", "Bournemouth"]
BUNDESLIGA_TEAMS = ["Bayern Munich", "Bor. Dortmund", "RB Leipzig",
                    "B. Leverkusen", "E. Frankfurt", "Bor. M'gladbach",
                    "VfL Wolfsburg", "SC Freiburg", "TSG Hoffenheim",
                    "Union Berlin", "FC Augsburg", "VfB Stuttgart",
                    "1.FSV Mainz 05", "1.FC Köln", "Hertha BSC",
                    "Werder Bremen", "FC Schalke 04", "VfL Bochum"]
LALIGA_TEAMS = ["Real Madrid", "Barcelona", "Atlético Madrid", "Real Sociedad",
                "Valencia", "Sevilla FC", "Celta de Vigo", "Getafe",
                "CA Osasuna", "Girona", "Espanyol", "Rayo Vallecano",
                "RCD Mallorca", "UD Almería", "Real Valladolid", "Cádiz CF",
                "Elche CF"]

def league(file, league_column, league_name):

    # Function to separate players into leagues
    # Create empty list and read file
    league_list = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # If name exists, add to list
        for line in csv_reader:
            if line[league_column] == league_name:
                league_list.append(line)
    return league_list
def club(list, club_column, club_name):

    # Function to separate into clubs using list of a league
    # Create empty list
    # Create a list with the same club
    club_list = []

    # Append to list if names match
    for line in list:
        if line[club_column] == club_name:
            club_list.append(line)
    return club_list

def height_average(list, height_column):

    # Function to find average height using list of a club
    # Create empty list
    heights = []

    # Convert heights to floats
    # Append
    for row in list:
        heights.append(float(row[height_column]))

    # Calculate average
    average_height = sum(heights) / len(heights)
    return average_height

def plot_heights(league_string, player_data_list):

    # Function to plot 
    # Create empty dictionary
    # Add clubs as key
    # Average height for value
    club_height_dict = {}

    # Create a dictionary of club and average height
    for i in range(len(league_string)):
        clubs = club(player_data_list, CLUB_COLUMN, league_string[i])
        heights = height_average(clubs, HEIGHT_COLUMN)
        club_height_dict[league_string[i]] = heights

    # Create empty dictionary to add values
    # Greatest to least
    new_dict = {}
    reorder = sorted(club_height_dict.items(), key=lambda item: item[1],
                     reverse=True)
    for key, value in reorder:
        new_dict[key] = value

    # Create empty lists for keys and values
    key_list = []
    value_list = []
    for key, value in new_dict.items():
        key_list.append(key)
        value_list.append(value)

    # Plot with lists given above
    # Include chart names and other specifications
    plt.bar(key_list, value_list, color=COLOR_CYCLE)
    plt.xlabel("Clubs")
    plt.ylabel("Average Height in Meters")
    plt.ylim(bottom=1.79, top=1.89)
    plt.title("League Average Height")
    plt.xticks(rotation=90)
    plt.savefig("club_heights", bbox_inches="tight")
    plt.tight_layout()
    plt.show()

def main():

    # Create lists of players and data in each league
    english= league(FILE, LEAGUE_COLUMN, "EPL")
    spanish = league(FILE, LEAGUE_COLUMN, "LaLiga")
    german = league(FILE, LEAGUE_COLUMN, "Bundesliga")

    # Create bar charts
    plot_heights(PREM_TEAMS, english)
    plot_heights(LALIGA_TEAMS, spanish)
    plot_heights(BUNDESLIGA_TEAMS, german)

main()