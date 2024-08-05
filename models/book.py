class Book:
    def __init__(self, title, author, genre, price, stock_quantity, book_id=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock_quantity = stock_quantity

    def get_book_details(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }

    def add_book(self, db):
        db.execute(
            "INSERT INTO books (title, author, genre, price, stock_quantity) VALUES (?, ?, ?, ?, ?)",
            (self.title, self.author, self.genre, self.price, self.stock_quantity)
        )
        self.id = db.cursor.lastrowid  # Assign the id after insertion

    @staticmethod
    def get_all_books(db):
        return db.fetchall("SELECT * FROM books")

    @staticmethod
    def search_book(db, title):
        return db.fetchone("SELECT * FROM books WHERE title = ?", (title,))
