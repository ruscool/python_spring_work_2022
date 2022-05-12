import datetime

from random import randint

A = [randint(-10000, 10000) for i in range(10000)]


# A = [31, 41, 9, 26, 41, 58, -1, 6, 101, 13]


def meg_w(func):
    print('on')
    def wrapper(A):
        now_time = datetime.datetime.now()
        t = now_time.strftime("%H:%M:%S")
        print("time:", t)
        res = func(A)
        now_time2 = datetime.datetime.now()
        t2 = now_time2.strftime("%H:%M:%S")
        result = now_time2 - now_time
        print(f'after {t2}')
        print(result)
        return res

    return wrapper

@meg_w
def insertion_sort(a_list: list) -> list:
    """
    Алгоритм сортировки вставками по убыванию
    :param a_list: list
    :return: list
    """
    len_a = len(a_list)
    for j in range(1, len_a):
        key = a_list[j]
        i = j - 1
        while i >= 0 and a_list[i] < key:
            a_list[i + 1] = a_list[i]
            i -= 1
        a_list[i + 1] = key
    return a_list


insertion_sort(A)
