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

    def remove_book_by_id(self, book_id):
            query = "DELETE FROM books WHERE id = ?"
            self.db.execute(query, (book_id,))

    def search_book(self, title):
        return Book.find_by_title(self.db, title)

    def update_stock(self, title, new_stock):
        try:
            self.db.execute("UPDATE books SET stock_quantity = ? WHERE title = ?", (new_stock, title))
        except Exception as e:
            print(f"Error updating stock: {e}")

    def get_all_books(self):
        query = "SELECT id, title, author, genre, price, stock_quantity FROM books"
        return self.db.fetchall(query)
