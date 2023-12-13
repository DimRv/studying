"""СТРОКИ - неизменяемая последовательность символов"""


#Интроспекция:
help(str)
print([i for i  in dir(str) if i[0] != '_'])

#СОЗДАНИЕ:
s1 = 'string cтрока'
s2 = "string строка"
s3 = """String  string"""
s4 = 'C:\\new\\folder'
s5 = r'C:\new\folder'
s6 = '\ttab string'
s7 = b'bytes'
s8 = 'sTrinG StRIng'
s9 = """
if True:
\tprint('True')
"""
s10 = "{} said: '{}'"
s11 = "{name} said: '{frase}'"
s12 = f'new_string: {s1}'
s13 = '10:35'

print(s4 == s5, s4 is s5)
print(s11)

#КОНКАТЕНАЦИЯ, ПОВТОРЕНИЕ, ДЛИНА, ДОСТУП ПО ИНДЕКСУ И СРЕЗУ:
print(s1 + " " + s3)
print((s1 + " ")* 5)
print(len(s1))
print(s1[0])
print(s1[4:])

#МЕТОДЫ:
print(s8.capitalize()) #строка с большим первым символом и малыми остальными
print(s8.casefold()) #все малые
print(s8.center(40, "-")) #центрирование строки с добавлением символов
print(s8.count('n', 2, len(s8))) #количество символов в диапазоне
print(s8.encode('utf-8')) #применение кодировки
print(s8.endswith('Ing')) #Проверка на наличие символов в конце строки
print(s9.expandtabs(12)) #замена tab на пробелы
print(s8.find('StR', 2, 18)) #поиск подстроки, -1 - не найдено
print(s10.format('Mike', 'Ok!')) #Форматирование заполнением
print(s11.format_map({'name': 'Lisa', 'frase': 'GO!'})) #форматирование словарем
print(s8.index("s")) #позиция подстроки
print(s13.isalnum())
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
print("-".join(['hi', 'all']))
print('hi'.ljust(5, '.'))
print("HELLO WORLD".lower())
print(" \tHI!".lstrip())
print('Иванов'.translate(str.maketrans({'И': 'I', "в": "v"})))
print("red;house;blue".partition(';'))
print('<p>Параграф</p>'.removeprefix('<p>'))
print('<p>Параграф</p>'.removesuffix('</p>'))
print('Hello world!'.replace('Hello', 'Привет'))
print('Hello world'.rfind('o'))
print('Hello world'.rindex('o'))
print('hi'.rjust(5, '.'))
print("red;house;blue".rpartition(';'))
print('Some text with spaces'.rsplit(' '))
print(' Some text with spaces '.rstrip())
print('Some text with spaces'.split(' '))
print('Hi\nmy\nfriend!'.splitlines())
print("__add__".startswith('__'))
print(' Some text with spaces '.strip())
print(s8.swapcase())
print('Some text with spaces'.title())
print('Some text with spaces'.upper())
print(str.zfill('4', 20))



