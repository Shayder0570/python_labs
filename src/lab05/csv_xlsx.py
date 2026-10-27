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
