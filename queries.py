import sqlite3 as sq

class Query:
    num = 0
    def __new__(cls, arg):
        cls.num += 1
        return super().__new__(cls)

    def __str__(self):
        return f'{self.num}. '+ self.query

    def __init__(self, query):
        self.query = query
        self.num = self.num
        print(f'{self.num}. {self.query}')
print("Доступные опции:")
q1 = Query("Информация о том, сколько заказов каждый курьер доставил клиенту")
q2 = Query("Информация о покупателях проживающих в Южном Бутово")
q3 = Query("Информация о заказах, которые не были приняты")
q4 = Query("Информация о заказанных продуктах из меню")
q5 = Query("Информация о продуктах из меню, которые НЕ были заказаны")
q6 = Query("Информация о частоте районов среди клиентов")
q7 = Query("Информация о списке клиентов и курьеров")
q8 = Query("Информация о деталях для каждого заказа")
with sq.connect('restaurant.db') as db:
    cur = db.cursor()
    while True:
        print('\n')
        print("Введите нужный запрос:")
        number = int(input())

        if number == 1:
            print("Информация о том, сколько заказов каждый курьер доставил клиенту")
            cur.execute("""
                        SELECT courier_info.courier_id, first_name, count(delivery_list.order_id) as "Колличество заказов" FROM courier_info
                        JOIN delivery_list ON courier_info.courier_id = delivery_list.courier_id
                        WHERE date_arrived IS NOT NULL
                        GROUP BY delivery_list.courier_id
                        """)
        if number == 2:
            print("Информация о покупателях проживающих в Южном Бутово")
            cur.execute("""
                        SELECT first_name, last_name, district FROM customers
                        WHERE district = 'Южное Бутово'
                        """)
        if number == 3:
            print("Информация о заказах, которые не были приняты")
            cur.execute("""
                        SELECT courier_info.first_name, courier_info.last_name, order_id, date_arrived FROM delivery_list
                        JOIN courier_info ON courier_info.courier_id = delivery_list.courier_id
                        WHERE taken = 'No'
                        """)
        if number == 4:
            print("Информация о заказанных продуктах из меню")
            cur.execute("""
                        SELECT courier_info.first_name, courier_info.last_name, order_id, date_arrived FROM delivery_list
                        JOIN courier_info ON courier_info.courier_id = delivery_list.courier_id
                        WHERE taken = 'Yes'
                        """)
        if number == 5:
            print("Информация о заказанных продуктах из меню")
            cur.execute("""
                        SELECT courier_info.first_name, courier_info.last_name, order_id, date_arrived FROM delivery_list
                        JOIN courier_info ON courier_info.courier_id = delivery_list.courier_id
                        WHERE taken = 'No'
                        """)
        if number == 6:
            print("Информация о частоте районов среди клиентов")
            cur.execute("""
                        SELECT count(customer_id) as "Колличество заказов", district FROM customers
                        GROUP BY district
                        """)
        if number == 7:
            print("Информация о списке клиентов и курьеров")
            cur.execute("""SELECT 'Customer' AS category, first_name, last_name, phone_number
                           FROM customers
                           UNION
                           SELECT 'Employee' AS category, first_name, last_name, phone_number
                           FROM courier_info""")
        if number == 8:
            print("Информация о деталях для каждого заказа")
            cur.execute("""SELECT order_id, menu_name, quantity, ROUND(price*quantity, 2) FROM products
                           JOIN orders_products ON products.product_id = orders_products.product_id



                        """)
        out = cur.fetchall()
        headers = list(map(lambda x: x[0], cur.description))
        columns_width = max(max(len(str(word)) for row in out for word in row), max(len(str(word)) for word in headers))
        columns_number = len(out[0])
        format_string = ("| {: <" + str(columns_width) + "} |") * columns_number
        print(('+' + ('-' * (columns_width + 2)) + '+') * columns_number)
        print(format_string.format(*headers))
        print(('+' + ('-' * (columns_width + 2)) + '+') * columns_number)
        for result in out:
            print(format_string.format(*result))
            print(('+' + ('-' * (columns_width + 2)) + '+') * columns_number)
#if number = Query.num
