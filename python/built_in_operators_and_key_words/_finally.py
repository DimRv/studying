"""
try:
    block_try
finally:
    block_finally

finally выполняется всегда не зависимо, возникло ли исключение в try или нет

"""

try:
    print("1")
finally:
    print("2")
print("3")

try:
    print("1")
    raise IndexError
except IndexError:
    print("2")
finally:
    print("3")
print("4")
