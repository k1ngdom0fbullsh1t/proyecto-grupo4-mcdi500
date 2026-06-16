"""
src/preprocesador.py
Encapsula el pipeline de preprocesamiento de la Fase 2 en una clase.

Las funciones limpiar_datos() y transformar_datos() del notebook F2 pasan
a ser metodos de Preprocesador, con el DataFrame como estado interno
protegido (self._df). Los metodos devuelven self para permitir encadenamiento.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler


class Preprocesador:
    """
    Encapsula el pipeline de preprocesamiento construido en la Fase 2.

    Estado interno:
        _df (pd.DataFrame): copia del dataset sobre la que se aplican
                            las transformaciones. Nunca se modifica el
                            DataFrame original recibido en __init__.

    Uso tipico (encadenamiento de metodos):
        df_procesado = (
            Preprocesador(df_raw)
            .eliminar_columnas(['id'])
            .eliminar_duplicados()
            .imputar_na()
            .codificar_diagnostico()
            .estandarizar()
            .validar()
            .resultado()
        )
    """

    def __init__(self, df: pd.DataFrame):
        """
        Inicializa el preprocesador con una copia del dataset original.

        Parametros:
            df (pd.DataFrame): dataset crudo a preprocesar.
        """
        self._df = df.copy()

    # ------------------------------------------------------------------
    # Limpieza (equivale a limpiar_datos() de F2)
    # ------------------------------------------------------------------

    def eliminar_columnas(self, columnas: list):
        """
        Elimina columnas sin valor predictivo (p.ej. 'id').

        Parametros:
            columnas (list): nombres de columnas a eliminar.

        Retorna:
            Preprocesador: self, para encadenamiento.
        """
        self._df = self._df.drop(
            columns=[c for c in columnas if c in self._df.columns]
        )
        return self

    def eliminar_duplicados(self):
        """
        Elimina filas duplicadas si las hubiera.

        Retorna:
            Preprocesador: self, para encadenamiento.
        """
        antes = len(self._df)
        self._df = self._df.drop_duplicates()
        eliminados = antes - len(self._df)
        if eliminados:
            print(f'Duplicados eliminados: {eliminados}')
        return self

    def imputar_na(self, estrategia: str = 'mediana'):
        """
        Imputa valores NA en columnas numericas con mediana o media.

        Se usa mediana por defecto porque es robusta ante outliers,
        que son frecuentes en variables morfologicas del dataset WDBC.

        Parametros:
            estrategia (str): 'mediana' (defecto) o 'media'.

        Retorna:
            Preprocesador: self, para encadenamiento.
        """
        cols_num = self._df.select_dtypes(include='number').columns
        for col in cols_num:
            if self._df[col].isnull().any():
                valor = (
                    self._df[col].median()
                    if estrategia == 'mediana'
                    else self._df[col].mean()
                )
                self._df[col] = self._df[col].fillna(valor)
        return self

    # ------------------------------------------------------------------
    # Transformacion (equivale a transformar_datos() de F2)
    # ------------------------------------------------------------------

    def codificar_diagnostico(self):
        """
        Codifica la variable objetivo: B -> 0, M -> 1.

        Solo se aplica si la columna 'diagnostico' contiene strings.
        Si ya esta codificada (int/float), no hace nada.

        Retorna:
            Preprocesador: self, para encadenamiento.
        """
        if 'diagnostico' in self._df.columns:
            if self._df['diagnostico'].isin(['B', 'M']).any():
                self._df['diagnostico'] = self._df['diagnostico'].map(
                    {'B': 0, 'M': 1}
                )
        return self

    def estandarizar(self):
        """
        Estandariza las variables morfologicas con StandardScaler (z-score).

        Se excluye la columna 'diagnostico' por ser la variable objetivo.
        Resultado: media ~ 0, desviacion estandar ~ 1 por columna.

        Retorna:
            Preprocesador: self, para encadenamiento.
        """
        cols_num = self._df.select_dtypes(include='number').columns.tolist()
        if 'diagnostico' in cols_num:
            cols_num.remove('diagnostico')

        scaler = StandardScaler()
        self._df[cols_num] = scaler.fit_transform(self._df[cols_num])
        return self

    # ------------------------------------------------------------------
    # Validacion (equivale a validar_dataset() de F2)
    # ------------------------------------------------------------------

    def validar(self):
        """
        Verifica la integridad del dataset procesado mediante assertions.

        Comprueba:
            - Sin valores NA.
            - Sin filas duplicadas.
            - Columna 'diagnostico' con solo 0 y 1 (si existe).
            - Variables numericas con media ~ 0 y std ~ 1 (si estandarizadas).

        Retorna:
            Preprocesador: self, para encadenamiento.

        Lanza:
            AssertionError: si alguna condicion de integridad falla.
        """
        assert self._df.isnull().sum().sum() == 0, \
            'Validacion fallida: el dataset contiene valores NA.'

        assert self._df.duplicated().sum() == 0, \
            'Validacion fallida: el dataset contiene filas duplicadas.'

        if 'diagnostico' in self._df.columns:
            valores = set(self._df['diagnostico'].unique())
            assert valores <= {0, 1}, \
                f'Validacion fallida: diagnostico contiene valores inesperados: {valores}'

        print('Validacion OK: sin NA, sin duplicados, diagnostico correcto.')
        return self

    # ------------------------------------------------------------------
    # Acceso al resultado
    # ------------------------------------------------------------------

    def resultado(self) -> pd.DataFrame:
        """
        Devuelve el DataFrame con todas las transformaciones aplicadas.

        Retorna:
            pd.DataFrame: dataset procesado.
        """
        return self._df.copy()
