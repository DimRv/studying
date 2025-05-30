import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет - интерфейс для общения с сервером
sock.connect(('localhost', 9999))  # подключемся к серверу
print("Подключение к localhost по 9999 порту")
sock.send("Hello! world!".encode())  # отправляем данные

data = sock.recv(1024).decode()  # Получаем 1024 килобайт данных
sock.close()  # Закрываем подключение

print(data)