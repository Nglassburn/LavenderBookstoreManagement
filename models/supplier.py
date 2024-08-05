class Supplier:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def add_supplier(self, db):
        db.execute(
            "INSERT INTO suppliers (name, email, address) VALUES (?, ?, ?)",
            (self.name, self.email, self.address)
        )

    @staticmethod
    def get_all_suppliers(db):
        return db.fetchall("SELECT * FROM suppliers")

    @staticmethod
    def search_supplier(db, supplier_id):
        return db.fetchone("SELECT * FROM suppliers WHERE id = ?", (supplier_id,))
