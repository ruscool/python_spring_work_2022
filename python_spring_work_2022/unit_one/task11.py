# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

year = int(input('Ввести год '))
if (year % 100 > 0):
    vek = year // 100 + 1
else:
    vek = year // 100
print(vek)
