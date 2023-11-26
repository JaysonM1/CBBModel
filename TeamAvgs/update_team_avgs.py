import pandas as pd
import os
import shutil
from datetime import datetime
DATE = datetime.now().strftime('%m-%d-%y')
CORE_URL = 'https://www.ncaa.com/stats/basketball-men/d1/current/team/'
csv_path = './TeamAvgs/DailyStats/TeamAverages/November23/' + DATE + '.csv'

def append_to_daily_main(df, col, corresponding_col):
    todays_df = pd.read_csv(csv_path)
    new_df = pd.merge(todays_df, df, on = 'Team')
    new_df[corresponding_col] = new_df[corresponding_col].fillna(new_df[col])
    new_df = new_df.drop(columns =  [col])
    new_df = new_df.drop_duplicates('Team')
    new_df.to_csv(csv_path, index=False)


def get_stat_df_for_today(init_df, code):
    for page in range(1,8):
        url = CORE_URL + code + '/p' + str(page)
        dfs = pd.read_html(url)
        df = dfs[0]
        init_df = pd.concat([init_df, df], ignore_index = True)
    return init_df


def get_init_df_for_stat(code):
    url = CORE_URL + code
    dfs = pd.read_html(url)
    df = dfs[0]
    return df


def update_ATRatios():
    code = '474'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'AST', 'TO'])
    append_to_daily_main(df, 'Ratio', 'ATRatio')


def update_Apg():
    code = '216'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'AST'])
    append_to_daily_main(df, 'APG', 'Apg')

def update_BPpg():
    code = '1284'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'Bench'])
    df.rename(columns={'PPG': 'pperg'}, inplace=True)
    append_to_daily_main(df, 'pperg', 'BPpg')

def update_Bpg():
    code = '214'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'BLKS'])
    append_to_daily_main(df, 'BKPG', 'Bpg')

def update_EFG():
    code = '1288'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','G', 'FGM', '3FG', 'FGA'])
    append_to_daily_main(df, 'Pct', 'EFG%')

def update_EFG():
    code = '1288'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','G', 'FGM', '3FG', 'FGA'])
    append_to_daily_main(df, 'Pct', 'EFG%')


def update_FBpg():
    code = '1285'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'FB pts'])
    df.rename(columns={'PPG': 'pperg'}, inplace=True)
    append_to_daily_main(df, 'pperg', 'FbP')

def update_FGp():
    code = '148'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'FGM', 'FGA'])
    append_to_daily_main(df, 'FG%', 'Fg%')


def update_FgD():
    code = '149'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'OPP FG', 'OPP FGA'])
    append_to_daily_main(df, 'OPP FG%', 'Fg%D')


def update_Fpg():
    code = '286'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'Fouls', 'DQ'])
    append_to_daily_main(df, 'PFPG', 'Fpg')

def update_FTApg():
    code = '638'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'FT', 'FTA'])
    append_to_daily_main(df, 'Avg', 'FTApg')


def update_FTp():
    code = '150'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'FT', 'FTA'])
    append_to_daily_main(df, 'FT%', 'FTp')

def update_FTMpg():
    code = '633'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'FT', 'FTA'])
    append_to_daily_main(df, 'Avg', 'FTMpg')


def update_RM():
    code = '151'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'REB', 'RPG', 'OPP REB', 'OPP RPG'])
    append_to_daily_main(df, 'REB MAR', 'RM')

def update_RDpg():
    code = '859'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'DRebs'])
    append_to_daily_main(df, 'RPG', 'RDpg')

def update_ROpg():
    code = '857'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'ORebs'])
    append_to_daily_main(df, 'RPG', 'ROpg')

def update_Rpg():
    code = '932'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'ORebs', 'DRebs', 'REB'])
    append_to_daily_main(df, 'RPG', 'Rpg')

def update_SD():
    code = '146'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'OPP PTS'])
    append_to_daily_main(df, 'OPP PPG', 'SD')


def update_SO():
    code = '145'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'PTS'])
    df.rename(columns={'PPG': 'pperg'}, inplace=True)
    append_to_daily_main(df, 'pperg', 'SO')


def update_SM():
    code = '147'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'PTS', 'OPP PTS', 'OPP PPG', 'PPG'])
    append_to_daily_main(df, 'SCR MAR', 'SM')

def update_Spg():
    code = '215'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'ST'])
    append_to_daily_main(df, 'STPG', 'Spg')


def update_TPApg():
    code = '625'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', '3FG', '3FGA'])
    append_to_daily_main(df, 'Avg', '3PApg')  


def update_TPp():
    code = '152'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', '3FG', '3FGA'])
    append_to_daily_main(df, '3FG%', '3P%') 

def update_TPpD():
    code = '518'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'Opp 3FGA', 'Opp 3FG'])
    append_to_daily_main(df, 'Pct', '3PD%')  

def update_TPpg():
    code = '153'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', '3FG'])
    append_to_daily_main(df,'3PG', '3Ppg')  

def update_TOM():
    code = '519'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'Opp TO', 'TO'])
    append_to_daily_main(df, 'Ratio', 'TOM')  

def update_TFpg():
    code = '931'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'Opp TO'])
    append_to_daily_main(df, 'Avg', 'TFpg') 

def update_Tpg():
    code = '217'
    df = get_init_df_for_stat(code)
    df = get_stat_df_for_today(df, code)
    df = df.drop(columns = ['Rank','GM', 'TO'])
    append_to_daily_main(df, 'TOPG', 'Tpg') 
 

def is_csv_present(year, month, day):

    file_path = os.path.join("TeamAvgs/DailyStats/TeamAverages/November23/", DATE + ".csv")
    return os.path.isfile(file_path) and file_path.lower().endswith('.csv')

def copy_and_rename_csv():
    # Construct source and destination paths
    source_path = os.path.join("TeamAvgs/DailyStats/TeamAverages/", "bare.csv")
    destination_path = os.path.join("TeamAvgs/DailyStats/TeamAverages/November23", DATE + ".csv")

    # Copy the file from source to destination
    shutil.copy(source_path, destination_path)

    # Optionally, rename the file
    os.rename(destination_path, os.path.join("TeamAvgs/DailyStats/TeamAverages/November23", DATE + ".csv"))


def update_team_stats_today():
    if is_csv_present():
        print("CSV is present")
        return
    else:
        copy_and_rename_csv()

    update_ATRatios()
    update_Apg()
    update_BPpg()
    update_Bpg()
    update_EFG()
    update_FBpg()
    update_FGp()
    update_FgD()
    update_Fpg()
    update_FTApg()
    update_FTp()
    update_FTMpg()
    update_RM()
    update_RDpg()
    update_ROpg()
    update_Rpg()
    update_SD()
    update_SM()
    update_Spg()
    update_TPApg()
    update_TPp()
    update_TPpD()
    update_TPpg()
    update_TOM()
    update_TFpg()
    update_Tpg()
    update_SO()
    

    
    
