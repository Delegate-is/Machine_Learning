import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='avatar'
);
cursor = connection.cursor()
sql_insert_products = "INSERT INTO products (u_name, price, quantity) VALUES (%s, %s, %s)"
products_values = [
    ('Product 1', 19.99, 10),
    ('Product 2', 29.99, 5),
    ('Product 3', 9.99, 20),
    ('Product 4', 14.99, 15),
    ('Product 5', 49.99, 8)
]
cursor.executemany(sql_insert_products, products_values)
# commit == make permanent changes to the database
connection.commit()
print(cursor.rowcount, "records inserted successfully into products table.")

sql_insert_users = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
users_values = [
    ('user1', 'max342@gmail.com', 'password123'),
    ('user2', 'wanjiru23@outlook.com', 'mypassword'),
    ('user3', 'maina254@yahoo.com', 'securepass'),
    ('user4', 'omondi001@hotmail.com', 'passw0rd'),
    ('user5', 'ekino23876@gmail.com', 'letmein123')
]
cursor.executemany(sql_insert_users, users_values)
connection.commit()
print(cursor.rowcount, "records inserted successfully into users table.")
connection.close()