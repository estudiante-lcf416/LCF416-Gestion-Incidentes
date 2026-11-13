import unittest

from modelos.incidente import Incidente
from servicios.gestor_incidentes import GestorIncidentes


class TestPriorizacion(unittest.TestCase):

    def test_T01_orden_por_gravedad(self):
        gestor = GestorIncidentes()

        i1 = Incidente(201, "Correo", "Media")
        i2 = Incidente(202, "Malware", "Critica")
        i3 = Incidente(203, "Acceso", "Alta")

        gestor.agregar(i1)
        gestor.agregar(i2)
        gestor.agregar(i3)

        resultado = gestor.pendientes_priorizados()

        self.assertEqual(resultado, [i2, i3, i1])

    def test_T02_excluir_cerrados(self):
        gestor = GestorIncidentes()

        i1 = Incidente(204, "Correo", "Alta")
        i2 = Incidente(205, "Malware", "Critica")

        gestor.agregar(i1)
        gestor.agregar(i2)

        i2.cerrar()

        resultado = gestor.pendientes_priorizados()

        self.assertEqual(resultado, [i1])

    def test_T03_lista_vacia(self):
        gestor = GestorIncidentes()

        resultado = gestor.pendientes_priorizados()

        self.assertEqual(resultado, [])

    def test_T04_conservar_orden_de_empates(self):
        gestor = GestorIncidentes()

        i1 = Incidente(206, "Correo", "Alta")
        i2 = Incidente(207, "Malware", "Alta")

        gestor.agregar(i1)
        gestor.agregar(i2)

        resultado = gestor.pendientes_priorizados()

        self.assertEqual(resultado, [i1, i2])

    def test_T05_no_modificar_lista_original(self):
        gestor = GestorIncidentes()

        i1 = Incidente(208, "Correo", "Media")
        i2 = Incidente(209, "Malware", "Critica")

        gestor.agregar(i1)
        gestor.agregar(i2)

        original = gestor.incidentes.copy()
        estados = [i.estado for i in original]

        gestor.pendientes_priorizados()

        self.assertEqual(gestor.incidentes, original)
        self.assertEqual([i.estado for i in original], estados)

    def test_T06_rechazar_gravedad_invalida(self):
        with self.assertRaises(ValueError):
            Incidente(210, "Prueba", "Urgente")


if __name__ == "__main__":
    unittest.main()