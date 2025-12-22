# src/preprocess.py
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Giữ các cột cần thiết
    df = df[['message', 'author', 'date']]

    # Xóa dòng thiếu dữ liệu
    df.dropna(inplace=True)

    # Chuyển commit_date sang datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)

    # Chuẩn hóa message về chữ thường
    df['message'] = df['message'].str.lower()
    return df
