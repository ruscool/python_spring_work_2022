

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
