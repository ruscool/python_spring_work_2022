# todo: Задан массив
surname = ['Электроник', 'Сыроежкин', 'Чижиков', 'Кукушкина']
sel = "<select>"
opt = "<option>"
# Код на выходе должен выдавать выпадающий список следующего вида.
"""
<select>
	<option>Электроник</option>
	<option>Сыроежкин</option>
	<option>Чижиков</option>
	<option>Кукушкина</option>
</select>
"""
print(sel)
for i in surname:
    print("\t", opt, i, opt[0], "/", opt[1:], sep="")

print(sel[0], "/", sel[1:], sep="")
