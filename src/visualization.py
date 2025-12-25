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
    plt.ylabel('Author')
    plt.xlabel('Commits')
    plt.tight_layout()
    plt.savefig("plot_top_authors.png")
    plt.show()


def plot_bugfix_ratio(series):
    series.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Bugfix vs Other Commits')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("plot_bugfix_ratio.png")
    plt.show()

