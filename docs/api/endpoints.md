# API Reference

## Endpoints

### 1. `/api/v1/optimizar_ruta`

- **Descripción**: Optimiza la ruta de vuelo utilizando AMEDEO QAO.
- **Método**: POST
- **URL**: `/api/v1/optimizar_ruta`
- **Cuerpo de la solicitud**:
  ```json
  {
    "origen": [40.7128, -74.0060],
    "destino": [34.0522, -118.2437],
    "condiciones_climaticas": {
      "viento": "moderado",
      "precipitaciones": "bajas"
    },
    "consumo_combustible": {
      "modelo": "A320",
      "consumo_por_km": 2.5
    },
    "restricciones": {
      "altitud_maxima": 35000,
      "zonas_restringidas": ["Z1", "Z2"]
    }
  }
  ```
- **Respuesta**:
  ```json
  {
    "ruta_optimizada": [
      {"waypoint": "WP1", "lat": 40.7128, "lon": -74.0060},
      {"waypoint": "WP2", "lat": 41.0, "lon": -75.0},
      {"waypoint": "WP3", "lat": 42.0, "lon": -76.0},
      {"waypoint": "WP4", "lat": 34.0522, "lon": -118.2437}
    ]
  }
  ```

### 2. `/api/v1/analizar_sensores`

- **Descripción**: Analiza patrones en datos de sensores para predecir fallos.
- **Método**: POST
- **URL**: `/api/v1/analizar_sensores`
- **Cuerpo de la solicitud**:
  ```json
  {
    "datos_sensores": {...}
  }
  ```
- **Respuesta**:
  ```json
  {
    "predicciones": [...]
  }
  ```

### 3. `/api/v1/gestionar_carga`

- **Descripción**: Optimiza la distribución de carga para maximizar eficiencia y seguridad.
- **Método**: POST
- **URL**: `/api/v1/gestionar_carga`
- **Cuerpo de la solicitud**:
  ```json
  {
    "datos_carga": {...}
  }
  ```
- **Respuesta**:
  ```json
  {
    "distribucion_optimizada": {...}
  }
  ```
