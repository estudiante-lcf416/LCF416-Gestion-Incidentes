# Clase 11: Ciclo de vida del software

## Etapas del ciclo de vida

1. Análisis: identificar el problema y las necesidades.
2. Requisitos: establecer las funciones que debe cumplir el sistema.
3. Diseño: definir las clases y los métodos necesarios.
4. Implementación: programar la solución en Python.
5. Pruebas: comprobar que el sistema funcione correctamente.
6. Entrega: preparar los archivos y la documentación.
7. Mantenimiento: corregir errores y realizar mejoras.

## Modelo seleccionado

Se seleccionó el modelo iterativo porque permite desarrollar el sistema por etapas, probar cada modificación y realizar mejoras conforme se identifican nuevas necesidades.

## Riesgos identificados

- Errores al ordenar los incidentes.
- Mostrar incidentes que ya están cerrados.
- Modificar accidentalmente la lista original.
- No conservar el orden de los incidentes con la misma gravedad.

## Solución propuesta

Se utiliza la función `sorted()` de Python para obtener una nueva lista ordenada por gravedad. De esta manera, se conserva la lista original y se muestran primero los incidentes críticos, después los altos, medios y bajos.