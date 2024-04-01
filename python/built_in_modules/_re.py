"""
re - regular expressions
получение совпадений по шаблону re

re.findall - список из всех найденных совпадений
re.match(re, text) -
re.match.groups() - список из всех найденных совпадений

"""
import re


li = ['Mike studying Python', 'Lisa studying C++']
exp = '(.*) studying (.*)'

for text in li:
    val = re.match(exp, text).groups()
    print(val[0], val[1])
