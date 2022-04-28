# todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
#
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import random, datetime
from workplace.serializer import to_pickle
from workplace.deserializer import from_pickle

FILE = "game_dump.pkl"


def begin():
    global FILE
    file = FILE
    print("1. Новая игра", "\n2. Восстановить игру", "\n3. Выход")
    menu = input("Введите номер: ")
    a = 10
    b = random.randint(0, 100)
    d = 0
    c = 0
    if not menu.isdigit():
        return begin()
    else:
        menu = int(menu)
    while True:
        if menu == 1:
            return game(a, b, d, c)
        elif menu == 2:
            ll = load_game(file)  # список файлов для выбора
            # print("ll", ll)
            return game(ll[0], ll[1], ll[2], c)
        elif menu == 3:
            break
        else:
            print("Нет такого в меню, выберите заново")
            return begin()


def end_game():
    print("Спасибо")
    return -1


def save_game(a, b, d, c):
    global FILE
    file = FILE
    print("\nСохранить игру?", "\n1. - Продолжить", "\n2. - Сохранить игру и выйти")
    save = input("Номер выбора ")
    if save.isdigit():
        save = int(save)
    else:
        print("Выберите номер из списка")
        return save_game(a, b, d, c)
    match save:
        case 1:
            return game(a, b, d, c)
        case 2:
            new_dict = from_pickle(file)
            dt = datetime.datetime.now()
            log = dt.strftime('%d%m%Y_%H%M%S')
            new_dict[log] = [a, b, d]  # присваивание
            # print({log: [a, b, d]})
            to_pickle(new_dict, file)
            print("Игра сохранена под номером: ", log)
            end_game()
            return -1
        case _:
            print("Номер? ")
            return -1


def last_five():
    f = input("Выберите номер записи (от 1 до 5) ")
    if f.isdigit():
        f = int(f)
        if f > 5 or f < 5:
            f = 5
    else:
        print("Не верный выбор, загружаем последнюю сохранненную игру")
        f = 5
    return f


def load_game(file):
    obj = from_pickle(file)
    count = len(obj)
    if count > 5:
        list_keys = list(obj.keys())
        list_keys.sort()
        new_list = list_keys[-5:]
        nn = {}
        for i in new_list:
            nn[i] = obj[i]
    obj = nn
    # последние 5 записей
    for g in range(5):
        print(g + 1, new_list[g])
    # выбор файла
    f = last_five()
    n_list = new_list[f - 1]
    # возврат списка значений останова игры
    for i, v in obj.items():
        if i == n_list:
            return v


def game(a, b, dobro, c):
    if dobro == 0:
        print("Добро пожаловать")
        dobro = 1
    else:
        print("Число попыток осталось", a)

    d = dobro
    while a > 0:
        c = input("Угадай число от 0 до 100: ")
        a -= 1
        if a == 0:
            print("Не угадали, попыток больше нет")
            # end_game()
            # break
            return -1
        if c == "s" or c == "S":
            # a += 1
            c = 0
            return save_game(a, b, d, c)
        elif c.isdigit():
            c = int(c)
            if c == b:
                # a = 0
                # print(a)
                print("Угадали, конец игры")
                end_game()
                break
                # return end_game()
            elif c < b:

                print("Нет, больше - еще", a, "попыток")
            elif c > b:
                print("Нет, меньше - еще", a, "попыток")
        else:
            print('Необходимо вводить цифры, для сохранения нажать "s""')
            # game(a, b, d)
    else:
        print("Не угадали, попыток больше нет")
        end_game()
    return -1


r = 0
if r == 0:
    begin()
    r = 1
