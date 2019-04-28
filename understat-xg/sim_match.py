import argparse
import random
import pandas as pd
import numpy as np


def sim_match(data_frame):
    sup = 0
    h_shots = []
    a_shots = []

    for index, row in data_frame.iterrows():
        if row['Team'] == row['Home']:
            h_shots.append(row['xG'])
        else:
            a_shots.append(row['xG'])

        if row['Result'] == 'OwnGoal':
            continue

        if check_goal(row['xG']):
            if row['Team'] == row['Home']:
                sup += 1
            else:
                sup -= 1

    return sup


def check_goal(xg):
    if random.random() <= float(xg):
        return True
    else:
        return False


def results(supremacies):
    home_wins, draws, away_wins = 0, 0, 0

    for result in supremacies:
        if result > 0:
            home_wins += 1
        elif result < 0:
            away_wins += 1
        else:
            draws += 1

    home_wins = home_wins / len(supremacies)
    draws = draws / len(supremacies)
    away_wins = away_wins / len(supremacies)

    return home_wins, draws, away_wins


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to CSV file')
    args = parser.parse_args()

    df = pd.read_csv(args.filename)
    sups = [sim_match(df) for _ in range(10000)]

    home_win, draw, away_win = results(sups)
    print(f'Average supremacy - {np.mean(sups)}\n'
          f'Home wins - {home_win:.1%}\n'
          f'Draws - {draw:.1%}\n'
          f'Away wins - {away_win:.1%}\n')


if __name__ == '__main__':
    main()


