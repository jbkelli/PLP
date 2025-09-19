from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

def plot_publications_over_time(data):
    """Plots the number of publications over time."""
    publications_per_year = data['year'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=publications_per_year.index, y=publications_per_year.values)
    plt.title('Publications Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.xticks(publications_per_year.index)
    plt.grid()
    plt.show()

def plot_top_journals(data, top_n=10):
    """Plots the top N journals by number of publications."""
    top_journals = data['journal'].value_counts().head(top_n)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_journals.values, y=top_journals.index)
    plt.title(f'Top {top_n} Journals by Number of Publications')
    plt.xlabel('Number of Publications')
    plt.ylabel('Journal')
    plt.grid()
    plt.show()