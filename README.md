Gestión de Incidentes de Ciberseguridad

Objetivo

Aplicación académica en Python para practicar programación orientada a objetos.

Clase 7

* Asociación entre Usuario e Incidente.
* Dependencia entre GestorIncidentes y Notificador.
* Uso de Git y GitHub para el control de versiones.

Organización del proyecto

* src/main.py: archivo principal y gestor de incidentes.
* src/modelos/usuario.py: clase Usuario.
* src/modelos/incidente.py: clase Incidente.
* src/servicios/notificador.py: clase Notificador.
* .gitignore: archivos y carpetas que Git debe ignorar.

Ejecución

Para ejecutar el programa, abre una terminal en la carpeta principal del proyecto y utiliza el siguiente comando:

python src/main.py

Funcionalidad

El programa permite registrar usuarios e incidentes, asignar responsables, consultar resúmenes y cerrar un incidente mediante el gestor, que envía una notificación.


Clase 8

En esta clase se trabajó la agregación entre las clases GestorIncidentes e Incidente.

Cambios realizados

* Se agregó la validación de las gravedades de los incidentes.
* Se implementó la clase GestorIncidentes para administrar incidentes.
* Se agregó el control para evitar IDs duplicados.
* Se implementó la eliminación de incidentes.
* Se agregó el conteo de incidentes por gravedad.
* Se realizaron pruebas con seis incidentes ficticios.

Ejecución

Para ejecutar el proyecto desde la terminal:

python src/main.py