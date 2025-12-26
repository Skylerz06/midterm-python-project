# src/visualization.py
import matplotlib.pyplot as plt

def plot_commits_per_month(series):
    series.sort_index().plot(kind='line')
    plt.title('Commits per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Commits')
    plt.tight_layout()
    plt.savefig("plot_commits_per_month.png")
    plt.show()

def plot_top_authors(series):
    series.plot(kind='bar')
    plt.title('Top Authors by Number of Commits')
    plt.xlabel('Author')
    plt.ylabel('Commits')
    plt.tight_layout()
    plt.savefig("plot_top_authors.png")
    plt.show()


def plot_commit_type_ratio(series):
    series.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Commits Type Ratio')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("plot_commit_type_ratio.png")
    plt.show()

