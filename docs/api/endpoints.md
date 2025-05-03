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
    },
    "consumo_combustible": {
      "tipo_aeronave": "Boeing 737",
      "peso_base": 41000,
      "carga": 10000,
      "combustible_inicial": 20000,
      "consumo_crucero": 2500,
      "consumo_ascenso": 3000,
      "consumo_descenso": 2000,
      "altitud_optima": 35000,
      "velocidad_optima": 450
    },
    "restricciones": {
      "zonas_prohibidas": [
        {"coord": [41.0, -75.0], "radio": 10}
      ],
      "altitud_minima": 10000,
      "altitud_maxima": 40000,
      "tiempo_maximo": 180,
      "reserva_combustible": 5000,
      "prioridad_optimizacion": "combustible"
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
    "datos_sensores": {
      "sensor_1": {"valor": 0.85, "umbral": 0.9},
      "sensor_2": {"valor": 0.75, "umbral": 0.8}
    }
  }
  ```
- **Respuesta**:
  ```json
  {
    "predicciones": [
      {"sensor": "S1", "fallo": "F1", "probabilidad": 0.85},
      {"sensor": "S2", "fallo": "F2", "probabilidad": 0.75}
    ]
  }
  ```

### 3. `/api/v1/gestionar_carga`

- **Descripción**: Optimiza la distribución de carga para maximizar eficiencia y seguridad.
- **Método**: POST
- **URL**: `/api/v1/gestionar_carga`
- **Cuerpo de la solicitud**:
  ```json
  {
    "datos_carga": {
      "seccion_1": {"peso": 1000, "centro_gravedad": 0.5},
      "seccion_2": {"peso": 1500, "centro_gravedad": 0.6}
    }
  }
  ```
- **Respuesta**:
  ```json
  {
    "distribucion_optimizada": {
      "seccion_1": {"peso": 1000, "centro_gravedad": 0.5},
      "seccion_2": {"peso": 1500, "centro_gravedad": 0.6}
    }
  }
  ```
