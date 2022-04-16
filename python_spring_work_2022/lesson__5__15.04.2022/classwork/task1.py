# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan', 'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"},
         {'login': 'Misha', 'age': 23, 'group': "master"}]

"""
Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
1. По возрасту
2. По первой букве
3. По группе

тип сортировки: 1

#Затем сообщение для ввода
Ввидите критерии поиска: 16

Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"
"""
v = """Тип сортировки
1. По возрасту
2. По первой букве
3. По группе
"""
for i in users:
    print(i)
notWord = []
a = int(input("тип сортировки "))

if a == 1:
    a_age = int(input("возраст "))
    for item in users:
        if item['age'] == a_age:
            print('Пользователь', item['login'], 'возраст', item['age'], 'года', 'группа', item['group'])
            notWord.append(2)
        else:
            notWord.append(1)
    if 2 in notWord:
        pass
    else:
        print("Нет такого возраста")
        notWord = []
elif a == 2:
    firstLetter = input("Первая буква ")
    for item in users:
        if item['login'][0] == firstLetter:
            print('Пользователь', item['login'], 'возраст', item['age'], 'года', 'группа', item['group'])
            notWord.append(2)
        else:
            notWord.append(1)
    if 2 in notWord:
        pass
    else:
        print("Нет такого имени")
        notWord = []
elif a == 3:
    myGroup = str(input("Группа "))
    for item in users:
        if item['group'] == myGroup:
            print('Пользователь', item['login'], 'возраст', item['age'], 'года', 'группа', item['group'])
            notWord.append(2)
        else:
            notWord.append(1)
    if 2 in notWord:
        pass
    else:
        print("Нет такой группы")
        notWord = []
else:
    print('Неправильный выбор')
