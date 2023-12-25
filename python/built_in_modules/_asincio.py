"""
asyncio - asynchronous input output - модуль для работы с сопрограммами

Модуль asyncio даёт нам средства для запуска объектов корутин
Цикл событий - среда выполнения для корутин

async def - определение корутины, функция возвращает объект-корутину, а не выполняет строки кода функции.

Объект-корунита - объект, допускающий ожидание, то есть в нем реализован метод __await__ и такой объект может быть
использован в операторе await.

Выполнять корутину можно только в цикле событий.
Цикл событий (Event Loop) выполняет:
    - корутины
    - коллбеки
    - асинхронные задачи
    - сетевые задачи ввода вывода
    - подпроцессы
Код объекта-корутины выполняется только когда запущен Цикл-событий
Цикл событий управляет списком задач и стремится продвинуть выполнение
каждой из своих задач в определенной последовательности на каждой своей итерации

asynco.run(main_coroutine) - типичный способ запуска цикла событий - возвращает объект цикла событий. Создаст Task.
asyncio.new_event_loop()  - создает новый цикл событий
asyncio.get_event_loop() - доступ к циклу, но вроде как устаревший
asyncio.get_running_loop() - доступ к запущенному циклу событий или Runtime error. Доступ из coroutine, для:
- мониторинга хода выполнения
- получения результатов работы задач
- для запуска одноразовых задач
Циклы событий имеют разную реализацию в зависимости от ОС:
linux: SelectorEventLoop
Windows: ProactorEventLoop
Цикл событий управляет задачами (Task)

Объект Task создаются из корутин и содержит инструмены для планирования и выполнения:
- постановка корутин в очередь выполнения и их независимы запуск
- отмена выполнения корутин
- получать в нужное время результат выполнения или исключения

asyncio.Task - объект task это Future-подобный объект
asuncio.Future - низкоуровневый объект который когда-нибудь вернет результат, имеет __await__

asyncio.create_task(coroutine(), name='Name') - создание задачи из coroutine(),
подразумевается выполнение в текущем цикле событий
asyncio.ensure_future(TASK/FUTURE/COROUTINE/EVENTLOOP) - низкоуровневый способ
loop.create_task() - нужен доступ к циклу событий asyncio.get_event_loop()/ asyncio.get_running_loop

Задача не будет запущена до тех пор, пока у цикла событий не появится возможность её запустить,
не будет выполнена до тех пор, пока вызывающая корутина, создавшая эту задачу, не будет приостановлена await

Жизненный цикл задачи:
- создание (creating)
- планирование выполнения (scheduled)
- выполнение (running)
- завершение (Done)

task.done - вернет True/False в зависимости от того завершена ли задача. True при:
- нормальное завершение
- Корутина вернула результат
- Выдала ошибку или исключение
- при отмене
Повторно task.done=True задачу запустить не получится

task.cancelled() - True при отмене выполнения задачи, иначе False
value = task.result() - None, ecли корутина не возвращала значения иначе return значение или:
asyncio.CancelledError - при завершении taskа cancel
asyncio.InvalidStateError - при еще ее выполнении

exception = task.exception() - получение исключение, вызванного задачей
was_censelled = task.cancel() - остановка задачи, вернет True/False
task.add_done_callback(func) - выполнение callback функции при выполнении задачи (можно несколько)
task.remove_done_callback(func) - удаление из коллбэк
task.set_name("Name") - Задать имя
task.get_name("Name") - Получить имя
asyncio.current_task() - получить текущую задачу - либо coro в asyncio.run(coro) или из task.create_task()
asyncio.all_tasks() - возвращает множество, список всех задач выполняющихся или готовых к выполнению

asyncio.gather(tasks) - группировка объектов, допускающих ожидание
"""
import asyncio
help(asyncio)
print('Пример1'.center(80, '-'))


async def my_coro():
    print('Hello coroutine!')
    my_coro_loop = asyncio.get_running_loop()
    print(my_coro_loop, type(my_coro_loop)) #объект цикла событий имеет статус running=True
    await asyncio.sleep(1)


coro = my_coro() #corotine-object
loop = asyncio.new_event_loop() #создание цикла событий
print(coro, type(coro))
print([i for i in dir(coro)])
print(loop, type(loop))
print([i for i in dir(loop)])


print('Пример2'.center(80, '-'))


async def f1(ticks, sleep):
    print('starting f1')
    for i in range(ticks):
        print(i)
        await asyncio.sleep(sleep)
    print('stopping f1')


async def f2(ticks, sleep):
    print('starting f2')
    for i in range(ticks):
        print(i)
        await asyncio.sleep(sleep)
    print('stopping f2')


async def run():
    """Основная корутина от которой запускаются все задачи"""
    task0 = asyncio.create_task(my_coro())
    task1 = asyncio.create_task(f1(10, 2))
    task2 = asyncio.create_task(f2(5, 4))
    print(task0, type(task0))
    await asyncio.gather(task0, task1, task2)

asyncio.run(run())
