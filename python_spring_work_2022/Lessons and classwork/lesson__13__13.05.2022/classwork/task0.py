# todo: Реализуйте функцию которая возвращает копию списка
def identity(nums):
    """Identity:
    Функция возвращает копию списка
    """
    return nums


print('identity ', identity([1, 2, 3, 4, 5]))


# Пример вызова:
# >>> identity([1, 2, 3, 4, 5])
# [1, 2, 3, 4, 5]
# >>> identity([])
# []

# todo: Реализуйте функцию которая возвращает степень числа каждого элемента
def power_(nums, pow):
    """Doubled:
    Функция возвращает степень каждого элемента
    """
    return [num * pow for num in nums]


print('power_', power_([1, 2, 3, 4, 5], 2))


# Пример вызова:
# >> > power_([1, 2, 3, 4, 5],2)
# [2, 4, 6, 8, 10]
# >> > power_([1, 2, 3, 4, 5],3)
# [0, 3, 6, 9, 12, 15]


# todo: Реализуйте функцию которая возвращает только четные значения
def evens(nums):
    """Evens:
      Функция возвращает четные значения каждого элемента
    """
    return [x for x in nums if x % 2 == 0]


# Пример вызова:
print('evens', evens([1, 2, 3, 4, 5]))
# [2, 4]
# >>> evens([1, 3, 5])
# []
# >>> evens([-2, -4, -7])
# [-2, -4]

# todo: Верните список с размерностью слов в том случае если они не исключение
# параметр exception принимает слово которое не нужно подсчитывать


def words_not_the(sentence, exception):
    """Words not 'the'
      Возвращает  список подсчинных слов без ислкючения (exception).
    """
    return [i for i in sentence.split() if i != exception]


# Пример вызова:
print('words_not_the',words_not_the('the quick brown fox jumps over the lazy dog', 'the' ))
# [5, 5, 3, 5, 4, 4, 3]


# todo: Верните список гласных букв
def vowels(word):
    """Vowels:
        Функция возврашает список гласных букв
    """

    return [x for x in word if x in ['a', 'e', 'i', 'o']]


print('vowels',vowels('mathematics'))
# ['a', 'e', 'a', 'i']


# todo: Задан массив [ 'one', 'two', 'three' ] с помощью спискового генератора преобразовать в словарь
# вида { 1:'one', 2:'two', 3:'three' }


def dict_new(name):
    return {k: v for (k, v) in enumerate(name, 1)}


print('dict_new',dict_new(['one', 'two', 'three']))
