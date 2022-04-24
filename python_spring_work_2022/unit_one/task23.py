# todo: Взлом шифра
"""Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу."""

# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

kod_cezar = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."


def english_alfa():
    "Буквы английского алфавита"
    english = ''.join([chr(i) for i in range(ord("a"), ord("a") + 26)])
    return english


def shifr_cezar_for(s_alfa, kod_cezar):  # для примера
    "ДеШифрование, поиск в цикле"
    shag = -8
    copy_the = kod_cezar[:]
    for f in range(1, 5):
        kod_cezar = copy_the
        i_index = 0
        for i in kod_cezar:
            if i in s_alfa:
                r_alfa = s_alfa + s_alfa
                step1 = kod_cezar[i_index:].replace(i, r_alfa[r_alfa.index(i, 0) + shag], 1)
                kod_cezar = kod_cezar[:i_index] + step1
            i_index += 1
        shag += 1
        print(f, kod_cezar, shag - 1)


def shifr_cezar(s_alfa, kod_cezar):  # для примера
    "ДеШифрование"
    shag = -6
    copy_the = kod_cezar[:]
    kod_cezar = copy_the
    i_index = 0
    for i in kod_cezar:
        if i in s_alfa:
            r_alfa = s_alfa + s_alfa
            step1 = kod_cezar[i_index:].replace(i, r_alfa[r_alfa.index(i, 0) + shag], 1)
            kod_cezar = kod_cezar[:i_index] + step1
        i_index += 1
    print("Зашифрованное предложение:", kod_cezar, "\nШаг сдвига", shag)


alfa = english_alfa()
# shifr_cezar_for(alfa, kod_cezar)
shifr_cezar(alfa, kod_cezar)
