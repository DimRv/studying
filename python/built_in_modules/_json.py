"""JSON - JavaScript Object Notation
Модуль преобразует типы данный JSON к типам python.
Предназначен для передачи данных

Типы данных для хранения в JSON:
- str, int, float, bool, list, dict, NoneType

json.loads() - загрузка JSON данных из json-строки и преобразование в dict
json.load() - загрузка JSON данных из json-файла
json.dumps() - выгрузка данных из dict и преобразование в json-строку
json.dump() - выгрузка JSON данных в файл
"""

import json
from pprint import pprint

print(dir(json))

# Преобразование JSON-строки в dict
json_data = '{"name": "Tima", "isCat": true, "mouseCaught": {"mouse": 0, "rats": 0}, "IQLevel": null}'
py_data = json.loads(json_data)
print(type(py_data))
pprint(py_data)
print("-"*30)

# Запись dict в JSON-файл
with open(r"dir_for_tests\test-json.json", 'w') as file:
    json.dump(py_data, file, indent=4)

# Преобразование dict в JSON-строку
py_dict = {
    "name": "Boris",
    "isCat": True,
    "mouseCaught": 1,
    "IQLevel": None,
    "hate_cats": ['Markiz', "Murzik"]
}
json_data2 = json.dumps(py_dict)
print(json_data2, type(json_data2))

# Чтение данных из JSON-файла
with open(r"dir_for_tests\test-json.json", 'r') as file:
    loaded_dict = json.load(file)

print(loaded_dict, type(py_dict))
loaded_dict["added_data"] = py_dict

with open(r"dir_for_tests\test-json.json", 'w') as file:
    json.dump(loaded_dict, file, indent=4)

