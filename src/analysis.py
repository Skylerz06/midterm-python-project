# src/analysis.py
import pandas as pd

def commits_per_month(df):
    # Ensure 'date' column is datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.to_period('M')
    return df.groupby('month').size()
# ...existing code...

def top_authors(df, top_n=10):
    return df['author'].value_counts().head(top_n)

def bugfix_ratio(df):
    bug_keywords = ['fix', 'bug', 'error', 'issue']
    df['is_bugfix'] = df['message'].apply(
        lambda x: any(k in x for k in bug_keywords)
    )
    return df['is_bugfix'].value_counts()
