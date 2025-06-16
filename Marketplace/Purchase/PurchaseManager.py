from Marketplace.User.User import User

# PurchaseManager.py --- Clase que gestiona las compras de los usuarios
class PurchaseManager:
    def __init__(self, user, products):
        self.user = user
        self.products = products

    # Submenú de compra luego del login exitoso
    def purchase_menu(self, user):
        while True:
            print("\n" + "-"*30)
            print("MENÚ DE COMPRA".center(30))
            print("-"*30)
            print("(1) Ver productos")
            print("(2) Agregar producto al carrito")
            print("(3) Finalizar compra")
            print("(4) Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            # Lista los productos disponibles, precio y stock
            if opcion == "1":
                print("\nProductos disponibles:")
                for idx, prod in enumerate(self.products, 1):
                    print(f"{idx}. {prod.name} - ${prod.price} (Stock: {prod.stock})")

            # Agrega un producto al carrito del usuario
            elif opcion == "2":
                try:
                    idx = int(input("Ingrese número de producto: ")) - 1
                    cantidad = int(input("Ingrese cantidad: "))
                    if 0 <= idx < len(self.products):
                        prod = self.products[idx]
                        if user.add_product(prod, cantidad):
                            print(f"{prod.name} agregado al carrito") # Si se pudo agregar al carrito, muestra un mensaje de éxito
                        else:
                            print(f"No se pudo agregar {prod.name} al carrito") # Si no se pudo agregar por stock insuficiente, muestra un mensaje de error
                    else:
                        print("Producto inválido")
                except ValueError:
                    print("Entrada inválida")

            # Finaliza la compra, genera un ticket y actualiza el stock
            elif opcion == "3":
                purchase = user.finalize_purchase()
                if purchase:
                    purchase.generate_receipt()
                else:
                    print("El carrito está vacío")

            # Cierra la sesión del usuario.
            elif opcion == "4":
                print("Sesión cerrada.")
                break

            else:
                print("Opción inválida")

