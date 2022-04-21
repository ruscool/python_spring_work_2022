# todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
"""
Содержимое файла import_this.txt
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

выходные данные
Complex is better than complicated.
Simple is better than complex.
Explicit is better than implicit.
Beautiful is better than ugly.
"""

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

def read_file(text):
    f = open("import_this.txt", "w+")
    f.writelines(text)
    f.seek(0)
    backwards = list(f)
    backwards.reverse()
    for i in backwards:
        print(i[:-2])
    f.close()


read_file(text)
