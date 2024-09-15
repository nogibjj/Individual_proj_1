"""main file with main functions"""

import pandas as pd
import matplotlib.pyplot as plt


FILE_PATH = "NBA_24_stats.csv"
df = pd.read_csv(FILE_PATH)

# Show the first few rows
# print(df["Player"])


def summary():
    """provides summary statistics"""
    summary_stats = df.describe()
    print(summary_stats)


# summary()


def points_plot():
    """provides visualization"""
    # player_name = df["Player"].astype(str)
    player_rank = df["Rk"].astype(str)
    plt.bar(player_rank, df["PTS"])
    plt.show()


points_plot()
