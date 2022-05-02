# todo: II вариант (алгоритм сортировки слиянием)

# Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 71 - 77.
#
# Задача.
# Перепишите процедуру  MERGE_SORT и отсортируйте последовательность
# A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13] по возрастанию

A = [31, 41, 9, 26, 41, 58, -1, 6, 101, 13]


# вариант решения по алгоритму сортировки
def merge_sort(A_list: list) -> list:
    """
    Сортировка по алгоритму известный как метод разбиения (“разделяй и властвуй”)
    :param A_list: list
    :return: list
    """
    ind = 0
    b = A[:]
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
                per = l[j]
                l[j] = l[j + 1]
                l[j + 1] = per
    for i in range(l_r):  # правая часть
        for j in range(l_r - i - 1):
            if r[j] > r[j + 1]:
                per = r[j]
                r[j] = r[j + 1]
                r[j + 1] = per
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


print(merge_sort(A))

# - быстрый вариант :)
# print(sorted(A))
