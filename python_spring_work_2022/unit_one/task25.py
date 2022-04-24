# todo: Убрать повторяющиеся буквы и лишние символы
"""Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

Input             	            Output
apple	                        aple
25.04.2022 Good morning !!	    godmrni
"""

letter = "apple"
pre = "25.04.2022 Good morning !!"
english = ''.join([chr(i) for i in range(ord("a"), ord("a") + 26)])


def lines(letter, eng):
    "Удаление повторяющихся букв и символов"
    letter = letter.lower()
    l = []
    i_index = 0
    for i in letter:
        if i in eng:
            if i not in l:
                l.append(i)
        i_index += 1
    text = "".join(l)
    return text


print((lines(letter, english)))
print(lines(pre, english))
