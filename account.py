import tkinter as tk
from tkinter import ttk

class Register(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #  # Username Label and Entry
        # self.username_label = ttk.Label(self, text="Username:")
        # self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # self.username_entry = ttk.Entry(self)
        # self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Email Label and Entry
        self.email_label = ttk.Label(self, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Password Label and Entry
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")


        # Confirm Password Label and Entry
        self.confirmPassword_label = ttk.Label(self, text="Confirm Password:")
        self.confirmPassword_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.confirmPassword = ttk.Entry(self, show="*")
        self.confirmPassword.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        # Sign-Up Button
        self.signup_button = ttk.Button(self, text="Sign Up", command=self.signup)
        self.signup_button.grid(row=4, columnspan=2, pady=20)

    def signup(self):
        # Retrieve the entered data
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Here you can add code to handle the signup logic
        self.forget(self.login_tab)

class Login(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Name label and entry
        label_username = ttk.Label(self, text="username:")
        label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = ttk.Entry(self)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        # Email label and entry
        label_password = ttk.Label(self, text="password:")
        label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = ttk.Entry(self)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)