from datetime import date

class Order:
    def __init__(self, supplier_id, book_id, quantity, order_id=None, order_date=None, status='Pending'):
        self.id = order_id
        self.supplier_id = supplier_id
        self.book_id = book_id
        self.quantity = quantity
        self.date = order_date if order_date else date.today().strftime('%Y-%m-%d')
        self.status = status

    def save_to_db(self, db):
        db.execute(
            "INSERT INTO orders (supplier_id, book_id, quantity, date, status) VALUES (?, ?, ?, ?, ?)",
            (self.supplier_id, self.book_id, self.quantity, self.date, self.status)
        )
        self.id = db.cursor.lastrowid

    @staticmethod
    def get_all_orders(db):
        try:
            return db.fetchall(
                "SELECT orders.id, suppliers.name, orders.date, orders.status, orders.book_id, orders.quantity "
                "FROM orders JOIN suppliers ON orders.supplier_id = suppliers.id"
            )
        except Exception as e:
            print(f"Error fetching orders: {e}")
            return []
