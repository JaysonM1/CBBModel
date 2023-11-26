import pandas as pd
from TeamAvgs.update_team_avgs import update_team_stats_today
from Scores.todays_games import update_latest_scores


def main():
    update_team_stats_today()
    update_latest_scores()
        

if __name__ == "__main__":
    main()
