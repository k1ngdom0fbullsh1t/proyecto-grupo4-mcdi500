# src/algoritmos.py
import numpy as np


def busqueda_lineal_iterativa(arreglo, objetivo):
    """
    Busqueda lineal iterativa sobre un arreglo ordenado o no ordenado.
    Recorre cada elemento secuencialmente hasta encontrar el objetivo.

    Complejidad Temporal: O(n) — recorre hasta n elementos en el peor caso.
    Complejidad Espacial: O(1) — solo usa una variable de indice.

    Parametros:
        arreglo (array-like): arreglo de valores numericos.
        objetivo (float): valor a buscar.

    Retorna:
        int: indice de la primera coincidencia, o -1 si no se encuentra.
    """
    # Revisamos elemnto por elemento hasta encontrar el valor buscadoque buscamos
    for i in range(len(arreglo)):
        if arreglo[i] == objetivo:
            return i

    # Ojo, si llegamos hasta acá significa que el valor no se encontró
    return -1


def busqueda_binaria_recursiva(arreglo_ordenado, objetivo, inicio, fin):
    """
    Busqueda binaria recursiva (Divide and Conquer) sobre un arreglo ordenado.
    Descarta la mitad del espacio de busqueda en cada llamada recursiva.

    Complejidad Temporal: O(log n) — divide el problema a la mitad en cada paso.
    Complejidad Espacial: O(log n) — pila de llamadas recursivas.

    Parametros:
        arreglo_ordenado (array-like): arreglo de valores numericos ordenados.
        objetivo (float): valor a buscar.
        inicio (int): indice inicial del segmento a buscar.
        fin (int): indice final del segmento a buscar.

    Retorna:
        int: indice de la coincidencia, o -1 si no se encuentra.
    """
    if inicio > fin:
        return -1

    # Calculamos el punto medio para dividir el problema en dos partes
    medio = (inicio + fin) // 2

    if arreglo_ordenado[medio] == objetivo:
        return medio
    elif arreglo_ordenado[medio] > objetivo:
        return busqueda_binaria_recursiva(arreglo_ordenado, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria_recursiva(arreglo_ordenado, objetivo, medio + 1, fin)


def filtro_estructurado_features(df, umbral_correlacion=0.8):
    """
    Algoritmo estructurado iterativo que identifica pares de variables
    morfologicas con correlacion absoluta superior al umbral dado.
    Util para detectar multicolinealidad antes del modelado.

    Complejidad Temporal: O(n^2) donde n es el numero de variables numericas.
    Complejidad Espacial: O(n^2) para almacenar la matriz de correlacion.

    Parametros:
        df (pd.DataFrame): dataset con variables numericas estandarizadas.
        umbral_correlacion (float): correlacion minima absoluta para reportar
                                    un par. Por defecto 0.8.

    Retorna:
        list[tuple]: lista de tuplas (var_a, var_b, correlacion) con los pares
                     que superan el umbral, ordenados de mayor a menor correlacion.
    """
    cols = df.select_dtypes(include='number').columns.tolist()
    if 'diagnostico' in cols:
        cols.remove('diagnostico')

    matriz_corr = df[cols].corr().abs()
    pares_alta_correlacion = []

    # Solo nos interesa la mitad superior para no repetir comparaciones
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            correlacion = matriz_corr.iloc[i, j]
            if correlacion >= umbral_correlacion:
                pares_alta_correlacion.append(
                    (cols[i], cols[j], round(float(correlacion), 4)))

    # Ponemos al inicio las correlaciones más altas para identificarlas más rápido
    pares_alta_correlacion.sort(key=lambda x: x[2], reverse=True)
    return pares_alta_correlacion
