class Book:
    def __init__(self, title, author, genre, price, stock_quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock_quantity = stock_quantity

    def update_book(self, title=None, author=None, genre=None, price=None, stock_quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if price:
            self.price = price
        if stock_quantity:
            self.stock_quantity = stock_quantity

    def get_book_details(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }