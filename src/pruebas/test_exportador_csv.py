import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.modelos.incidente import Incidente
from src.servicios.gestor_incidentes import GestorIncidentes
from src.exportador_csv import ExportadorCSV


class PruebasExportadorCSV(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorIncidentes()
        self.exportador = ExportadorCSV()

        self.incidentes = [
            Incidente(101, "Phishing", "Alta"),
            Incidente(102, "Malware", "Media"),
            Incidente(103, "Acceso no autorizado", "Critica"),
            Incidente(104, "Actividad sospechosa", "Alta"),
            Incidente(105, "Intento de fraude", "Baja")
        ]

        for incidente in self.incidentes:
            self.gestor.agregar(incidente)

        self.incidentes[1].cerrar()

    def test_01_filtrar_cerrados(self):
        pendientes = self.gestor.pendientes_priorizados()
        self.assertNotIn(102, [i.id for i in pendientes])

    def test_02_prioridad(self):
        pendientes = self.gestor.pendientes_priorizados()
        self.assertEqual(
            [i.id for i in pendientes],
            [103, 101, 104, 105]
        )

    def test_03_orden_estable(self):
        pendientes = self.gestor.pendientes_priorizados()
        self.assertEqual(
            [i.id for i in pendientes if i.gravedad == "Alta"],
            [101, 104]
        )

    def test_04_lista_vacia(self):
        with TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "vacio.csv"
            self.exportador.exportar([], ruta)

            with ruta.open(encoding="utf-8-sig", newline="") as archivo:
                lector = csv.reader(archivo)
                filas = list(lector)

            self.assertEqual(
                filas,
                [["folio", "tipo", "gravedad", "estado"]]
            )

    def test_05_acentos_y_comas(self):
        incidente = Incidente(
            106, "Acceso no autorizado, área crítica", "Alta"
        )

        with TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "acentos.csv"
            self.exportador.exportar([incidente], ruta)

            with ruta.open(encoding="utf-8-sig", newline="") as archivo:
                filas = list(csv.DictReader(archivo))

            self.assertEqual(
                filas[0]["tipo"],
                "Acceso no autorizado, área crítica"
            )

    def test_06_no_modificar_original(self):
        ids_antes = [i.id for i in self.gestor.listar()]
        estados_antes = [i.estado for i in self.gestor.listar()]

        pendientes = self.gestor.pendientes_priorizados()

        with TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "prueba.csv"
            self.exportador.exportar(pendientes, ruta)

        self.assertEqual(
            [i.id for i in self.gestor.listar()],
            ids_antes
        )
        self.assertEqual(
            [i.estado for i in self.gestor.listar()],
            estados_antes
        )


if __name__ == "__main__":
    unittest.main()