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

A = [randint(-10000, 10000) for i in range(30)]
dict_test = {"name": 'Иван', 'age': 25}
arg_time = datetime.datetime.now()


def counter_func(func):
    def wrapper(*args, **kwargs):
        dt = datetime.datetime.now()
        wrapper.count += 1
        f = open('debug.log', 'r+')
        da = f.readlines()
        b = {}
        for i in da:
            if i == '\n':
                continue
            ll = list(i.split())
            key_ll = ll[0][:-1]
            b[key_ll] = ll
        if da == []:
            log = func.__name__ + ', ' + str(wrapper.count) + '\t' + dt.strftime('%d.%m.%Y %H:%M')
            f.write(str(log))
        else:
            for line in da:
                if line == '\n':
                    continue
                ll = list(line.split())
                if func.__name__ not in b.keys():
                    f.write(
                        func.__name__ + ', ' + str(wrapper.count) + '\t' + dt.strftime('%d.%m.%Y %H:%M'))
                    b[func.__name__] = func.__name__ + ', ' + str(wrapper.count) + '\t' + dt.strftime('%d.%m.%Y %H:%M')
                else:
                    if ll[0][:-1] == func.__name__:
                        ll[1] = int(ll[1])
                        ll[1] += 1
                        log = func.__name__ + ', ' + str(ll[1]) + '\t' + dt.strftime('%d.%m.%Y %H:%M')
                        b[func.__name__] = ll
                        df = open('debug.log', 'w+')
                        if len(b) > 1:
                            for value in b.values():
                                new_v = " ".join(map(str, value))
                                df.write(str(new_v) + '\n')
                        else:
                            df.write(str(log) + '\n')
                        df.close()
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter_func
def render(list_a):
    return print(f'Render {list_a[:10]}')


@counter_func
def show(list_b, time):
    t = time
    return print(f'Show {list_b[5:20]}, {t}')


@counter_func
def data_base(A, time, data):
    new_a = random.choice(A)
    print(f'Случайное число из списка {new_a}')
    print(time)
    print('Меня зовут', data['name'], 'мне', data['age'], 'лет')


# render(A)

# show(A, arg_time)

data_base(A, arg_time, dict_test)
