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
file = 'debug.log'
count = 0


#
# def logger_two(t_file, per, name):
#     with open(t_file, "w+") as f:
#         dt = datetime.datetime.now()
#         log_file = f.readlines()
#
#         print(log_file)
#         log = '\n' + name + ', ' + str(per) + '\t' + dt.strftime('%d.%m.%Y %H:%M')
#         f.write(log)


def counter_func(func):
    def wrapper(*args, **kwargs):
        dt = datetime.datetime.now()
        wrapper.count += 1

        f = open('debug.log', 'r+')
        da = f.readlines()
        b = []
        c_readl = 0
        new_data = []
        # список функций в файле
        for i in da:
            if i == '\n':
                continue
            ll = list(i.split())
            b.append(ll[0][:-1])
        # b_set = set(b)
        if da == []:  # если пустой файл
            log = func.__name__ + ', ' + str(wrapper.count) + '\t' + dt.strftime('%d.%m.%Y %H:%M')
            f.write(str(log))
        else:
            for line in da:
                c_readl += 1
                if line == '\n':
                    continue
                ll = list(line.split())
                # l_str = str(line.split())
                if func.__name__ not in b:  # если нет в файле
                    f.write(
                        func.__name__ + ', ' + str(wrapper.count) + '\t' + dt.strftime('%d.%m.%Y %H:%M'))
                    b.append(func.__name__)
                    new_data.append(
                        func.__name__ + ', ' + str(wrapper.count) + '\t' + dt.strftime('%d.%m.%Y %H:%M'))
                else:
                    # ll = list(line.split())
                    if ll[0][:-1] == func.__name__:  # добавление

                        ll[1] = int(ll[1])
                        ll[1] += 1
                        # ll.pop()
                        # ll.append(dt.strftime('%d.%m.%Y %H:%M'))

                        log = func.__name__ + ', ' + str(ll[1]) + '\t' + dt.strftime('%d.%m.%Y %H:%M')
                        new_data.append(log)
                        # print(" ".join(map(str, flexiple)))
                        " ".join(map(str, new_data))
                        # new_data = str(new_data)
                        f.close()
                        df = open('debug.log', 'w+')
                        if len(new_data) > 1:
                            for i in new_data:
                                df.write(i+'\n')
                        else:
                            df.write(log+'\n')
                        df.close()
                    else:
                        new_data.append(line)
        f.close()
        return func(*args, **kwargs)
        print('after')

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
    # new_time = time
    print(time)
    print('Меня зовут', data['name'], 'мне', data['age'], 'лет')


# todo: сделать рандом по количеству функций


# render(A)

# show(A, arg_time)

data_base(A, arg_time, dict_test)

print(render.count, show.count, data_base.count)
