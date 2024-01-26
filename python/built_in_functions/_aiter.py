"""
aiter(obj) -> aiter

Встроенная функция aiter возвращает объект асинхронного итератора, который в будущем может быть использован
в корутине.

В качестве параметра передается объект, содержащий метод __aiter__.

Функция применяется при асинхронном программировании, при использовании модуля asyncio.
"""
import asyncio


class AsyncIter:
    def __init__(self):
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= 10:
            raise StopAsyncIteration
        self.counter += 1
        await asyncio.sleep(0.01)
        return self.counter


async def main():
    async for i in aiter(AsyncIter()):
        print(i)


asyncio.run(main())