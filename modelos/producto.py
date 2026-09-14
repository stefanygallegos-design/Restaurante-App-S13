class Producto:
    def __init__(self, id, nombre, descripcion, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto es obligatorio")
        self._nombre = valor

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if float(valor) < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = float(valor)

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"
