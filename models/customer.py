import json

class Customer:
    def __init__(self, customer_id, name, email, address, customer_file='data/customers.json'):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address
        self.customer_file = customer_file
        self.load_customers()

    def load_customers(self):
        try:
            with open(self.customer_file, 'r') as file:
                self.customers = json.load(file)
        except FileNotFoundError:
            self.customers = []

    def save_customers(self):
        with open(self.customer_file, 'w') as file:
            json.dump(self.customers, file, indent=4)

    def add_customer(self):
        self.customers.append({
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "address": self.address
        })
        self.save_customers()

    def remove_customer(self, customer_id):
        self.customers = [c for c in self.customers if c["customer_id"] != customer_id]
        self.save_customers()
