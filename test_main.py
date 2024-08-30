''' file for testing code'''
from main import subtract


def test_subtract():
    assert subtract(3, 2) == 1


if __name__ == "__main__":
    test_subtract
