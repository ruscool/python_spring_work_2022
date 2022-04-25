
text = "Написание теfghvgvjкстов для главных страниц сайта – дело непростое"

def logger(par_text):
    f = open("../error.log", mode="a+t", encoding="utf-8")

    f.write(par_text + "\n")
    f.close()
