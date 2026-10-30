class GestorIncidentes:
    def __init__(self):
        self.incidentes = []

    def agregar(self, incidente):
        for existente in self.incidentes:
            if existente.id == incidente.id:
                print("Error: ya existe un incidente con ese ID.")
                return

        self.incidentes.append(incidente)
        print("Incidente agregado correctamente.")

    def listar(self):
        return self.incidentes

    def contar_por_gravedad(self):
        gravedades = ["Critica", "Alta", "Media", "Baja"]

        for gravedad in gravedades:
            cantidad = 0

            for incidente in self.incidentes:
                if incidente.gravedad == gravedad:
                    cantidad += 1

            print(f"{gravedad}: {cantidad}")

    def quitar(self, id):
        for incidente in self.incidentes:
            if incidente.id == id:
                self.incidentes.remove(incidente)
                print("Incidente eliminado del gestor.")
                return incidente

        print("No se encontró el incidente.")
        return None

    def cerrar_incidente(self, incidente, notificador):
        incidente.cerrar()
        notificador.enviar(incidente)