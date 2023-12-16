"""При вызове функции происходи выполнение инструкций expressions указанных в теле
@dec
def func_name(parameters):
    expression_1
    ...
    expression_n
    return/yield
"""


def f1():
    pass


print(f1, type(f1))
help('def')
print([i for i in dir(f1) if not i.startswith('_')])
print(f1())


#Параметры и значение по умолчанию
def f2(name='Mike', *keys, **kwargs):
    if keys or kwargs:
        print(keys, kwargs)
    return f"{name} is reading Python book now."


print(f2())
print(f2('Kolya'))
print(f2('Kolya', 'test1', 'test2', t1='test3', t2='test4'))


#Декораторы
def dec_func(f):
    f.test = 'some string'
    return f


@dec_func
def f3(name='Dima'):
    return f'{name} wrote {f3.test}'


print(f3())


#Рекурсия
def f4(text):
    if len(text) > 0:
        return f"*{text[0]}*{f4(text[1:])}"
    else:
        return text


print(f4('hello'))


#Ламбда
f5_res = (lambda x: '*' + x + '*')("test")
print(f5_res)


#yield
def f6(text):
    for i in text:
        yield i


for i in f6('string'):
    print(i)


#function expression
print(sum(int(i) for i in '234123'))
