class Notificador:
    def enviar(self, incidente):
        print(
            f"Notificación: incidente {incidente.id} "
            f"=> {incidente.estado}"
        )