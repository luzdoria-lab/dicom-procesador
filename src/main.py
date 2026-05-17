from procesador_dicom import ProcesadorDICOM


if __name__ == "__main__":

    directorio_entrada = "../data/dicom"
    directorio_salida = "../data/output"

    procesador = ProcesadorDICOM(
        directorio_entrada,
        directorio_salida
    )

    df = procesador.ejecutar()

    print(df)

    df.to_csv(
        "../data/metadatos_dicom.csv",
        index=False
    )

    print("\nCSV generado correctamente.")