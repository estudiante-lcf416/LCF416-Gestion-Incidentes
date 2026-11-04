import unittest
from modelos.incidente import Incidente
from modelos.incidente_malware import IncidenteMalware
from modelos.incidente_acceso import IncidenteAcceso
from servicios.gestor_incidentes import GestorIncidentes
from io import StringIO
from contextlib import redirect_stdout


class TestIncidentes(unittest.TestCase):

    def test_T01_malware(self):
        incidente = IncidenteMalware(
            101, "Equipo infectado", "Alta", "Troyano"
        )
        self.assertIn("Troyano", incidente.generar_reporte())

    def test_T02_acceso(self):
        incidente = IncidenteAcceso(
            102, "Acceso sospechoso", "Media", "usuario01", 5
        )
        reporte = incidente.generar_reporte()
        self.assertIn("usuario01", reporte)
        self.assertIn("5", reporte)

    def test_T03_polimorfismo(self):
        gestor = GestorIncidentes()
        gestor.agregar(Incidente(103, "Correo sospechoso", "Alta"))
        gestor.agregar(
            IncidenteMalware(104, "Virus", "Critica", "Gusano")
        )
        gestor.agregar(
            IncidenteAcceso(105, "Acceso", "Media", "usuario02", 3)
        )

        salida = StringIO()
        with redirect_stdout(salida):
            gestor.generar_reportes()

        self.assertIn("Gusano", salida.getvalue())
        self.assertIn("usuario02", salida.getvalue())

    def test_T04_validacion(self):
        incidente = Incidente(106, "Prueba", "Baja")
        with self.assertRaises(ValueError):
            incidente.gravedad = "Urgente"

    def test_T05_estados(self):
        incidente = Incidente(107, "Prueba", "Media")
        incidente.cerrar()
        self.assertEqual(incidente.estado, "Cerrado")
        incidente.reabrir()
        self.assertEqual(incidente.estado, "Abierto")

    def test_T06_id_duplicado(self):
        gestor = GestorIncidentes()
        incidente = Incidente(108, "Prueba", "Alta")
        gestor.agregar(incidente)
        resultado = gestor.agregar(incidente)
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()