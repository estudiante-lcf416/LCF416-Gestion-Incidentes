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