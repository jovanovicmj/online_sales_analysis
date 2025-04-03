
# main.py

from product import Product
from product_manager import ProductManager
import random
from cart import Cart

manager = ProductManager()

product1 = Product("Laptop", 50000, 10)
product2 = Product("Telefon", 30000, 20)
product3 = Product("Slušalice", 5000, 50)
product4 = Product("Televizor", 60000, 5)
product5 = Product("Racunarski sto", 15000, 15)


manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)

manager.display_all_products()
manager.total_value()

cart = Cart()


random_products = random.sample(manager.products, 3)


for product in random_products:
    quantity = random.randint(1, 3) 
    cart.add_to_cart(product, quantity)


cart.display_cart()

print(f"Ukupna cena korpe za naplatu: {cart.total_price()} RSD")
