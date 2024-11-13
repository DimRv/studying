"""zlib - содержит алгоритм хеширования crc32"""

import zlib

data = b'Hello, world!'
print(type(data), data)

h = zlib.crc32(data)
h1 = hash(data)
print(type(h), h, len(str(h)))
print(type(h1), h1, len(str(h1)))
print(type(h1), h1, len(str(h1)))
