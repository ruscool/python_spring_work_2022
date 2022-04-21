# todo: Задан файл dictionary.xml (в текущей папке).
"""
<dict>
    <key>###</key>
    <value>##</value>
</dict>

Написать функцию которая принимает кортеж вида  ('age', 16) и записывает его значения в файл
Первое значение кортежа в позицию <key> второе в <value>
Итоговый файл должен получиться:
<dict>
<key>'age'</key>
<value>16</value>
</dict>

Задачу решить с помощь метода seek()"""


def read_rec(file):
    f = open(file, "r+t")
    f.seek(12, 0)
    f.write("age")
    f.seek(29, 0)
    f.write("16")
    f.close()


file = "dictionary.xml"
read_rec(file)
