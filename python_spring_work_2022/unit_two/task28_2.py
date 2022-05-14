# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе
# выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов,
# дата-время последнего выполнения

# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import datetime
import random
from random import randint
import pandas as pd

A = [randint(-10000, 10000) for i in range(30)]
dict_test = {"name": 'Иван', 'age': 25}
arg_time = datetime.datetime.now()


def save_log(func):
    """
    Декоратор - запись в лог при запуске функции

    """

    def wrapper(*args, **kwargs):
        with open('debug.log', 'a+') as f:
            dt = datetime.datetime.now()
            log = func.__name__ + ' ' + dt.strftime('%d.%m.%Y %H:%M') + '\n'
            f.write(log)
        res = func(*args, **kwargs)
        return res

    return wrapper


@save_log
def render(list_a):
    return print(f'Render {list_a[:10]}')


@save_log
def show(list_b, time):
    t = time
    return print(f'Show {list_b[5:20]}, {t}')


@save_log
def data_base(A, time, data):
    new_a = random.choice(A)
    print(f'Случайное число из списка {new_a}')
    print(time)
    print('Меня зовут', data['name'], 'мне', data['age'], 'лет')


def count_func():
    """
    Загрузка данных из файла

    """
    with open('debug.log', 'r') as f:
        df = f.readlines()
    temp_ll = []
    for i in df:
        temp_ll.append(i.split())

    return main_count(temp_ll)


def main_count(data):
    """
    Подсчет количества вызовов функций

    """
    df = pd.DataFrame(data, columns=['func', 'date', 'time'])
    res_time = df.groupby('func').agg({'func': 'count', 'date': max, 'time': max})
    print()
    print(res_time)


render(A)

show(A, arg_time)

# data_base(A, arg_time, dict_test)

count_func()
