# src/transformadores.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from base import Transformador

class EliminadorColumnas(Transformador):
    """
    Clase responsable de eliminar columnas específicas del DataFrame.
    Soporta la verificación de excepciones si las columnas no existen.
    """
    def __init__(self, columnas_a_eliminar: list):
        if not isinstance(columnas_a_eliminar, list):
            raise TypeError("El parámetro 'columnas_a_eliminar' debe ser una lista de strings.")
        self.columnas_a_eliminar = columnas_a_eliminar

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        # Validación de tipo de entrada
        if not isinstance(df, pd.DataFrame):
            raise TypeError("El insumo de entrada debe ser un pd.DataFrame.")
            
        df_copia = df.copy()
        
        # Verificación de caso límite: Filtrar solo las columnas que realmente existen
        existentes = [col for col in self.columnas_a_eliminar if col in df_copia.columns]
        
        if existentes:
            df_copia = df_copia.drop(columns=existentes)
            print(f"[EliminadorColumnas] Columnas eliminadas exitosamente: {existentes}")
        else:
            print("[EliminadorColumnas] Aviso: Ninguna de las columnas especificadas existía en el DataFrame.")
            
        return df_copia


class ImputadorNA(Transformador):
    """
    Clase responsable de gestionar valores faltantes (NA) de forma robusta.
    Imputa las variables numéricas utilizando la mediana calculada.
    """
    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("El insumo de entrada debe ser un pd.DataFrame.")
            
        df_copia = df.copy()
        columnas_num = df_copia.select_dtypes(include=[np.number]).columns
        
        # Almacenar diagnóstico inicial para el reporte de verificación intermedio
        total_nas = df_copia.isnull().sum().sum()
        
        if total_nas > 0:
            for col in columnas_num:
                mediana = df_copia[col].median()
                df_copia[col] = df_copia[col].fillna(mediana)
            print(f"[ImputadorNA] Se imputaron {total_nas} valores nulos utilizando la mediana de cada columna.")
        else:
            print("[ImputadorNA] Caso Límite Detectado: El dataset no presenta valores nulos. No se requiere imputación.")
            
        return df_copia


class CodificadorDiagnostico(Transformador):
    """
    Clase responsable de transformar la variable categórica objetivo 'diagnosis'
    a un formato binario numérico (M -> 1, B -> 0).
    """
    def __init__(self, columna_objetivo: str = 'diagnosis'):
        self.columna_objetivo = columna_objetivo

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("El insumo de entrada debe ser un pd.DataFrame.")
            
        df_copia = df.copy()
        
        # Control de excepciones: Validación de existencia de la columna objetivo
        if self.columna_objetivo not in df_copia.columns:
            raise KeyError(f"Error Crítico: La columna objetivo '{self.columna_objetivo}' no se encuentra en el DataFrame.")
            
        # Verificar si la columna ya fue transformada en ejecuciones previas (Evita errores de re-ejecución)
        if df_copia[self.columna_objetivo].dtype in [np.int64, np.int32, np.float64]:
            print(f"[CodificadorDiagnostico] La columna '{self.columna_objetivo}' ya es numérica. Omitiendo transformación.")
            return df_copia
            
        # Mapeo explícito controlado
        mapeo = {'M': 1, 'B': 0}
        
        # Validar si hay categorías inesperadas en los datos (Caso límite oncológico)
        valores_unicos = set(df_copia[self.columna_objetivo].unique())
        if not valores_unicos.issubset({'M', 'B'}):
            print(f"[CodificadorDiagnostico] Advertencia: Se detectaron categorías anómalas: {valores_unicos - {'M', 'B'}}")

        df_copia[self.columna_objetivo] = df_copia[self.columna_objetivo].map(mapeo).fillna(-1).astype(int)
        print(f"[CodificadorDiagnostico] Columna '{self.columna_objetivo}' codificada correctamente (M=1, B=0).")
        return df_copia


class EscaladorNumerico(Transformador):
    """
    Clase responsable de estandarizar las características morfológicas numéricas
    (media = 0, varianza = 1) excluyendo la variable objetivo ya codificada.
    """
    def __init__(self, columna_excluir: str = 'diagnosis'):
        self.columna_excluir = columna_excluir
        self.scaler = StandardScaler()

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("El insumo de entrada debe ser un pd.DataFrame.")
            
        df_copia = df.copy()
        
        # Seleccionar únicamente columnas numéricas predictoras
        columnas_features = df_copia.select_dtypes(include=[np.number]).columns.tolist()
        if self.columna_excluir in columnas_features:
            columnas_features.remove(self.columna_excluir)
            
        if not columnas_features:
            print("[EscaladorNumerico] Aviso: No se encontraron variables numéricas para escalar.")
            return df_copia
            
        # Aplicar el ajuste y transformación fit_transform
        df_copia[columnas_features] = self.scaler.fit_transform(df_copia[columnas_features])
        print(f"[EscaladorNumerico] Estandarización aplicada con éxito sobre {len(columnas_features)} características morfológicas.")
        return df_copia
