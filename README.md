# Procesador DICOM en Python

## Integrantes

- Luz Adriana Doria Sanchez 
- grupo 001 

# Procesador de Imágenes Médicas DICOM

## 1. Descripción del Proyecto
Este repositorio contiene una herramienta en Python diseñada para la lectura, preprocesamiento y análisis de imágenes médicas en formato DICOM. El sistema permite extraer metadatos clínicos estructurados y aplicar algoritmos de procesamiento digital de imágenes (PDI) para optimizar la visualización de estructuras anatómicas, facilitando el análisis de datos biomédicos.

## 2. Interoperabilidad en Salud: DICOM vs. HL7
Ambos estándares son los pilares de la informática médica, permitiendo que sistemas de diferentes fabricantes intercambien información sin fricciones.

* **DICOM (Digital Imaging and Communications in Medicine):** Especializado en **imágenes médicas y datos asociados**. Modela e integra en un solo archivo (.dcm) tanto el píxel de la imagen (rayos X, tomografías) como los metadatos del paciente y del estudio.
* **HL7 (Health Level Seven):** Especializado en el **intercambio de datos clínicos y administrativos** (texto/mensajes). Gestiona admisiones, altas, historias clínicas electrónicas (HCE) y órdenes de laboratorio.
* **Diferencia Conceptual:** DICOM maneja el *contenido diagnóstico visual* y su contexto, mientras que HL7 gestiona el *flujo de información clínica y operativa* a nivel hospitalario.

## 3. Análisis de Algoritmos PDI en Escenarios Clínicos

### 3.1. Ecualización de Histograma
* **Ventajas:** Maximiza el contraste global de la imagen distribuyendo las intensidades de píxeles uniformemente. Revela detalles ocultos en zonas muy oscuras o quemadas.
* **Limitaciones:** Puede saturar el fondo, amplificar el ruido de fondo y alterar los valores reales de las unidades Hounsfield (HU) en tomografías.
* **Escenarios Clínicos:** 
  * *Útil:* En radiografías de tórax o mamografías donde el contraste entre tejidos blandos y densos es muy bajo.
  * *Perjudicial:* En segmentación cuantitativa de tumores, ya que la alteración de los niveles de gris falsea la densidad real del tejido.

### 3.2. Detección de Bordes con Canny
* **Ventajas:** Identifica discontinuidades abruptas de intensidad con alta precisión y reducción de ruido gracias a su filtro gaussiano integrado.
* **Limitaciones:** Sensible a texturas complejas; puede generar bordes falsos o fragmentados en estructuras anatómicas irregulares.
* **Escenarios Clínicos:**
  * *Útil:* Preprocesamiento para la detección automática de fracturas óseas o delineación del contorno cortical en tomografías craneales.
  * *Perjudicial:* En resonancias magnéticas de cerebro, donde las transiciones suaves entre materia gris y blanca confunden al algoritmo, generando ruido visual.


## 4. Discusión

### 4.1. Dificultades Encontradas
Durante el desarrollo se identificaron los siguientes retos técnicos:
1. **Gestión de Entornos Aislados:** Restricciones de seguridad del sistema operativo al instalar dependencias globales con gestores modernos como `uv`. Se solucionó mediante la abstracción del entorno en un entorno virtual (`.venv`) y la flexibilización temporal de las políticas de ejecución de PowerShell.
2. **Control de Dependencias:** La fragmentación y el orden estricto de importación de librerías científicas (`pydicom`, `opencv-python`, `pandas`, `numpy`).

### 4.2. Importancia de las Herramientas de Python en el Análisis Médico
Python se ha consolidado como el estándar de la industria biomédica debido a su ecosistema robusto:
* **`pydicom`:** Permite la abstracción y parseo nativo de la compleja estructura de archivos médicos sin perder la integridad de los metadatos protegidos.
* **`opencv` y `numpy`:** Permiten tratar las matrices de los píxeles médicos con operaciones vectorizadas de alta velocidad, crucial para el procesamiento en tiempo real.
* **`pandas`:** Facilita la estructuración de los metadatos extraídos de múltiples pacientes en DataFrames para su posterior análisis estadístico o entrenamiento de modelos de IA.