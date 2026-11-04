from modelos.incidente import Incidente


class IncidenteAcceso(Incidente):
    def __init__(self, id, descripcion, gravedad, usuario_afectado, intentos_detectados):
        super().__init__(id, descripcion, gravedad)
        self.usuario_afectado = usuario_afectado
        self.intentos_detectados = intentos_detectados

    def generar_reporte(self):
        reporte = super().generar_reporte()
        return f"{reporte} | Usuario afectado: {self.usuario_afectado} | Intentos detectados: {self.intentos_detectados}"