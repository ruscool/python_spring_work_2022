# todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

# Формат вывода:
"""Количество букв a - 13
Количество букв o - 12
Количество букв e - 11
.....................
"""


def find2(file, glas):
    "Подсчет гласных"
    for i in file:
        if i in glas:
            glas[i] += 1
    for key, value in glas.items():
        print("Количество букв", key, ":", value)


def open_file():
    "Открытие и чтение файла"
    f = open("dump.txt", 'r')
    file = f.read()
    f.close()
    return file


alfa = {"а": 0, "о": 0, "е": 0, "у": 0, "э": 0, "ё": 0, "я": 0, "и": 0, "ю": 0, "ы": 0}
file = open_file()
find2(file, alfa)
