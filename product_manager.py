# product_manager.py
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        """Adaugă un produs în lista de produse."""
        self.products.append(product)
    
    def remove_product_by_name(self, product_name):
        """Elimină un produs din lista de produse după numele său."""
        self.products = [product for product in self.products if product.name != product_name]
        print(f"Produsul '{product_name}' a fost eliminat din inventar.")
    
    def display_products(self):
        """Afișează toate produsele din lista de produse."""
        if not self.products:
            print("Nu există produse în inventar.")
        else:
            for product in self.products:
                product.display_info()
    
    def total_inventory_value(self):
        """Calculează și afișează valoarea totală a inventarului."""
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totală a inventarului: {total_value} RON")


