import tkinter as tk
from tkinter import ttk, messagebox
from db import Database
from models.book import Book
from models.customer import Customer
from models.supplier import Supplier
from models.inventory import Inventory
from models.sale import Sale
from models.order import Order

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lavender Bookstore Management System")

        self.db = Database('data/bookstore.db')
        self.inventory = Inventory(self.db)
        self.book_dict = {}  # Dictionary to store book titles and their IDs

        # Create the notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Add tabs
        self.create_inventory_tab()
        self.create_customer_tab()
        self.create_supplier_tab()
        self.create_sales_tab()
        self.create_order_tab()

    def create_inventory_tab(self):
        self.inventory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_tab, text='Inventory')

        # Create inventory treeview
        self.inventory_tree = ttk.Treeview(self.inventory_tab, columns=("ID", "Title", "Author", "Genre", "Price", "Stock"), show='headings')
        self.inventory_tree.heading("ID", text="ID")
        self.inventory_tree.heading("Title", text="Title")
        self.inventory_tree.heading("Author", text="Author")
        self.inventory_tree.heading("Genre", text="Genre")
        self.inventory_tree.heading("Price", text="Price")
        self.inventory_tree.heading("Stock", text="Stock Quantity")
        self.inventory_tree.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.inventory_tab, orient='vertical', command=self.inventory_tree.yview)
        self.scrollbar.pack(side='left', fill='y')

        self.inventory_tree.config(yscrollcommand=self.scrollbar.set)

        # Add buttons
        self.refresh_button = ttk.Button(self.inventory_tab, text='Refresh Inventory', command=self.refresh_inventory)
        self.refresh_button.pack(side='top', fill='x')

        self.update_button = ttk.Button(self.inventory_tab, text='Update Selected Book', command=self.update_book)
        self.update_button.pack(side='top', fill='x')

        self.delete_button = ttk.Button(self.inventory_tab, text='Delete Selected Book', command=self.delete_book)
        self.delete_button.pack(side='top', fill='x')

        # Add book form
        self.add_book_form()

    def add_book_form(self):
        self.add_book_frame = ttk.Frame(self.inventory_tab)
        self.add_book_frame.pack(side='right', fill='both', expand=True)

        ttk.Label(self.add_book_frame, text='Title').pack()
        self.title_entry = ttk.Entry(self.add_book_frame)
        self.title_entry.pack()

        ttk.Label(self.add_book_frame, text='Author').pack()
        self.author_entry = ttk.Entry(self.add_book_frame)
        self.author_entry.pack()

        ttk.Label(self.add_book_frame, text='Genre').pack()
        self.genre_entry = ttk.Entry(self.add_book_frame)
        self.genre_entry.pack()

        ttk.Label(self.add_book_frame, text='Price').pack()
        self.price_entry = ttk.Entry(self.add_book_frame)
        self.price_entry.pack()

        ttk.Label(self.add_book_frame, text='Stock Quantity').pack()
        self.stock_entry = ttk.Entry(self.add_book_frame)
        self.stock_entry.pack()

        self.add_book_button = ttk.Button(self.add_book_frame, text='Add Book', command=self.add_book)
        self.add_book_button.pack()

    def refresh_inventory(self):
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)
        books = self.inventory.get_all_books()
        for book in books:
            self.inventory_tree.insert('', 'end', values=book)
        self.refresh_books_comboboxes()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        price = float(self.price_entry.get())
        stock_quantity = int(self.stock_entry.get())

        book = Book(title, author, genre, price, stock_quantity)
        self.inventory.add_book(book)

        messagebox.showinfo("Success", "Book added successfully!")
        self.refresh_inventory()

    def update_book(self):
        selected_item = self.inventory_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No book selected")
            return

        item = self.inventory_tree.item(selected_item)
        book_id = item['values'][0]

        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        price = float(self.price_entry.get())
        stock_quantity = int(self.stock_entry.get())

        book = Book(title, author, genre, price, stock_quantity, book_id)
        self.inventory.update_stock(book.title, book.stock_quantity)

        messagebox.showinfo("Success", "Book updated successfully!")
        self.refresh_inventory()

    def delete_book(self):
        selected_item = self.inventory_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No book selected")
            return

        item = self.inventory_tree.item(selected_item)
        book_id = item['values'][0]
        book_title = item['values'][1]

        self.inventory.remove_book(book_title)
        messagebox.showinfo("Success", "Book deleted successfully!")
        self.refresh_inventory()

    def create_customer_tab(self):
        self.customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_tab, text='Customers')

        # Customer treeview
        self.customer_tree = ttk.Treeview(self.customer_tab, columns=("ID", "Name", "Email", "Address"), show='headings')
        self.customer_tree.heading("ID", text="ID")
        self.customer_tree.heading("Name", text="Name")
        self.customer_tree.heading("Email", text="Email")
        self.customer_tree.heading("Address", text="Address")
        self.customer_tree.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.customer_scrollbar = ttk.Scrollbar(self.customer_tab, orient='vertical', command=self.customer_tree.yview)
        self.customer_scrollbar.pack(side='left', fill='y')

        self.customer_tree.config(yscrollcommand=self.customer_scrollbar.set)

        # Add refresh button
        self.refresh_customers_button = ttk.Button(self.customer_tab, text='Refresh Customers', command=self.refresh_customers)
        self.refresh_customers_button.pack(side='top', fill='x')

        # Add customer form
        self.add_customer_form()

    def add_customer_form(self):
        self.add_customer_frame = ttk.Frame(self.customer_tab)
        self.add_customer_frame.pack(side='right', fill='both', expand=True)

        ttk.Label(self.add_customer_frame, text='Name').pack()
        self.customer_name_entry = ttk.Entry(self.add_customer_frame)
        self.customer_name_entry.pack()

        ttk.Label(self.add_customer_frame, text='Email').pack()
        self.customer_email_entry = ttk.Entry(self.add_customer_frame)
        self.customer_email_entry.pack()

        ttk.Label(self.add_customer_frame, text='Address').pack()
        self.customer_address_entry = ttk.Entry(self.add_customer_frame)
        self.customer_address_entry.pack()

        self.add_customer_button = ttk.Button(self.add_customer_frame, text='Add Customer', command=self.add_customer)
        self.add_customer_button.pack()

    def refresh_customers(self):
        for item in self.customer_tree.get_children():
            self.customer_tree.delete(item)
        customers = Customer.get_all_customers(self.db)
        for customer in customers:
            self.customer_tree.insert('', 'end', values=customer)

    def add_customer(self):
        name = self.customer_name_entry.get()
        email = self.customer_email_entry.get()
        address = self.customer_address_entry.get()

        customer = Customer(name, email, address)
        customer.save_to_db(self.db)

        messagebox.showinfo("Success", "Customer added successfully!")
        self.refresh_customers()

    def create_supplier_tab(self):
        self.supplier_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.supplier_tab, text='Suppliers')

        # Supplier treeview
        self.supplier_tree = ttk.Treeview(self.supplier_tab, columns=("ID", "Name", "Email", "Address"), show='headings')
        self.supplier_tree.heading("ID", text="ID")
        self.supplier_tree.heading("Name", text="Name")
        self.supplier_tree.heading("Email", text="Email")
        self.supplier_tree.heading("Address", text="Address")
        self.supplier_tree.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.supplier_scrollbar = ttk.Scrollbar(self.supplier_tab, orient='vertical', command=self.supplier_tree.yview)
        self.supplier_scrollbar.pack(side='left', fill='y')

        self.supplier_tree.config(yscrollcommand=self.supplier_scrollbar.set)

        # Add refresh button
        self.refresh_suppliers_button = ttk.Button(self.supplier_tab, text='Refresh Suppliers', command=self.refresh_suppliers)
        self.refresh_suppliers_button.pack(side='top', fill='x')

        # Add supplier form
        self.add_supplier_form()

    def add_supplier_form(self):
        self.add_supplier_frame = ttk.Frame(self.supplier_tab)
        self.add_supplier_frame.pack(side='right', fill='both', expand=True)

        ttk.Label(self.add_supplier_frame, text='Name').pack()
        self.supplier_name_entry = ttk.Entry(self.add_supplier_frame)
        self.supplier_name_entry.pack()

        ttk.Label(self.add_supplier_frame, text='Email').pack()
        self.supplier_email_entry = ttk.Entry(self.add_supplier_frame)
        self.supplier_email_entry.pack()

        ttk.Label(self.add_supplier_frame, text='Address').pack()
        self.supplier_address_entry = ttk.Entry(self.add_supplier_frame)
        self.supplier_address_entry.pack()

        self.add_supplier_button = ttk.Button(self.add_supplier_frame, text='Add Supplier', command=self.add_supplier)
        self.add_supplier_button.pack()

    def refresh_suppliers(self):
        for item in self.supplier_tree.get_children():
            self.supplier_tree.delete(item)
        suppliers = Supplier.get_all_suppliers(self.db)
        for supplier in suppliers:
            self.supplier_tree.insert('', 'end', values=supplier)
        self.refresh_suppliers_combobox()

    def add_supplier(self):
        name = self.supplier_name_entry.get()
        email = self.supplier_email_entry.get()
        address = self.supplier_address_entry.get()

        supplier = Supplier(name, email, address)
        supplier.save_to_db(self.db)

        messagebox.showinfo("Success", "Supplier added successfully!")
        self.refresh_suppliers()

    def create_sales_tab(self):
        self.sales_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sales_tab, text='Sales')

        # Sales treeview
        self.sales_tree = ttk.Treeview(self.sales_tab, columns=("ID", "Customer", "Date", "Total Amount"), show='headings')
        self.sales_tree.heading("ID", text="ID")
        self.sales_tree.heading("Customer", text="Customer")
        self.sales_tree.heading("Date", text="Date")
        self.sales_tree.heading("Total Amount", text="Total Amount")
        self.sales_tree.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.sales_scrollbar = ttk.Scrollbar(self.sales_tab, orient='vertical', command=self.sales_tree.yview)
        self.sales_scrollbar.pack(side='left', fill='y')

        self.sales_tree.config(yscrollcommand=self.sales_scrollbar.set)

        # Add refresh button
        self.refresh_sales_button = ttk.Button(self.sales_tab, text='Refresh Sales', command=self.refresh_sales)
        self.refresh_sales_button.pack(side='top', fill='x')

        # Add sale form
        self.add_sale_form()

    def add_sale_form(self):
        self.add_sale_frame = ttk.Frame(self.sales_tab)
        self.add_sale_frame.pack(side='right', fill='both', expand=True)

        ttk.Label(self.add_sale_frame, text='Customer ID').pack()
        self.sale_customer_id_entry = ttk.Entry(self.add_sale_frame)
        self.sale_customer_id_entry.pack()

        ttk.Label(self.add_sale_frame, text='Book').pack()
        self.sale_book_combobox = ttk.Combobox(self.add_sale_frame)
        self.sale_book_combobox.pack()
        self.refresh_books_comboboxes()

        ttk.Label(self.add_sale_frame, text='Quantity').pack()
        self.sale_quantity_entry = ttk.Entry(self.add_sale_frame)
        self.sale_quantity_entry.pack()

        self.add_sale_button = ttk.Button(self.add_sale_frame, text='Add Sale', command=self.add_sale)
        self.add_sale_button.pack()

    def refresh_books_comboboxes(self):
        books = self.inventory.get_all_books()
        self.book_dict = {book[1]: book[0] for book in books}  # Create a dictionary with title as key and ID as value
        self.sale_book_combobox['values'] = list(self.book_dict.keys())  # Set combobox values to book titles
        if hasattr(self, 'order_book_combobox'):
            self.order_book_combobox['values'] = list(self.book_dict.keys())  # Set combobox values to book titles

    def refresh_sales(self):
        for item in self.sales_tree.get_children():
            self.sales_tree.delete(item)
        sales = self.get_all_sales()
        for sale in sales:
            self.sales_tree.insert('', 'end', values=sale)

    def add_sale(self):
        try:
            customer_id = int(self.sale_customer_id_entry.get())
            selected_book_title = self.sale_book_combobox.get()
            quantity = int(self.sale_quantity_entry.get())

            if not selected_book_title:
                raise ValueError("Please select a book.")
                
            book_id = self.book_dict.get(selected_book_title)  # Retrieve the book ID using the selected title

            sale = Sale(customer_id)
            sale.add_book_to_sale(self.db, book_id, quantity)
            sale.record_sale(self.db)

            messagebox.showinfo("Success", "Sale added successfully!")
            self.refresh_sales()
        except ValueError as ve:
            messagebox.showerror("Error", f"Failed to add sale: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def get_all_sales(self):
        try:
            return self.db.fetchall("SELECT sales.id, customers.name, sales.date, sales.total_amount FROM sales JOIN customers ON sales.customer_id = customers.id")
        except Exception as e:
            print(f"Error fetching sales: {e}")
            return []

    def create_order_tab(self):
        self.order_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.order_tab, text='Orders')

        # Order treeview
        self.order_tree = ttk.Treeview(self.order_tab, columns=("ID", "Supplier", "Date", "Status", "Book ID", "Quantity"), show='headings')
        self.order_tree.heading("ID", text="ID")
        self.order_tree.heading("Supplier", text="Supplier")
        self.order_tree.heading("Date", text="Date")
        self.order_tree.heading("Status", text="Status")
        self.order_tree.heading("Book ID", text="Book ID")
        self.order_tree.heading("Quantity", text="Quantity")
        self.order_tree.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.order_scrollbar = ttk.Scrollbar(self.order_tab, orient='vertical', command=self.order_tree.yview)
        self.order_scrollbar.pack(side='left', fill='y')

        self.order_tree.config(yscrollcommand=self.order_scrollbar.set)

        # Add refresh button
        self.refresh_orders_button = ttk.Button(self.order_tab, text='Refresh Orders', command=self.refresh_orders)
        self.refresh_orders_button.pack(side='top', fill='x')

        # Add order form
        self.add_order_form()

    def add_order_form(self):
        self.add_order_frame = ttk.Frame(self.order_tab)
        self.add_order_frame.pack(side='right', fill='both', expand=True)

        ttk.Label(self.add_order_frame, text='Supplier').pack()
        self.order_supplier_combobox = ttk.Combobox(self.add_order_frame)
        self.order_supplier_combobox.pack()
        self.refresh_suppliers_combobox()

        ttk.Label(self.add_order_frame, text='Book').pack()
        self.order_book_combobox = ttk.Combobox(self.add_order_frame)
        self.order_book_combobox.pack()
        self.refresh_books_comboboxes()

        ttk.Label(self.add_order_frame, text='Quantity').pack()
        self.order_quantity_entry = ttk.Entry(self.add_order_frame)
        self.order_quantity_entry.pack()

        self.add_order_button = ttk.Button(self.add_order_frame, text='Add Order', command=self.add_order)
        self.add_order_button.pack()

    def refresh_suppliers_combobox(self):
        suppliers = Supplier.get_all_suppliers(self.db)
        self.order_supplier_combobox['values'] = [f"{supplier[0]}: {supplier[1]}" for supplier in suppliers]

    def refresh_orders(self):
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)
        orders = Order.get_all_orders(self.db)
        for order in orders:
            self.order_tree.insert('', 'end', values=order)

    def add_order(self):
        try:
            selected_supplier = self.order_supplier_combobox.get()
            selected_book_title = self.order_book_combobox.get()
            print(f"Selected Supplier: {selected_supplier}, Selected Book Title: {selected_book_title}")
            if not selected_supplier or not selected_book_title:
                raise ValueError("Please select a supplier and a book.")
                
            supplier_id = int(selected_supplier.split(":")[0].strip())
            book_id = self.book_dict.get(selected_book_title)  # Retrieve the book ID using the selected title
            print(f"Parsed Supplier ID: {supplier_id}, Retrieved Book ID: {book_id}")

            quantity = int(self.order_quantity_entry.get())

            order = Order(supplier_id, book_id, quantity)
            order.save_to_db(self.db)

            messagebox.showinfo("Success", "Order added successfully!")
            self.refresh_orders()
        except ValueError as ve:
            messagebox.showerror("Error", f"Failed to add order: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def on_closing(self):
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
