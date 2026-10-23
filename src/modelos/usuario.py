class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def resumen(self):
        return f"Usuario {self.id}: {self.nombre}"