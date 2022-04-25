
text = "Написание теfghvgvjкстов для главных страниц сайта – дело непростое"

def logger(par_text):
    """
    Открывает и записывает сообщения в лог файл
    :param par_text: - текст в файл
    :return: -без возврата"""
    f = open("error.log", mode="a+t", encoding="utf-8")
    f.write(par_text + "\n")
    f.close()
