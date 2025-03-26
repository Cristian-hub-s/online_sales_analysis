class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        """Afișează informațiile produsului."""
        print(f"Produs: {self.name}, Preț: {self.price} RON, Cantitate: {self.quantity}")
    
    def update_quantity(self, new_quantity):
        """Actualizează cantitatea produsului."""
        self.quantity = new_quantity
        print(f"Cantitatea produsului '{self.name}' a fost actualizată la {self.quantity}.")
