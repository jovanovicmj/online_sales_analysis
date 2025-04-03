from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
   
        for item in self.cart_items:
            if item["product"].name == product.name:
                item["quantity"] += quantity
                print(f"Proizvod '{product.name}' je dodan u korpu. Nova količina: {item['quantity']} kom.")
                return
        
        self.cart_items.append({"product": product, "quantity": quantity})
        print(f"Proizvod '{product.name}' je uspešno dodat u korpu sa količinom {quantity} kom.")

    def total_price(self):
        total = 0
        for item in self.cart_items:
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Vaša korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for item in self.cart_items:
                print(f"Proizvod: {item['product'].name}, Količina: {item['quantity']}, Cena po komadu: {item['product'].price} RSD")
            print("-" * 40)
