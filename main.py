"""main file with main functions"""

import pandas as pd
import matplotlib.pyplot as plt


file_path = "NBA_24_stats.csv"
df = pd.read_csv(file_path)

# Show the first few rows
# print(df["Player"])


def summary():
    summary_stats = df.describe()
    print(summary_stats)


# summary()


def points_plot():
    player_name = df["Player"].astype(str)
    player_rank = df["Rk"].astype(str)
    plt.bar(player_rank, df["PTS"])
    plt.show()
    return


points_plot()
