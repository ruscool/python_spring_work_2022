# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
"""Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
Ценыхранятся в словаре:"""
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(unit):
    summa = 0
    for key, value in unit.items():
        print("Товар", key, "количество", prices[key], "цена", value, "стоимость =", prices[key] * value)
        amount_product = value * prices[key]
        summa = summa + amount_product
    return summa


amount = {"banana": 3,
          "apple": 5,
          "orange": 5,
          "pear": 2}
result = compute_bill(amount)
print("Сумма товара равна", result, "y.e")
