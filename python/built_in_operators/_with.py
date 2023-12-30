"""Оператор запускает логику управления контекстом объекта
__enter__
__exit__ - при выходе

with obj as name:

"""
help('with')

with open('test_with', 'a') as log:
    log.write("Testing with operator...")

print(log)