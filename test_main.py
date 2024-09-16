""" file for testing code"""

from main import summary, points_plot


def test_summary():
    summary()


def test_plot():
    points_plot()


if __name__ == "__main__":
    test_summary()
    test_plot()
