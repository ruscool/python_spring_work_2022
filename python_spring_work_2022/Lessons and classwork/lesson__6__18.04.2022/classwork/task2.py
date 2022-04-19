# :todo Написать функцию is_ascending(list_) проверки на монотонность?
"""Функция принимает список и определяет  является ли он монотонно возрастающим
(то есть проверяет верно ли, что каждый элемент этого списка больше предыдущего).
В качестве результата возвращайте  YES, если массив монотонно возрастает и NO в противном случае.

Пример:
mass = [ 2, 5, 7]

def is_ascending(list_):
    ваша реализация


result = is_ascending(mass)
print(result)
YES
"""
mass = [2, 5, 7, 45 ]


def is_ascending(list_):
    i, v = 0, -len(mass) + 1
    res = []
    for i in mass:
        if i < mass[v]:
            res.append(1)
        else:
            res.append(0)
        if v == -1:
            break
        else:
            v += 1
    for f in res:
        if 0 in res:
            s = "NO"
        else:
            s = "YES"""
    return s


result = is_ascending(mass)
print(result)
