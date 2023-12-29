"""Возвращает следующее значение в асинхронном итераторе aiter()
async anext(aiterator[, default])
"""
import asyncio

help(anext)


class AsyncIter:
    def __init__(self):
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= 5:
            raise StopAsyncIteration
        self.counter += 1
        await asyncio.sleep(1)
        return self.counter


async def main():
    """ai = aiter(AsyncIter())
    print(anext(ai))
    print(anext(ai))
    print(anext(ai))
    print(anext(ai))
    print(anext(ai))
    print(anext(ai))"""
    async for i in aiter(AsyncIter()):
        print(i)


asyncio.run(main())
