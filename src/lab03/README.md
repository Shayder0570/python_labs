## ЛР3 — Тексты и частоты слов (словарь/множество)
### * Задание 1 — text.py

#### В коде реализованы функции:
* normalize():
Если casefold=True — приводит к casefold. Если casefold=False - используется lower(). @changelog: 29.09
Если yo2e=True — заменяется все ё/Ё на е/Е.
Убрает невидимые управляющие символы (например, \t, \r) → заменяет на пробелы, схлопывает повторяющиеся пробелы в один.
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text: return text
    if casefold: text = text.casefold()
    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    return ' '.join(text.split())
```

* tokenize():
Разбивает на «слова» по небуквенно-цифровым разделителям.
В качестве слова считается последовательности символов \w (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
Числа (например, 2025) считются словами.

```python
def tokenize(text: str) -> list[str]: 
    return re.findall(r'\w+(?:-\w+)*', text)
```
* count_freq():
Подсчитывает частоты, вернуть словарь слово → количество.

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    result = {}
    for token in tokens:
        try:
            result[token] += 1
        except KeyError:
            result.update({token:1})
    return result
```
* top_n():
Возвращает топ-N по убыванию частоты; при равенстве — по алфавиту слова
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError("число n не может быть отрицательным")
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```

### Тест-кейсы:




![Пример работы](https://github.com/Shayder0570/python_labs/blob/main/images/lab03/text.png)

### * Задание 2 — text_stats.py

#### Скрипт читает одну строку текста из stdin (или весь ввод до EOF — на ваш выбор, опишите в README), вызывает функции из lib/text.py и печатает:
##### ```Всего слов: <N>```
##### ```Уникальных слов: <K>```
##### ```Топ-5:```

```python
from text import *
import sys

def text_statistic(text: str, n: int = 3, table_form: bool = False) -> str:
    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    counts = count_freq(tokens)

    if n > len(counts.keys()):
        n = len(counts.keys())

    top = top_n(freq=counts, n=n)

    if table_form:
        table = []
        max_len = max(len(max(tokens, key=len)), len('Слово')) + 5
        max_num_len = max(max(counts.values()), len('Частота')) + 2
        table.append(f'{'Слово':<{max_len}}|{'Частота':>{max_num_len}}')
        table.append('-' * (max_len)  + '-' * (max_num_len))

        for word in counts.keys():
            count = counts[word]
            table.append(f'{word:<{max_len}}|{count:>{max_num_len}}')
        
        return '\n'.join(table)

    else:
        top_text = "\n".join(
            f"{word}: {count}"
            for word, count in top
        )

        return (
            f"Всего слов: {len(tokens)}\n"
            f"Уникальных слов: {len(counts)}\n"
            f"Топ слов:\n{top_text}"
        )

print('Введите что-либо:(для завершения- Ctrl+D)', end='\n')
text = sys.stdin.read()

print(text_statistic(text, table_form=True, n=100))
```

### Тест-кейсы: 

![Пример работы](https://github.com/Shayder0570/python_labs/blob/main/images/lab03/text_stats.png)


