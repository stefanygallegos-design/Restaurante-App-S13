import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(self, ventana, servicio, mostrar_principal):

        self.ventana = ventana
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.crear_interfaz()

    def crear_interfaz(self):

        self.frame = ttk.Frame(
            self.ventana,
            padding=30
        )

        self.frame.pack(
            expand=True
        )

        titulo = ttk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=15)

        subtitulo = ttk.Label(
            self.frame,
            text="Sistema de gestión de restaurante"
        )

        subtitulo.pack(pady=5)

        ttk.Label(
            self.frame,
            text="Usuario:"
        ).pack(anchor="w", pady=(15, 5))

        self.usuario_entry = ttk.Entry(
            self.frame,
            width=35
        )

        self.usuario_entry.pack(pady=5)

        ttk.Label(
            self.frame,
            text="Contraseña:"
        ).pack(anchor="w", pady=(10, 5))

        self.contrasena_entry = ttk.Entry(
            self.frame,
            width=35,
            show="*"
        )

        self.contrasena_entry.pack(pady=5)

        self.boton_ingresar = ttk.Button(
            self.frame,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )

        self.boton_ingresar.pack(pady=20)

        self.ventana.bind(
            "<Return>",
            lambda evento: self.iniciar_sesion()
        )

    def iniciar_sesion(self):

        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:

            messagebox.showwarning(
                "Campos vacíos",
                "Por favor, ingrese usuario y contraseña."
            )

            return

        usuario_validado = self.servicio.validar_acceso(
            usuario,
            contrasena
        )

        if usuario_validado:

            messagebox.showinfo(
                "Acceso correcto",
                f"Bienvenido, {usuario_validado.nombre}"
            )

            self.frame.destroy()

            self.mostrar_principal(usuario_validado)

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )
