# todo: Написать игру , где программа загадывает число от 0 до 100 (через функцию random) , а пользователь
# пытается его отгадать(через консоль). При успехе выводится поздравление в победе и результат попыток.
# По истечении 10 неудачных попыток выводится проигрышь.

# Для получения функции числа из диапазона от 0 до 100 подключать библиотеку
# import random
# random.randint(0,100)

import random

a = 10
b = random.randint(0, 100)
print(b)
while a > 0:
    c = int(input("Угадай число: "))
    a -= 1
    if c == b:
        print("Угадали")
        break
    elif c < b:
        print("Нет, больше - еще", a, " попыток")
    elif c > b:
        print("Нет, меньше - еще", a, " попыток")
else:
    print("Не угадали, попыток больше нет")