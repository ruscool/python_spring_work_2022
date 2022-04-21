# todo: Модифицировать программу таким образом чтобы она выводила при повторном считывании стр. 5 приветствие "Hello"

def writer_file(par_file):
    f = open(par_file, "w+t")
    f.write("Hello\n")
    f.seek(0)
    print(f.read())
    f.close()


file = "text.txt"
writer_file(file)
