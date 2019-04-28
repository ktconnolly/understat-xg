import argparse
import csv
import matplotlib.pyplot as plt
import numpy as np


def get_coordinates(filename):
    with open(filename, mode='r') as f:
        shots_data = csv.reader(f)

        header = next(shots_data)

        # Get column numbers from header
        x = header.index('X Coordinate')
        y = header.index('Y Coordinate')
        situation = header.index('Situation')
        result = header.index('Result')

        x_coords = []
        y_coords = []
        for row in shots_data:
            if row[situation] == 'Penalty':
                continue

            if row[result] == 'OwnGoal':
                continue

            x_coord = float(row[x]) * 100
            y_coord = float(row[y]) * 100

            # Change goal line from 100 to 0
            x_coords.append(100 - x_coord)
            y_coords.append(100 - y_coord)

    return x_coords, y_coords


def create_heatmap(x_coordinates, y_coordinates):
    plt.hist2d(
        x_coordinates, y_coordinates,
        bins=(100, 100),
        range=np.array([(0, 100), (0, 100)])
    )

    # Plot six yard box
    plt.plot([0, 6], [63, 63], color='w', linewidth=3)
    plt.plot([0, 6], [37, 37], color='w', linewidth=3)
    plt.plot([6, 6], [63, 37], color='w', linewidth=3)

    # Plot penalty area
    plt.plot([0, 17], [78, 78], color='w', linewidth=3)
    plt.plot([0, 17], [22, 22], color='w', linewidth=3)
    plt.plot([17, 17], [78, 22], color='w', linewidth=3)

    # Add penalty spot
    plt.plot(11.5, 50, 'wo', linewidth=3)

    plt.axis('off')
    plt.title('Title', fontsize=14)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to CSV file')
    args = parser.parse_args()

    x, y = get_coordinates(args.filename)
    create_heatmap(x, y)


if __name__ == '__main__':
    main()
