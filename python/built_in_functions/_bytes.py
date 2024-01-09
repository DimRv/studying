"""
bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Возвращает объект bytes - байтовую строку.
"""
print(bytes([60, 70, 80, 90]))
print(bytes('string', 'utf-8'))
print(bytes(bytes('string', 'utf-8')))
print(bytes(10))
print(bytes())
