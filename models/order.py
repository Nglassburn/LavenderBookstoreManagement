import json
from datetime import date
from .supplier import Supplier
from .book import Book

class Order:
    def __init__(self, supplier):
        self.supplier = supplier
        self.date = date.today()
        self.status = "Pending"
        self.books = []

    def add_book_to_order(self, book):
        self.books.append(book)

    def remove_book_from_order(self, book_title):
        self.books = [b for b in self.books if b.title != book_title]

    def update_order_status(self, status):
        self.status = status

    def get_order_details(self):
        return {
            "supplier": self.supplier,
            "date": str(self.date),
            "status": self.status,
            "books": [book.get_book_details() for book in self.books]
        }
