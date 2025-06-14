from Marketplace.UserManager import UserManager
from Marketplace.User import User
from Marketplace.Product import Product

# main.py --- Sistema de gestión de usuarios con login y registro
# Este script implementa un sistema de gestión de usuarios que permite el registro, login y listado de usuarios.
# El sistema permite un máximo de 3 intentos para login o registro, bloqueando la cuenta si se superan.
# Importación de las clases User y UserManager

# Clase principal que ejecuta el sistema y contiene el menú
class MainApp:
    def __init__(self):
        self.manager = UserManager()
        self.intentos = 0
        # Lista fija de productos disponibles en el sistema
        self.products = [
            Product("Manzanas", 1000, 10),
            Product("Peras", 2000, 5),
            Product("Naranjas", 3000, 20)
        ]

    # Menú principal
    def run(self):
        while self.intentos < 3:
            print("\n" + "="*30)
            print("Bienvenido al sistema".center(30))
            print("="*30)

            # Validación de opción del menú que sea un int y esté dentro del rango de opciones ofrecidas.
            opcion = self.menu()

            # Opción 1: Login
            if opcion == 1:
                user = self.manager.login()
                if user:  # Login exitoso
                    self.menu_compra(user)  # Llama al submenú de compra
                    break
                else:
                    self.intentos += 1
                    print(f"\nIntento fallido. Intentos restantes: {3 - self.intentos}")

            # Opción 2: Registro
            elif opcion == 2:
                if not self.manager.sign_up():
                    self.intentos += 1
                    print(f"\nIntento fallido. Intentos restantes: {3 - self.intentos}")

            # Opción 3: Salir
            elif opcion == 3:
                print("\nGracias por usar el sistema")
                break

            # Bloqueo por intentos
            if self.intentos >= 3:
                self.bloqueo()
                break

        # Mostrar estado final
        print("\nEstado final del sistema:")
        self.manager.show_users()

    def menu(self):
        while True:
            try:
                opcion = int(input("\n(1) Ingreso\n(2) Nuevo usuario\n(3) Salir\n\nSeleccione opción: "))
                if opcion in (1, 2, 3):
                    return opcion
                print("Error: Ingrese 1, 2 o 3")
            except ValueError:
                print("Error: Debe ingresar un número")

    def bloqueo(self):
        print("\n" + "!"*30)
        print("CUENTA BLOQUEADA".center(30))
        print("Demasiados intentos fallidos".center(30))
        print("!"*30)

    # Submenú de compra luego del login exitoso
    def menu_compra(self, user):
        while True:
            print("\n" + "-"*30)
            print("MENÚ DE COMPRA".center(30))
            print("-"*30)
            print("(1) Ver productos")
            print("(2) Agregar producto al carrito")
            print("(3) Finalizar compra")
            print("(4) Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("\nProductos disponibles:")
                for idx, prod in enumerate(self.products, 1):
                    print(f"{idx}. {prod.name} - ${prod.price} (Stock: {prod.stock})")

            elif opcion == "2":
                try:
                    idx = int(input("Ingrese número de producto: ")) - 1
                    cantidad = int(input("Ingrese cantidad: "))
                    if 0 <= idx < len(self.products):
                        prod = self.products[idx]
                        if user.add_product(prod, cantidad):
                            print(f"{prod.name} agregado al carrito")
                        else:
                            print(f"No se pudo agregar {prod.name} al carrito")
                    else:
                        print("Producto inválido")
                except ValueError:
                    print("Entrada inválida")

            elif opcion == "3":
                purchase = user.finalize_purchase()
                if purchase:
                    purchase.generate_receipt()
                else:
                    print("El carrito está vacío")

            elif opcion == "4":
                print("Sesión cerrada.")
                break

            else:
                print("Opción inválida")

if __name__ == "__main__":
    app = MainApp()
    app.run()

# Este script es el punto de entrada del sistema de gestión de usuarios y compras.
# Permite registrar e iniciar sesión con hasta 3 intentos, y realizar compras desde un submenú.
# La clase App controla el flujo principal, usando clases modulares como User, UserManager, Product y Purchase.
# El sistema es extensible, modular y fácil de usar como aplicación independiente.
# El código está diseñado para ser ejecutado directamente, iniciando la aplicación y mostrando el menú principal.