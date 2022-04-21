# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""


def change_html(words, text):
    # print(template)
    for key in words.keys():
        # print(key)
        d = len(key)
        find_first = text.find(key)
        # print(key, d, find_first)
        # quest = text.find(key) + d
        ss = text.find("?", text.find(key) + d)  # индекс ?
        text = text.replace("?", "{" + key + "}", 1)

        print(ss, text[43])
        new_template = template[:ss] + key + template[ss + len(key):]
        # ss += 1
        qw = 3
    print(text)
    # print(new_template, end=" ")
    # f = text.find(str("<" + words.keys(


def rec_file():
    pass


change_html(page, template)
