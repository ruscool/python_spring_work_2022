# todo: Создайте объект сериализации любым методом для соседа, запишите его в файл,
# педайте его ему для считывания. Соседу необходимо десириализовать полученый объект.


# todo: Заданы два списка. Необходимо их сериализовать в один файл.

list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = (False, 'Sparse is better than dense.', {'age': 90})

from Serializis.serializer import to_pickle
from Serializis.deserializer import from_pickle


def saves(*obj):
    output = to_pickle(obj, 'data.pkl')
    print(output)


def testing(file: str):
    with open("data.pkl", "rb") as f:
        obj = from_pickle(file)
    print(obj)


file = "data.pkl"
saves(list_one, list_two)
testing(file)

