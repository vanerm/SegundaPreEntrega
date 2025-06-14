from Marketplace.UserManager import UserManager
from Marketplace.User import User

# main.py --- Sistema de gestión de usuarios con login y registro
# Este script implementa un sistema de gestión de usuarios que permite el registro, login y listado de usuarios.
# El sistema permite un máximo de 3 intentos para login o registro, bloqueando la cuenta si se superan.
# Importación de las clases User y UserManager

# Clase principal que ejecuta el sistema y contiene el menú
class App:
    def __init__(self):
        self.manager = UserManager()
        self.intentos = 0

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
                if self.manager.login():
                    break  # Login exitoso, salir del sistema
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


if __name__ == "__main__":
    app = App()
    app.run()
