from datetime import datetime

class Order:
    def __init__(self, supplier_id, book_id, quantity, date=None, status="Pending"):
        self.supplier_id = supplier_id
        self.book_id = book_id
        self.quantity = quantity
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.status = status

    def save_to_db(self, db):
        query = """
        INSERT INTO orders (supplier_id, book_id, quantity, date, status) 
        VALUES (?, ?, ?, ?, ?)
        """
        db.execute(query, (self.supplier_id, self.book_id, self.quantity, self.date, self.status))

    @staticmethod
    def get_all_orders(db):
        query = """
        SELECT orders.id, suppliers.name, orders.date, orders.status, orders.book_id, orders.quantity 
        FROM orders 
        JOIN suppliers ON orders.supplier_id = suppliers.id
        """
        return db.fetchall(query)

    @staticmethod
    def find_order_by_id(db, order_id):
        query = "SELECT * FROM orders WHERE id = ?"
        return db.fetchone(query, (order_id,))

    @staticmethod
    def update_order_status(db, order_id, new_status):
        query = "UPDATE orders SET status = ? WHERE id = ?"
        db.execute(query, (new_status, order_id))

    @staticmethod
    def delete_order(db, order_id):
        query = "DELETE FROM orders WHERE id = ?"
        db.execute(query, (order_id,))
