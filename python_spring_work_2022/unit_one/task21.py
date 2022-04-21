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


def find_tag(words, text):
    "Поиск и замена на тэги"
    for key in words.keys():
        text = text.replace("?", "{" + key + "}", 1)
    return text


def change_html(text, tags):
    "Форматирование html"
    old_tags = tags.copy()
    for key in old_tags.keys():
        if key in tags.keys():
            tags["{" + key + "}"] = tags.pop(key)
    text = text.format(**old_tags)
    return text


def rec_file(tags):
    "Запись данных в файл"
    f = open("index.html", "w+")
    f.write(tags)
    f.seek(0) # вещь)
    print(f.read())
    f.close()


first = find_tag(page, template)
second = change_html(first, page)
third = rec_file(second)

# под конец кода - улыбка )))
