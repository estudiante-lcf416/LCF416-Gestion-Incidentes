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

Clase 9

En esta clase se trabajó la herencia, el polimorfismo y la visibilidad en Python.

Cambios realizados

* Se agregaron las clases IncidenteMalware e IncidenteAcceso.
* Se implementó la herencia mediante super().
* Se utilizó el polimorfismo para generar reportes según el tipo de incidente.
* Se agregaron propiedades y validaciones para controlar la gravedad y el estado.
* Se realizaron pruebas automatizadas.

Clase 10

En esta clase se integraron los temas de la Unidad III al proyecto de Gestión de Incidentes de Ciberseguridad.

Cambios realizados

* Se reforzó la asociación entre Usuario e Incidente mediante la asignación de responsables.
* Se mantuvo la agregación entre GestorIncidentes e Incidente.
* Se implementó la dependencia entre GestorIncidentes y Notificador.
* Se integró la jerarquía de clases mediante IncidenteMalware e IncidenteAcceso.
* Se verificó el funcionamiento del polimorfismo.
* Se ejecutaron seis pruebas automatizadas, todas aprobadas.

Pruebas automatizadas

Para ejecutar las pruebas desde la carpeta principal del proyecto en PowerShell:

$env:PYTHONPATH = "src"
python -m unittest discover -s src/pruebas -p "test_*.py" -v

Resultado: 6 pruebas aprobadas (OK).