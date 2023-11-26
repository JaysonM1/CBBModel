from TeamAvgs.update_team_avgs import update_team_stats_today
from Scores.todays_games import update_latest_scores, get_historical_game_data
from Model.v1.model_v1 import build_model_today


def main():
    update_team_stats_today()
    ##get_historical_game_data()
    update_latest_scores()
    build_model_today()
        

if __name__ == "__main__":
    main()
