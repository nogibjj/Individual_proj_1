"""main file with main functions"""

import pandas as pd
import matplotlib.pyplot as plt

# import markdownify
from ydata_profiling import ProfileReport


FILE_PATH = "NBA_24_stats.csv"
df = pd.read_csv(FILE_PATH)


def summary():
    """provides summary statistics"""
    summary_stats = df.describe()
    print(summary_stats)


def points_plot():
    """provides visualization"""
    accurate = df[df["3P%"] >= 0.5]
    player_rank = accurate["Player"].astype(str) + ", " + accurate["3P%"].astype(str)
    plt.bar(player_rank, accurate["PTS"], color="green", width=0.9)
    plt.xticks(rotation="vertical")
    plt.xlabel("Players and 3P%")
    plt.ylabel("PPG")
    plt.title("PPG for Players with higher than 50% 3P%")
    plt.subplots_adjust(bottom=0.43)
    plt.show()


def report():
    "generates report and converts to markdown"
    profile = ProfileReport(df, title="NBA Statistics")
    profile.to_notebook_iframe()
    profile.to_file("NBA_report.html")


points_plot()
