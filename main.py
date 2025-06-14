from Marketplace.Product import Product
from Marketplace.UserManager import UserManager
from Marketplace.PurchaseManager import PurchaseManager

# main.py --- Sistema de gestión de usuarios con login y registro
# Este script es el punto de entrada del sistema de gestión de usuarios y compras.
# Permite registrar e iniciar sesión con hasta 3 intentos, y realizar compras desde un submenú.
# La clase MainApp controla el flujo principal, usando clases modulares como UserManager, Product, Purchase y PurchaseManager.

# Clase principal que ejecuta el sistema y contiene el menú
class MainApp:
    def __init__(self):
        self.user_manager = UserManager()
        self.intentos = 0
        # Lista fija de productos disponibles en el sistema
        self.products = [
            Product("Manzanas", 1000, 10),
            Product("Peras", 2000, 5),
            Product("Naranjas", 3000, 20)
        ]
        self.purchase_manager = PurchaseManager(self.user_manager, self.products)

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
                user = self.user_manager.login()
                if user:  # Login exitoso
                    self.purchase_manager.purchase_menu(user)  # Llama al submenú de compra de PurchaseManager
                    break
                else:
                    self.intentos += 1
                    print(f"\nIntento fallido. Intentos restantes: {3 - self.intentos}")

            # Opción 2: Registro
            elif opcion == 2:
                if not self.user_manager.sign_up():
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
        self.user_manager.show_users()

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

if __name__ == "__main__":
    app = MainApp()
    app.run()
