from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

def main():
    db = Database('data/bookstore.db')

    # Create some sample data
    book1 = Book("Book 1", "Author 1", "Genre 1", 20.0, 10)
    book2 = Book("Book 2", "Author 2", "Genre 2", 15.0, 5)
    customer1 = Customer(1, "Customer 1", "customer1@example.com", "Address 1")
    supplier1 = Supplier(1, "Supplier 1", "supplier1@example.com", "Supplier Address 1")

    # Inventory operations
    inventory = Inventory(db)
    inventory.add_book(book1)
    inventory.add_book(book2)
    
    # Remove a book from inventory
    inventory.remove_book("Book 1")
    
    # Search for a book
    searched_book = inventory.search_book("Book 2")
    if searched_book:
        print("Book found:", searched_book)
    else:
        print("Book not found")

    # Update stock of a book
    inventory.update_stock("Book 2", 3)

    # Display inventory
    print("Inventory:")
    for book in inventory.get_all_books():
        print(book)

    db.close()

if __name__ == "__main__":
    main()
