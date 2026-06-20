# Changelog — PROYECTO-GRUPO4-MCDI500

## [F1] Definición del problema y entorno — 06/06/2026 – 07/06/2026

| Fecha | Descripción | Commit | Autor | Justificación técnica |
|-------|-------------|--------|-------|-----------------------|
| 06/06/2026 | Inicialización estructura base del proyecto | `900de61` | Marcelo Corro | Establece la arquitectura de directorios, .gitignore y requirements.txt para garantizar reproducibilidad desde el inicio. |
| 06/06/2026 | Notebook F1_Definicion.ipynb con carga del dataset y formulación de la pregunta central | `d0fb6f1` | Marcelo Corro | Primera evidencia ejecutable: carga de wdbc.data, exploración inicial y definición de la variable objetivo (diagnostico). |
| 07/06/2026 | Agrega wdbc.data y wdbc.names al repositorio | `589b912` | Marcelo Corro | El dataset debe estar versionado para que todos los integrantes trabajen con la misma fuente sin depender de descargas externas. |

## [F2] Preprocesamiento y transformación — 07/06/2026 – 10/06/2026

| Fecha | Descripción | Commit | Autor | Justificación técnica |
|-------|-------------|--------|-------|-----------------------|
| 07/06/2026 | Notebook F2 con pipeline completo de preprocesamiento | `d049c3d` | Marcelo Corro | Implementa limpieza, imputación por mediana, codificación B→0/M→1 y estandarización con StandardScaler, generando wdbc_procesado.csv. |
| 08/06/2026 | Verificación de casos límite y excepciones en F2 | `5263a31` | Marcelo Corro | Agrega validaciones automáticas (asserts) para garantizar integridad del dataset procesado antes de usarlo en fases posteriores. |
| 09/06/2026 | EDA complementario: heatmap de correlación y boxplot por diagnóstico | `850dd9b` | Carolina Cortés | Enriquece el análisis exploratorio con visualizaciones bivariadas que evidencian relaciones entre variables morfológicas y el diagnóstico. |
| 09/06/2026 | Script automatizado de descarga del dataset | `07fb003` | Pedro Espinoza | Agrega descarga_datos.py para automatizar la obtención del dataset desde UCI, mejorando la reproducibilidad del entorno. |
| 10/06/2026 | Restaurar wdbc.data y wdbc.names tras error de .gitignore | `4b34167` | Marcelo Corro | Se corrigió una configuración incorrecta que excluía los archivos raw del repo, lo que impedía la reproducibilidad del proyecto. |

## [F3] Núcleo algorítmico y POO — 11/06/2026 – 18/06/2026

| Fecha | Descripción | Commit | Autor | Justificación técnica |
|-------|-------------|--------|-------|-----------------------|
| 11/06/2026 | Implementar búsqueda binaria recursiva y análisis Big O | `b7cf4ed` | Pedro Espinoza | Primera versión del núcleo algorítmico: O(log n) recursivo sobre dataset ordenado, con análisis formal de complejidad temporal y espacial. |
| 12/06/2026 | Implementar búsqueda lineal iterativa y filtro de correlación de features | `98f6a5f` | Marcelo Corro | Completa algoritmos.py con O(n) iterativo y filtro O(n²) para identificar pares de variables con alta correlación (umbral 0.8). |
| 14/06/2026 | Actualizar README con tabla de algoritmos y análisis de complejidad | `6a7f584` | Pedro Espinoza | Documenta formalmente los algoritmos implementados y su complejidad, mejorando la trazabilidad del proyecto. |
| 15/06/2026 | Agregar validación técnica y benchmark timeit 500 repeticiones | `d18159c` | Marcelo Corro | Mide el rendimiento de ambos algoritmos con métodos formales y reproducibles, permitiendo comparación empírica de eficiencia. |
| 15/06/2026 | Agregar introducción, preprocesamiento y referencia al notebook F3 | `52d1288` | Carolina Cortés | Integra portada, contexto, carga de datos desde wdbc_procesado.csv y conexión con F1/F2 al notebook. |
| 16/06/2026 | Agregar clase abstracta Transformador y Preprocesador con pipeline encadenado | `bb961c0` | Marcelo Corro | Refactorización del pipeline funcional de F2 a POO: encapsulamiento en Preprocesador con métodos encadenables y Transformador como contrato abstracto. |
| 17/06/2026 | Implementar Pipeline orientado a objetos y corregir imports | `6887e20` | Pedro Espinoza | Agrega clase Pipeline que orquesta transformadores mediante polimorfismo; corrige imports relativos para compatibilidad con sys.path del notebook. |
| 17/06/2026 | Implementar BuscadorLineal y BuscadorBinario con herencia y polimorfismo | `ee9774a` | Carolina Cortés | Encapsula los algoritmos de búsqueda en clases concretas que heredan de Buscador(ABC), con interfaz buscar(objetivo) unificada. |
| 17/06/2026 | Corregir imports y rutas en transformadores, pipeline y notebook POO | `d011704` | Marcelo Corro | Resuelve incompatibilidades de imports relativos entre src/ y el notebook para que el pipeline POO ejecute sin errores. |
| 17/06/2026 | Integrar buscadores POO en notebook F3 | `054c741` | Marcelo Corro | Consolida en el notebook la demostración completa de POO: Transformadores, Pipeline, BuscadorLineal y BuscadorBinario sobre datos reales. |
| 18/06/2026 | Integrar sección Juan Pablo y markdowns explicativos en notebook F3 | `9d27c9c` | Marcelo Corro | Incorpora validación OOP con dataset real y comparación timeit 5000 repeticiones funcional vs POO. |
| 18/06/2026 | Corrección en la sección de comparación de eficiencia | `6d9da27` | Juan Pablo Valdebenito | Ajuste en la celda de comparación de resultados funcional vs POO para mejorar precisión del análisis. |
| 18/06/2026 | Reescribir interpretación de resultados funcional vs POO | `2527f25` | Marcelo Corro | La versión funcional es más rápida que la POO por ausencia de overhead de instanciación, evidenciado con timeit de mayor precisión. |
| 18/06/2026 | Correcciones mínimas a notebooks tras revisión de funcionamiento | `1979a96` | Carolina Cortés | Revisión final de consistencia y corrección de detalles menores antes del cierre de F3. |
| 18/06/2026 | Merge a main: notebook completo, buscadores y README | `5e42a5f` | Marcelo Corro | Cierre de F3: versión estable mergeada a main con todos los módulos src/ funcionando y notebook ejecutable sin errores. |

## [F4] Visualizaciones y comunicación — 19/06/2026

| Fecha | Descripción | Commit | Autor | Justificación técnica |
|-------|-------------|--------|-------|-----------------------|
| 19/06/2026 | Notebook F4: portada, setup, resúmenes F1–F3 y validación del dataset | `74892fb` | Marcelo Corro | Estructura inicial del notebook de cierre: consolida el hilo conductor F1–F4 y valida que wdbc_procesado.csv está listo para visualizar. |
