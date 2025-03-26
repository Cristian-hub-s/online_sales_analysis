class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product, quantity):
        """Adaugă un produs în coș."""
        product.quantity = quantity
        self.cart_items.append(product)
        print(f"Produsul '{product.name}' a fost adăugat în coș cu cantitatea de {quantity}.")
    
    def total_cart_value(self):
        """Calculează valoarea totală a coșului."""
        total_value = sum(product.price * product.quantity for product in self.cart_items)
        return total_value
    
    def display_cart(self):
        """Afișează produsele din coș."""
        if not self.cart_items:
            print("Coșul este gol.")
        else:
            for item in self.cart_items:
                print(f"Produs: {item.name}, Cantitate: {item.quantity}, Preț: {item.price}")
