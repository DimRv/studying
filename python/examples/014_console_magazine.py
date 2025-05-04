"""
Создание консольного магазина:

1) Создать каталог товаров, то есть список словарей, каждый товар
из себя представляет словарь с ключами id, title, price:

2) Создать пустой список для товаров корзины. Должна быть функция, которая
принимает в качестве параметра id товара и проверяет есть ли такой id в списке
товаров корзины. Если есть, то у текущего товара корзины увеличиваем
свойство количество на 1. А если товар не найден в корзине, то его нужно
создать и добавить в корзину с количеством 1 ед. У товара корзины должно
быть два свойства - id товара и количество товаров.

3) Создать функцию для вывода корзины покупок
4) Сделать меню с 4 пунктами:
    1) Вывести все товары каталога
    2) Добавить товар в корзину по id.
    3) Вывести корзину
    4) Выход
"""


def show_line():
    """Линия чтобы все не смешивалось в один текст"""
    print("-" * 40)


def show_catalog():
    """Выводим список товаров"""
    show_line()
    for item in goods:
        print(f"\t{item['id']}) {item['title']} {item['price']}руб")


def get_good(good_id):
    """Возвращаем данные о товаре по его id"""
    for item in goods:
        if item['id'] == good_id:
            return item


def get_id():
    """Получаем id от пользователя"""
    while 1:
        show_line()
        good_id = input("Введите id товара для покупки или -1 для выхода:\n")
        if good_id.isdigit():
            good_id = int(good_id)
            if get_good(good_id):
                return good_id
        if good_id == '-1':
            return
        print("Такого товара у нас нет в каталоге")


def add_goods():
    """Добавляем товар в корзину"""
    good_id = get_id()
    if not good_id:
        return
    if shopping:
        for item in shopping:
            if good_id == item["id"]:
                item["count"] += 1
                show_line()
                print("Увеличено кол-во товаров")
                return
    shopping.append({'id': good_id, 'count': 1})
    show_line()
    print("Товар успешно добавлен в корзину")


def show_shopping():
    """Отображаем товары в корзине"""
    show_line()
    total_price = 0
    if shopping:
        print("Ваш заказ:")
        for good in shopping:
            good_info = get_good(good['id'])
            price = good_info['price'] * good['count']
            print(f"{good_info['title']} {good_info['price']}руб * {good['count']} = {price}руб")
            total_price += price
        print(f"Итого:\n\t{total_price}руб")
    else:
        print("Нет товаров в корзине")


goods = [{'id': 1, 'title': 'ноутбук', 'price': 50000},
         {'id': 2, 'title': 'смартфон', 'price': 25000},
         {'id': 3, 'title': 'монитор', 'price': 15000},
         {'id': 4, 'title': 'системный блок', 'price': 70000}]

shopping = []

show_line()
print("Добро пожаловать в магазин!")

while 1:
    show_line()
    enter = input("Выберите нужное действие (1-4):\n"
                  "1) Вывести все товары каталога\n"
                  "2) Добавить товар в корзину по id\n"
                  "3) Вывести корзину\n"
                  "4) Выход\n")

    match enter:
        case '1':
            show_catalog()
        case '2':
            add_goods()
        case '3':
            show_shopping()
        case "4":
            show_line()
            print("Всего доброго!")
            break
