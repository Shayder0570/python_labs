from src.lab04.io_txt_csv import read_text, write_csv

txt = read_text("data/lab04/input.txt")  # должен вернуть строку

print(txt)

write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV

print("csv был создан")