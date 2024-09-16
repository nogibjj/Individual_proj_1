# First_project
Data engineering gitlab template

[![CI](https://github.com/nogibjj/First_project/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/First_project/actions/workflows/hello.yml)

Requirements

- Python script using Pandass for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization

Dataset
- Basketball Referemce 2023-2024 NBA Player Stats: Per Game
    - https://www.basketball-reference.com/leagues/NBA_2024_per_game.html#per_game_stats

Required Files

- requirements.txt
    - required dependencies to run this file
    - provides required versions of devops and web components
- MAKEFILE
    - instructions to install, format, lint, and test python files
- devcontainer
    - devcontainer.json
        - contains docker container for python 3 dependencies
- main.py
    - contains code to subtract two numbers
- test_main.py
    - contains code to test main.py file
- hello.yml
    - provides the functionality to do CI runs
- .gitignore
    - ignores unecessary files and programs to prevent installation conflicts