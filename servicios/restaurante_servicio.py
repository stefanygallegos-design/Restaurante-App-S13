from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio

        self.productos = []
        self.usuarios = []

    def cargar_productos(self, ruta):
        datos = self.archivo_servicio.leer_json(ruta)

        self.productos = [
            Producto(
                id=producto["id"],
                nombre=producto["nombre"],
                descripcion=producto["descripcion"],
                precio=producto["precio"],
                categoria=producto["categoria"]
            )
            for producto in datos
        ]

        return self.productos

    def cargar_usuarios(self, ruta):
        datos = self.archivo_servicio.leer_json(ruta)

        self.usuarios = [
            Usuario(
                id=usuario["id"],
                nombre=usuario["nombre"],
                usuario=usuario["usuario"],
                contrasena=usuario["contrasena"]
            )
            for usuario in datos
        ]

        return self.usuarios

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado

        return None

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios
