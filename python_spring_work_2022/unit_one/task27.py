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
from workplace.loggers import logger_two


def begin():
    print("1. Новая игра", "\n2. Восстановить игру", "\n3. Выход")
    menu = int(input("Ваш выбор: "))
    a = 10
    b = random.randint(0, 100)
    d = 0
    while True:
        if menu == 1:
            return game(a, b, d)
        elif menu == 2:
            return load_game()
        elif menu == 3:
            break
        else:
            print("Нет такого в меню, выберите заново")
            return begin()


def end_game():
    return print("Спасибо")



def save_game(a, b, d):
    print("\nСохранить игру?", "\n1. - Продолжить", "\n2. - Сохранить игру и выйти")
    save = int(input("Номер выбора "))
    match save:
        case 1:
            return game(a, b, d)
        case 2:
            print(2)
            sl = "save_list.txt"
            file = "game_dump.pkl"
            to_pickle([a, b], file)
            time = datetime.datetime.now()
            print(time)
            log = "Запись от " + str(time.now())

            logger_two(log, sl)
        case _:
            print("Номер ")
            save_game(a, b, d)


def load_game():
    return print("load")


def game(a, b, dobro):
    print("b=", b)  # del
    if dobro == 0:
        print("Добро пожаловать")
        dobro = 1
    else:
        print("Число попыток осталось", a)
    d = dobro
    while a > 0:
        c = input("Угадай число от 0 до 100: ")
        if c == "s" or c == "S":
            return save_game(a, b, d)
        else:
            if c.isdigit():
                c = int(c)
            else:
                print('Необходимо вводить цифры, для сохранения нажать "s""')
                game(a, b, d)

        a -= 1
        if c == b:
            print("Угадали, конец игры")
            return end_game()
        elif c < b:
            print("Нет, больше - еще", a, "попыток")
        elif c > b:
            print("Нет, меньше - еще", a, "попыток")
    else:
        print("Не угадали, попыток больше нет")


begin()
