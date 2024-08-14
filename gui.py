import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from db import Database
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
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
        self.style = ttk.Style()  # For styling elements

        # Create the notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

<<<<<<< HEAD
        # Add tabs
        self.create_all_tab()
    
     # Funtion to create tab
    def create_all_tab(self):
        self.create_loging_tab()
        self.create_signup_tab()
        # self.create_inventory_tab()
        # self.create_customer_tab()
        # self.create_supplier_tab()
        # self.create_sales_tab()
        # self.create_order_tab()

    def create_loging_tab(self):
        self.login_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.login_tab, text="Login")

        # Name label and entry
        label_username = ttk.Label(self.login_tab, text="username:")
        label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = ttk.Entry(self.login_tab)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        # Email label and entry
        label_password = ttk.Label(self.login_tab, text="password:")
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = ttk.Entry(self.login_tab)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        button_login = ttk.Button(self.login_tab, text="Login", command=self.login)
        button_login.grid(row=2, columnspan=2, pady=20)
    
    # login function
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        account_exit = self.db.fetchone("SELECT id FROM customers WHERE name = ? AND email = ?", (username, password))
        if account_exit:
            self.notebook.forget(self.login_tab)
            self.notebook.forget(self.signup_tab)
            self.create_inventory_tab()
            self.create_customer_tab()
            self.create_supplier_tab()
            self.create_sales_tab()
            self.create_order_tab()

            messagebox.showinfo("Login Success", f"Welcome, {username}!")
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password.")

    def create_signup_tab(self):
        self.signup_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.signup_tab, text="Sign UP")
=======
        # Create tabs
        self.create_home_tab()
        self.create_inventory_tab()
        self.create_customer_tab()
        self.create_supplier_tab()
        self.create_sales_tab()
        self.create_order_tab()
>>>>>>> upstream/sadric.0

    def create_home_tab(self):
        self.home_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.home_tab, text='Home')

        # Welcome message
        welcome_label = ttk.Label(self.home_tab, text="Welcome to the Lavender Bookstore Management System!", font=('Helvetica', 16))
        welcome_label.pack(pady=20)

        # Navigation buttons
        button_frame = ttk.Frame(self.home_tab)
        button_frame.pack(pady=10)

        inventory_button = ttk.Button(button_frame, text="Inventory Management", command=self.show_inventory_tab)
        inventory_button.grid(row=0, column=0, padx=10, pady=10)

        sales_button = ttk.Button(button_frame, text="Sales Report", command=self.show_sales_tab)
        sales_button.grid(row=0, column=1, padx=10, pady=10)

        order_button = ttk.Button(button_frame, text="Order Management", command=self.show_order_tab)
        order_button.grid(row=1, column=0, padx=10, pady=10)

        customer_button = ttk.Button(button_frame, text="Customer Management", command=self.show_customer_tab)
        customer_button.grid(row=1, column=1, padx=10, pady=10)

        supplier_button = ttk.Button(button_frame, text="Supplier Management", command=self.show_supplier_tab)
        supplier_button.grid(row=2, column=0, padx=10, pady=10)

        # Quick Stats
        stats_frame = ttk.Frame(self.home_tab)
        stats_frame.pack(pady=20)

        # Example of quick stats
        total_books_label = ttk.Label(stats_frame, text="Total Books in Stock: 100")  # Replace with actual dynamic data
        total_books_label.pack(pady=5)

        total_sales_label = ttk.Label(stats_frame, text="Total Sales Today: $500")  # Replace with actual dynamic data
        total_sales_label.pack(pady=5)

        # Logout button
        logout_button = ttk.Button(self.home_tab, text="Logout", command=self.logout)
        logout_button.pack(side='bottom', pady=20)

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

        existing_book = self.db.fetchone("SELECT id, stock_quantity FROM books WHERE title = ? AND author = ?", (title, author))
        
        if existing_book:
            new_quantity = existing_book[1] + stock_quantity
            self.db.execute("UPDATE books SET stock_quantity = ? WHERE id = ?", (new_quantity, existing_book[0]))
            messagebox.showinfo("Success", "Book already exists. Stock quantity updated!")
        else:
            self.db.execute(
                "INSERT INTO books (title, author, genre, price, stock_quantity) VALUES (?, ?, ?, ?, ?)",
                (title, author, genre, price, stock_quantity)
            )
            messagebox.showinfo("Success", "New book added to the inventory!")
        
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

        self.db.execute(
            "UPDATE books SET title = ?, author = ?, genre = ?, price = ?, stock_quantity = ? WHERE id = ?",
            (title, author, genre, price, stock_quantity, book_id)
        )

        messagebox.showinfo("Success", "Book updated successfully!")
        self.refresh_inventory()

    def delete_book(self):
        selected_item = self.inventory_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No book selected")
            return

        item = self.inventory_tree.item(selected_item)
        book_id = item['values'][0]

        self.inventory.remove_book_by_id(book_id)
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
        self.notebook.add(self.sales_tab, text='Sales Report')

        # Header Section
        header_frame = ttk.Frame(self.sales_tab)
        header_frame.pack(pady=10)

        # Title
        title_label = ttk.Label(header_frame, text="Sales Report", font=('Helvetica', 24, 'bold'))
        title_label.pack(pady=10)

        # Date Range Selector
        date_range_frame = ttk.Frame(header_frame)
        date_range_frame.pack()

        date_range_label = ttk.Label(date_range_frame, text="Date Range:", font=('Helvetica', 12))
        date_range_label.pack(side='left', padx=5)

        self.date_range_combobox = ttk.Combobox(date_range_frame, values=["Today", "Last 7 Days", "This Month", "Custom Range"])
        self.date_range_combobox.current(0)
        self.date_range_combobox.pack(side='left', padx=5)

        # Generate Report Button
        generate_report_button = ttk.Button(header_frame, text="Generate Report", command=self.generate_sales_report)
        generate_report_button.pack(pady=10)
        generate_report_button.configure(style="TButton")
        # Style the button with lavender color
        self.style.configure("TButton", background='#E6E6FA', foreground='black', font=('Helvetica', 12, 'bold'))
        self.style.map("TButton", background=[("active", "#D8BFD8")])  # Lighter lavender on hover

        # Summary Section
        summary_frame = ttk.Frame(self.sales_tab)
        summary_frame.pack(pady=10)

        # Total Sales
        self.total_sales_label = ttk.Label(summary_frame, text="Total Sales: $0.00", font=('Helvetica', 16, 'bold'))
        self.total_sales_label.pack(pady=5)

        # Number of Transactions
        self.transactions_label = ttk.Label(summary_frame, text="Transactions: 0", font=('Helvetica', 16, 'bold'))
        self.transactions_label.pack(pady=5)

        # Chart Section
        self.chart_frame = ttk.Frame(self.sales_tab)
        self.chart_frame.pack(fill="both", expand=True, pady=10)

        # Create a placeholder for the chart (actual plotting will be done later)
        self.plot_sales_over_time([])

        # Detailed Sales Table
        self.sales_tree = ttk.Treeview(self.sales_tab, columns=("Date", "Book Title", "Quantity", "Total Amount"), show='headings')
        self.sales_tree.heading("Date", text="Date")
        self.sales_tree.heading("Book Title", text="Book Title")
        self.sales_tree.heading("Quantity", text="Quantity")
        self.sales_tree.heading("Total Amount", text="Total Amount")

        self.sales_tree.pack(fill="both", expand=True, pady=10)

        # Make columns sortable
        for col in self.sales_tree["columns"]:
            self.sales_tree.heading(col, text=col, command=lambda _col=col: self.sort_sales_table(_col))

        # Search bar
        search_frame = ttk.Frame(self.sales_tab)
        search_frame.pack(pady=10)
        search_label = ttk.Label(search_frame, text="Search:")
        search_label.pack(side="left", padx=5)
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)
        search_button = ttk.Button(search_frame, text="Search", command=self.search_sales_table)
        search_button.pack(side="left", padx=5)

        # Export Button
        self.create_export_button()

    def plot_sales_over_time(self, sales_data):
        # Prepare data for plotting
        df = pd.DataFrame(sales_data, columns=["Date", "Book Title", "Quantity", "Total Amount"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.groupby("Date")["Total Amount"].sum().reset_index()

        # Create the plot with animations
        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Total Amount"], marker="o", color='#8A2BE2')  # Lavender color
        ax.set_title("Sales Over Time", fontdict={'fontsize': 16, 'fontweight': 'bold'})
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Sales ($)")
        ax.grid(True)

        # Display the plot in the Tkinter GUI
        for widget in self.chart_frame.winfo_children():
            widget.destroy()  # Clear any previous chart
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def generate_sales_report(self):
        # Determine the date range based on user selection
        date_range = self.date_range_combobox.get()
        if date_range == "Today":
            start_date = end_date = datetime.today().date()
        elif date_range == "Last 7 Days":
            end_date = datetime.today().date()
            start_date = end_date - timedelta(days=7)
        elif date_range == "This Month":
            end_date = datetime.today().date()
            start_date = end_date.replace(day=1)
        else:
            start_date, end_date = self.select_custom_date_range()

        # Fetch sales data and summary
        sales_data = self.db.get_sales_data(start_date, end_date)
        summary = self.db.get_total_sales_summary(start_date, end_date)

        # Update summary labels with correct tuple indexing
        self.total_sales_label.config(text=f"Total Sales: ${summary[1]:.2f}")
        self.transactions_label.config(text=f"Transactions: {summary[0]}")

        # Update the sales table
        for item in self.sales_tree.get_children():
            self.sales_tree.delete(item)
        for sale in sales_data:
            self.sales_tree.insert('', 'end', values=sale)

        # Plot sales over time
        self.plot_sales_over_time(sales_data)

    def sort_sales_table(self, col):
        # Get data from the treeview and sort it
        data = [(self.sales_tree.set(child, col), child) for child in self.sales_tree.get_children('')]
        data.sort(reverse=self.sales_tree.heading(col, "command") == "DESC")

        for index, (_, child) in enumerate(data):
            self.sales_tree.move(child, '', index)

        self.sales_tree.heading(col, command=lambda: self.sort_sales_table(col))

    def search_sales_table(self):
        query = self.search_entry.get()
        for item in self.sales_tree.get_children():
            self.sales_tree.delete(item)
        sales = self.db.fetchall(f"SELECT * FROM sales WHERE book_title LIKE '%{query}%'")
        for sale in sales:
            self.sales_tree.insert('', 'end', values=sale)

    def create_export_button(self):
        export_button = ttk.Button(self.sales_tab, text="Export Report", command=self.export_report)
        export_button.pack(pady=10)
        export_button.configure(style="TButton")

    def export_report(self):
        # Implement export functionality (e.g., export to CSV)
        pass

    def select_custom_date_range(self):
        # Implement a custom date range selector (for simplicity, return a static range)
        start_date = datetime.today().date() - timedelta(days=30)
        end_date = datetime.today().date()
        return start_date, end_date

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
            if not selected_supplier or not selected_book_title:
                raise ValueError("Please select a supplier and a book.")
                
            supplier_id = int(selected_supplier.split(":")[0].strip())
            book_id = self.book_dict.get(selected_book_title)  # Retrieve the book ID using the selected title

            quantity = int(self.order_quantity_entry.get())

            order = Order(supplier_id, book_id, quantity)
            order.save_to_db(self.db)

            messagebox.showinfo("Success", "Order added successfully!")
            self.refresh_orders()
        except ValueError as ve:
            messagebox.showerror("Error", f"Failed to add order: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def refresh_books_comboboxes(self):
        books = self.inventory.get_all_books()
        self.book_dict = {book[1]: book[0] for book in books}  # Create a dictionary with title as key and ID as value
        
        if hasattr(self, 'sale_book_combobox'):  # Ensure sale_book_combobox exists
            self.sale_book_combobox['values'] = list(self.book_dict.keys())  # Set combobox values to book titles

        if hasattr(self, 'order_book_combobox'):  # Ensure order_book_combobox exists
            self.order_book_combobox['values'] = list(self.book_dict.keys())  # Set combobox values to book titles

    def show_inventory_tab(self):
        self.notebook.select(self.inventory_tab)

    def show_sales_tab(self):
        self.notebook.select(self.sales_tab)

    def show_order_tab(self):
        self.notebook.select(self.order_tab)

    def show_customer_tab(self):
        self.notebook.select(self.customer_tab)

    def show_supplier_tab(self):
        self.notebook.select(self.supplier_tab)

    def logout(self):
        # Implement logout functionality if needed
        self.root.quit()

    def on_closing(self):
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the geometry of the root window to match the screen size
    root.geometry(f"{screen_width}x{screen_height}")
    app = BookstoreApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
