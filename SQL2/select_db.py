import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='avatar'
)

cursor = connection.cursor()
sql_select = "SELECT * FROM products"
cursor.execute(sql_select)
results = cursor.fetchall()
for row in results:
    print(f"Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}")
connection.close()