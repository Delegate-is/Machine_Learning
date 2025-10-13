import sqlite3

# ---------- DATABASE SETUP ----------
def connect():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # Create tables if they don’t exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            bio TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            available INTEGER DEFAULT 1,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS borrow_history (
            borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            return_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    ''')

    conn.commit()
    conn.close()


# ---------- BOOK FUNCTIONS ----------
def add_book(title, author_name):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # Check if author exists
    cur.execute("SELECT author_id FROM authors WHERE name = ?", (author_name,))
    author = cur.fetchone()
    if not author:
        cur.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
        conn.commit()
        cur.execute("SELECT author_id FROM authors WHERE name = ?", (author_name,))
        author = cur.fetchone()

    author_id = author[0]
    cur.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
    conn.commit()
    conn.close()


def view_books():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT b.book_id, b.title, a.name, b.available
        FROM books b
        JOIN authors a ON b.author_id = a.author_id
    ''')
    books = cur.fetchall()
    conn.close()
    return books


def search_books(keyword):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT b.book_id, b.title, a.name, b.available
        FROM books b
        JOIN authors a ON b.author_id = a.author_id
        WHERE b.title LIKE ? OR a.name LIKE ?
    ''', (f'%{keyword}%', f'%{keyword}%'))
    results = cur.fetchall()
    conn.close()
    return results


# ---------- USER & BORROW FUNCTIONS ----------
def add_user(name, email):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()


def borrow_book(user_email, book_id):
    import datetime
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    # Check if user exists
    cur.execute("SELECT user_id FROM users WHERE email = ?", (user_email,))
    user = cur.fetchone()
    if not user:
        print("⚠️ User not found. Please register first.")
        conn.close()
        return
    user_id = user[0]

    # Check if book is available
    cur.execute("SELECT available FROM books WHERE book_id = ?", (book_id,))
    book = cur.fetchone()
    if not book or book[0] == 0:
        print("❌ Book is not available.")
        conn.close()
        return

    # Borrow the book
    borrow_date = datetime.date.today().isoformat()
    cur.execute("UPDATE books SET available = 0 WHERE book_id = ?", (book_id,))
    cur.execute("INSERT INTO borrow_history (user_id, book_id, borrow_date) VALUES (?, ?, ?)",
                (user_id, book_id, borrow_date))
    conn.commit()
    conn.close()
    print("✅ Book borrowed successfully!")


def return_book(book_id):
    import datetime
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    return_date = datetime.date.today().isoformat()
    cur.execute('''
        UPDATE borrow_history
        SET return_date = ?
        WHERE book_id = ? AND return_date IS NULL
    ''', (return_date, book_id))
    cur.execute("UPDATE books SET available = 1 WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("📗 Book returned successfully!")
