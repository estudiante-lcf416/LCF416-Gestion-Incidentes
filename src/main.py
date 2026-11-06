from modelos.incidente import Incidente
from modelos.incidente_malware import IncidenteMalware
from modelos.incidente_acceso import IncidenteAcceso
from servicios.gestor_incidentes import GestorIncidentes
from servicios.notificador import Notificador
from modelos.usuario import Usuario


# Crear el gestor
gestor = GestorIncidentes()

# Crear incidentes de diferentes tipos
incidente1 = Incidente(101, "Correo sospechoso", "Alta")

incidente2 = IncidenteMalware(
    102, "Equipo infectado", "Critica", "Troyano"
)

incidente3 = IncidenteAcceso(
    103, "Intentos de acceso no autorizado",
    "Media", "usuario01", 5
)

usuario1 = Usuario(1, "Ana Torres")
incidente1.asignar_responsable(usuario1)
print("Responsable:", incidente1.responsable.resumen())

# Agregar incidentes al gestor
gestor.agregar(incidente1)
gestor.agregar(incidente2)
gestor.agregar(incidente3)

# Mostrar reportes polimórficos
print("\n--- REPORTES DE INCIDENTES ---")
gestor.generar_reportes()

# Probar cierre y reapertura
print("\n--- ESTADO DEL INCIDENTE ---")
incidente1.cerrar()
print(incidente1.generar_reporte())

incidente1.reabrir()
print(incidente1.generar_reporte())

# Probar validación de gravedad
print("\n--- PRUEBA DE VALIDACIÓN ---")
try:
    incidente1.gravedad = "Urgente"
except ValueError as error:
    print("Error controlado:", error)

# Probar ID duplicado
print("\n--- PRUEBA DE ID DUPLICADO ---")
gestor.agregar(incidente1)

# Probar notificador
print("\n--- NOTIFICACIÓN ---")
notificador = Notificador()
gestor.cerrar_incidente(incidente2, notificador)