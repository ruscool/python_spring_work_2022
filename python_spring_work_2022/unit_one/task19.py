# todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
"""– id - номер по порядку (от 1 до 10);
– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

Каждое значение из списка должно находится на отдельной строке.
"""

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
            "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]
rows = ["id", "text"]


# сделано как говорится из того, что знаем на данный момент
# в будущем можно переделать через import csv

def create_csv(info, rows):
    f = open("algoritm.csv", "w+", encoding="utf-8")
    for i in rows:
        if i == rows[-1]:
            f.write('\"' + i + '\"' + '\n')
        else:
            f.write('\"' + i + '\"' + ',')
    for new_line in info:
        f.write(str(info.index(new_line) + 1) + ',\"' + new_line + '\"\n')
    f.seek(0)
    print(f.read())
    f.close()


create_csv(algoritm, rows)
