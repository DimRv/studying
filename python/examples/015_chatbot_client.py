import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет - интерфейс для общения с сервером
while True:
    sock.connect(('localhost', 9999))  # подключаемся к серверу
    data = sock.recv(1024).decode()  # Получаем 1024 килобайт данных
    print(data)

    while True:
        command = input().lower()
        sock.send(command.encode())
        data = sock.recv(1024*10).decode()
        print(data)
        if data == "выход":
            break
    sock.close()
    break
