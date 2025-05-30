from pprint import pprint
import psycopg2
from psycopg2.extras import RealDictCursor

# Импортируем класс, чтобы каждая строка из таблицы в базе данных была
# считана как объект, который является оболочкой для словаря. Другими
# словами, мы сможем таким образом работать с каждой строкой из таблицы
# как со словарем, каждое название столбца является названием ключа в словаре


connect = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    dbname='lesson09',
    port='5432'
)


def show_data():
    sql = "SELECT * FROM cars"
    cursor.execute(sql)  # Запустим sql на сервере
    data = cursor.fetchall()  # Получим список объектов, каждый объект описывает одну запись
    pprint(data)
    for item in data:
        print(f"{item['title']} стоит {item['price']}")


def update_car():
    info = input("Введите название авто у которой необходимо"
                 " изменить цену и новую цену через пробел").split()
    sql_update = f"UPDATE cars SET price={info[1]} WHERE title='{info[0]}'"
    cursor.execute(sql_update)


with connect:
    # Для возможности запуска sql запросов на сервере используем объект cursor
    cursor = connect.cursor(cursor_factory=RealDictCursor)
    show_data()
    update_car()
    print("*"*50)
    show_data()
    connect.commit()  # Для сохранения сделанных изменений в базе нужно данные сохранить:
