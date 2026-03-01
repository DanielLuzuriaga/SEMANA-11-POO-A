"""
Clase Inventario

Gestiona la colección de productos utilizando un diccionario.
Permite realizar operaciones CRUD y manejar la persistencia en archivos JSON.
"""

import json
from modelos.producto import Producto

class Inventario:

    def __init__(self):
        """
        Inicializa el inventario como un diccionario vacío.
        La clave será el ID del producto.
        """
        self.productos = {}

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario."""
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto ingresado.
        Devuelve una lista de productos encontrados.
        """
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

    def mostrar_todos(self):
        """Muestra todos los productos almacenados."""
        for producto in self.productos.values():
            print(producto)

    def calcular_valor_total_inventario(self):
        """Calcula el valor total del inventario."""
        return sum(p.valor_total() for p in self.productos.values())

    def guardar_archivo(self, archivo="inventario.json"):
        """
        Guarda el inventario en un archivo JSON.
        Se utiliza serialización para convertir objetos en diccionarios.
        """
        with open(archivo, "w") as f:
            json.dump(
                {id: p.to_dict() for id, p in self.productos.items()},
                f,
                indent=4
            )

    def cargar_archivo(self, archivo="inventario.json"):
        """
        Carga el inventario desde un archivo JSON.
        Realiza deserialización para convertir diccionarios en objetos Producto.
        """
        try:
            with open(archivo, "r") as f:
                contenido = f.read().strip()

                if not contenido:
                    return

                data = json.loads(contenido)

                for id_producto, info in data.items():
                    self.productos[id_producto] = Producto.from_dict(info)

        except FileNotFoundError:
            pass