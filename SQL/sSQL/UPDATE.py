# UPDATE
import pymysql
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