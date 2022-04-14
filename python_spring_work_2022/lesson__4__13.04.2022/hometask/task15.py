# Написать игру "Поле чудес"
"""
Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
либо победы.

Пример вывода:

"Это слово обозначает наименьшую автономную часть языка программирования"

▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

Введите букву: O

O  ▒  ▒  ▒  ▒  ▒  O  ▒


Введите букву: Я

Нет такой буквы.
У вас осталось 9 попыток !
Введите букву:
"""
import random

a = 10
words = ["оператор", "конструкция", "объект", "информатика", "авиаотряд", "очевидец",
         "водонагреватель", "зуб"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования",
         ".2.", "3 Это слово обозначает", "4 Это слово обозначает",
         "5 Это слово обозначает", "6 Это слово обозначает", "7 Это слово обозначает", "8 Это слово обозначает"]
word_random = random.choice(words)
print(words, word_random)  # удалить потом
print(desc_[words.index(word_random)])
word_kod = "#" * len(word_random)
print(word_kod, type(word_kod))
# print(("# " * len(word_random)))
word_list = list(word_kod)
word_ord = [ord(x) for x in word_random]
print("ord", word_ord)
# print(b)

while a > 0:
    letter = input("Введите букву: ")
    print(ord(letter))
    count_list = []
    b = 0
    count_letter = word_random.count(letter)

    if count_letter > 1:
        # count_list = []
        for i in word_random:
            if i == letter:
                count_list.append(word_random.index(letter, b))
                b = count_list[-1] + 1

        print("индексы", count_list, type(count_list))

        if letter in word_random:
            print("Есть такая буква")
            for f in count_list:
                print(word_kod, f)
                if f > 0:
                    # pass
                    word_list[f] = word_random[f]
                elif f == 0:
                    # pass
                    word_list[f] = word_random[f]
                # d = word_list

                # word_kod.replace(count_list[],)
            print("new word", word_list)

            count_list = []

    else:
        a -= 1
        print("-" * 10)
        print("Такой буквы здесь нет\nосталось попыток", a)
        print("word_random", word_random)
        print("Word_list", word_list)
    print(count_list)
else:
    print("Игра окончена")

sd = 2
