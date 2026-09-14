# Restaurante App – Semana 13

## Descripción

Este proyecto corresponde a la Semana 13 de la asignatura Programación Orientada a Objetos.

La aplicación consiste en una versión inicial de un sistema de restaurante desarrollado en Python, utilizando Tkinter para construir una interfaz gráfica de usuario.

El sistema permite simular el inicio de sesión y visualizar productos y usuarios registrados desde archivos JSON.

## Objetivo

Aplicar los fundamentos de interfaces gráficas de usuario mediante Tkinter, manteniendo una organización modular basada en modelos, servicios, datos y vistas.

## Tecnologías utilizadas

* Python 3.x
* Tkinter
* Programación Orientada a Objetos
* Archivos JSON

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

## Funcionalidades implementadas

* Pantalla de inicio de sesión.
* Validación de usuario y contraseña.
* Mensajes para campos vacíos y credenciales incorrectas.
* Visualización de productos registrados.
* Visualización de usuarios registrados.
* Cierre de sesión.
* Lectura de información desde archivos JSON.
* Organización modular del sistema.

## Flujo de la aplicación

```text
Inicio de la aplicación
        ↓
Pantalla de Login
        ↓
Ingreso de usuario y contraseña
        ↓
Validación mediante RestauranteServicio
        ↓
Interfaz principal
        ↓
Visualización de productos o usuarios
        ↓
Cerrar sesión
        ↓
Regreso al Login
```

## Cómo ejecutar

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Verificar que Python esté instalado.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

En Windows también se puede utilizar:

```bash
py main.py
```

## Credenciales de demostración

**Usuario:** admin

**Contraseña:** 1234

También se puede utilizar:

**Usuario:** docente

**Contraseña:** abcd

## Nota

La autenticación utilizada es únicamente una simulación educativa. El proyecto no implementa un sistema real de autenticación segura.

## Autor

Stefany Gallegos

## Asignatura

Programación Orientada a Objetos

## Semana

Semana 13
