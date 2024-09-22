"""main file with main functions"""

import polars as pl
import matplotlib.pyplot as plt
import markdownify as md
from ydata_profiling import ProfileReport


FILE_PATH = "NBA_24_stats.csv"
df = pl.read_csv(FILE_PATH, ignore_errors=True)
df_3p = pl.read_csv(FILE_PATH, ignore_errors=True).filter(pl.col("3P%") >= 0.5)


def summary():
    """provides summary statistics"""
    summary_stats = df.describe()
    print(summary_stats)


def points_plot():
    """provides visualization"""
    # player_rank = df.select(pl.col("Player"))
    plt.bar(df_3p["Player"], df_3p["PTS"], color="green", width=0.9)
    plt.xticks(rotation="vertical")
    plt.xlabel("Players")
    plt.ylabel("PPG")
    plt.title("PPG for Players with higher than 50% 3P%")
    plt.subplots_adjust(bottom=0.43)
    plt.savefig("NBA_pts_bar.png")
    plt.show()


def report():
    "generates report and converts to pdf"
    profile = ProfileReport(df, title="NBA Statistics")
    export = profile.to_html()
    markdown = md.markdownify(export)
    with open("NBA_report.md", "w", encoding="utf-8") as f_write:
        f_write.write(markdown)


points_plot()
summary()
# report()
