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
В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.
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
    f = open(file, 'r')
    s_text = str()
    for i in range(lines):
        i_index = 0
        file = f.readline()
        new_line = file.lower().strip()
        for letter in new_line:
            if letter in alfa:
                text = alfa[alfa.index(letter) - shag]
                new_line = new_line[:i_index] + text + new_line[i_index + 1:]
            i_index += 1
        shag += 1
        if len(s_text) == 0:
            s_text = s_text + new_line
        else:
            s_text = s_text + "\n" + new_line
    f.close()
    return s_text


def cezar_shifr():
    "Буквы алфавита"
    alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    a_lower = alfavit.lower()
    return a_lower


file = "message.txt"
shifr = cezar_shifr()
count_lines = count_line(file)
print(open_file(shifr, file, count_lines))
