import os
import subprocess
import sys


def instalar(paquete):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", paquete]
    )


print("Instalando librerías necesarias...\n")

librerias = [
    "pydicom",
    "numpy",
    "pandas",
    "opencv-python",
    "matplotlib"
]

for lib in librerias:

    try:
        __import__(lib.replace("-", "_"))
        print(f"{lib} ya está instalado.")

    except ImportError:
        print(f"Instalando {lib}...")
        instalar(lib)

print("\nTodo listo.")