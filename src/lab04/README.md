## ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике
### * Задание 1 — io_txt_csv.py

#### В коде реализованы функции:
* read_text():
Читает файл в указанной кодировке и возвращает его содержимое одной строкой.
По умолчанию используется UTF-8. Для другой кодировки можно передать encoding="cp1251".
Если файл не найден — возникает FileNotFoundError, если кодировка не подходит — UnicodeDecodeError.
Пустой файл возвращает пустую строку. Файл читается целиком; для больших файлов лучше использовать построчное чтение.

```python
def read_text(path: str | Path, encoding: str = 'utf-8') -> str:
    with open(path, 'r', encoding=encoding) as file:
        return file.read()
```

* write_csv():
Записывает строки в CSV с разделителем-запятой и кодировкой UTF-8.
Если передан header, записывает его первой строкой.
Проверяет одинаковую длину строк и соответствие длине заголовка. При несовпадении возникает ValueError.
Пустой rows без header создаёт пустой файл. С header — файл только с заголовком.
Файл открывается через with, поэтому закрывается после выхода из блока.
Параметр newline="" используется, чтобы при записи CSV на Windows не появлялись лишние пустые строки.

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

#### Скрипт читает текст из одного файла, вызывает функции из lib/text.py, сохраняет частоты в CSV и печатает:
##### `Всего слов: <N>`
##### `Уникальных слов: <K>`
##### `Топ-5:`

Без аргументов читает data/lab04/input.txt и сохраняет результат в data/lab04/report.csv.
Путь входного файла задаётся через --in, выходного — через --out, кодировка — через --encoding.
Все слова записываются в CSV с колонками word,count: по убыванию частоты, при равенстве — по алфавиту.
В консоли выводятся только первые пять слов.
Если входной файл пустой, отчёт содержит только заголовок word,count.
При ошибке чтения, кодировки или записи программа выводит сообщение в stderr и завершается с кодом 1.

Запуск из корня репозитория: `python3 -m src.lab04.text_report`.
Пример с другой кодировкой: `python3 -m src.lab04.text_report --in data/lab04/cp1251.txt --encoding cp1251`.

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
