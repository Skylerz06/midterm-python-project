# main.py
from src.preprocess import load_and_clean_data
from src.analysis import (
    commits_per_month, 
    top_authors, 
    commit_type_ratio, 
    contribution_rate_author,
    message_length_stats,
    commits_by_time_frame
)
from src.visualization import (
    plot_commits_per_month,
    plot_top_authors,
    plot_commit_type_ratio,
    plot_message_length,
    plot_commits_by_time
)

DATA_PATH = './project/data/sampled.csv'

def main():
    df = load_and_clean_data(DATA_PATH)


    commits_month = commits_per_month(df)
    authors = top_authors(df)
    commit_types = commit_type_ratio(df)

    print(contribution_rate_author(df))
    print('\n')

    msg_stats, msg_categories = message_length_stats(df)
    print(f"Trung bình: {msg_stats['mean']:.2f} ký tự")
    print(f"Trung vị: {msg_stats['median']:.2f} ký tự")
    print(f"Nhỏ nhất: {msg_stats['min']} ký tự")
    print(f"Lớn nhất: {msg_stats['max']} ký tự")
    print(f"\nPhân bố theo category:\n{msg_categories}")
    print('\n')

    hourly_commits, time_frame_commits = commits_by_time_frame(df)
    print(f"Phân bố theo khung giờ:\n{time_frame_commits}")
    print('\n')

    plot_commits_per_month(commits_month)
    plot_top_authors(authors)
    plot_commit_type_ratio(commit_types)
    plot_message_length(msg_stats, msg_categories)
    plot_commits_by_time(hourly_commits, time_frame_commits)

if __name__ == '__main__':
    main()
