# todo 3.1: Получите заданное количество N (например, 20) различных
# случайных целых чисел в диапазоне от 0 до N-1. Найдите их
# сумму.

import random

diapazon = []
vvod = int(input("Number "))
for i in range(vvod):
    a = random.randrange(0, vvod - 1)
    diapazon.append(a)

print(diapazon)

b = 0
for i in diapazon:
    b = b + i
print("Summ ", b)

# todo 3.2:  Известно, что сейф открывается при правильном вводе
# кода из 3 цифр 0...9. Задайте код и затем откройте сейф, ис-
# пользуя метод перебора с помощью нескольких операторов
# цикла for.
print('\n')

kod = random.randrange(0, 999)
print(kod)
for i in range(0, 999):
    if i == kod:
        print("kod find ", i)

