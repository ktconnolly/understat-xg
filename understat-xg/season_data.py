import argparse
import json
import re
import csv
import requests


def get_json(url):
    response = requests.get(url)
    data = re.search("datesData\s+=\s+JSON.parse\('([^']+)", response.text)
    decoded_string = bytes(data.groups()[0], 'utf-8').decode('unicode_escape')
    season_json = json.loads(decoded_string)
    return season_json


def write_csv(season_json, filename='xg.csv'):
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
                'Home xG',
                'Away xG'
            ]
        )

        for match in season_json:
            csv_writer.writerow(
                [
                    match['datetime'],
                    match['h']['title'],
                    match['a']['title'],
                    match['goals']['h'],
                    match['goals']['a'],
                    match['xG']['h'],
                    match['xG']['a']
                ]
            )


def main():
    leagues = ['EPL', 'La_Liga', 'Bundesliga',
               'Serie_A', 'Ligue_1', 'RFPL']

    parser = argparse.ArgumentParser()
    parser.add_argument('league', help=', '.join(leagues))
    parser.add_argument('year', help='2014 - current')
    args = parser.parse_args()

    if args.league not in leagues:
        print(f'Invalid league: {args.league}')
        return

    url = f'https://understat.com/league/{args.league}/{args.year}'
    season_json = get_json(url)
    write_csv(season_json, filename=f'{args.league}_{args.year}.csv')


if __name__ == '__main__':
    main()
