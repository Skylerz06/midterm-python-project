# src/preprocess.py
import pandas as pd
from datetime import datetime as dt

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    
    # Xóa các dòng thiếu dữ liệu hoặc trùng lặp
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # Chuyển đổi sang định dạng datetime.
    df['date'] = pd.to_datetime(df['date'].apply(lambda x: dt.strptime(x, "%a %b %d %H:%M:%S %Y %z")), utc=True)
    df.dropna(subset=['date'], inplace=True)

    # Thực hiện việc chuẩn hóa dữ liệu
    # Tách date thành các cột dday (yy/mm/dd), wday (tuần trong năm), month, year, time
    df['dday'] = df['date'].dt.date
    df['wday'] = df['date'].dt.weekday
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['time'] = df['date'].dt.strftime('%H:%M:%S')

    # Tách thông tin author thành 2 cột author (tên) và mail
    df = df.join(df['author'].str.split('(<)', expand=True, n=2))
    df = df.drop('author', axis=1)
    df = df.drop(1, axis=1)
    df = df.rename({0:'author', 2:'mail'}, axis=1)
    df['mail'] = df['mail'].str.strip('>')

    
    return df
