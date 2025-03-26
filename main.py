from product_manager import ProductManager
from product import Product

def main():
    # Crează instanța de ProductManager
    manager = ProductManager()
    
    # Creează câteva produse arbitrare
    product1 = Product("Laptop", 3500, 10)
    product2 = Product("Telefon", 1500, 20)
    product3 = Product("Mouse", 50, 100)
    
    # Adaugă produsele în inventar
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    # Afișează toate produsele
    print("Produse în inventar:")
    manager.display_products()
    
    # Afișează valoarea totală a inventarului
    manager.total_inventory_value()

if __name__ == "__main__":
    main()
