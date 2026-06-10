# Esta funcionalidad probablemente la usaremos en fases posteriores
import os
import pandas as pd

def descargar_datos_wdbc():
    """
    Descarga el dataset Breast Cancer Wisconsin (Diagnostic) desde el repositorio UCI
    y lo guarda localmente en el directorio data/raw/.
    """
    # URL directa del archivo raw en UCI
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
    
    # Definición de columnas: ID, Diagnosis (M/B), y las 30 características morfológicas
    columnas = ['id', 'diagnosis'] + [f'feature_{i}' for i in range(1, 31)]
    
    # Construir la ruta de destino de forma dinámica para evitar errores de sistema operativo
    ruta_directorio = os.path.join("data", "raw")
    ruta_archivo = os.path.join(ruta_directorio, "wdbc.csv")
    
    # Asegurar que el directorio de destino exista
    os.makedirs(ruta_directorio, exist_ok=True)
    
    try:
        print("Iniciando la descarga del dataset Breast Cancer Wisconsin (Diagnostic)...")
        
        # Leer el dataset desde la web
        df = pd.read_csv(url, header=None, names=columnas)
        
        # Exportar el DataFrame a CSV
        df.to_csv(ruta_archivo, index=False)
        
        print(f"✅ ¡Descarga exitosa! Dataset guardado correctamente en: {ruta_archivo}")
        print(f"Resumen de los datos: {df.shape[0]} registros y {df.shape[1]} columnas obtenidas.")
        
    except Exception as e:
        print(f"❌ Se produjo un error al intentar descargar los datos: {e}")

if __name__ == "__main__":
    descargar_datos_wdbc()