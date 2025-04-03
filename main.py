
# main.py

from product import Product
from product_manager import ProductManager
import random
from cart import Cart

manager = ProductManager()

product1 = Product("Smartphone", 40000, 15)
product2 = Product("Tablet", 25000, 30)     
product3 = Product("Bežične slušalice", 6000, 40)
product4 = Product("Pametan TV", 45000, 8)  
product5 = Product("Gaming računar", 120000, 10)


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
