import logging
from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier
from db import Database

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    db = Database('data/bookstore.db')

    # Create some sample data
    book1 = Book("Book 1", "Author 1", "Genre 1", 20.0, 10)
    book2 = Book("Book 2", "Author 2", "Genre 2", 15.0, 5)
    customer1 = Customer("Customer 1", "customer1@example.com", "Address 1")
    supplier1 = Supplier("Supplier 1", "supplier1@example.com", "Supplier Address 1")

    try:
        # Inventory operations
        inventory = Inventory(db)
        inventory.add_book(book1)
        inventory.add_book(book2)
        inventory.add_book(Book("Book 2", "Author 2", "Genre 2", 15.0, 5))
        
        # Search for a book
        searched_book = inventory.search_book("Book 2")
        if searched_book:
            logging.info(f"Book found: {searched_book}")
        else:
            logging.info("Book not found")

        # Update stock of a book
        inventory.update_stock("Book 2", 3)

        # Display inventory
        logging.info("Inventory:")
        for book in inventory.get_all_books():
            logging.info(book)

        # Customer operations
        customer1.save_to_db(db)
        customers = Customer.get_all_customers(db)
        logging.info("Customers:")
        for customer in customers:
            logging.info(customer)
        
        # Supplier operations
        supplier1.save_to_db(db)
        suppliers = Supplier.get_all_suppliers(db)
        logging.info("Suppliers:")
        for supplier in suppliers:
            logging.info(supplier)
        
        # Order operations
        order1 = Order(supplier1)
        order1.add_book_to_order(book2)
        order1.update_order_status("Shipped")
        logging.info(f"Order details: {order1.get_order_details()}")

        # Sale operations
        sale1 = Sale(customer1.id)
        sale1.add_book_to_sale(db, book2.id)
        sale1.record_sale(db)
        logging.info(f"Sale details: {sale1.get_sale_details()}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
