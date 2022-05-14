# todo: Найти сумму элементов матрицы,

# Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423

matrix = [[1, 2, 3], [4, 5, 6]]


def msum(matrix):
    l = [x for i in matrix for x in i]

    return sum(l)


def load_matrix(filename):
    with open(filename, 'r') as f:
        l = [i.rstrip().split() for i in f.readlines()]
        for x in l:
            for i in x:
                x[x.index(i)] = int(i)

        return l if len(set([len(l) for x in l])) == 1 else False


print(msum(matrix))
print(msum(load_matrix('matrix.txt')))
