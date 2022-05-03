#todo: III вариант (пирамидальная сортировка )

# Реализовать на Python пирамидальную сортировку представленную в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 178 - 184.
#
# Задача.
# Перепишите процедуру  MAX_HEAPIFY и напечатайте получившеестся бинарное дерево
# при входном списке A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]

A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]  # 50,14,60  14,7,20  50,70,55  7,5,15 55,-10


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


print(main(A))
