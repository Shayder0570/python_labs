from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


if __name__ == '__main__':
    json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
    print('Создан data/out/people_from_json.csv')
    json_to_csv('data/samples/people_missing.json', 'data/out/people_missing.csv')
    print('Создан data/out/people_missing.csv')
    csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
    print('Создан data/out/people_from_csv.json')
    csv_to_json('data/samples/people_missing.csv', 'data/out/people_missing.json')
    print('Создан data/out/people_missing.json')
    csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')
    print('Создан data/out/people.xlsx')
    csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')
    print('Создан data/out/cities.xlsx')
