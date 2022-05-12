

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
        result = now_time2-now_time
        print(f'after {t2}')
        print(result)
        return res
    return wrapper




def parent(a_list: list) -> int:  # страница 179
    """
    Индекс его родительского узла
    :param A: list
    :return: int
    """
    return (len(a_list) - 1) // 2


def left(i: int) -> int:
    """
    Индекс левого дочернего узла
    :param i:int
    :return: int
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
        Индекс правого дочернего узла
        :param i:int
        :return: int
        """
    return 2 * i + 2

@meg_w
def main(l_A: list) -> list:
    """
    Основная функция
    :param l_A: list
    :return: list
    """
    length = len(l_A)
    begin = parent(A)
    while begin >= 0:
        max_heapify(l_A, begin, length)
        begin = begin - 1
        for i in range(length - 1, 0, -1):
            l_A[0], l_A[i] = l_A[i], l_A[0]
            max_heapify(l_A, 0, i)
    return l_A


def max_heapify(A: list, ind: int, a_len: int):
    """
    Функция перебора- бинарные деревья
    :param A: list
    :param ind: int
    :param a_len: int

    """
    l = left(ind)
    r = right(ind)
    if (l < a_len and A[l] > A[ind]):
        largest = l
    else:
        largest = ind
    if (r < a_len and A[r] > A[largest]):
        largest = r
    if (largest != ind):
        A[largest], A[ind] = A[ind], A[largest]
        max_heapify(A, largest, a_len)


main(A)
