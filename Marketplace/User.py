import random
from Marketplace.Purchase import Purchase

# User.py --- Clase que representa un usuario
# Esta clase permite crear un usuario con nombre, dni, teléfono y contraseña.
# En relación a la compra, permite agregar productos al carrito, eliminar productos del carrito y finalizar la compra.

class User:
    def __init__(self, name, dni, password):
        self.name = name
        self.dni = dni
        self.password = password
        self.cart = []                    # productos actualmente en el carrito (lista de tuplas (producto, cantidad))
        self.purchase_history = []       # todas las compras realizadas por ese cliente

    def __str__(self):
        return f"User: {self.name} | DNI: {self.dni} | Purchases: {len(self.purchase_history)}"

    def add_product(self, product, quantity=1):
        if product.sell(quantity):
            self.cart.append((product, quantity))     # verifica stock, descuenta y lo agrega al carrito
            return True
        return False

    def remove_product(self, product):
        for item in self.cart:                        # itera cada item de la lista de compra
            if item[0] == product:                    # si el producto del ítem es igual al que se quiere eliminar
                product.increase_stock(item[1])       # devuelve al producto la cantidad que se había descontado (restituye el stock)
                self.cart.remove(item)                # elimina el producto del carrito y devuelve el stock
                return True
        return False

    def finalize_purchase(self):
        """Crea un ticket de compra y limpia el carrito"""
        if not self.cart:
            return None

        total = sum(p.price * quantity for p, quantity in self.cart)
        purchase_id = f"{self.dni[:4]}-{random.randint(1000, 9999)}"

        new_purchase = Purchase(                      # genera una compra
            id=purchase_id,
            user_name=self.name,
            user_dni=self.dni,                            
            total=total,
            cart_items=self.cart.copy()
        )

        self.purchase_history.append(new_purchase)    # agrega la compra al historial
        self.cart.clear()                             # limpia el carrito
        return new_purchase                           # retorna Objeto Compra

    

