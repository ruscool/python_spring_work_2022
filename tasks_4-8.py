# todo: Домашние задания от 08.04 - task4-8
# tasks = 4
tasks = int(input('Номер задания - от 4 до 8: '))

if tasks <= 3 or tasks >= 9:
    print('Нет таково задания - заново\n')

elif tasks == 4:
    s = int(input('Сторона квадрата = '))
    print('Площадь квадрата = ', s ** 2, ', Тип:', type(s))
    # print(type(s))
# todo: task 5
elif tasks == 5:
    a = int(input('Введите точку А: '))
    b = int(input('Введите точку B: '))
    c = int(input('Введите точку C: '))
    ac = c - a
    bc = b - c
    if bc < 0:
        bc = -bc
    print('Длина отрезков АС =', ac, 'BC =', bc, 'Сумма =', ac + bc)
# todo: task 6
elif tasks == 6:
    a = int(input('Введите А: '))
    b = int(input('Введите B: '))
    if a <= 0:
        a = int(input('Введите А больше нуля: '))
    x = -b / a
    print('x =', x)

# todo: task 7
elif tasks == 7:
    print('Проверка двух чисел')
    a = int(input('Введите число: '))
    if a % 2 == 0:
        print('Число четное:', True)
    else:
        print('Число четное:', False)
    a = int(input('Введите число: '))
    if a % 2 != 0:
        print('Число нечетное:', True)
    else:
        print('Число нечетное:', False)

# todo: task 8
elif tasks == 8:
    a = int(input('Введите А: '))
    b = int(input('Введите B: '))
    c = int(input('Введите C: '))
    print('Введенные значения А =', a, ', B =', b, ', C =', c)
    a, b, c = c, a, b
    print('Новые значения A =', a, ', B =', b, ', C =', c)
