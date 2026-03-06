import sqlite3
import os

# 1. Path to your database - adjust 'site.db' to your actual filename
DB_PATH = os.path.join('instance', 'njuwan_farm.db')

def sync_database():
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}. Run your Flask app first!")
        return

    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 2. Define the columns you want to ensure exist
        # Format: (column_name, data_type)
        required_columns = [
            ('name', 'VARCHAR(100)'),
            ('age', 'INTEGER'),
            ('weight_kg', 'FLOAT'),
            ('status', 'VARCHAR(50)')
        ]

        # Get existing columns in the 'cows' table
        cursor.execute("PRAGMA table_info(cows)")
        existing_columns = [info[1] for info in cursor.fetchall()]

        # 3. Check and Add missing columns
        for col_name, col_type in required_columns:
            if col_name not in existing_columns:
                print(f"🛠️  Adding missing column: {col_name}...")
                cursor.execute(f"ALTER TABLE cows ADD COLUMN {col_name} {col_type}")
                print(f"✅ Column {col_name} added successfully.")
            else:
                print(f"✔️  Column {col_name} already exists.")

        conn.commit()
        conn.close()
        print("\n✨ Database sync complete!")

    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    sync_database()