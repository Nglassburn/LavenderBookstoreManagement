from datetime import date

class Sale:
    def __init__(self, customer_id):
        self.date = date.today()
        self.total_amount = 0.0
        self.books = []
        self.customer_id = customer_id

    def add_book_to_sale(self, db, book_id):
        book = db.fetchone("SELECT * FROM books WHERE id = ?", (book_id,))
        if book:
            self.books.append(book)
            self.calculate_total_amount()
        else:
            raise ValueError("Book not found")

    def remove_book_from_sale(self, book_id):
        self.books = [b for b in self.books if b[0] != book_id]
        self.calculate_total_amount()

    def calculate_total_amount(self):
        self.total_amount = sum(book[4] for book in self.books)

    def record_sale(self, db):
        try:
            db.execute("INSERT INTO sales (date, total_amount, customer_id) VALUES (?, ?, ?)",
                       (self.date, self.total_amount, self.customer_id))
            sale_id = db.cursor.lastrowid
            for book in self.books:
                db.execute("INSERT INTO sale_books (sale_id, book_id) VALUES (?, ?)", (sale_id, book[0]))
        except Exception as e:
            print(f"Error recording sale: {e}")

    def get_sale_details(self):
        return {
            "date": str(self.date),
            "total_amount": self.total_amount,
            "books": self.books,
            "customer_id": self.customer_id
        }
