class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name}")
        print(f"Cena: {self.price} RSD")
        print(f"Količina: {self.quantity} kom")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Količina proizvoda '{self.name}' je ažurirana na {self.quantity} kom.")


product1 = Product("Laptop", 50000, 10)

product1.display_info()
product1.update_quantity(15)
product1.display_info()
