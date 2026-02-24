import pymysql

# Database connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password='',
)

# Create a cursor object
cursor = conn.cursor()
# Create database if it doesn't exist
sql_create_db = "CREATE DATABASE IF NOT EXISTS Njuwan_Farm"
cursor.execute(sql_create_db)
# Select the database
sql_use_db = "USE Njuwan_Farm"
cursor.execute(sql_use_db)

# 1. Create the Cattle Table (Posterity & Pedigree)
create_cattle = """
CREATE TABLE IF NOT EXISTS cattle (
    cow_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    breed VARCHAR(50),
    date_of_birth DATE,
    sire_id VARCHAR(50),
    dam_id VARCHAR(50),
    status ENUM('Active', 'Sold', 'Deceased') DEFAULT 'Active'
)
"""
cursor.execute(create_cattle)

# 2. Daily Milk Production Table (Productivity)
create_milk_production = """
CREATE TABLE IF NOT EXISTS milk_production (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    cow_id VARCHAR(50),
    record_date DATE DEFAULT CURRENT_DATE,
    morning_liters DECIMAL(5, 2),
    evening_liters DECIMAL(5, 2),
    total_liters DECIMAL(5, 2) AS (morning_liters + evening_liters) STORED,
    FOREIGN KEY (cow_id) REFERENCES cattle(cow_id)
)
"""
cursor.execute(create_milk_production)

# 3. Health and Breeding Table (Efficiency)
create_health_breeding = """
CREATE TABLE IF NOT EXISTS health_breeding (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    cow_id VARCHAR(50),
    event_type ENUM('Vaccination', 'Treatment', 'AI', 'Calving', 'Heat'),
    event_date DATE,
    details TEXT,
    cost DECIMAL(10, 2) DEFAULT 0.00,
    next_due_date DATE,
    FOREIGN KEY (cow_id) REFERENCES cattle(cow_id)
)
"""
cursor.execute(create_health_breeding)

# 4. Farm Finances Table (Profitability)
create_farm_finances = """
CREATE TABLE IF NOT EXISTS farm_finances (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_date DATE DEFAULT CURRENT_DATE,
    category ENUM('Milk Sale', 'Feed Purchase', 'Vet Bill', 'Labor', 'Equipment'),
    transaction_type ENUM('Income', 'Expense'),
    amount DECIMAL(15, 2),
    description VARCHAR(255)
)
"""
cursor.execute(create_farm_finances)

conn.commit()
cursor.close()
conn.close()
print("Tables created successfully!")