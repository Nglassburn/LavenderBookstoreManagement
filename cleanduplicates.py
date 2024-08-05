from db import Database

def clean_up_duplicates(db):
    # Remove duplicate customers
    db.execute("""
        DELETE FROM customers
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM customers
            GROUP BY email
        )
    """)
    # Remove duplicate suppliers
    db.execute("""
        DELETE FROM suppliers
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM suppliers
            GROUP BY email
        )
    """)

if __name__ == "__main__":
    db = Database('data/bookstore.db')
    clean_up_duplicates(db)
    db.close()
