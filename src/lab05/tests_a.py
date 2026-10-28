import csv
import json
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def main() -> None:
    samples = Path('data/samples/lab05_tests_a')
    results = Path('data/out/lab05_tests_a')
    samples.mkdir(parents=True, exist_ok=True)
    results.mkdir(parents=True, exist_ok=True)
    total = 0

    data = [{'name': 'Анна', 'age': 19},
            {'name': 'Иван, Иванов', 'city': 'Москва'}]
    with (samples / 'people.json').open('w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    json_to_csv(str(samples / 'people.json'), str(results / 'people.csv'))
    with (results / 'people.csv').open(encoding='utf-8', newline='') as file:
        rows = list(csv.reader(file))
    assert rows == [['name', 'age', 'city'],
                    ['Анна', '19', ''], ['Иван, Иванов', '', 'Москва']]
    print('JSON -> CSV: ключи, пропуски и запятая в значении — OK')
    total += 1

    csv_to_json(str(results / 'people.csv'), str(results / 'people.json'))
    text = (results / 'people.json').read_text(encoding='utf-8')
    assert json.loads(text) == [
        {'name': 'Анна', 'age': '19', 'city': ''},
        {'name': 'Иван, Иванов', 'age': '', 'city': 'Москва'}]
    assert 'Анна' in text and '\n  {' in text
    print('CSV -> JSON: строки, кириллица и отступы — OK')
    total += 1

    json_cases = [('empty', ''), ('empty_list', '[]'),
                  ('wrong_structure', '[1]'), ('invalid', '{')]
    for name, text in json_cases:
        path = samples / (name + '.json')
        path.write_text(text, encoding='utf-8')
        try:
            json_to_csv(str(path), str(results / 'error.csv'))
        except ValueError:
            print(f'{name}.json: ValueError — OK')
            total += 1
        else:
            raise AssertionError(f'{name}.json: ожидался ValueError')

    csv_cases = [('empty', ''), ('header_only', 'name,age\n'),
                 ('duplicate_header', 'name,name\nАнна,19\n'),
                 ('short_row', 'name,age\nАнна\n'),
                 ('empty_header', ',age\nАнна,19\n')]
    for name, text in csv_cases:
        path = samples / (name + '.csv')
        path.write_text(text, encoding='utf-8')
        try:
            csv_to_json(str(path), str(results / 'error.json'))
        except ValueError:
            print(f'{name}.csv -> JSON: ValueError — OK')
            total += 1
        else:
            raise AssertionError(f'{name}.csv -> JSON: ожидался ValueError')

    extension_cases = [
        (json_to_csv, samples / 'people.json', results / 'wrong.txt'),
        (csv_to_json, results / 'people.csv', results / 'wrong.txt')]
    for function, source, target in extension_cases:
        try:
            function(str(source), str(target))
        except ValueError:
            print(f'{function.__name__}: неверное расширение — OK')
            total += 1
        else:
            raise AssertionError('Неверное расширение: ожидался ValueError')

    missing_cases = [
        (json_to_csv, samples / 'missing.json', results / 'missing.csv'),
        (csv_to_json, samples / 'missing.csv', results / 'missing.json')]
    for function, source, target in missing_cases:
        try:
            function(str(source), str(target))
        except FileNotFoundError:
            print(f'{function.__name__}: файл отсутствует — OK')
            total += 1
        else:
            raise AssertionError('Отсутствующий файл: ожидался FileNotFoundError')

    print(f'Задание A: {total} проверок. Все пройдены.')


if __name__ == '__main__':
    main()
