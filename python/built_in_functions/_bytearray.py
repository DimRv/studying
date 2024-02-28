"""
bytearray(iterable_of_ints) -> bytearray
bytearray(string, encoding[, errors]) -> bytearray
bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
bytearray() -> empty bytes array

Встроенная функция bytearray преобразует объект, переданный в качестве аргумента в типу изменяемая байтовая строка
"""
print(bytearray([60, 70, 80, 90]))
print(bytearray('string', 'utf-8'))
print(bytearray(10))
print(bytearray())