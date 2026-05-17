import os
import cv2
import numpy as np
import pandas as pd
import pydicom


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
