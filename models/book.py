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

    def save_to_db(self, db):
        existing_book = Book.find_by_title(db, self.title)
        if existing_book:
            db.execute(
                "UPDATE books SET stock_quantity = stock_quantity + ? WHERE title = ?",
                (self.stock_quantity, self.title)
            )
            # Fetch the updated book details to get the id
            updated_book = Book.find_by_title(db, self.title)
            self.id = updated_book[0]  # Assign the id from the updated book details
        else:
            db.execute(
                "INSERT INTO books (title, author, genre, price, stock_quantity) VALUES (?, ?, ?, ?, ?)",
                (self.title, self.author, self.genre, self.price, self.stock_quantity)
            )
            self.id = db.cursor.lastrowid

    @staticmethod
    def get_all_books(db):
        try:
            return db.fetchall("SELECT * FROM books")
        except Exception as e:
            print(f"Error fetching books: {e}")
            return []

    @staticmethod
    def find_by_title(db, title):
        try:
            return db.fetchone("SELECT * FROM books WHERE title = ?", (title,))
        except Exception as e:
            print(f"Error finding book by title: {e}")
            return None
