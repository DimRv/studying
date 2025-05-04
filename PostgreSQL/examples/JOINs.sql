CREATE TABLE CUSTOMERS (
customer_id serial PRIMARY KEY,
customer_name varchar(30)
);

CREATE TABLE ORDERS (
order_id serial PRIMARY KEY,
customer_id integer,
amount decimal,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO CUSTOMERS (customer_name)
VALUES ('Иванов Иван'), ('Брюс Уиллис')

INSERT INTO ORDERS (customer_id, amount)
VALUES (1, 156.78), (2, 99.99), (1, 75.00)

SELECT * FROM CUSTOMERS

SELECT * FROM ORDERS

SELECT * FROM CUSTOMERS CROSS JOIN ORDERS

SELECT * FROM CUSTOMERS NATURAL JOIN ORDERS  (по совпадающему столбцу)

SELECT * FROM CUSTOMERS JOIN ORDERS
ON customers.customer_id = ORDERS.customer_id
WHERE customers.customer_name = 'Брюс Уиллис'

SELECT * FROM CUSTOMERS JOIN ORDERS
USING (customer_id)
WHERE customers.customer_name = 'Брюс Уиллис'

INSERT INTO CUSTOMERS (customer_name)
VALUES ('Петров Петя')

SELECT * FROM CUSTOMERS LEFT OUTER JOIN ORDERS
USING (customer_id)

SELECT * FROM ORDERS RIGHT JOIN CUSTOMERS
USING (customer_id)

SELECT * FROM ORDERS WHERE amount > 80

CREATE INDEX amount ON ORDERS(amount)