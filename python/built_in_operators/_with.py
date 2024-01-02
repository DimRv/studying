"""Оператор запускает логику управления контекстом объекта
__enter__
__exit__ - при выходе

with obj as name:

"""
help('with')

with open('test_with', 'a') as log:
    log.write("Testing with operator...")


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
