class ExportadorCSV:
    CAMPOS = ("folio", "tipo", "gravedad", "estado")

    def construir_filas(self, incidentes):
        return [
            {
                "folio": str(i.id),
                "tipo": i.descripcion,
                "gravedad": i.gravedad,
                "estado": i.estado
            }
            for i in incidentes
        ]

    def exportar(self, incidentes, destino):
        import csv
        from pathlib import Path

        destino = Path(destino)

        with destino.open("w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=self.CAMPOS
            )
            escritor.writeheader()
            escritor.writerows(self.construir_filas(incidentes))

        return destino