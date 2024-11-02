"""JSON - JavaScript Object Notation

Типы данных для хранения в JSON:
- str, int, float, bool, list, dict, NoneType

json.loads() - загрузка данных из JSON-формата
json.dumps() - выгрузка данных в JSON

"""

import json

json_data = '{"name": "Tima", "isCat": true, "mouseCaught": 0, "IQLevel": null}'
py_data = json.loads(json_data)
print(py_data)

py_dict = {
    "name": "Boris",
    "isCat": True,
    "mouseCaught": 1,
    "IQLevel": None,
}

json_data2 = json.dumps(py_dict)
print(json_data2)