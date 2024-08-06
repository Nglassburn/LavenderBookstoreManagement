from datetime import datetime

class Sale:
    def __init__(self, customer_id, date=None, total_amount=0):
        self.customer_id = customer_id
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.total_amount = total_amount
        self.books = []

    def add_book_to_sale(self, db, book_id, quantity):
        book = db.fetchone("SELECT * FROM books WHERE id = ?", (book_id,))
        if book:
            self.books.append((book_id, quantity))
            self.total_amount += book[4] * quantity  # assuming price is the 5th column in books table
        else:
            raise ValueError("Book not found")

    def record_sale(self, db):
        db.execute("INSERT INTO sales (customer_id, date, total_amount) VALUES (?, ?, ?)",
                   (self.customer_id, self.date, self.total_amount))
        sale_id = db.fetchone("SELECT last_insert_rowid()")[0]
        for book_id, quantity in self.books:
            db.execute("INSERT INTO sale_books (sale_id, book_id, quantity) VALUES (?, ?, ?)",
                       (sale_id, book_id, quantity))

    @staticmethod
    def get_all_sales(db):
        return db.fetchall("SELECT sales.id, customers.name, sales.date, sales.total_amount FROM sales "
                           "JOIN customers ON sales.customer_id = customers.id")
