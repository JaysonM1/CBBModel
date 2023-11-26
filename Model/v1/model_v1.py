import pandas as pd
from datetime import datetime


def is_before_date(date_str1, date_str2):
    # Convert date strings to datetime objects
    date1 = datetime.strptime(date_str1, '%m-%d-%y')
    date2 = datetime.strptime(date_str2, '%m-%d-%y')

    # Compare the dates
    return date1 < date2


def build_entire_dataset():
    month = '11'
    year = '23'
    first_stats_date = '11-21-23'
    master_df = pd.DataFrame()
    for d in range(6,24):
        if d < 10:
            strings = [month,'0' + str(d), year]
            date = '-'.join(strings)
        else:
            strings = [month, str(d), year]
            date = '-'.join(strings)

        
        print(date)
        if is_before_date(date, first_stats_date):
            stats_df = pd.read_csv('TeamAvgs/DailyStats/TeamAverages/November23/11-21-23.csv')
        else:
            stats_df = pd.read_csv('TeamAvgs/DailyStats/TeamAverages/November23/' + date + '.csv')
        scores_df = pd.read_csv('Scores/' + date + '.csv')

        merged_on_home = pd.merge(scores_df,stats_df, left_on = 'Home', right_on = 'Team', how = 'left')
        merged_on_home.drop(columns='Team', inplace=True)

        merged_on_home.rename(columns={'ATRatio':'home_ATRatio', 'Apg':'home_Apg',
                                        'BPpg': 'home_BPpg', 'Bpg': 'home_Bpg',
                                        'EFG%': 'home_EFG%', 'FbP': 'home_FbP',
                                        'Fg%': 'home_Fg%', 'Fg%D': 'home_Fg%D',
                                        'Fpg': 'home_Fpg', 'FTApg': 'home_FTApg',
                                        'FTp': 'home_FTp', 'FTMpg': 'home_FTMpg',
                                        'FTp': 'home_FTp', 'FTMpg': 'home_FTMpg',
                                        'RM': 'home_RM', 'ROpg': 'home_ROpg',
                                        'Rpg': 'home_Rpg', 'SD': 'home_SD',
                                        'SO': 'home_SO', 'SM': 'home_SM',
                                        'Spg': 'home_Spg', '3PApg': 'home_3PApg',
                                        '3P%': 'home_3P%', '3PD%': 'home_3PD%',
                                        '3Ppg': 'home_3Ppg', 'TOM': 'home_TOM',
                                        'Tpg': 'home_Tpg', 'TFpg': 'home_TFpg'}, inplace=True)
        
        merged_df = pd.merge(merged_on_home,stats_df, left_on='Away',right_on='Team', how= 'left')
        merged_df.drop(columns='Team', inplace=True)

        merged_df.rename(columns={'ATRatio':'away_ATRatio', 'Apg':'away_Apg',
                                        'BPpg': 'away_BPpg', 'Bpg': 'away_Bpg',
                                        'EFG%': 'away_EFG%', 'FbP': 'away_FbP',
                                        'Fg%': 'away_Fg%', 'Fg%D': 'away_Fg%D',
                                        'Fpg': 'away_Fpg', 'FTApg': 'away_FTApg',
                                        'FTp': 'away_FTp', 'FTMpg': 'away_FTMpg',
                                        'FTp': 'away_FTp', 'FTMpg': 'away_FTMpg',
                                        'RM': 'away_RM', 'ROpg': 'away_ROpg',
                                        'Rpg': 'away_Rpg', 'SD': 'away_SD',
                                        'SO': 'away_SO', 'SM': 'away_SM',
                                        'Spg': 'away_Spg', '3PApg': 'away_3PApg',
                                        '3P%': 'away_3P%', '3PD%': 'away_3PD%',
                                        '3Ppg': 'away_3Ppg', 'TOM': 'away_TOM',
                                        'Tpg': 'away_Tpg', 'TFpg': 'away_TFpg'}, inplace=True)
        merged_df = merged_df.dropna()
        master_df = pd.concat([master_df,merged_df], ignore_index=True)
    master_df.to_csv('Model/v1/dataset_with_teams.csv')


def build_model_today():
    build_entire_dataset()
    dataset
        


            