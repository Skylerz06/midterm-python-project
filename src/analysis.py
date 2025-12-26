# src/analysis.py
import pandas as pd

def commits_per_month(df):
    # Ensure 'date' column is datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.to_period('M')
    return df.groupby('month').size()

def top_authors(df, top_n=10):
    return df['author'].value_counts().head(top_n)

def classify_commit(message):
    if any(k in message for k in ['fix', 'bug', 'error', 'issue']):
        return 'Bugfix'
    elif any(k in message for k in ['feat', 'feature', 'add']):
        return 'Feature'
    elif any(k in message for k in ['refactor', 'clean']):
        return 'Refactor'
    elif any(k in message for k in ['doc', 'readme']):
        return 'Documentation'
    elif any(k in message for k in ['test', 'testing']):
        return 'Test'
    else:
        return 'Other'

def commit_type_ratio(df):
    df['commit_type'] = df['message'].apply(classify_commit)
    return df['commit_type'].value_counts()
