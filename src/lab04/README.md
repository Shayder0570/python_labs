## ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
### * Задание 1 — io_txt_csv.py

#### В коде реализованы функции:
* read_text():
Читает файл и возвращает текст одной строкой. По умолчанию кодировка UTF-8.

```python
def read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    with open(path, 'r', encoding=encoding) as file:
        return file.read()
```

* write_csv():
Записывает строки в CSV. Если длины строк различаются, вызывает ValueError.

```python
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
```

### Тест-кейсы:

![Пример работы](https://github.com/Shayder0570/python_labs/blob/main/images/lab04/skip.gif)

### * Задание 2 — text_report.py

#### Скрипт читает файл, сохраняет частоты слов в CSV и печатает:
##### `Всего слов: <N>`
##### `Уникальных слов: <K>`
##### `Топ-5:`

Запуск: `python3 -m src.lab04.text_report`.

```python
def main() -> int:
    parser = argparse.ArgumentParser(description='Частоты слов в текстовом файле')
    parser.add_argument('--in', dest='input_file', default='data/lab04/input.txt',
                        help='входной TXT')
    parser.add_argument('--out', dest='output_file', default='data/lab04/report.csv',
                        help='выходной CSV')
    parser.add_argument('--encoding', default='utf-8', help='кодировка входного файла')
    args = parser.parse_args()

    try:
        text = read_text(args.input_file, encoding=args.encoding)
    except (OSError, UnicodeError, LookupError) as error:
        print(f'Ошибка: {error}', file=sys.stderr)
        return 1

    tokens = tokenize(normalize(text))
    counts = count_freq(tokens)
    rows = top_n(counts, len(counts))

    try:
        write_csv(rows, args.output_file, header=('word', 'count'))
    except OSError as error:
        print(f'Ошибка: {error}', file=sys.stderr)
        return 1

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(counts)}')
    print('Топ-5:')
    for word, count in top_n(counts):
        print(f'{word}:{count}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

### Тест-кейсы:

![Пример работы](https://github.com/Shayder0570/python_labs/blob/main/images/lab04/text_report.png)
