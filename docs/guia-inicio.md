# Guía de Inicio de GAIA AIR Memories

## Requisitos previos

- Python 3.9+
- Qiskit 0.39.0+
- Dependencias adicionales en `requirements.txt`

## Configuración del entorno

### Clonar el repositorio

```bash
git clone https://github.com/Robbbo-T/gaia-air-memories-project.git
cd gaia-air-memories-project
```

### Configurar entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
python src/main.py
```

## Ejemplos básicos de uso

### Ejemplo 1: Optimización de ruta de vuelo

```python
from gaia_air_memories import optimizar_ruta

origen = (40.7128, -74.0060)  # Nueva York
destino = (34.0522, -118.2437)  # Los Ángeles
condiciones_climaticas = {...}  # Datos meteorológicos
consumo_combustible = {...}  # Modelo de consumo
restricciones = {...}  # Restricciones operativas

ruta_optimizada = optimizar_ruta(origen, destino, condiciones_climaticas, consumo_combustible, restricciones)
print(ruta_optimizada)
```

### Ejemplo 2: Mantenimiento predictivo

```python
from gaia_air_memories import analizar_sensores

datos_sensores = {...}  # Datos de sensores de la aeronave

predicciones = analizar_sensores(datos_sensores)
print(predicciones)
```

Para más ejemplos y detalles, consulte la [documentación completa](https://robbbo-t.github.io/gaia-air-memories-project/).
