from modelos.usuario import Usuario
from modelos.incidente import Incidente
from servicios.notificador import Notificador


class GestorIncidentes:
    def cerrar_incidente(self, incidente, notificador):
        incidente.cerrar()
        notificador.enviar(incidente)


usuario1 = Usuario(1, "Ana Torres")
usuario2 = Usuario(2, "Luis Pérez")

incidente1 = Incidente(101, "Phishing", "Alta")
incidente2 = Incidente(102, "Malware", "Media")
incidente3 = Incidente(103, "Acceso no autorizado", "Crítica")

incidente1.asignar_responsable(usuario1)
incidente2.asignar_responsable(usuario2)
incidente3.asignar_responsable(usuario1)

print("--- Usuarios ---")
print(usuario1.resumen())
print(usuario2.resumen())

print("\n--- Incidentes iniciales ---")
print(incidente1.resumen())
print(incidente2.resumen())
print(incidente3.resumen())

gestor = GestorIncidentes()
notificador = Notificador()

print("\n--- Cierre de incidente ---")
gestor.cerrar_incidente(incidente1, notificador)

print("\n--- Resumen final ---")
print(incidente1.resumen())
print(incidente2.resumen())
print(incidente3.resumen())