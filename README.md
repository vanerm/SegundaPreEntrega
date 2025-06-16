# Sistema de Gestión de Usuarios y Compras

Este proyecto fue desarrollado como parte de la materia de Python de la [Diplomatura de Data Science en Coder House](https://www.coderhouse.com/ar/diplomaturas/data/). Es una aplicación modular que permite gestionar usuarios, realizar compras y administrar productos. El sistema está diseñado para ser extensible, fácil de usar y ejecutable como una aplicación independiente.

## Funcionalidades

1. **Gestión de Usuarios**:
   - Registro de nuevos usuarios.
   - Inicio de sesión con validación de credenciales.
   - Listado de usuarios registrados.

2. **Gestión de Compras**:
   - Visualización de productos disponibles.
   - Agregar productos al carrito.
   - Finalizar compras con generación de recibos.
   - Actualización automática del stock de productos.

3. **Gestión de Productos**:
   - Visualización de stock disponible.
   - Actualización del stock tras cada compra.

## Estructura del Proyecto

El proyecto está organizado en módulos para facilitar su mantenimiento y escalabilidad:

```
SegundaPreEntrega/
├── main.py
├── Marketplace/
│   ├── __init__.py
│   ├── User/
│   │   ├── __init__.py
│   │   ├── User.py
│   │   └── UserManager.py
│   ├── Product/
│   │   ├── __init__.py
│   │   └── Product.py
│   ├── Purchase/
│   │   ├── __init__.py
│   │   ├── Purchase.py
│   │   └── PurchaseManager.py

```

- **`main.py`**: Punto de entrada del sistema. Controla el flujo principal de la aplicación.
- **`Marketplace/Product/Product.py`**: Clase que representa un producto con atributos como nombre, precio y stock.
- **`Marketplace/Purchase/Purchase.py`**: Clase que gestiona las compras y genera recibos.
- **`Marketplace/Purchase/PurchaseManager.py`**: Clase que administra el proceso de compra.
- **`Marketplace/User/User.py`**: Clase que representa un usuario con carrito e historial de compras.
- **`Marketplace/User/UserManager.py`**: Clase que administra el registro, login y listado de usuarios.

## Cómo Ejecutar el Proyecto

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. Ejecuta el archivo `main.py` desde la terminal:

```bash
python main.py
```

## Ejemplo de Uso

Al iniciar la aplicación, se mostrará un menú principal con las siguientes opciones:

1. **Ingreso**: Permite iniciar sesión con un usuario registrado.
2. **Nuevo Usuario**: Permite registrar un nuevo usuario.
3. **Salir**: Finaliza la ejecución del programa.

Tras un inicio de sesión exitoso, se accede al menú de compras, donde se pueden visualizar productos, agregar al carrito y finalizar la compra.

## Créditos

Este proyecto fue desarrollado como parte de la [Diplomatura de Data Science en Coder House](https://www.coderhouse.com/ar/diplomaturas/data/).