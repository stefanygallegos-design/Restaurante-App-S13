class Usuario:
    def __init__(self, id, nombre, usuario, contrasena):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena

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
            raise ValueError("El nombre es obligatorio")
        self._nombre = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El usuario es obligatorio")
        self._usuario = valor

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor):
        if not valor:
            raise ValueError("La contraseña es obligatoria")
        self._contrasena = valor

    def __str__(self):
        return f"{self.nombre} ({self.usuario})"
