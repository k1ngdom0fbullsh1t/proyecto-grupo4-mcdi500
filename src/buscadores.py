"""
src/buscadores.py

Implementación de algoritmos de búsqueda mediante Programación
Orientada a Objetos.

Contiene una clase abstracta que define el contrato común
y dos implementaciones concretas:
    - BuscadorLineal
    - BuscadorBinario

Proyecto: Breast Cancer Wisconsin Diagnostic
MCDI500 - Programación para la Ciencia de Datos
"""

from abc import ABC, abstractmethod


class Buscador(ABC):
    """
    Clase abstracta que define el contrato común para todos
    los algoritmos de búsqueda.

    Permite aplicar polimorfismo: cualquier buscador debe
    implementar el método buscar().
    """

    def __init__(self, datos):
        self._datos = datos

    @abstractmethod
    def buscar(self, objetivo):
        """
        Busca un elemento dentro de la colección.

        Parámetros:
            objetivo: valor a buscar.

        Retorna:
            int: índice encontrado o -1.
        """
        pass


class BuscadorLineal(Buscador):
    """
    Implementa búsqueda secuencial.

    Complejidad temporal:
        O(n)

    Complejidad espacial:
        O(1)
    """

    def buscar(self, objetivo):

        for indice, valor in enumerate(self._datos):
            if valor == objetivo:
                return indice

        return -1


class BuscadorBinario(Buscador):
    """
    Implementa búsqueda binaria recursiva.

    Requiere datos ordenados.

    Complejidad temporal:
        O(log n)

    Complejidad espacial:
        O(log n)
    """

    def __init__(self, datos):
        super().__init__(sorted(datos))

    def buscar(self, objetivo):
        return self._buscar_recursivo(
            objetivo,
            0,
            len(self._datos) - 1
        )

    def _buscar_recursivo(self, objetivo, inicio, fin):

        if inicio > fin:
            return -1

        medio = (inicio + fin) // 2

        if self._datos[medio] == objetivo:
            return medio

        if objetivo < self._datos[medio]:
            return self._buscar_recursivo(
                objetivo,
                inicio,
                medio - 1
            )

        return self._buscar_recursivo(
            objetivo,
            medio + 1,
            fin
        )