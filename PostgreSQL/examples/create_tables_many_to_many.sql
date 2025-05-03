CREATE TABLE funcs(
	id serial PRIMARY KEY,
	title varchar(30) NOT NULL,
	s_desc varchar(30) NOT NULL,
	l_desc text NOT NULL
);

CREATE TABLE params(
	id serial PRIMARY KEY,
	title varchar(30) NOT NULL,
	s_desc varchar(30) NOT NULL
);

CREATE table func_params(
	f_id integer NOT NULL,
	p_id integer NOT NULL,
	FOREIGN KEY (f_id) REFERENCES funcs(id),
	FOREIGN KEY (p_id) REFERENCES params(id)
);

CREATE table examples(
	id serial PRIMARY KEY,
	code text NOT NULL
);

CREATE table func_examples(
	f_id integer NOT NULL,
	e_id integer NOT NULL,
	FOREIGN KEY (f_id) REFERENCES funcs(id),
	FOREIGN KEY (e_id) REFERENCES examples(id)
);

INSERT INTO funcs (title, s_desc, l_desc)
VALUES ('abs',
'абсолютное значение числа',
'возвращает абсолютное значение числа, переданного в параметре. Тип возвращаемого числа зависит от типа переданного числа в параметре: если в параметре int, то и вернет int, в остальных случаях - float.

Абсолютное значение числа (модуль числа) &mdash; не отрицательное значение этого числа, неформально объясняется как расстояние от начала координат до указанной точки.

В модуле Math есть похожая функция Math.fabs() которая возвращает абсолютное значение числа, но только в десятичном виде float.
');

INSERT INTO funcs (title, s_desc, l_desc)
VALUES ('delattr',
'удаление атрибута объекта',
'удаляет атрибут в указанном объекте. Аналог команды del obj.attr, только в качестве аргумента передается строка.');

INSERT INTO funcs (title, s_desc, l_desc)
VALUES ('getattr',
'получение значение атрибута',
'получает атрибут указанного объекта. Аналог команды obj.attr, только в качестве аргумента передается строка.');

INSERT INTO params (title, s_desc)
VALUES ('number',
'число любого типа');

INSERT INTO params (title, s_desc)
VALUES ('obj',
'объект любого типа');

INSERT INTO params (title, s_desc)
VALUES ('attr_name',
'Строка. Имя атрибута');

INSERT INTO params (title, s_desc)
VALUES ('default',
'Значение по умолчанию');


INSERT INTO func_params (f_id, p_id)
VALUES (2,
3);

INSERT INTO func_params (f_id, p_id)
VALUES (3,
4);

INSERT INTO examples (code)
VALUES ('"""Пример работы abs с числами"""

abs1 = abs(4)
abs2 = abs(-4)
abs3 = abs(-3.5)
abs4 = abs(-4 + 3j)

print(abs1)  # 4
print(abs2)  # 4
print(abs3)  # 3.5
print(abs4)  # 5.0');

INSERT INTO examples (code)
VALUES ('"""Пример работы abs с числами"""

abs1 = abs(4)
abs2 = abs(-4)
abs3 = abs(-3.5)
abs4 = abs(-4 + 3j)

print(abs1)  # 4
print(abs2)  # 4
print(abs3)  # 3.5
print(abs4)  # 5.0');

INSERT INTO examples (code)
VALUES ('"""Пример применения встроенной функции abs с объектами"""


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


coord = Coord(-6, -8)
print(abs(coord))  # 10.0'
);

INSERT INTO examples (code)
Values('
"""Пример использования встроенной функции delattr"""


class C:
    attrib = "attr"
    attrib2 = "attr2"


print([i for i in C.__dict__ if not i.startswith("__")])  # ["attrib", "attrib2"]
delattr(C, "attrib")
del C.attrib2
print([i for i in C.__dict__ if not i.startswith("__")])  # []
');

UPDATE examples
SET code = ('"""Пример использования встроенной функции delattr"""


class C:
    attrib = "attr"
    attrib2 = "attr2"


print([i for i in C.__dict__ if not i.startswith("__")])  # ["attrib", "attrib2"]
delattr(C, "attrib")
del C.attrib2
print([i for i in C.__dict__ if not i.startswith("__")])  # []
')
WHERE id = 3


SELECT * FROM examples;

SELECT * FROM func_examples;

INSERT INTO func_examples (f_id, e_id)
VALUES (2, 3);


ALTER TABLE params
ADD is_req bool

ALTER TABLE params
DROP is_req

SELECT f.title as f_title, f.s_desc as f_s_desc, p.title as p_title, p.s_desc as p_s_desc
FROM funcs as f
INNER JOIN func_params as fp
ON f.id = fp.f_id
INNER JOIN params as p
ON fp.p_id = p.id
WHERE f.title = 'abs'

SELECT f.title, f.s_desc, code
FROM funcs as f
INNER JOIN func_examples as fe
ON f.id = fe.f_id
INNER JOIN examples as ex
ON fe.e_id = ex.id
WHERE f.title = 'delattr'

SELECT f.title as f_title, f.s_desc as f_s_desc, p.title as p_title, p.s_desc as p_s_desc, code
FROM funcs as f
INNER JOIN func_params as fp
ON f.id = fp.f_id
INNER JOIN params as p
ON fp.p_id = p.id
INNER JOIN func_examples as fe
ON f.id = fe.f_id
INNER JOIN examples as ex
ON fe.e_id = ex.id
WHERE f.title = 'abs'