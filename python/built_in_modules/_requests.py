"""Загрузка файлов и веб страницы из Интерента

res = requests.get() - запрос содержимого WEB-страницы
res.status_code == requests.codes.ok
res.raise_for_status() - исключение если во время загрузки файла произошла ошибка
res.text - содержимое WEB-страницы, можно обработать с помощью BeautifulSoup()
data = res.iter_content(100000) - получение данных по 100000 байт

обработать


"""

import requests

res = requests.get('https://ya.ru')
print(len(res.text))
