import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
)
cursor = connection.cursor()
sQl ="CREATE DATABASE IF NOT EXISTS maxdele"
cursor.execute(sQl)
sql2 = "USE maxdele"
cursor.execute(sql2)

sql3 = """CREATE TABLE IF NOT EXISTS products (
    u_id INT AUTO_INCREMENT PRIMARY KEY,
    u_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL
)"""
cursor.execute(sql3)

sql4 = """CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
)"""  
cursor.execute(sql4)

print("Database 'maxdele' created successfully or already exists.")
connection.close()