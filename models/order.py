import json
from datetime import date
from .supplier import Supplier
from .book import Book

class Order:
    def __init__(self, order_id, supplier, order_file='data/orders.json'):
        self.order_id = order_id
        self.date = date.today()
        self.status = "Pending"
        self.books = []
        self.supplier = supplier
        self.order_file = order_file
        self.load_orders()

    def load_orders(self):
        try:
            with open(self.order_file, 'r') as file:
                self.orders = json.load(file)
        except FileNotFoundError:
            self.orders = []

    def save_orders(self):
        with open(self.order_file, 'w') as file:
            json.dump(self.orders, file, indent=4)

    def add_book_to_order(self, book):
        self.books.append(book.get_book_details())
        self.save_orders()

    def remove_book_from_order(self, book_title):
        self.books = [b for b in self.books if b["title"] != book_title]
        self.save_orders()

    def update_order_status(self, status):
        self.status = status
        self.save_orders()

    def get_order_details(self):
        return {
            "order_id": self.order_id,
            "date": str(self.date),
            "status": self.status,
            "books": self.books,
            "supplier": self.supplier
        }
