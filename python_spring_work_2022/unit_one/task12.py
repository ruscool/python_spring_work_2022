# Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
# Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4

# Введите  массу тела
# >1
# Ответ: 1000 кг


zadacha = """Введите единицу массы тела
\t1 - килограмм
\t2 — миллиграмм
\t3 — грамм
\t4 — тонна
\t5 — центнер
"""
nomer = str(input(zadacha))

match nomer:
    case "1":
        massa_tela = float(input("Масса тела, кг = "))
        print("Масса =", massa_tela, "кг")
    case "2":
        massa_tela = float(input("Масса тела, милиграмм = "))
        miligramm = 1000000
        print("Масса = {:.6f} кг".format(1 / miligramm * massa_tela))
    case "3":
        massa_tela = float(input("Масса тела, грамм = "))
        gramm = 1000
        print("Масса = {:.3f} кг".format(1 / gramm * massa_tela, "кг"))
    case "4":
        massa_tela = float(input("Масса тела, тонн = "))
        tonna = 1 / 1000
        print("Масса = {:.2f} кг".format(1 / tonna * massa_tela, "кг"))
    case "5":
        massa_tela = float(input("Масса тела, центнеров = "))
        centner = 1 / 100
        print("Масса = {:.2f} кг".format(1 / centner * massa_tela, "кг"))