import tkinter as tk
from tkinter import ttk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title(
            "Restaurante App"
        )

        self.ventana.geometry(
            "850x550"
        )

        self.ventana.minsize(
            700,
            450
        )

        self.configurar_estilos()

        self.archivo_servicio = ArchivoServicio()

        self.restaurante_servicio = RestauranteServicio(
            self.archivo_servicio
        )

        self.cargar_datos()

        self.mostrar_login()

    def configurar_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "TButton",
            padding=8
        )

        estilo.configure(
            "TLabel",
            padding=3
        )

    def cargar_datos(self):

        self.restaurante_servicio.cargar_productos(
            "datos/productos.json"
        )

        self.restaurante_servicio.cargar_usuarios(
            "datos/usuarios.json"
        )

    def limpiar_ventana(self):

        for widget in self.ventana.winfo_children():
            widget.destroy()

    def mostrar_login(self):

        self.limpiar_ventana()

        LoginView(
            ventana=self.ventana,
            servicio=self.restaurante_servicio,
            mostrar_principal=self.mostrar_principal
        )

    def mostrar_principal(self, usuario):

        self.limpiar_ventana()

        MainView(
            ventana=self.ventana,
            servicio=self.restaurante_servicio,
            usuario_actual=usuario,
            cerrar_sesion=self.mostrar_login
        )

    def ejecutar(self):

        self.ventana.mainloop()


if __name__ == "__main__":

    app = RestauranteApp()

    app.ejecutar()
