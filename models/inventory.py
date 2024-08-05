from .book import Book

class Inventory:
    def __init__(self, db):
        self.db = db

    def add_book(self, book):
        book.save_to_db(self.db)

    def remove_book(self, title):
        try:
            self.db.execute("DELETE FROM books WHERE title = ?", (title,))
        except Exception as e:
            print(f"Error removing book: {e}")

    def search_book(self, title):
        return Book.find_by_title(self.db, title)

    def update_stock(self, title, new_stock):
        try:
            self.db.execute("UPDATE books SET stock_quantity = ? WHERE title = ?", (new_stock, title))
        except Exception as e:
            print(f"Error updating stock: {e}")

    def get_all_books(self):
        try:
            return self.db.fetchall("SELECT title, author, genre, price, SUM(stock_quantity) as stock_quantity FROM books GROUP BY title, author, genre, price")
        except Exception as e:
            print(f"Error fetching books: {e}")
            return []
