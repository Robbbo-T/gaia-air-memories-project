# Ejemplos Básicos de Uso de GAIA AIR Memories

## Ejemplo 1: Optimización de ruta de vuelo

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

## Ejemplo 2: Mantenimiento predictivo

```python
from gaia_air_memories import analizar_sensores

datos_sensores = {...}  # Datos de sensores de la aeronave

predicciones = analizar_sensores(datos_sensores)
print(predicciones)
```
