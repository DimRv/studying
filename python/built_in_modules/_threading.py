"""Многопоточное выполнение кода программы

threading.Thread(target=ta) - создание объекта потока

"""


if __name__ == "__main__":
    import threading, time
    print("Начало программы в основном потоке")

    def long_liming_func(t):
        print("Начало выполнения второго потока")
        time.sleep(t)
        print("Конец выполненения 2го потока!")

    thread_obj = threading.Thread(target=long_liming_func, args=[5])
    thread_obj.start()
    print("Основной поток завершается")
