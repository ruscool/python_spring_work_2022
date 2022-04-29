# todo: Сформируйте таблицу переходов для задачи 12 лекция 3.


massa=float(input("Масса тела, = "))
Area = {
    '1': print("Масса =", (lambda x: x)(massa), "кг"),
    '2': print("Масса =", (lambda x: 1000000 * x)(massa), "мкг"),
    '3': print("Масса =", (lambda x: 1000 * x)(massa), "гр"),
    '4': print("Масса =", (lambda x: x * 1/1000)(float(massa)), "т"),
    '5': print("Масса =", (lambda x: x * 1/100)(massa), "ц")
}

