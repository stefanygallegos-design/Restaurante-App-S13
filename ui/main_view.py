import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(
        self,
        ventana,
        servicio,
        usuario_actual,
        cerrar_sesion
    ):

        self.ventana = ventana
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.cerrar_sesion = cerrar_sesion

        self.crear_interfaz()

    def crear_interfaz(self):

        self.frame = ttk.Frame(
            self.ventana,
            padding=20
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        titulo = ttk.Label(
            self.frame,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=10)

        bienvenida = ttk.Label(
            self.frame,
            text=f"Bienvenido, {self.usuario_actual.nombre}"
        )

        bienvenida.pack(pady=5)

        menu_frame = ttk.Frame(
            self.frame
        )

        menu_frame.pack(pady=15)

        ttk.Button(
            menu_frame,
            text="Ver productos",
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            menu_frame,
            text="Ver usuarios",
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            menu_frame,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).grid(row=0, column=2, padx=5)

        self.contenido = ttk.Frame(
            self.frame
        )

        self.contenido.pack(
            fill="both",
            expand=True,
            pady=15
        )

        self.mostrar_inicio()

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Seleccione una opción del menú",
            font=("Arial", 14)
        ).pack(pady=30)

    def mostrar_productos(self):

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="PRODUCTOS REGISTRADOS",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tabla = ttk.Treeview(
            self.contenido,
            columns=(
                "id",
                "nombre",
                "descripcion",
                "precio",
                "categoria"
            ),
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("descripcion", text="Descripción")
        tabla.heading("precio", text="Precio")
        tabla.heading("categoria", text="Categoría")

        tabla.column("id", width=50)
        tabla.column("nombre", width=150)
        tabla.column("descripcion", width=250)
        tabla.column("precio", width=80)
        tabla.column("categoria", width=130)

        productos = self.servicio.listar_productos()

        for producto in productos:

            tabla.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    producto.descripcion,
                    f"${producto.precio:.2f}",
                    producto.categoria
                )
            )

        tabla.pack(
            fill="both",
            expand=True
        )

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="USUARIOS REGISTRADOS",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tabla = ttk.Treeview(
            self.contenido,
            columns=(
                "id",
                "nombre",
                "usuario"
            ),
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("usuario", text="Usuario")

        tabla.column("id", width=50)
        tabla.column("nombre", width=200)
        tabla.column("usuario", width=150)

        usuarios = self.servicio.listar_usuarios()

        for usuario in usuarios:

            tabla.insert(
                "",
                "end",
                values=(
                    usuario.id,
                    usuario.nombre,
                    usuario.usuario
                )
            )

        tabla.pack(
            fill="both",
            expand=True
        )
