import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.initialize_db()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def initialize_db(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                price REAL NOT NULL,
                stock_quantity INTEGER NOT NULL
            )
        """)
        self.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
        self.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)
        self.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)
        self.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        """)
        self.execute("""
            CREATE TABLE IF NOT EXISTS sale_books (
                sale_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (sale_id) REFERENCES sales(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)


    def get_sales_data(self, start_date, end_date):
        query = """
        SELECT 
            sales.date,
            books.title,
            sale_books.quantity,
            (sale_books.quantity * books.price) AS total_amount
        FROM 
            sales
        JOIN 
            sale_books ON sales.id = sale_books.sale_id
        JOIN 
            books ON sale_books.book_id = books.id
        WHERE 
            sales.date BETWEEN ? AND ?
        ORDER BY 
            sales.date ASC
        """
        return self.fetchall(query, (start_date, end_date))

    def get_total_sales_summary(self, start_date, end_date):
        query = """
        SELECT 
            COUNT(sales.id) as transaction_count, 
            SUM(sales.total_amount) as total_revenue
        FROM 
            sales
        WHERE 
            sales.date BETWEEN ? AND ?
        """
        return self.fetchone(query, (start_date, end_date))

    def close(self):
        self.connection.close()
