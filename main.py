from models.book import Book
from models.customer import Customer
from models.inventory import Inventory
from models.order import Order
from models.sale import Sale
from models.supplier import Supplier

def main():
    # Create some sample data
    book1 = Book("Book 1", "Author 1", "Genre 1", 20.0, 10)
    book2 = Book("Book 2", "Author 2", "Genre 2", 15.0, 5)
    customer1 = Customer(1, "Customer 1", "customer1@example.com", "Address 1")
    supplier1 = Supplier(1, "Supplier 1", "supplier1@example.com", "Supplier Address 1")

    # Inventory operations
    inventory = Inventory('data/inventory.json')
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
    for book in inventory.books:
        print(book)

    # Customer operations
    customer1.add_customer()
    
    # Order operations
    order1 = Order(1, supplier1)
    order1.add_book_to_order(book2)
    order1.update_order_status("Shipped")
    print("Order details:", order1.get_order_details())

    # Sale operations
    sale1 = Sale(1, customer1)
    sale1.add_book_to_sale(book2)
    print("Sale details:", sale1.get_sale_details())

if __name__ == "__main__":
    main()
