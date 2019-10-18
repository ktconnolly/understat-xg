import argparse
import json
import re
import csv
import requests


def get_json(url):
    response = requests.get(url)
    data = re.search("shotsData\s+=\s+JSON.parse\('([^']+)", response.text)
    decoded_string = bytes(data.groups()[0], 'utf-8').decode('unicode_escape')
    match_json = json.loads(decoded_string)
    return match_json['h'] + match_json['a']


def write_csv(match_json):
    date = match_json[0]['date'].split()[0]
    home_team = match_json[0]['h_team']
    away_team = match_json[0]['a_team']

    filename = f'{date}-{home_team} vs {away_team}.csv'

    with open(filename, mode='w', newline='') as f:
        csv_writer = csv.writer(f)

        # Write headers
        csv_writer.writerow(
            [
                'Date',
                'Home',
                'Away',
                'Home Goals',
                'Away Goals',
                'Team',
                'Minute',
                'Player',
                'xG',
                'Shot Type',
                'Result',
                'X Coordinate',
                'Y Coordinate',
                'Situation',
                'Assist Player',
                'Last Action'
            ]
        )

        for shot in match_json:
            # Replace 'h' and 'a' with actual team names
            if shot['h_a'] == 'h':
                shot_team = shot['h_team']
            elif shot['h_a'] == 'a':
                shot_team = shot['a_team']
            else:
                shot_team = None

            csv_writer.writerow(
                [
                    shot['date'],
                    shot['h_team'],
                    shot['a_team'],
                    shot['h_goals'],
                    shot['a_goals'],
                    shot_team,
                    shot['minute'],
                    convert_apostrophe(shot['player']),
                    shot['xG'],
                    shot['shotType'],
                    shot['result'],
                    shot['X'],
                    shot['Y'],
                    shot['situation'],
                    convert_apostrophe(shot['player_assisted']),
                    shot['lastAction']
                ]
            )


def convert_apostrophe(string):
    if string is None:
        return None

    return string.replace('&#039;', "'")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('match_id', help='ID for the match eg. 7426')
    args = parser.parse_args()

    url = f'https://understat.com/match/{args.match_id}'
    match_json = get_json(url)
    write_csv(match_json)


if __name__ == '__main__':
    main()
