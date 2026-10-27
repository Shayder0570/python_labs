import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    with open(path, 'r', encoding=encoding) as file:
        return file.read()


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    if header is not None:
        length = len(header)
    elif rows:
        length = len(rows[0])
    else:
        length = 0

    for row in rows:
        if len(row) != length:
            raise ValueError('Все строки CSV должны иметь одинаковую длину')

    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)
