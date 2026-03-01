"""
Archivo principal del Sistema Avanzado de Gestión de Inventario.

Este módulo contiene:
- La interfaz de usuario en consola.
- El menú interactivo.
- La conexión entre el usuario y la lógica del sistema (clase Inventario).
"""

# Importación de las clases necesarias
from servicios.inventario import Inventario
from modelos.producto import Producto


# ------------------ FUNCIONES AUXILIARES ------------------

def obtener_entero(mensaje):
    """
    Solicita al usuario un número entero.
    Implementa validación para evitar errores de entrada.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠️  Ingrese un número entero válido.")


def obtener_decimal(mensaje):
    """
    Solicita al usuario un número decimal (float).
    Implementa validación para evitar errores.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️  Ingrese un número válido.")


# ------------------ FUNCIÓN PRINCIPAL DEL MENÚ ------------------

def menu():
    """
    Función principal que ejecuta el sistema.
    Muestra el menú interactivo y gestiona las opciones seleccionadas.
    """

    # Se crea una instancia del inventario
    inventario = Inventario()

    # Se cargan los datos previamente guardados en el archivo JSON
    inventario.cargar_archivo()

    # Bucle principal del programa
    while True:
        print("="*50)
        print("     UNIVERSIDAD ESTATAL AMAZÓNICA")
        print("   SISTEMA  AVANZADO  DE  INVENTARIO")
        print("        AUTOR: DANIEL LUZURIAGA")
        print("="*50)
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Ver valor total del inventario")
        print("7. Guardar y salir")

        # Captura de la opción elegida por el usuario
        opcion = input("Seleccione una opción: ")

        # ------------------ OPCIÓN 1: AGREGAR PRODUCTO ------------------
        if opcion == "1":
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = obtener_entero("Cantidad: ")
            precio = obtener_decimal("Precio: ")

            # Se crea el objeto Producto
            producto = Producto(id_p, nombre, cantidad, precio)

            # Se agrega el producto al inventario
            inventario.agregar_producto(producto)

        # ------------------ OPCIÓN 2: ELIMINAR PRODUCTO ------------------
        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            inventario.eliminar_producto(id_p)

        # ------------------ OPCIÓN 3: ACTUALIZAR PRODUCTO ------------------
        elif opcion == "3":
            id_p = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (enter para omitir): ")
            precio = input("Nuevo precio (enter para omitir): ")

            # Conversión opcional de datos
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_p, cantidad, precio)

        # ------------------ OPCIÓN 4: BUSCAR PRODUCTO ------------------
        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron productos.")

        # ------------------ OPCIÓN 5: MOSTRAR INVENTARIO ------------------
        elif opcion == "5":
            inventario.mostrar_todos()

        # ------------------ OPCIÓN 6: VALOR TOTAL ------------------
        elif opcion == "6":
            total = inventario.calcular_valor_total_inventario()
            print(f"💰 Valor total del inventario: ${total:.2f}")

        # ------------------ OPCIÓN 7: GUARDAR Y SALIR ------------------
        elif opcion == "7":
            inventario.guardar_archivo()
            print("👋 Saliendo del sistema...")
            break

        # ------------------ OPCIÓN INVÁLIDA ------------------
        else:
            print("❌ Opción inválida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    """
    Esta condición asegura que el menú solo se ejecute
    cuando el archivo se ejecuta directamente,
    y no cuando es importado como módulo.
    """
    menu()