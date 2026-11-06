class Incidente:
    def __init__(self, id, descripcion, gravedad):
        self.id = id
        self.descripcion = descripcion
        self.gravedad = gravedad
        self._estado = "Abierto"

    @property
    def gravedad(self):
        return self._gravedad

    @gravedad.setter
    def gravedad(self, valor):
        if valor not in ["Baja", "Media", "Alta", "Critica"]:
            raise ValueError("Gravedad no permitida")
        self._gravedad = valor

    @property
    def estado(self):
        return self._estado

    def cerrar(self):
        self._estado = "Cerrado"

    def reabrir(self):
        self._estado = "Abierto"
        self.responsable = None

    def asignar_responsable(self, usuario):
        self.responsable = usuario

    def generar_reporte(self):
        return (
            f"Incidente {self.id}: {self.descripcion} | "
            f"Gravedad: {self.gravedad} | Estado: {self.estado}"
        )

    def resumen(self):
        return self.generar_reporte()
    