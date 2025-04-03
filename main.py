
# main.py

from product import Product
from product_manager import ProductManager

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

