class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def resumen(self):
        return f"Usuario {self.id}: {self.nombre}"


class Incidente:
    def __init__(self, id, descripcion, gravedad):
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


class Notificador:
    def enviar(self, incidente):
        print(
            f"Notificación: incidente {incidente.id} "
            f"=> {incidente.estado}"
        )


class GestorIncidentes:
    def cerrar_incidente(self, incidente, notificador):
        incidente.cerrar()
        notificador.enviar(incidente)


# Crear dos usuarios
usuario1 = Usuario(1, "Ana Torres")
usuario2 = Usuario(2, "Luis Pérez")

# Crear tres incidentes
incidente1 = Incidente(
    101, "Intento de phishing", "Alta"
)
incidente2 = Incidente(
    102, "Malware detectado", "Media"
)
incidente3 = Incidente(
    103, "Acceso no autorizado", "Crítica"
)

# Asignar responsables
incidente1.asignar_responsable(usuario1)
incidente2.asignar_responsable(usuario2)
incidente3.asignar_responsable(usuario1)

# Mostrar información inicial
print("=== USUARIOS ===")
print(usuario1.resumen())
print(usuario2.resumen())

print("\n=== INCIDENTES ===")
print(incidente1.resumen())
print(incidente2.resumen())
print(incidente3.resumen())

# Cerrar un incidente usando el gestor y el notificador
gestor = GestorIncidentes()
notificador = Notificador()

print("\n=== CIERRE DE INCIDENTE ===")
gestor.cerrar_incidente(incidente1, notificador)

print("\n=== ESTADO FINAL ===")
print(incidente1.resumen())