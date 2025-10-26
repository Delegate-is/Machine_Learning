import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='maxdele'
)
cursor = connection.cursor()
sql = "SELECT * FROM products"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
connection.close()
# UPDATE
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='maxdele'
)
cursor = connection.cursor()
sql_update = "UPDATE products SET price = %s WHERE u_name = %s"
values_update = (24.99, 'Product A')
cursor.execute(sql_update, values_update)
connection.commit()
print(cursor.rowcount, "record(s) updated successfully.")
connection.close()
# DELETE
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='maxdele'
)
cursor = connection.cursor()
sql_delete = "DELETE FROM products WHERE u_name = %s"
value_delete = ('Product E',)
cursor.execute(sql_delete, value_delete)
connection.commit()
print(cursor.rowcount, "record(s) deleted successfully.")
connection.close()

