"""Работа с .csv-файлами
r = csv.reader() - создание объекта reader, через которое происходит чтение данных файла
w = csv.writer(delimiter=',' lineterminator='\n') - создание объекта wrighter, запись в файл
цикл по объекту reader может быть только один раз
r.line_num() - номер строки
w.writerow() - запись строки

"""
import csv
file1 = open(r'.\dir_for_tests\csv-file.csv')
reader1 = csv.reader(file1)
print(reader1)
content = list(reader1)
print(content)
print(content[0])
print(content[0][0])
file1.close()

file2 = open(r'.\dir_for_tests\csv-file.csv')
reader2 = reader1 = csv.reader(file2)
for row in reader2:
    print(f"{reader2.line_num}. {row}")
file2.close()

with open(r'.\dir_for_tests\csv-file.csv', 'a', newline='') as file3:
    writer = csv.writer(file3)
    writer.writerow(['ha', 'haha', 'hahaha'])
