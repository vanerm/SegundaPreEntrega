class Purchase:
    def __init__(self,id,user_name,user_dni,total,cart_items):
        self.id = id
        self.user_name = user_name
        self.user_dni = user_dni
        self.total = total
        self.cart_items = cart_items  # Lista de tuplas (producto, cantidad)

    def generate_receipt(self):      # imprime resúmen con los datos de la compra:
        """Muestra el detalle de la compra y el stock actualizado"""
        print(f"\n--- RECEIPT #{self.id} ---")
        print(f"Cliente: {self.user_name}")
        for product, quantity in self.cart_items:
            print(f"{product.name:20} x{quantity:2} ${product.price * quantity:>7}")
        print(f"\nTOTAL: ${self.total}")
        print("\nStock actualizado:")
        for product, _ in self.cart_items:
            print(f"{product.name}: {product.stock} units")
        print("----------------------")