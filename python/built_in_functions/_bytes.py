"""
bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Встроенная функция bytes преобразует объект, переданный в качестве аргумента в типу не изменяемая байтовая строка
По своей сути это последовательность из целых чисел от 0-255.



"""
print(bytes([60, 70, 80, 90]))
print(bytes('string', 'utf-8'))
print(bytes(10))
print(bytes())
