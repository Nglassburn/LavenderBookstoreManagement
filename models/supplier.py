class Supplier:
    def __init__(self, name, email, address, supplier_id=None):
        self.id = supplier_id
        self.name = name
        self.email = email
        self.address = address

    def save_to_db(self, db):
        existing_supplier = Supplier.find_by_email(db, self.email)
        if not existing_supplier:
            db.execute(
                "INSERT INTO suppliers (name, email, address) VALUES (?, ?, ?)",
                (self.name, self.email, self.address)
            )
            self.id = db.cursor.lastrowid
        else:
            self.id = existing_supplier[0]

    @staticmethod
    def get_all_suppliers(db):
        try:
            return db.fetchall("SELECT * FROM suppliers")
        except Exception as e:
            print(f"Error fetching suppliers: {e}")
            return []

    @staticmethod
    def find_by_email(db, email):
        try:
            return db.fetchone("SELECT * FROM suppliers WHERE email = ?", (email,))
        except Exception as e:
            print(f"Error finding supplier by email: {e}")
            return None
