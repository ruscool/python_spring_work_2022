# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
"""функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
чтобы каждая функция выполняла одно универсальное действие."""

import random

a = 10
words = ["оператор", "конструкция", "объект", "информатика", "авиаотряд", "очевидец",
         "водонагреватель", "зуб"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования",
         "Состав и взаимное расположение частей какого-н. строения, сооружения, механизма, а также само строение, "
         "сооружение, машина с таким устройством", "То, что существует вне нас и независимо от нашего сознания, "
                                                   "внешний мир, материальная действительность",
         "Наука, изучающая структуру, общие свойства и методы передачи информации, в том числе "
         "связанной с применением ЭВМ",
         "Тактическое и огневое подразделение тяжело бомбардировочных частей, состоящее из нескольких самолетов",
         "Человек, к-рый сам, своими глазами наблюдал какое-н. событие",
         "Устройство для непрерывного нагрева воды в местной системе водоснабжения",
         "Костное образование, во множестве расположенное в ротовой полости большинства позвоночных "]
word_random = str(random.choice(words))
word_random_list = [word_random]
print(words, word_random)  # подсказка - удалить потом
print(desc_[words.index(word_random)])
word_kod = "#" * len(word_random)
print('Загаданное слово: ', ' '.join(word_kod))
word_list = list(word_kod)
word_ord = [ord(x) for x in word_random]
bufer = []


def entering():
    first_enter = str(input("Введите букву: "))
    return first_enter


def add_bufer(par_letter):
    letter = par_letter
    if letter in word_random:  # если нет в списке - добавляем
        return bufer.append(ord_letter)


def game_over(): return print("-" * 30, "\nИгра окончена")


def find_and_test(letter, count_letter, b, count_list, ord_letter):
    global a
    if count_letter >= 1:  # ищем индексы и добавляем в список
        print("Есть такая буква")
        for i in word_random:
            if i == letter:
                count_list.append(word_random.index(letter, b))
                b = count_list[-1] + 1
        if letter in word_random:  # если есть индексы - меняем на буквы
            for f in count_list:
                # print(word_kod, f)
                word_list[f] = word_random[f]
                if "".join(word_list) == word_random:
                    #print("a in find ", a)
                    #a_in_find = 0
                    print("=" * 30, "\nУгадали все слово - это", word_random, "\n", "-" * 30)
                    a = 0

        print(" ".join(word_list))  # вывод предварительный
    else:
        a -= 1
        print("-" * 30)
        print("Такой буквы здесь нет\nосталось попыток", a)
    return a


def main(main_letter, a):
    if len(main_letter) > 1:
        print("Введено больше одной буквы, заново, минус попытка")
        a -= 1
        print("Осталось попыток", a)
    else:
        ord_letter = ord(main_letter)
        if ord_letter in bufer:
            print("уже была эта буква, заново")
            print(" ".join(word_list))
        else:
            add_bufer(main_letter)

    return main_letter


while a > 0:  # start game

    clist = []
    arg_b = 0
    arg_letter = entering()
    if arg_letter == 'quit' or arg_letter == 'выход':
        break
    main_game = main(arg_letter, a)
    arg_count_letter = word_random.count(main_game)
    ord_letter = bufer
    #print(a)
    arg_a = a
    end_game = find_and_test(main_game, arg_count_letter, arg_b, clist, ord_letter)
else:
    game_over()
