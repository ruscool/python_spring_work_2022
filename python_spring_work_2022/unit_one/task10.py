# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

a = str(input('Введите число четырехзначное '))

if a == a[::-1]:
    print(True)
else:
    print(False)
