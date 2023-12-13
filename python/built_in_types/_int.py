"""int - целые числа в python
Диапазон целых чисел: от -inf до +inf и ограничен только памятью компьютера
Неизменяемый тип данных
"""

#Интроспекция
help(1)
print([i for i in dir(int) if i[0] != '_'])

#Объявление целых чисел

a1 = 1
a2 = int(2)
a3 = int('5')
a4 = int('111', base=2)
a5 = int('FF', base=16)
a6 = 0b111
a7 = 0xF
a8 = 0o11
print(a1, a2, a3, a4, a5, a6, a7, a8)

#int поддерживает математические операторы: +, -, *, /, //, %, **, унарные +б -
print('math', "-"*30)
print(a1 + a2, a1 - a2, a1 * a2, a1 / a2, a1 // a2, a1 % a2, a1 ** a2)

#int поддерживает битовые операторы: |, ^, &, <<, >>, ~
print('bit', "-"*30)
print(bin(7), bin(4))
print(bin(7 | 4), bin(7 ^ 4), bin(7 & 4), bin(7 << 1), bin(7 >> 1), ~4)

#дополительные методы:
#to_bytes - возвращает байтовую строку, полученную из числа
print('to_bytes', '-' * 30)
help(int.to_bytes)
print((7).to_bytes(2), (7).to_bytes(10, byteorder='little'), (255).to_bytes(1))
print('to_bytes', '-' * 30)
help(int.from_bytes)
#from_bytes - возвращает число из байтовой строки
help(int.from_bytes)
print(int.from_bytes(b'\xff'), int.from_bytes(b'\xff\xff'))
#bit_length - длина байтовой строки
help(int.bit_length)
print(bin(65533), (65533).bit_length())
#bit_count - количество единичных бит в байтовой строке
help(int.bit_count)
print(bin(6), (6).bit_count())
#conjugate - возвращает сопряженное комплексного числа
help(int.conjugate)
print((255+4j).conjugate())
#imag - возвращает мнимую часть комплексного числа
help(int.imag)
print((255+4j).imag)
#real - возвращает реальную часть комплексного числа
help(int.real)
print((255+4j).real)
#as_integer_ratio - возвращает кортеж содержащий числитель и знаменатель дробного представления числа
help(int.as_integer_ratio)
print((7).as_integer_ratio())
#denominator
print((7).denominator)
#numerator
print((7).numerator)
