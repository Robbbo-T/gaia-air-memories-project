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
condiciones_climaticas = {
    "vientos": [
        {"coord": [41.0, -75.0], "direccion": 90, "velocidad": 30},
        {"coord": [42.0, -76.0], "direccion": 180, "velocidad": 20}
    ],
    "turbulencia": [
        {"coord": [41.5, -75.5], "intensidad": 5}
    ],
    "tormentas": [
        {"coord": [42.5, -76.5], "radio": 50, "intensidad": 8}
    ],
    "temperatura": [
        {"coord": [41.0, -75.0], "valor": 15}
    ]
}
consumo_combustible = {
    "tipo_aeronave": "Boeing 737",
    "peso_base": 41000,
    "carga": 10000,
    "combustible_inicial": 20000,
    "consumo_crucero": 2500,
    "consumo_ascenso": 3000,
    "consumo_descenso": 2000,
    "altitud_optima": 35000,
    "velocidad_optima": 450
}
restricciones = {
    "zonas_prohibidas": [
        {"coord": [41.0, -75.0], "radio": 10}
    ],
    "altitud_minima": 10000,
    "altitud_maxima": 40000,
    "tiempo_maximo": 180,
    "reserva_combustible": 5000,
    "prioridad_optimizacion": "combustible"
}

ruta_optimizada = optimizar_ruta(origen, destino, condiciones_climaticas, consumo_combustible, restricciones)
print(ruta_optimizada)
```

### Ejemplo 2: Mantenimiento predictivo

```python
from gaia_air_memories import analizar_sensores

datos_sensores = {
    "sensor_1": {"valor": 0.85, "umbral": 0.9},
    "sensor_2": {"valor": 0.75, "umbral": 0.8}
}

predicciones = analizar_sensores(datos_sensores)
print(predicciones)
```

### Ejemplo 3: Gestión de carga

```python
from gaia_air_memories import gestionar_carga

datos_carga = {
    "seccion_1": {"peso": 1000, "centro_gravedad": 0.5},
    "seccion_2": {"peso": 1500, "centro_gravedad": 0.6}
}

distribucion_optimizada = gestionar_carga(datos_carga)
print(distribucion_optimizada)
```

Para más ejemplos y detalles, consulte la [documentación completa](https://robbbo-t.github.io/gaia-air-memories-project/).
