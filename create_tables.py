import sqlite3 as sq
with sq.connect('restaurant.db') as db:
    cur = db.cursor()

    # Table 1 (courier_info)
    cur.execute("DROP TABlE IF EXISTS courier_info")
    cur.execute("""CREATE TABLE IF NOT EXISTS courier_info(
    courier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    delivery_type TEXT)
    """)
    values_1 = [
        ('Алексей', 'Филимонов', '+ 8 915 655 0954', 'пешком'),
        ('Артем', 'Луньков', '+ 8 916 743 0146', 'авто'),
        ('Александр', 'Чибисов', '+ 8 915 107 7798', 'авто'),
        ('Александр', 'Мясников', '+ 8 995 566 5516', 'авто')
    ]
    cur.executemany("INSERT INTO courier_info VALUES(NULL,?,?,?,?)", values_1)

    # Table 2 (customers)
    cur.execute("DROP TABlE IF EXISTS customers")
    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    district TEXT,
    street TEXT,
    house INTEGER,
    apartment INTEGER)
    """)
    values_2 = [
        ('Дарья', 'Смитт', '+ 8 916 572 3771', 'Южное Бутово', 'Изюмская', 1, 10),
        ('Ольга', 'Викторова', '+ 8 916 568 8452', 'Северное Бутово', 'Чечерская', 2, 35),
        ('Иван', 'Волков', '+ 8 916 782 5648', 'Раменки', 'Ленинский Пр.', 77, 14),
        ('Тимур', 'Маслов', '+ 8 916 752 1224', 'Южное Бутово', 'Изюмская', 24, 89),
        ('Анна', 'Шувалова', '+ 8 916 555 4568', 'Тропарево', 'Ветренная', 11, 85),
        ('Анна', 'Задорожная', '+ 8 916 321 3211', 'Измайлово', 'Измайловская', 123, 52),
        ('Алексей', 'Жигулевцев', '+ 8 916 321 1232', 'ВДНХ', 'Ботаническая', 76, 44),
        ('Максим', 'Смагин', '+ 8 916 122 4554', 'Северное Бутово', 'Октябрьская', 21, 91),
        ('Юрий', 'Волков', '+ 8 916 758 1667', 'Чертаново', 'Победная', 23, 67),
        ('Кристина', 'Александрова', '+ 8 916 765 8582', 'Чертаново', 'Ленина', 62, 44),
        ('Наталья', 'Тарасова', '+ 8 916 657 5528', 'Чертаново', 'Победная', 15, 56),
        ('Руслан', 'Меркулов', '+ 8 916 624 3643', 'Царицыно', 'Царицынская', 5, 13),
        ('Иван', 'Алексеев', '+ 8 916 303 8181', 'Берюлево', 'Восточная', 18, 88),
        ('Григорий', 'Отрепьев', '+ 8 916 466 7562', 'Южное Бутово', 'Кадырова', 17, 7),
        ('Ада', 'Ватсон', '+ 8 916 114 7812', 'Южное Бутово', 'Изюмская', 18, 9)
    ]
    cur.executemany("INSERT INTO customers VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", values_2)

    # Table 3 (products)
    cur.execute("DROP TABlE IF EXISTS products")
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    menu_name TEXT,
    price REAL)
    """)
    values_3 = [
        ('РОЛЛЫ КАЛИФОРНИЯ', 300),
        ('РОЛЛЫ ФИЛАДЕЛЬФИЯ', 300),
        ('СУШИ', 250),
        ('РОЛЛ ЦЕЗАРЬ', 300),
        ('РОЛЛ С КРЕВЕТКАМИ', 350),
        ('ВЕГАТАРИАНСКИЙ САЛАТ', 220),
        ('ГРЕЧЕСКИЙ САЛАТ', 300),
        ('ЧАЙ', 175),
        ('КОФФЕ', 200),
        ('МИНЕРАЛЬНАЯ ВОДА', 150)
    ]
    cur.executemany("INSERT INTO products VALUES(NULL, ?, ?)", values_3)

    # Table 4 (delivery_list)
    cur.execute("DROP TABlE IF EXISTS delivery_list")
    cur.execute("""CREATE TABLE IF NOT EXISTS delivery_list(
    delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    courier_id INTEGER,
    date_arrived TEXT,
    taken TEXT,
    payment_method TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (courier_id) REFERENCES courier_info(courier_id))
    """)
    values_4 = [
        (1, 3, '2021-12-26 17:59:15', 'Yes', 'Наличные'),
        (2, 4, '2021-12-26 18:01:05', 'Yes', 'Карта'),
        (3, 1, '2021-12-26 18:04:36', 'Yes', 'Наличные'),
        (4, 2, '2021-12-26 18:03:11', 'Yes', 'Наличные'),
        (5, 1, '2021-12-26 18:19:56', 'Yes', 'Наличные'),
        (6, 3, '2021-12-26 18:18:44', 'Yes', 'Карта'),
        (7, 2, '2021-12-26 19:50:11', 'No', 'NULL'),
        (8, 4, '2021-12-26 18:35:07', 'Yes', 'Карта'),
        (9, 4, '2021-12-26 19:58:28', 'No', 'NULL'),
        (10, 3, '2021-12-26 18:36:51', 'Yes', 'Карта'),
        (11, 2, '2021-12-26 19:10:34', 'Yes', 'Наличные'),
        (12, 2, '2021-12-26 19:17:04', 'Yes', 'Наличные'),
        (13, 3, '2021-12-26 19:56:17', 'Yes', 'Карта'),
        (14, 4, '2021-12-26 20:05:29', 'Yes', 'Карта'),
        (15, 4, '2021-12-26 20:25:29', 'Yes', 'Карта'),
    ]
    cur.executemany("INSERT INTO delivery_list VALUES(NULL, ?, ?, ?, ?, ?)", values_4)

    # Table 5 (orders)
    cur.execute("DROP TABlE IF EXISTS orders")
    cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    date_get TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id))
    """)
    values_5 = [
        (1, '2021-12-26 16:59:15'),
        (2, '2021-12-26 17:01:05'),
        (3, '2021-12-26 17:04:36'),
        (4, '2021-12-26 17:03:11'),
        (5, '2021-12-26 17:19:56'),
        (6, '2021-12-26 17:18:44'),
        (7, '2021-12-26 17:50:11'),
        (8, '2021-12-26 17:35:07'),
        (9, '2021-12-26 17:58:28'),
        (10, '2021-12-26 17:36:51'),
        (11, '2021-12-26 18:10:34'),
        (12, '2021-12-26 18:17:04'),
        (13, '2021-12-26 18:56:17'),
        (14, '2021-12-26 19:05:29'),
        (15, '2021-12-26 19:25:29')
    ]
    cur.executemany("INSERT INTO orders VALUES(NULL, ?, ?)", values_5)

    # Table 6 (orders_products)
    cur.execute("DROP TABlE IF EXISTS orders_products")
    cur.execute("""CREATE TABLE IF NOT EXISTS orders_products(
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        PRIMARY KEY (order_id, product_id),
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id))
        """)
    values_6 = [
        (1, 1, 2), (1, 4, 1), (1, 10, 1),
        (2, 4, 1), (2, 5, 1),
        (3, 3, 1),
        (4, 7, 2),
        (5, 2, 1), (5, 3, 1),
        (6, 8, 3),
        (7, 1, 1), (7, 6, 4),
        (8, 1, 2),
        (9, 2, 1), (9, 3, 1),
        (10, 1, 2), (10, 2, 1),
        (11, 1, 1), (11, 2, 3),
        (12, 5, 2), (12, 10, 1),
        (13, 4, 2),
        (14, 5, 1),
        (15, 8, 1), (15, 7, 2)
    ]
    cur.executemany("INSERT INTO orders_products VALUES(?, ?, ?)", values_6)
sq.connect("restaurant.db").close()
    # Output
    # cur.execute("SELECT * FROM orders_products")
    # all_results = cur.fetchall()
    # print(all_results)
