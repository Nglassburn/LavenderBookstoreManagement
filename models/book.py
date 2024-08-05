class Book:
    def __init__(self, title, author, genre, price, stock_quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock_quantity = stock_quantity

    def add_book(self, db):
        db.execute(
            "INSERT INTO books (title, author, genre, price, stock_quantity) VALUES (?, ?, ?, ?, ?)",
            (self.title, self.author, self.genre, self.price, self.stock_quantity)
        )

    @staticmethod
    def get_all_books(db):
        return db.fetchall("SELECT * FROM books")

    @staticmethod
    def search_book(db, title):
        return db.fetchone("SELECT * FROM books WHERE title = ?", (title,))
