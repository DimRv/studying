"""
bytearray(iterable_of_ints) -> bytearray
bytearray(string, encoding[, errors]) -> bytearray
bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
bytearray() -> empty bytes array

Возвращает неизменяемый объект - байтовую строку.
"""
print(bytes([60, 70, 80, 90]))
print(bytes('string', 'utf-8'))
print(bytes(bytes('string', 'utf-8'))) #копия
print(bytes(10))
print(bytes())