from pathlib import Path

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


def main():

    input_path = Path("data/lab04/input.txt")
    output_path = Path("data/lab04/report.csv")

    text = read_text(input_path)

    text = normalize(text)

    words = tokenize(text)

    freq = count_freq(words)

    sorted_words = sorted(
        freq.items(),
        key=lambda item: (-item[1], item[0])
    )

    write_csv(
        sorted_words,
        output_path,
        header=("word", "count")
    )

    print("Всего слов:", len(words))

    print("Уникальных слов:", len(freq))

    print("Топ-5:")

    for word, count in top_n(freq, 5):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()