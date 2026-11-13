# Clase 11: Análisis y requisitos

## Objetivo
Desarrollar una función para consultar los incidentes pendientes y mostrarlos ordenados según su nivel de gravedad.

## Datos esenciales
- Folio del incidente.
- Descripción.
- Gravedad.
- Estado.
- Responsable.

## Actores
- Operador: consulta los incidentes pendientes.
- Supervisor: revisa la prioridad de los incidentes.
- Administrador: supervisa la gestión del sistema.

## Requisitos funcionales
- RF-01: El sistema debe registrar incidentes.
- RF-02: El sistema debe identificar la gravedad.
- RF-03: El sistema debe mostrar únicamente incidentes abiertos.
- RF-04: El sistema debe ordenar los incidentes por gravedad.

## Requisitos no funcionales
- RNF-01: El sistema debe ser fácil de utilizar.
- RNF-02: El sistema debe conservar los datos originales al ordenar los resultados.

## Alcance
La función de priorización permite consultar los incidentes abiertos ordenados desde gravedad crítica hasta baja, conservando el orden de registro cuando tienen la misma gravedad.