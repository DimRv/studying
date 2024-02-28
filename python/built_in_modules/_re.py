"""
re - regular expressions
получение совпадений по шаблону re

"""
import re


li = ['Mike studying Python', 'Lisa studying C++']
exp = '(.*) studying (.*)'

for text in li:
    val = re.match(exp, text).groups()
    print(val[0], val[1])
