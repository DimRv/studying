"""Сокет - программный интерфейс для обеспечения информационного обмена
socket.AF_INET - IPv4
socket.SOCK_STREAM - TCP
"""

import socket

# пример кода для сервера
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем объект Сокет
sock.bind(("localhost", 9999))  # привязываем сокет с хостом и портом ('' - доступ ко всем интерфейсам)
print(f"Стартуем сервер на 9999 порту")
sock.listen(1)  # Запускаем сокет в режим прослушивания. 1 - максимальное кол-во подключений в очереди
print("Ожидаем соединение...")
conn, addr = sock.accept()  # Принятие подключений, возвращает кортеж с новым сокетом и адресом клиента
print("Соединение установлено")
while True:
    data = conn.recv(1024)  # Получаем данные по 1024 байт
    print(f"Получили данные: {data.decode()}")
    data = data.upper()
    print(f"Обработка данных завершена: {data}")
    conn.sendall(data)  # Отправка клиенту данных
    print(f"Отправка данных клиенту")
    if not data:
        print("Соединение завершено")
        break
conn.close()


