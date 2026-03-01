"""
Clase Producto

Representa un producto dentro del sistema de inventario.
Contiene atributos básicos como ID, nombre, cantidad y precio.
Incluye métodos para manipular y representar la información del producto.
"""

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicia los atributos principales del producto.
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # ------------------ MÉTODOS GETTERS ------------------

    def get_id(self):
        """Devuelve el ID del producto."""
        return self._id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible."""
        return self._cantidad

    def get_precio(self):
        """Devuelve el precio unitario."""
        return self._precio

    # ------------------ MÉTODOS SETTERS ------------------

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad del producto."""
        if cantidad >= 0:
            self._cantidad = cantidad

    def set_precio(self, precio):
        """Actualiza el precio del producto."""
        if precio >= 0:
            self._precio = precio

    # ------------------ MÉTODOS ADICIONALES ------------------

    def valor_total(self):
        """Calcula el valor total del producto en inventario."""
        return self._cantidad * self._precio

    def to_dict(self):
        """
        Convierte el objeto Producto en un diccionario.
        Se utiliza para guardar la información en formato JSON.
        """
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Producto a partir de un diccionario.
        Se utiliza al cargar datos desde el archivo JSON.
        """
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        """Devuelve una representación formateada del producto."""
        return (f"ID: {self._id} | "
                f"Nombre: {self._nombre} | "
                f"Cantidad: {self._cantidad} | "
                f"Precio: ${self._precio:.2f} | "
                f"Valor Total: ${self.valor_total():.2f}")