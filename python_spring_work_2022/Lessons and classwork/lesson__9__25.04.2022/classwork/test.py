from helpers.io import logger, text
from helpers.crypt import *

print(logger(text))

file = "message.txt"
shifr = cezar_shifr()
count_lines = count_line(file)
print(open_file(shifr, file, count_lines))
