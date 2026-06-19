# PROYECTO-GRUPO4-MCDI500

**Curso:** MCDI500 — Programación para la Ciencia de Datos  
**Docente:** Omar Iván Salinas Silva  
**Integrantes:**
- Carolina Cortés Donoso
- Pedro Espinoza Vicentela
- Marcelo Corro Troncoso
- Juan Pablo Valdebenito Loyola

---

## Descripción

Proyecto de clasificación supervisada que busca responder la pregunta:

> ¿Es posible predecir si un tumor mamario es benigno o maligno a partir de características celulares?

Se utiliza el dataset **Breast Cancer Wisconsin (Diagnostic)** (UCI Machine Learning Repository), que contiene 569 registros con 30 variables morfológicas numéricas y una variable objetivo binaria (B = benigno, M = maligno).

---

## Estructura del proyecto

```
proyecto-grupo4-mcdi500/
├─ data/
│   ├─ raw/              # Dataset original sin modificar
│   └─ processed/        # Datos transformados y listos para modelado
├─ notebooks/
│   ├─ f1_definicion/    # Fase 1: definición del problema y configuración del entorno
│   ├─ f2_preprocesamiento/  # Fase 2: limpieza, transformación y EDA
│   └─ f3_modelamiento/  # Fase 3: algoritmos, validación y análisis de complejidad
├─ src/                  # Módulos y funciones reutilizables
├─ docs/                 # Documentación adicional del proyecto
├─ models/               # Reservado para fases posteriores
├─ requirements.txt      # Dependencias del proyecto
├─ .gitignore
└─ README.md
```

---

## Instalación y reproducibilidad

### 1. Clonar el repositorio

```bash
git clone https://github.com/k1ngdom0fbullsh1t/proyecto-grupo4-mcdi500.git
cd proyecto-grupo4-mcdi500
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar Jupyter

```bash
jupyter notebook
```

---

## Fases del proyecto

| Fase | Descripción | Estado |
|------|-------------|--------|
| F1 | Definición del problema y configuración del entorno | Completada |
| F2 | Preprocesamiento, limpieza y transformación del dataset | Completada |
| F3 | Modelamiento, evaluación e interpretación | Completada |

---

## Fase 1 — Definición del problema

**Notebook:** `notebooks/f1_definicion/F1_Definicion.ipynb`

Contenido:
- Contextualización del problema (cáncer de mama, OMS)
- Objetivos general y específicos
- Descripción del dataset (569 instancias, 32 variables)
- Verificación del entorno (versiones de librerías)
- Carga del dataset con columnas en español
- Exploración estructural: función `explorar_dataset()`
- Estadísticas descriptivas
- Visualización de distribución de diagnóstico
- Conclusiones y proyección a F2 y F3

**Para ejecutar:**
```bash
jupyter notebook notebooks/f1_definicion/F1_Definicion.ipynb
```

---

## Fase 2 — Preprocesamiento y transformación

**Notebook:** `notebooks/f2_preprocesamiento/F2_Limpieza_Transformacion.ipynb`

Pipeline implementado (funciones modulares):

| Función | Descripción |
|---------|-------------|
| `cargar_datos(ruta, columnas)` | Carga `wdbc.data` desde `data/raw/` con columnas nombradas |
| `explorar_datos(df)` | Diagnóstico: dimensiones, tipos, NA, duplicados, estadísticas |
| `limpiar_datos(df)` | Elimina columna `id`, duplicados e imputa NA con mediana |
| `transformar_datos(df)` | Codifica diagnóstico (B→0, M→1) y estandariza con `StandardScaler` |
| `visualizar_transformaciones(df_orig, df_trans)` | Gráficos comparativos antes/después de la transformación |
| `validar_dataset(df)` | Assertions de integridad: sin NA, sin duplicados, media≈0, std≈1 |
| `exportar_dataset(df, ruta)` | Guarda el dataset procesado en `data/processed/` |

**Resultado:** `data/processed/wdbc_procesado.csv` — 569 filas × 31 columnas  
(excluido del repositorio vía `.gitignore`; se regenera ejecutando el notebook)

**Para ejecutar:**
```bash
jupyter notebook notebooks/f2_preprocesamiento/F2_Limpieza_Transformacion.ipynb
```

---

## Fase 3 — Algoritmos y análisis de complejidad

**Notebook:** `notebooks/f3_modelamiento/F3_Algoritmos_Complejidad.ipynb`

**Script:** `src/algoritmos.py`

Algoritmos implementados:

| Función | Descripción | Complejidad |
|----------|-------------|-------------|
| `busqueda_lineal_iterativa()` | Búsqueda secuencial sobre una lista | O(n) |
| `busqueda_binaria_recursiva()` | Búsqueda recursiva mediante Divide and Conquer | O(log n) |
| `filtro_estructurado_features()` | Identificación de variables altamente correlacionadas | O(n²) |

Validaciones realizadas:

- Caso normal
- Casos límite
- Entradas inválidas
- Ejecución completa mediante Restart & Run All

Benchmark:

- Medición de tiempos mediante `timeit`
- Comparación entre algoritmos iterativos y recursivos
- Análisis teórico y empírico de complejidad Big O

**Para ejecutar:**

```bash
jupyter notebook notebooks/f3_modelamiento/F3_Algoritmos_Complejidad.ipynb
```

> Ejecutar con **Restart & Run All** para reproducir correctamente todas las validaciones y mediciones de rendimiento.

---

## Dataset

- **Nombre:** Breast Cancer Wisconsin (Diagnostic)
- **Fuente:** UCI Machine Learning Repository
- **Instancias:** 569
- **Variables:** 32 (ID, diagnóstico, 30 características morfológicas)
- **Variable objetivo:** Diagnosis (B = benigno, M = maligno)

---

### Dataset procesado

Archivo generado:

```text
data/processed/wdbc_procesado.csv
```

Transformaciones aplicadas:

- Eliminación de columna ID
- Eliminación de duplicados
- Codificación de diagnóstico (B → 0, M → 1)
- Estandarización mediante StandardScaler

