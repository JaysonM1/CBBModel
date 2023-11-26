import pandas as pd
from datetime import datetime


def is_before_date(date_str1, date_str2):
    # Convert date strings to datetime objects
    date1 = datetime.strptime(date_str1, '%m-%d-%y')
    date2 = datetime.strptime(date_str2, '%m-%d-%y')

    # Compare the dates
    return date1 < date2


def build_model_today():
    month = '11'
    year = '23'
    first_stats_date = '11-21-23'
    for day in range(6,25):
        if day in ['1','2','3','4','5','6','7','8','9']:
            day = '0' + str(day)
        strings = [month, str(day), year]
        print(type(day), type(month), type(year))
        date = '-'.join(strings)
        if is_before_date(date, first_stats_date):
            stats_df = pd.read_csv('TeamAvgs/DailyStats/TeamAverages/November23/11-21-23.csv')
        print(stats_df)

            