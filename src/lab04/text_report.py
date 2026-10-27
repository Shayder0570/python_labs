import argparse
import sys
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n


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
