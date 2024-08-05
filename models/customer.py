class Customer:
    def __init__(self, name, email, address, customer_id=None):
        self.id = customer_id
        self.name = name
        self.email = email
        self.address = address

    def add_customer(self, db):
        db.execute(
            "INSERT INTO customers (name, email, address) VALUES (?, ?, ?)",
            (self.name, self.email, self.address)
        )
        self.id = db.cursor.lastrowid  # Assign the id after insertion

    @staticmethod
    def get_all_customers(db):
        return db.fetchall("SELECT * FROM customers")

    @staticmethod
    def search_customer(db, customer_id):
        return db.fetchone("SELECT * FROM customers WHERE id = ?", (customer_id,))
