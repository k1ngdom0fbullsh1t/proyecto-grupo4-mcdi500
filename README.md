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
│   └─ f3_modelamiento/  # Fase 3: entrenamiento, evaluación e interpretación
├─ src/                  # Módulos y funciones reutilizables
├─ docs/                 # Documentación adicional del proyecto
├─ models/               # Modelos entrenados serializados
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
| F1 | Definición del problema y configuración del entorno | En progreso |
| F2 | Preprocesamiento, limpieza y análisis exploratorio | Pendiente |
| F3 | Modelamiento, evaluación e interpretación | Pendiente |

---

## Dataset

- **Nombre:** Breast Cancer Wisconsin (Diagnostic)
- **Fuente:** UCI Machine Learning Repository
- **Instancias:** 569
- **Variables:** 32 (ID, diagnóstico, 30 características morfológicas)
- **Variable objetivo:** Diagnosis (B = benigno, M = maligno)
