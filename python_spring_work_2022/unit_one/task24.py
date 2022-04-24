# todo: Числа в буквы
"""Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
"""

english = ''.join([chr(i) for i in range(ord("a"), ord("a") + 26)])
first_line = "8 5 12 12 15"
second_line = "8 5 12 12 15 , 0 23 15 18 12 4 !"


def create_dict(alfa):
    "Создание словаря"
    # print(alfa)
    digi_dict = {}
    count = 1
    for i in alfa:
        digi_dict[count] = i
        count += 1
    return digi_dict


def insert_digi_second(d_digi, s_second_line):
    "Замена чисел на буквы 2"
    l2 = list(s_second_line.split(" "))
    i_index = 0
    for i in l2:
        for key in d_digi.keys():  # dict
            if i == str(key):
                l2[i_index] = d_digi[key]
            elif i == "0":
                l2[i_index] = " "
                break
        i_index += 1
    s_second_line = "".join(l2)
    return s_second_line


dict_alfa = create_dict(english)

print(insert_digi_second(dict_alfa, first_line))
print(insert_digi_second(dict_alfa, second_line))
