# todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.
"""
Пример:
mass = [1,2,17,16,30,51,2,70,3,2]

Для числа 2 индексы двух ближайших чисел: 6 и 9

Пример:
mass = [1,2,17,54,30,89,2,1,6,2]
Для числа 1 индексы двух ближайших чисел: 0 и 7
Для числа 2 индексы двух ближайших чисел: 6 и 9
"""

mass = [1, 2, 17, 16, 2, 30, 51, 1, 2, 70, 3, 2, 1]
a = 0
print(mass)
zapros = int(input("Число: "))

summaIndex = mass.count(zapros)

if summaIndex > 1:
    b = []
    for i in mass:
        if i == zapros:
            b.append(mass.index(zapros, a))
            a = b[-1] + 1

    print("Число", zapros, "есть по Индексам", b)
elif summaIndex <= 0:
    print("нет числа в массиве")
else:
    print("Число", zapros, "Индекс:", mass.index(zapros))
