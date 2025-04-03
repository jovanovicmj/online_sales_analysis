# online_sales_analysis

# Product Management System

## Project Description

This project represents a system for managing products and carts, with basic functionalities such as adding, updating, and deleting products, as well as managing the cart. Through this system, users can add products, track their quantities, calculate the total value of the inventory, and make purchases via the cart.

## Classes in the Project

### 1. **Product**

The `Product` class represents a product and contains basic information about the product, including its name, price, and quantity. It also includes methods to display product information and update quantities.

#### Attributes:
- `name` (str): The product's name
- `price` (float): The product's price
- `quantity` (int): The quantity of the product in stock

#### Methods:
- `display_info()`: Displays the product's basic information (name, price, quantity).
- `update_quantity(new_quantity)`: Updates the product's quantity.

### 2. **ProductManager**

The `ProductManager` class is responsible for managing the list of products. It allows adding, deleting, and displaying all products, as well as calculating the total value of the inventory.

#### Attributes:
- `products` (list): A list of all products available in the manager

#### Methods:
- `add_product(product)`: Adds a product to the list.
- `remove_product_by_name(product_name)`: Removes a product from the list by its name.
- `display_all_products()`: Displays all products in the list.
- `total_value()`: Calculates the total value of the inventory (the total price of all products in stock).

### 3. **Cart**

The `Cart` class represents a shopping cart in which users can add products and track the total value of their purchase.

#### Attributes:
- `cart_items` (list): A list of products added to the cart, along with their quantities.

#### Methods:
- `add_to_cart(product, quantity)`: Adds a product to the cart with a specified quantity.
- `total_price()`: Calculates the total value of the cart.
- `display_cart()`: Displays all products in the cart, along with their quantities.


