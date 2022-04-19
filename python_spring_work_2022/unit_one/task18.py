# todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
"""и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

Пример вывода:
Сумма 2   комбинация [(1,1)]
Сумма 3   комбинация [(1,2),(2,1)]
Сумма 4   комбинация [(1,3),(3,1),(2,2)]
........................................
Выводы комбинаций оформить в список кортежей.
"""
import random


def numbers():  # кость игральная от 1 до 6
    "Подсчет"
    pass


def main(combi_main):
    "Основной расчет"
    s_list = []
    summa = combi_main[0] + combi_main[1]
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == summa:
                s_list.append((i, j,))
    tuple_list = sorted(tuple(s_list))
    return tuple_list


def printing(result, variants):
    "Вывод результата"
    summa_print = sum(result)
    print("Сумма", summa_print, "комбинация", variants)


def randoms():
    "Случайные числа"
    bone1 = random.randrange(1, 6)
    bone2 = random.randrange(1, 6)
    return bone1, bone2,


combi = randoms()
count = main(combi)
printing(combi, count)
