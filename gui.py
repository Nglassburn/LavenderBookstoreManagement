import tkinter as tk
from tkinter import ttk, messagebox
from db import Database
from models.book import Book
from models.customer import Customer
from models.supplier import Supplier
from models.inventory import Inventory

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore Management System")

        self.db = Database('data/bookstore.db')
        self.inventory = Inventory(self.db)

        # Create the notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Add tabs
        self.create_inventory_tab()
        self.create_customer_tab()
        self.create_supplier_tab()

    def create_inventory_tab(self):
        self.inventory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_tab, text='Inventory')

        # Create inventory listbox
        self.inventory_listbox = tk.Listbox(self.inventory_tab)
        self.inventory_listbox.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.inventory_tab, orient='vertical', command=self.inventory_listbox.yview)
        self.scrollbar.pack(side='left', fill='y')

        self.inventory_listbox.config(yscrollcommand=self.scrollbar.set)

        # Add refresh button
        self.refresh_button = ttk.Button(self.inventory_tab, text='Refresh Inventory', command=self.refresh_inventory)
        self.refresh_button.pack(side='top', fill='x')

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
        self.inventory_listbox.delete(0, tk.END)
        books = self.inventory.get_all_books()
        for book in books:
            self.inventory_listbox.insert(tk.END, f"{book[0]} by {book[1]} - {book[2]} - ${book[3]} - Stock: {book[4]}")

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

    def create_customer_tab(self):
        self.customer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_tab, text='Customers')

        # Customer listbox
        self.customer_listbox = tk.Listbox(self.customer_tab)
        self.customer_listbox.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.customer_scrollbar = ttk.Scrollbar(self.customer_tab, orient='vertical', command=self.customer_listbox.yview)
        self.customer_scrollbar.pack(side='left', fill='y')

        self.customer_listbox.config(yscrollcommand=self.customer_scrollbar.set)

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
        self.customer_listbox.delete(0, tk.END)
        customers = Customer.get_all_customers(self.db)
        for customer in customers:
            self.customer_listbox.insert(tk.END, f"{customer[1]} - {customer[2]} - {customer[3]}")

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

        # Supplier listbox
        self.supplier_listbox = tk.Listbox(self.supplier_tab)
        self.supplier_listbox.pack(side='left', fill='both', expand=True)

        # Create a scrollbar
        self.supplier_scrollbar = ttk.Scrollbar(self.supplier_tab, orient='vertical', command=self.supplier_listbox.yview)
        self.supplier_scrollbar.pack(side='left', fill='y')

        self.supplier_listbox.config(yscrollcommand=self.supplier_scrollbar.set)

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
        self.supplier_listbox.delete(0, tk.END)
        suppliers = Supplier.get_all_suppliers(self.db)
        for supplier in suppliers:
            self.supplier_listbox.insert(tk.END, f"{supplier[1]} - {supplier[2]} - {supplier[3]}")

    def add_supplier(self):
        name = self.supplier_name_entry.get()
        email = self.supplier_email_entry.get()
        address = self.supplier_address_entry.get()

        supplier = Supplier(name, email, address)
        supplier.save_to_db(self.db)

        messagebox.showinfo("Success", "Supplier added successfully!")
        self.refresh_suppliers()

    def on_closing(self):
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
