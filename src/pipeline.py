# src/pipeline.py (o al final de transformadores.py)
import pandas as pd
from base import Transformador

class Pipeline:
    """
    Clase orquestadora que ejecuta secuencialmente una lista de objetos
    que cumplen con el contrato de la clase base Transformador.
    """
    def __init__(self, pasos: list):
        """
        Inicializa el pipeline con una lista de pasos (transformadores).
        
        Args:
            pasos (list): Lista de instancias de clases que heredan de Transformador.
        """
        # Validación: Asegurarse de que todos los pasos son realmente transformadores
        for i, paso in enumerate(pasos):
            if not isinstance(paso, Transformador):
                raise TypeError(f"El paso en el índice {i} no es una instancia de Transformador. Recibido: {type(paso)}")
        
        self.pasos = pasos

    def ejecutar(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Aplica secuencialmente cada transformación al DataFrame.
        
        Args:
            df (pd.DataFrame): El dataset original a procesar.
            
        Returns:
            pd.DataFrame: El dataset con todas las transformaciones aplicadas.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("La entrada al pipeline debe ser un pandas DataFrame.")
            
        df_actual = df.copy()
        
        print(f"--- Iniciando Pipeline ({len(self.pasos)} pasos) ---")
        
        # El corazón del pipeline: iterar sobre cada transformador
        for i, paso in enumerate(self.pasos, 1):
            nombre_paso = paso.__class__.__name__
            print(f"\\nEjecutando Paso {i}: {nombre_paso}...")
            
            # Polimorfismo en acción: todos los pasos tienen el método 'aplicar'
            df_actual = paso.aplicar(df_actual)
            
        print("\\n--- Pipeline Finalizado con Éxito ---")
        return df_actual
