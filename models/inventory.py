import json
from .book import Book

class Inventory:
    def __init__(self, inventory_file='data/inventory.json'):
        self.inventory_file = inventory_file
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.inventory_file, 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []

    def save_inventory(self):
        with open(self.inventory_file, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book):
        self.books.append(book.get_book_details())
        self.save_inventory()

    def remove_book(self, title):
        self.books = [b for b in self.books if b["title"] != title]
        self.save_inventory()

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return None

    def update_stock(self, title, stock_quantity):
        for book in self.books:
            if book["title"] == title:
                book["stock_quantity"] = stock_quantity
        self.save_inventory()
