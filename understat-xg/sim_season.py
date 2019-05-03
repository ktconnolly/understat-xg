import argparse
import random
import pandas as pd
from scipy.stats import skellam


def sim_season(dataframe, iterations):
    # Team names as keys and points (initially 0) as values
    d = dict.fromkeys(
        dataframe['Home'].unique().tolist(), 0
    )

    for _ in range(iterations):
        for _, row in dataframe.iterrows():
            h_xg = row['Home xG']
            a_xg = row['Away xG']

            # Calculate prob of home winning by 1-10 goals
            h_win = sum(
                [skellam.pmf(sup, h_xg, a_xg) for sup in range(1, 10)]
            )

            # Calculate prob of away winning by 1-10 goals
            a_win = sum(
                [skellam.pmf(-sup, h_xg, a_xg) for sup in range(1, 10)]
            )

            # Supremacy of 0 is a draw
            draw = skellam.pmf(0, h_xg, a_xg)

            # Calculate match outcome
            result = random.choices(
                ('Home', 'Draw', 'Away'),
                weights=[h_win, draw, a_win]
            )[0]

            # Add 3 points for win, 1 for draw
            if result == 'Home':
                d[row.Home] += 3
            elif result == 'Away':
                d[row.Away] += 3
            else:
                d[row.Home] += 1
                d[row.Away] += 1

    # Update dict with average points rather than total
    d.update((team, pts / iterations) for team, pts in d.items())

    # Create a list sorted by points
    points_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

    return points_sorted


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to CSV file')
    parser.add_argument('iterations', help='Number of iterations', type=int)
    args = parser.parse_args()

    df = pd.read_csv(args.filename)
    points = sim_season(df, args.iterations)

    for team in points:
        print(f'{team[0]} - {team[1]:.1f}')


if __name__ == '__main__':
    main()
