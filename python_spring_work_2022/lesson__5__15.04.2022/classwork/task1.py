# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan', 'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

for item in users:
    item['login']


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
# a = int(input("тип сортировки "))
a = 1

if a == 1:
    for item in users:
        print(item['age'])
    a_age = int(input("Число "))
    print("")

elif a == 2:
    for item in users:
        print(item['login'])
elif a == 3:
    for item in users:
        print(item['group'])
