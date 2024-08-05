from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

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
    customer1 = Customer("Customer 1", "customer1@example.com", "Address 1")
    supplier1 = Supplier("Supplier 1", "supplier1@example.com", "Supplier Address 1")

    # Inventory operations
    inventory = Inventory(db)
    inventory.add_book(book1)
    inventory.add_book(book2)
    
    # Ensure book2 now has an id
    book2.id = inventory.search_book("Book 2")[0]

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

    # Customer operations
    customer1.add_customer(db)
    customers = Customer.get_all_customers(db)
    print("Customers:")
    for customer in customers:
        print(customer)
    
    # Supplier operations
    supplier1.add_supplier(db)
    suppliers = Supplier.get_all_suppliers(db)
    print("Suppliers:")
    for supplier in suppliers:
        print(supplier)
    
    # Order operations
    order1 = Order(supplier1)
    order1.add_book_to_order(book2)
    order1.update_order_status("Shipped")
    print("Order details:", order1.get_order_details())

    # Sale operations
    sale1 = Sale(customer1.id)
    sale1.add_book_to_sale(db, book2.id)
    sale1.record_sale(db)
    print("Sale details:", sale1.get_sale_details())

    db.close()

if __name__ == "__main__":
    main()
