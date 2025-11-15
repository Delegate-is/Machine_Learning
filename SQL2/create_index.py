# first import pymysql
import pymysql
# Connect to the database
# create connection object by giving database host, user, password, database name
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='newmaxi' # replace with your database name
)
# once connection is established, user cursor to execute SQL queries
# create cursor object
cursor = connection.cursor()
# create table
sql_create_table = """
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    u_name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INT
);
"""
cursor.execute(sql_create_table)
print("Index 'idx_u_name' created successfully on 'u_name' column.")

# Create an index on the 'u_name' column of the 'products' table
sql_create_index = "CREATE INDEX idx_u_name ON products (u_name)"
cursor.execute(sql_create_index)

# show table
sql = 'SELECT * FROM products'
cursor.execute(sql)
#Fetch all the records
results = cursor.fetchall()
# print the records
for row in results:
    print(row)
    
# create table structure
sql_describe_table = "DESCRIBE products"
cursor.execute(sql_describe_table)
# Fetch and print the table structure
table_structure = cursor.fetchall()

# Open XAMPP and start Apache and MySQL modules.
# Open phpMyAdmin in your web browser by navigating to http://localhost/phpmyadmin.
# Select your database (e.g., 'newmaxi') from the left sidebar.
# Click on the 'products' table to view its structure.
# Click priveleges to view and edit indexes.
for column in table_structure:
    print(column)
    
# You should see the index 'idx_u_name' listed under the 'Indexes' section for the 'u_name' column.
# This confirms that the index has been successfully created.
# Note: Make sure to handle exceptions and errors in a production environment.
# You can also verify the index creation by running the following SQL command in phpMyAdmin:
# SHOW INDEX FROM products;
cursor.execute("SHOW INDEX FROM products")
indexes = cursor.fetchall()
for index in indexes:
    print(index)
# This will display all indexes on the 'products' table, including the one you just created.
connection.close()

# commiting == making permanent changes to the database
connection.commit()
# close the connection
connection.close()