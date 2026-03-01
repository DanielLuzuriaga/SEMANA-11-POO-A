# SEMANA-11-POO-A
# 📦 Sistema Avanzado de Gestión de Inventario

## 📌 Descripción

Mi proyecto consiste en el desarrollo de un sistema avanzado de gestión de inventario utilizando Programación Orientada a Objetos (POO) en Python.  

El sistema desarrollado permite administrar productos mediante operaciones como agregar, eliminar, actualizar, buscar y visualizar el inventario, almacenando la información de manera persistente en un archivo JSON, que reemplaza al archivo txt. de la semana 10.

---

## 🎯 Objetivos

- Aplicar conceptos de Programación Orientada a Objetos.
- Utilizar colecciones (diccionarios y listas) para gestionar datos.
- Implementar lectura y escritura de archivos (persistencia).
- Desarrollar un menú interactivo en consola.

---

## 🏗 Estructura del Proyecto
inventario_app/
│
├── main.py
├── inventario.json
│
├── modelos/
│ └── producto.py
│
└── servicios/
└── inventario.py


---

## 🧠 Conceptos de POO Aplicados

- Clases y Objetos
- Encapsulamiento
- Métodos getters y setters
- Modularización
- Separación de responsabilidades

---

## 📚 Colecciones Utilizadas

- **Diccionario** → Almacena los productos usando el ID como clave.
- **Lista** → Para resultados de búsqueda.
- **JSON (estructura tipo diccionario)** → Para almacenamiento persistente.

---

## 💾 Persistencia de Datos

El sistema utiliza serialización en formato JSON para guardar y cargar la información del inventario.  

Esto permite que los datos permanezcan almacenados incluso después de cerrar el programa.

---

## ▶️ Cómo Ejecutar

1. Ubicarse en la carpeta del proyecto.
2. Ejecutar el archivo principal:

```bash
python main.py
