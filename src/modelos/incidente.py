class Incidente:
    GRAVEDADES_VALIDAS = ["Critica", "Alta", "Media", "Baja"]

    def __init__(self, id, descripcion, gravedad):
        if gravedad not in self.GRAVEDADES_VALIDAS:
            raise ValueError("La gravedad no es válida")

        self.id = id
        self.descripcion = descripcion
        self.gravedad = gravedad
        self.estado = "Abierto"
        self.responsable = None

    def asignar_responsable(self, usuario):
        self.responsable = usuario

    def cerrar(self):
        self.estado = "Cerrado"

    def resumen(self):
        nombre = (
            self.responsable.nombre
            if self.responsable else "Sin asignar"
        )
        return (
            f"Incidente {self.id}: {self.descripcion} | "
            f"Gravedad: {self.gravedad} | "
            f"Estado: {self.estado} | Responsable: {nombre}"
        )