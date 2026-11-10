import lib 
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    #при необходимоости можно использовать другую кодировку(подать нужную в аргументе)
    try:
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        return "Файл не найден"
    except UnicodeDecodeError:
        return "Не удалось декодировать файл"


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    #проверка длины 
    if header is not None:
        length = len(header)
    elif rows:
        length = len(rows[0])
    else:
        length = 0
    for row in rows:
        if len(row) != length:
            raise ValueError('Все строки CSV должны иметь одинаковую длину')
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
