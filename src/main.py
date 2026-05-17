import os
from procesador_dicom import ProcesadorDICOM


if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    directorio_entrada = os.path.join(base_dir, "data", "dicom")

    directorio_salida = os.path.join(base_dir, "data", "output")

    print("Buscando DICOM en:")
    print(directorio_entrada)

    procesador = ProcesadorDICOM(
        directorio_entrada,
        directorio_salida
    )

    df = procesador.ejecutar()

    print("\nDATAFRAME:")
    print(df)

    csv_path = os.path.join(
        base_dir,
        "data",
        "metadatos_dicom.csv"
    )

    df.to_csv(
        csv_path,
        index=False
    )

    print("\nCSV generado correctamente.")