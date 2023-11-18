import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    csv_path = 'UpdateTeamAvgs/DailyStats/TeamAverages/November23/11-17-23.csv'
    df = pd.read_csv(csv_path)
    print(df['Team'].values)
    return teams[0] in df['Team'].values and teams[1] in df['Team'].values


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
def get_historical_game_data():
    year = '2023'
    month = '11'
    for day in range(6,7):
        day = str(day)
        if day in ['1','2','3','4','5','6','7','8','9']:
            day = '0' + day
        date = year + month + day
        URL = 'https://www.cbssports.com/college-basketball/scoreboard/FBS/' + date + '/'
        dfs = pd.read_html(URL)
        master_df = pd.DataFrame()
        for df in dfs:
            df = drop_ot_columns(df)
            df['Team'] = df['Unnamed: 0'].str.extract(r'\s*\d*([a-zA-Z\s.]+[a-zA-Z])\d+-\d+')
            df = df.drop('Unnamed: 0', axis=1)
            df = df.drop('2', axis=1)
            if nan_values(df) or not valid_teams(df['Team'].tolist()):
                continue
            df = restructure_home_away(df)
            master_df = pd.concat([df, master_df], ignore_index= True)
    master_df = master_df.reset_index(drop=True)

    master_df.to_csv('./Scores/test.csv', index = False)