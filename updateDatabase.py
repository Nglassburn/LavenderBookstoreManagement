import bcrypt
import sqlite3

def hash_existing_passwords():
    conn = sqlite3.connect('data/bookstore.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, password FROM customers")
    users = cursor.fetchall()

    for user in users:
        user_id, plain_password = user
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("UPDATE customers SET password = ? WHERE id = ?", (hashed_password, user_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    hash_existing_passwords()
    print("Passwords updated to hashed versions.")
