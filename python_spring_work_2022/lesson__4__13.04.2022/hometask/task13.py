# todo: Дан целочисленный массив размера N из 10 элементов.
# Преобразовать массив, увеличить каждый его элемент на единицу.
n = 10
a = [n] * 10

for i in range(10):
    a[i] = a[i] + 1
print(a)