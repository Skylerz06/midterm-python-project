# main.py
from src.preprocess import load_and_clean_data
from src.analysis import commits_per_month, top_authors, bugfix_ratio
from src.visualization import (
    plot_commits_per_month,
    plot_top_authors,
    plot_bugfix_ratio
)

DATA_PATH = './data/commit_20000.csv'

def main():
    df = load_and_clean_data(DATA_PATH)

    commits_month = commits_per_month(df)
    authors = top_authors(df)
    bug_ratio = bugfix_ratio(df)

    plot_commits_per_month(commits_month)
    plot_top_authors(authors)
    plot_bugfix_ratio(bug_ratio)

if __name__ == '__main__':
    main()
