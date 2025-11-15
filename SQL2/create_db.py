import pymysql
# Connect to the database server
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
)
# Create a cursor object
cursor = connection.cursor()
# Create database if it doesn't exist
sql_create_db = "CREATE DATABASE IF NOT EXISTS avatar"
cursor.execute(sql_create_db)
# Select the database
sql_use_db = "USE avatar"
cursor.execute(sql_use_db)
# Create 'products' table
sql_create_table = """CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    u_name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INT
);"""
cursor.execute(sql_create_table)
# Create 'users' table
sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);"""
cursor.execute(sql_create_users_table)
print("Database 'avatar' and tables 'products' and 'users' created successfully or already exist.")
# Close the connection
connection.close()