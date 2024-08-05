import sqlite3

def view_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    # View data in the 'books' table
    cursor.execute("SELECT * FROM books;")
    rows = cursor.fetchall()
    print("\nData in 'books' table:")
    for row in rows:
        print(row)
    
    conn.close()

view_data('data/bookstore.db')
