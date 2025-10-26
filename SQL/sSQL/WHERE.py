# Where Clause
import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='maxdele'
)
cursor = connection.cursor()
sql_where = "SELECT * FROM products WHERE u_price > %s"
value_where = (29.99,)
cursor.execute(sql_where, value_where)
results = cursor.fetchall()
for row in results:
    print(row)
connection.close()