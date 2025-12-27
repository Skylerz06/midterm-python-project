# src/analysis.py
import pandas as pd

def commits_per_month(df):
    # return lượng commit mỗi tháng theo năm
    return df.groupby(['year', 'month']).size()

def top_authors(df, top_n=10):
    return df['author'].value_counts().head(top_n)

def contribution_rate_author(df):
    # Tỉ lệ được tính theo số lượng commit của mỗi author so với tổng số lượng commit của repo
    contribution_stats = df.groupby(['repo', 'author']).size().reset_index(name='author_commits')
    contribution_stats['total_repo_commits'] = contribution_stats.groupby('repo')['author_commits'].transform('sum')
    contribution_stats['contribution_percentage'] = ((contribution_stats['author_commits'] / contribution_stats['total_repo_commits']) * 100).round(2)
    result = contribution_stats.groupby('repo').apply(
        lambda x: x.sort_values(by='contribution_percentage', ascending=False).head(1),
        include_groups=False
    ).reset_index(level=1, drop=True)  
    return result

def classify_commit(message):
    message = message.lower()
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


def message_length_stats(df):
    df['message_length'] = df['message'].str.len()
    
    stats = {
        'mean': df['message_length'].mean(),
        'median': df['message_length'].median(),
        'min': df['message_length'].min(),
        'max': df['message_length'].max(),
        'std': df['message_length'].std()
    }
    
    # Phân loại độ dài message
    bins = [0, 50, 100, 200, 500, float('inf')]
    labels = ['Rất ngắn (0-50)', 'Ngắn (51-100)', 'Trung bình (101-200)', 'Dài (201-500)', 'Rất dài (>500)']
    df['length_category'] = pd.cut(df['message_length'], bins=bins, labels=labels)
    
    return stats, df['length_category'].value_counts()

def commits_by_time_frame(df):
    # Tách giờ từ cột time (HH:MM:SS)
    df['hour'] = df['time'].str.split(':').str[0].astype(int)
    
    # Phân loại theo khung giờ
    def get_time_frame(hour):
        if 6 <= hour < 12:
            return 'Sáng (6h-12h)'
        elif 12 <= hour < 18:
            return 'Chiều (12h-18h)'
        elif 18 <= hour < 22:
            return 'Tối (18h-22h)'
        else:
            return 'Đêm (22h-6h)'
    
    df['time_frame'] = df['hour'].apply(get_time_frame)
    
    return df['hour'].value_counts().sort_index(), df['time_frame'].value_counts()
