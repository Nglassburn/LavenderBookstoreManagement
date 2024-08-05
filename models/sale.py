import json
from datetime import date
from .customer import Customer
from .book import Book

class Sale:
    def __init__(self, sale_id, customer, sales_file='data/sales.json'):
        self.sale_id = sale_id
        self.date = date.today()
        self.total_amount = 0.0
        self.books = []
        self.customer = customer
        self.sales_file = sales_file
        self.load_sales()

    def load_sales(self):
        try:
            with open(self.sales_file, 'r') as file:
                self.sales = json.load(file)
        except FileNotFoundError:
            self.sales = []

    def save_sales(self):
        with open(self.sales_file, 'w') as file:
            json.dump(self.sales, file, indent=4)

    def add_book_to_sale(self, book):
        self.books.append(book.get_book_details())
        self.calculate_total_amount()
        self.save_sales()

    def remove_book_from_sale(self, book_title):
        self.books = [b for b in self.books if b["title"] != book_title]
        self.calculate_total_amount()
        self.save_sales()

    def calculate_total_amount(self):
        self.total_amount = sum(book["price"] for book in self.books)

    def get_sale_details(self):
        return {
            "sale_id": self.sale_id,
            "date": str(self.date),
            "total_amount": self.total_amount,
            "books": self.books,
            "customer": self.customer
        }
