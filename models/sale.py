from datetime import datetime

class Sale:
    def __init__(self, customer_id, date=None, total_amount=0):
        self.customer_id = customer_id
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.total_amount = total_amount
        self.books = []

    def add_book_to_sale(self, db, book_id, quantity):
        query = "SELECT price FROM books WHERE id = ?"
        result = db.fetchone(query, (book_id,))
        if result:
            price = result[0]
            self.total_amount += price * quantity
            self.books.append((book_id, quantity))
        else:
            raise ValueError("Book not found")

    def record_sale(self, db):
        # Insert into sales table
        sale_query = "INSERT INTO sales (customer_id, date, total_amount) VALUES (?, ?, ?)"
        db.execute(sale_query, (self.customer_id, self.date, self.total_amount))

        # Get the last inserted sale ID
        sale_id = db.cursor.lastrowid

        # Insert into sale_books table
        for book_id, quantity in self.books:
            sale_book_query = "INSERT INTO sale_books (sale_id, book_id, quantity) VALUES (?, ?, ?)"
            db.execute(sale_book_query, (sale_id, book_id, quantity))

        # Update the stock in the books table
        for book_id, quantity in self.books:
            update_stock_query = "UPDATE books SET stock_quantity = stock_quantity - ? WHERE id = ?"
            db.execute(update_stock_query, (quantity, book_id))

    @staticmethod
    def get_all_sales(db):
        return db.fetchall("SELECT sales.id, customers.name, sales.date, sales.total_amount FROM sales "
                           "JOIN customers ON sales.customer_id = customers.id")
