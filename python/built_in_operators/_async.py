"""Coroutines - сопрограмма
async - ключевое слово используется для создания сопрограммы.
Оператор используется совместно с встроенным модулем asyncio, см built_in_modules

Функции генератора, с выражением yield from <expr> внутри него, являются почти сопрограммами, но не совсем.
Единственное отличие состоит в том, что функция генератор не может контролировать где продолжиться выполнение
после ее завершения, при этом дальнейшее управление всегда передается вызывающей стороне.

"""
import asyncio

help('async')


async def some_task(param):
    print(f'task is running with {param}')
    await asyncio.sleep(2)
    print('ending task')


async def main():
    print('Starting main Event Loop')
    tasks = [asyncio.create_task(some_task(i)) for i in range(10)]
    await asyncio.sleep(0.1)
    print([(i.get_name(), i.get_coro()) for i in asyncio.all_tasks()])
    for i in tasks:
        await i
    print('Exiting main Event Loop')

asyncio.run(main())
