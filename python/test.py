a = 10
b = 20

a, b = b, a
print(a, b)

c = a
b = a
a = c
del c

print(a, b)
