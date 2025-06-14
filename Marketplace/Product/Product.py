# Esta clase representa un producto en un marketplace. 
# Permite crear un producto con nombre, precio y stock.
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"
    
    def check_stock(self, quantity=1):
        return self.stock >= quantity         # retorna True si hay suficiente stock

    def sell(self, quantity):
        if self.check_stock(quantity):
            self.stock -= quantity
            return True                       # descuenta el stock si hay suficiente
        print(f"Stock insuficiente de {self.name} (Stock actual: {self.stock})")   # si no hay suficiente stock muestra un mensaje de error.
        return False

    def increase_stock(self, quantity):
        self.stock += quantity                # suma unidades al stock
        print(f"Stock incrementado: {quantity} unidades añadidas a {self.name}.")
        return True