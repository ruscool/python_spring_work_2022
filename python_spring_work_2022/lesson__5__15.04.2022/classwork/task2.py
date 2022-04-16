# todo 2.1: Заданы множества
# все позьзователи
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}

# Вычислить пользователей online
online = all_users.difference(offline_users)
print("Online users", online)

# todo 2.2: Заданы множества
# Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}

# Даны читатели газет
readers_magazines = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

# Найти пользователей кто читает и книги и газеты
r = readers_books.intersection(readers_magazines)
print("Readers books and magazines", r)
