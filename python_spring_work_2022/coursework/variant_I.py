# todo: I вариант (алгоритм сортировки вставками)

# Реализовать на Python алгоритм сортировки вставками представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 57 - 63.
#
# Задача.
# Перепишите процедуру INSERTION_SORT и отсортируйте последовательность
# A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7] по убыванию.

A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7]


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


print(insertion_sort(A))
