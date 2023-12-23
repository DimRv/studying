"""Генераторы вместо return используют yield
функция не выполняется полностью, а возвращает объект генератора как доходит до yield,
то есть такая функция генерирует значения по запросу с течением времени.

next(gen) - получение след значения генератора

Методы:
gen.close() - закрывает генератор, next(gen) вызовет StopIteration
"""

help('yield')


def f1():
    """Функция создает генератор"""
    for i in range(5):
        yield i


print(f1(), type(f1()))
"""
Оба генератора не зависят от дуг друга:
"""
a1 = f1()
a2 = f1()
print([i for i in dir(a1) if not i.startswith('_')])

print(next(a1))
print(next(a1))
print(next(a1))
print(next(a2))
print(next(a2))
a2.close()
#next(a2) - вызовет ошибку


def f2():
    """Генератор эквивалент f1, но использует более короткую запись"""
    yield from range(5)


g3 = f2()
print(next(g3))
print(next(g3))
print(next(g3))

#Доп аргументы:
print(a1.gi_code)
print(a1.gi_frame)
print(a1.gi_running)
print(a1.gi_suspended)
print(a1.gi_yieldfrom)


def f3():
    for i in range(5):
        x = yield i
        print(x + i)


g2 = f3()
next(g2) #инициируем выполнение, доходим до yield
g2.send(10)
g2.send(10)
g2.send(10)
#g2.throw(StopIteration)
#g2.send(10)


def create_counter_generator():
    counter = 0
    while True:
        sender = yield
        if sender is None:
            return counter
        counter += 1


def create_adder_tolist_generator():
    while True:
        """Делегирование выполнения другому генератору"""
        counter_result = yield from create_counter_generator()
        counter_list.append(counter_result)
        print(counter_list)


counter_list = []
gen = create_adder_tolist_generator()
next(gen)
gen.send(1)
gen.send(1)
gen.send(None)
gen.send(1)
gen.send(1)
gen.send(1)
gen.send(1)
gen.send(None)


def create_gen():
    while True:
        i = yield from corontine()
        if i is None:
            print('gen stoped')
            return None
        else:
            print('next step')


def corontine():
    while True:
        i = yield
        if i is 0:
            return None
        else:
            print(i)


gen = create_gen()
next(gen)
for i in range(5,-1,-1):
    gen.send(i)








