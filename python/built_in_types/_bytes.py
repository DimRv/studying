"""Байтовые строки - последовательность из байт - может быть строкой, картинкой, музыкой...
Неизменяемый тип
bytearray - изменяемый

Основное применение:
- запись в файл
- декодирование в текст
- memoryview
"""


#Создание
b1 = bytes('string', 'utf-8')
b2 = b'string'
b3 = 'string'.encode('utf-8')
print(b1 == b2, b1 is b2)
print(b1 == b3, b1 is b3)

print(b1, type(b1))
print(b2, type(b2))
print(b3, type(b3))

#Интроспекция
help(bytes)
print([i for i in dir(b1) if not i.startswith('_')], len([i for i in dir(b1) if not i.startswith('_')]))

#Поддерживает большинство методов строк, так что смотри str
#Декодирование:
print(b1.decode('utf-8'))

#Мемори:
m1 = memoryview(b1)
print(m1, type(m1))
