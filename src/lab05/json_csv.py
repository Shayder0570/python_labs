import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    source = Path(json_path)
    target = Path(csv_path)
    if source.suffix.lower() != '.json' or target.suffix.lower() != '.csv':
        raise ValueError('Нужны входной JSON и выходной CSV')

    with source.open(encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError('Некорректный или пустой JSON')

    if not isinstance(data, list) or not data:
        raise ValueError('JSON должен содержать непустой список словарей')

    fields = []
    for row in data:
        if not isinstance(row, dict):
            raise ValueError('Каждый элемент JSON должен быть словарём')
        for key in row:
            if key not in fields:
                fields.append(key)

    if not fields:
        raise ValueError('В JSON нет названий столбцов')

    if '' in fields:
        raise ValueError('Название столбца не должно быть пустым')

    with target.open('w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    source = Path(csv_path)
    target = Path(json_path)
    if source.suffix.lower() != '.csv' or target.suffix.lower() != '.json':
        raise ValueError('Нужны входной CSV и выходной JSON')

    with source.open(encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        if not fields:
            raise ValueError('В CSV нет заголовка')
        if '' in fields or len(set(fields)) != len(fields):
            raise ValueError('Названия столбцов должны быть непустыми и уникальными')

        rows = []
        for row in reader:
            if None in row or None in row.values():
                raise ValueError('Количество полей не совпадает с заголовком')
            rows.append(row)

    if not rows:
        raise ValueError('В CSV нет строк данных')

    with target.open('w', encoding='utf-8') as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)
