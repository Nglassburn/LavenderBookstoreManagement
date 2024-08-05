import json
from .book import Book

class Inventory:
    def __init__(self, db):
        self.db = db

    def add_book(self, book):
        book.add_book(self.db)

    def remove_book(self, title):
        self.db.execute("DELETE FROM books WHERE title = ?", (title,))

    def search_book(self, title):
        return Book.search_book(self.db, title)

    def update_stock(self, title, new_stock):
        self.db.execute("UPDATE books SET stock_quantity = ? WHERE title = ?", (new_stock, title))

    def get_all_books(self):
        return Book.get_all_books(self.db)
