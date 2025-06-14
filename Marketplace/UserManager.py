from Marketplace.User import User
# UserManager.py

# Clase que administra a los usuarios: registro, login y listado
class UserManager:
    def __init__(self):
        # Lista de usuarios
        self.users = []

    # Función que solicita los datos (nombre y pass) para ingresar por teclado por el usuario
    def input_data(self):
        name = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        return name, password

    # Función de bienvenida que informa el nombre del usuario
    def welcome(self, name):
        print(f"\nBienvenido/a: {name}")

    # Función para agregar nuevos usuarios a la lista de usuarios
    def save_new_user(self, name, password):
        new_user = User(name, password)
        self.users.append(new_user)
        return True

    # Función para verificar si un usuario existe
    def user_exists(self, name):
        return any(user.name == name for user in self.users)

    # Función para mostrar los nombres de todos los usuarios registrados en mi lista de users
    def show_users(self):
        print("\nUsuarios en el sistema:")
        for user in self.users:
            print(f"Usuario: {user.name}")

    # Función para registro de nuevos usuarios
    def sign_up(self):
        print("\nBienvenido al sistema de Registro")
        name, password = self.input_data()

        if self.user_exists(name):
            print("Error: El usuario ya existe")
            return False  # Indica fallo en el registro porque el usuario ya existe

        self.save_new_user(name, password)
        self.welcome(name)
        return True  # Registro exitoso

    # Función para login de usuarios
    def login(self):
        print("\nBienvenido al sistema de Login")
        name, password = self.input_data()

        for user in self.users:
            if user.name == name and user.password == password:
                self.welcome(name)
                return True

        print("Error: Usuario o contraseña incorrectos")
        return False
