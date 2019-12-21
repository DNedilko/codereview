"""
Користувач вводить стрічку з будь-якими символами,
розділити її на слова, знайти слово,
що повторюється найбільшу кількість разів та
вивести усі слова у нижньому регістрі
"""



import re
import string
def check(line):
    return bool(re.match("[A-z]*\s*\\.*[;,:!&-]*",line))
def define_words(line):
    line=input(line)
    linewith = line.replace("-", " ")
    line1 = linewith.split(" ")
    while not check(line):
        line = input(line)
        linewith = line.replace("-", " ")
        line1 = linewith.split(" ")
    return line1

#def find_most_frequent(line):




line=input()
print(check(line))
print(define_words(line))