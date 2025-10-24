import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='magicmax'
)
print("Database connection established successfully.")

# localhost/phpmyadmin/
if connection:
    print("Connection to the database is successful!")
else:
    print("Failed to connect to the database.")

cursor = connection.cursor()
