"""
with obj as var:
    block_with

with/as похож на try/finally

Оператор запускает логику управления контекстом объекта:
1. Вычисляется выражение в with, давая объект с методами __enter__ и __exit__
2. Запускается __enter__, возвращаемое значение записывается в as
3. Выполняется block_with
4. Вызывается __exit__ с заполненными аргументами, если возникли исключения и со значениями None при отсутствии
исключений. Если возвращает False, то исключение генерируется повторно
__exit__ - при выходе

with obj as name:

"""
help('with')


# Диспетчер контекста c встроенной функцией open()
print("Пример 1".center(60, "-"))
with open('test_with', 'a') as log:
    log.write("\nTesting with operator...")
    print("Запись в файл")


# Диспетчер контекста c собственным объектом
print("Пример 2".center(60, "-"))
class Test:
    def __init__(self):
        self.test = 'test'

    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('in exit')
        if exc_type is None:
            print('no exceptions')
        else:
            print('has exception')
            return False


with Test() as t:
    print('in with')

# Пример о
print("Пример 3".center(60, "-"))


class ReadFile:
    def __init__(self, file):
        self.file_name = file

    def __enter__(self):
        self.file = open(self.file_name)
        self.data = self.file.read()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            return False


with ReadFile("test_with") as rf:
    print(rf.data)