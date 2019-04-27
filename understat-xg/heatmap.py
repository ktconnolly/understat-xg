import argparse
import csv
import matplotlib.pyplot as plt
import numpy as np


def get_coordinates(filename):
    with open(filename, mode='r') as f:
        shots_data = csv.reader(f)

        header = next(shots_data)

        # Get column numbers from header
        x_index = header.index('X Coordinate')
        y_index = header.index('Y Coordinate')
        situation_index = header.index('Situation')
        result_index = header.index('Result')

        x_coordinates = []
        y_coordinates = []
        for row in shots_data:
            if row[situation_index] == 'Penalty':
                continue

            if row[result_index] == 'OwnGoal':
                continue

            x = float(row[x_index]) * 100
            y = float(row[y_index]) * 100

            # Change goal line from 100 to 0
            x_coordinates.append(100 - x)
            y_coordinates.append(100 - y)

    return x_coordinates, y_coordinates


def create_heatmap(x_coordinates, y_coordinates):
    plt.hist2d(x_coordinates, y_coordinates,
               bins=(100, 100), range=np.array([(0, 100), (0, 100)]))

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
