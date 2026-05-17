import pydicom

import os
import cv2
import numpy as np
import pandas as pd


class ProcesadorDICOM:

    def __init__(self, directorio_entrada, directorio_salida):
        self.directorio_entrada = directorio_entrada
        self.directorio_salida = directorio_salida
        self.metadatos = []

        os.makedirs(self.directorio_salida, exist_ok=True)

    def cargar_dicoms(self):

        archivos_dicom = []

        for root, _, files in os.walk(self.directorio_entrada):

                for file in files:

                    ruta = os.path.join(root, file)

                    try:
                        ds = pydicom.dcmread(ruta)
                        archivos_dicom.append((ruta, ds))

                    except Exception as e:
                        print(f"[ERROR] Archivo no válido: {ruta}")
                        print(e)

        return archivos_dicom

    def extraer_metadatos(self, ds, ruta_archivo):

        datos = {

                "Archivo": os.path.basename(ruta_archivo),

                "PatientID":
                    getattr(ds, "PatientID", "No disponible"),

                "PatientName":
                    str(getattr(ds, "PatientName", "No disponible")),

                "StudyInstanceUID":
                    getattr(ds, "StudyInstanceUID", "No disponible"),

                "StudyDescription":
                    getattr(ds, "StudyDescription", "No disponible"),

                "StudyDate":
                    getattr(ds, "StudyDate", "No disponible"),

                "Modality":
                    getattr(ds, "Modality", "No disponible"),

                "Rows":
                    getattr(ds, "Rows", None),

                "Columns":
                    getattr(ds, "Columns", None),

                "IntensidadPromedio":
                    None
            }
        
        return datos
    
    def procesar_imagen(self, ds, identificador):
        
        try:

            imagen = ds.pixel_array

            intensidad_promedio = np.mean(imagen)

            imagen_normalizada = cv2.normalize(
                imagen,
                None,
                0,
                255,
                cv2.NORM_MINMAX
            ).astype(np.uint8)

            imagen_ecualizada = cv2.equalizeHist(
                imagen_normalizada
            )
            bordes = cv2.Canny(
                imagen_ecualizada,
                50,
                150
            )

            ruta_ecualizada = os.path.join(
                self.directorio_salida,
                f"{identificador}_ecualizada.png"
            )

            ruta_bordes = os.path.join(
                self.directorio_salida,
                f"{identificador}_bordes.png"
            )

            cv2.imwrite(
                ruta_ecualizada,
                imagen_ecualizada
            )

            cv2.imwrite(
                ruta_bordes,
                bordes
            )

            return intensidad_promedio

        except Exception as e:

            print(f"[WARNING] No se pudo procesar: {identificador}")
            print(e)

            return None
        
    def ejecutar(self):

        archivos = self.cargar_dicoms()

        for ruta, ds in archivos:

            datos = self.extraer_metadatos(ds, ruta)

            identificador = datos["StudyInstanceUID"]

            intensidad = self.procesar_imagen(
                ds,
                identificador
            )

            datos["IntensidadPromedio"] = intensidad

            self.metadatos.append(datos)

        df = pd.DataFrame(self.metadatos)

        return df
