"""Работа с .csv-файлами
r = csv.reader() - создание объекта reader, через которое происходит чтение данных файла
w = csv.writer(delimiter=',' lineterminator='\n') - создание объекта writer, запись в файл
цикл по объекту reader может быть только один раз
r.line_num - номер строки
w.writerow() - запись строки

csv.DictWriter - oбъект записи в файл
"""
import csv

print(dir(csv))

with open(r'.\dir_for_tests\csv-file.csv') as file:
    reader1 = csv.reader(file)
    print(reader1)
    content = list(reader1)
    print(content)
    print(content[0])
    print(content[0][0])

with open(r'.\dir_for_tests\csv-file.csv') as file:
    reader2 = csv.reader(file)
    for row in reader2:
        print(f"{reader2.line_num}. {row}")

with open(r'.\dir_for_tests\csv-file.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ha', 'haha', 'hahaha'])

print('Работа со словарем'.center(50, '-'))

data = [
    {"cat": "Tima", "age": 2, "is_fool": True},
    {"cat": "Borya", "age": 3, "is_fool": False},
]

with open(r"dir_for_tests\csv-file-new.csv", 'w', newline="") as file:
    headers = data[0].keys()
    dw = csv.DictWriter(file, headers)
    dw.writeheader()
    dw.writerows(data)

with open(r"dir_for_tests\csv-file-new.csv", 'r', newline="") as file:
    dr = csv.DictReader(file)
    for i in dr:
        print(i)

with open(r"dir_for_tests\csv-file-new.csv", 'r', newline="") as file:
    r = csv.DictReader(file).reader
    for i in r:
        print(i)

