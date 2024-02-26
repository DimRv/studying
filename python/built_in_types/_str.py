"""СТРОКИ - последовательность символов.
Неизменяемый тип.
Итерируемый тип.

"""


#Интроспекция:
help(str)
print([i for i in dir(str) if i[0] != '_'], len([i for i in dir(str) if i[0] != '_']))

#СОЗДАНИЕ:
s1 = 'string cтрока'
s2 = "string строка"
s3 = """
<html>
    <head>
        <title>Заголовок</title>
    </head>
</html>
"""
s4 = 'C:\\new\\folder'
s5 = r'C:\new\folder'
s6 = '\ttab string\n'
s7 = b'bytes'
s8 = f'new_string: {s1}'

print(s4 == s5, s4 is s5)
#КОНКАТЕНАЦИЯ, ПОВТОРЕНИЕ, ДЛИНА, ДОСТУП ПО ИНДЕКСУ И СРЕЗУ И ФОРМАТИРОВНИЕ:
print(s1 + " " + s3)
print((s1 + " ") * 5)
print(len(s1))
print(s1[0])
print(s1[4:])
print('%s - programming language' % 'Python')
#ИТЕРАЦИЯ:
for i in 'string':
    print(i+'-', sep='', end='')
print([i + str('string'.index(i)) for i in 'string'])

#МЕТОДЫ:
#ИЗМЕНЕНИЕ
print('-'*20, 'changes', '-'*20)
print("sTrIng".capitalize()) #строка с большим первым символом и малыми остальными
print("StRinG".casefold()) #все малые
print('str'.center(40, "-")) #центрирование строки с добавлением символов
print('string'.encode('utf-8')) #применение кодировки
print('\t\tstring'.expandtabs(12)) #замена tab на пробелы
print("{} said: '{}'".format('Mike', 'Ok!')) #Форматирование заполнением
print("{name} said: '{frase}'".format_map({'name': 'Lisa', 'frase': 'GO!'})) #форматирование словарем
print('hi'.ljust(5, '.'))
print("HELLO WORLD".lower())
print(" \tHI!".lstrip())
print('<p>Параграф</p>'.removeprefix('<p>'))
print('<p>Параграф</p>'.removesuffix('</p>'))
print('Hello world!'.replace('Hello', 'Привет'))
print('hi'.rjust(5, '.'))
print(' Some text with spaces '.rstrip())
print(' Some text with spaces '.strip())
print("StRiNg".swapcase())
print('Some text with spaces'.title())
print('Some text with spaces'.upper())
print(str.zfill('4', 20))

#ПРОВЕРКИ:
print('-'*20, 'testings', '-'*20)
print("strIng".endswith('Ing')) #Проверка на наличие символов в конце строки
print('18:30'.isalnum())
print('12true'.isalpha())
print('true'.isascii())
print('2.3'.isdecimal())
print('34'.isdigit())
print('if'.isidentifier())
print('is_lower'.islower())
print('2.4'.isnumeric())
print('\u0020'.isprintable())
print('\n'.isspace())
print("Is Title".istitle())
print("IS UPPER".isupper())
print("__add__".startswith('__'))

#СВОЙСТВА
print('-'*20, 'values', '-'*20)
print("new string".count('n', 2, 8)) #количество символов в диапазоне
print("StRing".find('StR', 2, 18)) #поиск подстроки, -1 - не найдено
print('string'.index("s")) #позиция подстроки
print('Hello world'.rfind('o'))
print('Hello world'.rindex('o'))

#Преобразования в другие типы:
print("-".join(['hi', 'all']))
print('Иванов'.translate(str.maketrans({'И': 'I', "в": "v"})))
print("red;house;blue".partition(';'))
print("red;house;blue".rpartition(';'))
print('Hi\nmy\nfriend!'.splitlines())



