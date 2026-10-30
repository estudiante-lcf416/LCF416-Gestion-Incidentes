from modelos.usuario import Usuario
from modelos.incidente import Incidente
from servicios.notificador import Notificador


from servicios.gestor_incidentes import GestorIncidentes


class GestorIncidentesAnterior:
    def cerrar_incidente(self, incidente, notificador):
        incidente.cerrar()
        notificador.enviar(incidente)


usuario1 = Usuario(1, "Ana Torres")
usuario2 = Usuario(2, "Luis Pérez")

incidente1 = Incidente(101, "Phishing", "Alta")
incidente2 = Incidente(102, "Malware", "Media")
incidente3 = Incidente(103, "Acceso no autorizado", "Critica")

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

gestor.agregar(incidente1)
gestor.agregar(incidente2)
gestor.agregar(incidente3)

incidente4 = Incidente(104, "Robo de credenciales", "Baja")
incidente5 = Incidente(105, "Ataque de ransomware", "Critica")
incidente6 = Incidente(106, "Intento de acceso sospechoso", "Alta")

gestor.agregar(incidente4)
gestor.agregar(incidente5)
gestor.agregar(incidente6)

print("\n--- Conteo por gravedad ---")
gestor.contar_por_gravedad()

print("\n--- Prueba de eliminación ---")
gestor.quitar(102)

print("\n--- Incidentes después de eliminar ---")
for incidente in gestor.listar():
    print(incidente.resumen())

print("\n--- Prueba de ID duplicado ---")
incidente_duplicado = Incidente(101, "Intento duplicado", "Baja")
gestor.agregar(incidente_duplicado)

print("\n--- Cierre de incidente ---")
gestor.cerrar_incidente(incidente1, notificador)

print("\n--- Resumen final ---")
print(incidente1.resumen())
print(incidente2.resumen())
print(incidente3.resumen())