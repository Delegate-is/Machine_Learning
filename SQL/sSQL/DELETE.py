# DELETE
import pymysql
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