import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from .Names.names import inconsistent_names, cbs2ncaa
def drop_ot_columns(df):
    # Check if 'OT' or 'OT2' columns exist
    ot_columns = [col for col in ['OT', 'OT2'] if col in df.columns]

    # Drop the columns if they exist
    if ot_columns:
        df = df.drop(ot_columns, axis=1)

    return df
    
def nan_values(df):
    # Check if there are any NaN values in the DataFrame
    if df.isna().any().any():
        return True
    return False

def valid_teams(teams):
    csv_path = 'TeamAvgs/DailyStats/TeamAverages/bare.csv'
    df = pd.read_csv(csv_path)
    valid_names = df['Team'].values
    return teams[0] in valid_names and teams[1] in valid_names
        


def restructure_home_away(df):
    new_df = pd.DataFrame({
    'Home': df['Team'].shift().fillna(''),
    '1h': df['1'].shift().fillna(0).astype(int),
    'Th': df['T'].shift().fillna(0).astype(int),
    'Away': df['Team'],
    '1w': df['1'],
    'Tw': df['T']
    })

# Drop the first row since it will have NaN values
    new_df = new_df.iloc[1:].reset_index(drop=True)
    return new_df


def cancelled_game(df):
    return len(df.columns) < 3

def inconsistent_team_names(teams):
    return teams[0] in inconsistent_names or teams[1] in inconsistent_names

def change_to_consistent_names(df):
    team1 = df['Team'][0]
    team2 = df['Team'][1]
    if team1 in cbs2ncaa.keys():
        df['Team'][0] = cbs2ncaa[team1]
    if team2 in cbs2ncaa.keys():
        df['Team'][1] = cbs2ncaa[team2]

    return df

def get_raw_game_scores_from_day(day, month, year):
    date = year + month + day
    URL = 'https://www.cbssports.com/college-basketball/scoreboard/FBS/' + date + '/'
    return pd.read_html(URL)

def drop_leading_space(team_names):
    return [s.lstrip() for s in team_names]


def drop_leading_space_df(df):
    df['Team'] = df['Team'].str.strip()
    return df
def get_historical_game_data():
    year = '2023'
    month = '11'
    header = ['Home', '1h', 'Th', 'Away', '1w', 'Tw']
    master_df = pd.DataFrame(columns=header)
    for day in range(6,24):
        day = str(day)
        if day in ['1','2','3','4','5','6','7','8','9']:
            day = '0' + day
        date = year + month + day
        URL = 'https://www.cbssports.com/college-basketball/scoreboard/FBS/' + date + '/'
        dfs = pd.read_html(URL)
        for df in dfs:
            df = drop_ot_columns(df)
            df['Team'] = df['Unnamed: 0'].str.extract(r'(\D+)(?:\d+-\d*|\d*$)')
            df = df.drop('Unnamed: 0', axis=1)
            team_names = drop_leading_space(df['Team'].tolist())
            df = drop_leading_space_df(df)
            if nan_values(df) or not valid_teams(team_names) or cancelled_game(df):
                if inconsistent_team_names(team_names):
                    df = change_to_consistent_names(df)
                else:
                    continue
            df = df.drop('2', axis=1)
            df = restructure_home_away(df)
            master_df = pd.concat([master_df,df], ignore_index= True)
        master_df.to_csv('./Scores/' + date + '.csv', index = False)
    master_df = master_df.reset_index(drop=True)

    master_df.to_csv('./Scores/test.csv', index = False)