"""
src/base.py
Contrato base del sistema de transformacion por etapas.

Define la clase abstracta Transformador que todas las etapas del pipeline
deben implementar. Garantiza una interfaz comun para que Pipeline pueda
orquestar etapas sin conocer su implementacion concreta (polimorfismo).
"""
from abc import ABC, abstractmethod


class Transformador(ABC):
    """
    Contrato comun para todas las etapas del pipeline de transformacion.

    Toda subclase debe implementar aplicar(df) -> pd.DataFrame.
    Esto permite que Pipeline las trate de forma uniforme sin importar
    si la etapa imputa, escala, codifica o realiza cualquier otra operacion.
    """

    @abstractmethod
    def aplicar(self, df):
        """
        Aplica la transformacion sobre el DataFrame recibido.

        Parametros:
            df (pd.DataFrame): dataset de entrada.

        Retorna:
            pd.DataFrame: dataset con la transformacion aplicada.
        """
        ...
