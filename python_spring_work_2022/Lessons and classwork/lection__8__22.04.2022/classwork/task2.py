# todo: Шифр Цезаря
"""Описание шифра.
В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
является одним из самых простых и широко известных методов шифрования.
Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

Задача.
Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
В каждой строчке содержатся различные символы. Шифровать нужно только буквы латинского алфавита.
"""


def count_line(file):
    "Подсчет строк в файле"
    f = open(file, "r")
    text = f.read()
    count_line = text.count("\n")
    return count_line


def open_file(alfa, file, lines):
    "Шифрование"
    shag = 1
    digi = "0123456789"
    english = ''.join([chr(i) for i in range(ord("a"), ord("a") + 26)])
    hz = ''.join([chr(i) for i in range(35, 48)])
    f = open(file, 'r')
    for i in range(lines):
        l = []
        file = f.readline()
        new_line = file.lower().strip()
        for letter in new_line:
            if letter in alfa:  # шифрование русских букв
                if not letter in l:
                    new_line = new_line.replace(letter, alfa[alfa.index(letter) - shag])
                    l.append(letter)
        for letter in new_line:
            if letter in digi:  # цифры
                if not letter in l:
                    new_line = new_line.replace(letter, digi[digi.index(letter) - shag])
                    l.append(letter)
        for letter in new_line:
            if letter in english:  # английский алфавит
                if not letter in l:
                    new_line = new_line.replace(letter, english[english.index(letter) - shag])
                    l.append(letter)
        for letter in new_line:
            if letter in hz:  # hz
                if not letter in l:
                    new_line = new_line.replace(letter, hz[hz.index(letter) - shag])
                    l.append(letter)
        shag += 1
        print(new_line)
    f.close()


def cezar_shifr():
    "Буквы алфавита"
    alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    a_lower = alfavit.lower()
    return a_lower


file = "message.txt"
shifr = cezar_shifr()
count_lines = count_line(file)
open_file(shifr, file, count_lines)
