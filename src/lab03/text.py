import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text: return text
    if casefold: text = text.casefold()
    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    return ' '.join(text.split())

#############################################################################
def tokenize(text: str) -> list[str]: 
    return re.findall(r'\w+(?:-\w+)*', text)
#############################################################################
def count_freq(tokens: list[str]) -> dict[str, int]:
    result = {}
    for token in tokens:
        try:
            result[token] += 1
        except KeyError:
            result.update({token:1})
    return result
#############################################################################
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError("число n не может быть отрицательным")
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
########################################################################################
print("!!!normalize:")
print(f" 'ПрИвЕт\nМИр\t'→{normalize('ПрИвЕт\nМИр\t')}")
print(f'"ёжик, Ёлка"→{normalize("ёжик, Ёлка")}')
print(f'"Hello\r\nWorld"→{normalize("Hello\r\nWorld")}')
print(f'"  двойные   пробелы  "→{normalize("  двойные   пробелы  ")}')
####
print("!!!tokenize:")
print(f'"привет мир"→{tokenize("привет мир")}')
print(f'"hello,world!!!"→{tokenize("hello,world!!!")}')
print(f'"по-настоящему круто"→{tokenize("по-настоящему круто")}')
print(f'"2025 год"→{tokenize("2025 год")}')
print(f'"emoji 😀 не слово"→{tokenize("emoji 😀 не слово")}')
###
print("!!!count_freq + top_n:")
print(f'["a","b","a","c","b","a"]→{top_n(count_freq(["a","b","a","c","b","a"]))}')
print(f'["bb","aa","bb","aa","cc"]→{top_n(count_freq(["bb","aa","bb","aa","cc"]))}')
