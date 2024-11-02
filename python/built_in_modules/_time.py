"""Работа с системными часами
Эра Unix - полночь 1 января 1970года

import time

time.time() - кол-во секунд прошедшее с Эры Unix (float)
time.sleep(sec) - остановка выполнения программы на sec

"""

import time
print(time.time())
print(time.sleep(1))
print(time.time())