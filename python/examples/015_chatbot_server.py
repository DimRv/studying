import socket
import datetime
import json
import requests


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем объект Сокет
sock.bind(("localhost", 9999))  # привязываем сокет с хостом и портом ('' - доступ ко всем интерфейсам)
print(f"Стартуем сервер на 9999 порту")
sock.listen(1)  # Запускаем сокет в режим прослушивания. 1 - максимальное кол-во подключений в очереди
print("Ожидаем соединение...")
while True:
    conn, addr = sock.accept()  # Принятие подключений, возвращает кортеж с новым сокетом и адресом клиента
    print("Соединение установлено")
    data = """
    Напишите:
        "время" - для получения актуального времени
        "праздники" - для получения списка праздничных дней в году
        "курсы" - для получения списка курсов валют
        "пример" - для расчета математического примера
        "выход" - для закрытия чата
    """
    conn.sendall(data.encode())
    while True:
        data = conn.recv(1024).decode()
        answer = 'Не корректный запрос'
        match data:
            case 'время':
                print("Получен запрос на вывод времени")
                answer = datetime.datetime.now().strftime("%H:%M:%S")

            case "праздники":
                year = str(datetime.date.today().year)
                print("Получен запрос на получение списка праздников в текущем году")
                answer = f'Праздники в {year} году:\n'
                url = 'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant' + year + '.json'
                holidays_calendar = json.loads(requests.get(url).text)
                for holiday in holidays_calendar['holidays']:
                    answer += f"{holiday}\n"

            case "курсы":
                print("Получен запрос на получение курса валют")
                url = "https://www.cbr-xml-daily.ru/daily_json.js"
                valutes = json.loads(requests.get(url).text)
                valutes_codes = valutes['Valute'].keys()
                answer = "Выберите интересующую валюту из списка:\n"
                answer += str(valutes_codes)
                conn.sendall(answer.encode())
                val_code = conn.recv(1024).decode().upper()
                print(f"Получен код: {val_code}")
                if val_code in valutes_codes:
                    answer = ""
                    for k, v in valutes['Valute'][val_code].items():
                        answer += f"{k}:\t{v}\n"
                else:
                    answer = 'Не корректен код валюты'

            case 'пример':
                print("Получен запрос на расчет примера")
                answer = 'Введите пример для расчета, например: 3 + 4'
                conn.sendall(answer.encode())
                primer = conn.recv(1024).decode()
                print(f"Расчет {primer}")
                answer = str(eval(primer))

            case 'выход':
                print("Получен запрос на выход")
                conn.send("выход".encode())
                conn.close()
                break
        conn.sendall(answer.encode())
    sock.close()
    break


