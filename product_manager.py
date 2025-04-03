
from product import Product

class ProductManager:
    def __init__(self):
        # Lista koja sadrži sve proizvode
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' je uspešno dodat.")

    def display_all_products(self):
        if not self.products:
            print("Nema proizvoda u listi.")
        else:
            print("Lista svih proizvoda:")
            for product in self.products:
                product.display_info()
                print("-" * 30)  

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Ukupna vrednost svih proizvoda je {total} RSD.")

product1 = Product("Laptop", 50000, 10)
product2 = Product("Telefon", 30000, 20)
product3 = Product("Slušalice", 5000, 50)

manager = ProductManager()

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.display_all_products()

manager.total_value()
