"""Использование typing может расширить возможности аннотаций:
Optional[int] - опциональная переменная
List[str] - список из строк
Tuple[str] - кортеж из строк
Dict[str, str]
Union[int, float] - разные типы
Any - любая переменная
"""


import typing
print([i for i in dir(typing)])

print(__annotations__)
var1: str = "Hello? World!"
var2: int = '4'
print(__annotations__)
var3: typing.List[str] = [1, 2]
print(__annotations__)
var4: typing.Union[int, float, complex] = 'ad'
print(__annotations__)
var5: int | float | complex = 'ad'
print(__annotations__)
var6: list[str] = [1, 2]
print(__annotations__)

