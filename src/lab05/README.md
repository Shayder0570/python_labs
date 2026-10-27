## ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)
### * Задание 1 — json_csv.py

#### В коде реализованы функции:
* json_to_csv():
Преобразует список словарей из JSON в CSV. Отсутствующие поля заполняет пустыми строками.

```python
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
```

* csv_to_json():
Преобразует CSV в JSON. Значения сохраняются строками.

```python
import csv
import json
from pathlib import Path

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
```

### Тест-кейсы:



### * Задание 2 — csv_xlsx.py

#### В коде реализована функция:
* csv_to_xlsx():
Переносит CSV на лист Sheet1 книги Excel. Ширина столбцов рассчитывается по содержимому.

```python
import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    source = Path(csv_path)
    target = Path(xlsx_path)
    if source.suffix.lower() != '.csv' or target.suffix.lower() != '.xlsx':
        raise ValueError('Нужны входной CSV и выходной XLSX')

    rows = []
    with source.open(encoding='utf-8', newline='') as file:
        for row in csv.reader(file):
            if row or not rows:
                rows.append(row)

    if len(rows) < 2 or not rows[0]:
        raise ValueError('В CSV должны быть заголовок и строки данных')
    if '' in rows[0] or len(set(rows[0])) != len(rows[0]):
        raise ValueError('Названия столбцов должны быть непустыми и уникальными')
    for row in rows:
        if len(row) != len(rows[0]):
            raise ValueError('Количество полей не совпадает с заголовком')

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Sheet1'
    for row in rows:
        sheet.append(row)

    for column in sheet.columns:
        width = 8
        for cell in column:
            cell.data_type = 's'
            if len(str(cell.value)) + 2 > width:
                width = len(str(cell.value)) + 2
        sheet.column_dimensions[column[0].column_letter].width = width

    workbook.save(target)
```

Запуск примеров: `./.venv/bin/python -m src.lab05.examples`.

### Тест-кейсы:

![Пример работы](https://github.com/Shayder0570/python_labs/blob/main/images/lab05/stop.gif)
