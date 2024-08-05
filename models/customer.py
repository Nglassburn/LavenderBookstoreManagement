class Customer:
    def __init__(self, name, email, address, customer_id=None):
        self.id = customer_id
        self.name = name
        self.email = email
        self.address = address

    def save_to_db(self, db):
        existing_customer = Customer.find_by_email(db, self.email)
        if not existing_customer:
            db.execute(
                "INSERT INTO customers (name, email, address) VALUES (?, ?, ?)",
                (self.name, self.email, self.address)
            )
            self.id = db.cursor.lastrowid
        else:
            self.id = existing_customer[0]

    @staticmethod
    def get_all_customers(db):
        try:
            return db.fetchall("SELECT * FROM customers")
        except Exception as e:
            print(f"Error fetching customers: {e}")
            return []

    @staticmethod
    def find_by_email(db, email):
        try:
            return db.fetchone("SELECT * FROM customers WHERE email = ?", (email,))
        except Exception as e:
            print(f"Error finding customer by email: {e}")
            return None
