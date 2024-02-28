"""
Пример использования разных кодировок.

Кодировка применяется для хранения текста в ПЗУ.
В ОЗУ текст хранится в 'нейтральном к кодировкам формате' с переменной длиной с 1,2 или 4 байтами на символ
в зависимости от текста.
"""

text = 'text'
codings = ['ascii', 'latin1', 'utf8', 'utf16', 'utf32']

print('text:')
for coding in codings:
    print(text.encode(coding), len(text.encode(coding)), text.encode(coding).__sizeof__())

text = 'Текст'
print('Текст, кодировки ascii, latin1 не работают для кириллицы')
for coding in codings[2:]:
    print(text.encode(coding), len(text.encode(coding)), text.encode(coding).__sizeof__())

