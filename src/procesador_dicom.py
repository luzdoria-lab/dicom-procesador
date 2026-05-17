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
        