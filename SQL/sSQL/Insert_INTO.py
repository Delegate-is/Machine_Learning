import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='maxdele'
)
cursor = connection.cursor()
sql = "INSERT INTO products (u_name, price, quantity) VALUES (%s, %s, %s)"
values = [
    ('Product A', 19.99, 10),
    ('Product B', 29.99, 5),
    ('Product C', 9.99, 20),
    ('Product D', 14.99, 15),
    ('Product E', 49.99, 8)
]
cursor.executemany(sql, values)
connection.commit()
print(cursor.rowcount, "records inserted successfully into products table.")
connection.close()