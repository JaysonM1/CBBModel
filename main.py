import pandas as pd
from TeamAvgs.update_team_avgs import update_team_stats_today
from Scores.todays_games import get_historical_game_data


def main():
    month = input("Month: ")
    day = input("Day: ")
    year = input("Year: ")
    update_team_stats_today()
    get_historical_game_data()
        

if __name__ == "__main__":
    main()
