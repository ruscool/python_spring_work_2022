# todo: Написать функцию logger() которая принимает в качестве аргумента текст который дописывается
# в файл error.log Новое сообщение должно распологаться на новой строчки.

text = "Написание теfghvgvjкстов для главных страниц сайта – дело непростое"


def logger(par_text):
    """

    :param par_text:
    :return:
    """
    f = open("error.log", mode="a+t", encoding="utf-8")

    f.write(par_text + "\n")
    f.close()


logger(text)
print(help(logger))

