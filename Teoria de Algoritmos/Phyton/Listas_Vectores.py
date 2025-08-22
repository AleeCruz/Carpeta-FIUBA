from dataclasses import dataclass

# 1. Definir el "struct" de Producto con dataclass
@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int

# 2. Crear una instancia del struct con valores específicos
mi_producto = Producto(nombre="Smartphone X", precio=699.99, stock=150)

# 3. Acceder a los valores y usarlos
print("--- Detalles del Producto ---")
print(f"Nombre: {mi_producto.nombre}")
print(f"Precio: ${mi_producto.precio}")
print(f"Stock disponible: {mi_producto.stock} unidades")

# 4. Imprimir la representación completa del objeto (muy útil para depurar)
print("\n--- Representación del objeto ---")
print(mi_producto)
