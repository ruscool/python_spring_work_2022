# todo: Реализовать декоратор который подсчитывает время выполнения функции.

# Для этого необходимо взять время до начала запуска функции и после ее окончания.
# Проверить декоратор для различного рода алгоритмов сортировок на большом наборе данных.

import time
# todo: II вариант (алгоритм сортировки слиянием)

# Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 71 - 77.
#
# Задача.
# Перепишите процедуру  MERGE_SORT и отсортируйте последовательность
# A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13] по возрастанию

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


@meg_w
def merge_sort(A_list: list) -> list:
    """
    Сортировка по алгоритму известный как метод разбиения (“разделяй и властвуй”)
    :param A_list: list
    :return: list
    """
    ind = 0
    if len(A_list) % 2 != 0:
        A_list.append(abs(sum(A_list)))
        ind += 1
    l_l = int(len(A_list) // 2)
    l_r = int(len(A_list) - l_l)
    l = A_list[:l_l]
    l.append(abs(sum(A_list)))  # в будущем точка останова в цикле
    r = A_list[l_r:]
    r.append(abs(sum(A_list)))

    for i in range(l_l):  # левая часть
        for j in range(l_l - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    for i in range(l_r):  # правая часть
        for j in range(l_r - i - 1):
            if r[j] > r[j + 1]:
                r[j], r[j + 1] = r[j + 1], r[j]
    # объединение
    ind_l, ind_r = 0, 0
    for i in range(len(A_list)):
        while l[ind_l] <= r[ind_r]:
            A[i] = l[ind_l]
            ind_l += 1
            break
        else:
            A[i] = r[ind_r]
            ind_r += 1
    if ind == 1:
        A_list = A_list[:-1]
    return A_list


merge_sort(A)
