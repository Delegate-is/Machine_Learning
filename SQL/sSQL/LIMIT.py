# LIMIT 
import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='maxdele'
)
cursor = connection.cursor()
sql_limit = "SELECT * FROM products LIMIT %s"
limit_value = (3,)
cursor.execute(sql_limit, limit_value)
results = cursor.fetchall()
for row in results:
    print(row)
connection.close()
