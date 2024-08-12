class Book:
    def __init__(self, title, author, genre, price, stock_quantity, book_id=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock_quantity = stock_quantity

    def save_to_db(self, db):
        if self.id:
            db.execute(
                "UPDATE books SET title=?, author=?, genre=?, price=?, stock_quantity=? WHERE id=?",
                (self.title, self.author, self.genre, self.price, self.stock_quantity, self.id)
            )
        else:
            db.execute(
                "INSERT INTO books (title, author, genre, price, stock_quantity) VALUES (?, ?, ?, ?, ?)",
                (self.title, self.author, self.genre, self.price, self.stock_quantity)
            )
            self.id = db.cursor.lastrowid

    @staticmethod
    def get_all_books(db):
        try:
            return db.fetchall("SELECT id, title, author, genre, price, stock_quantity FROM books")
        except Exception as e:
            print(f"Error fetching books: {e}")
            return []
    def find_by_title(db, title):
        query = "SELECT * FROM books WHERE title = ?"
        result = db.fetchone(query, (title,))
        if result:
            return Book(*result)  # Assuming your database columns match the order of your Book attributes
        return None
