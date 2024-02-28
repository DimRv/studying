"""
chr(i) -> str

Возвращает символ по переданному Unicode
"""
print(chr(98))
print(chr(1040))

for i in range(256):
    print(f'{i}: ', chr(i))
