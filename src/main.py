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

### 4. `/api/v1/quantum_route`

- **Descripción**: Optimiza la ruta cuántica utilizando Quantum Approximate Optimization Algorithm (QAOA).
- **Método**: POST
- **URL**: `/api/v1/quantum_route`
- **Cuerpo de la solicitud**:
  ```json
  {
    "qubit": {...},
    "origen": {...},
    "destino": {...}
  }
  ```
- **Respuesta**:
  ```json
  {
    "ruta_cuantica": {...}
  }
  ```

- **Ejemplo de solicitud**:
  ```json
  {
    "qubit": "q1",
    "origen": "node1",
    "destino": "node2"
  }
  ```

- **Ejemplo de respuesta**:
  ```json
  {
    "ruta_cuantica": "optimized_route"
  }
  ```

### 4. `/api/v1/gaia_interface_robbbot`

- **Descripción**: Recibe datos de los sensores del motor cuántico y ajusta parámetros de entalpía/entropía en tiempo real.
- **Método**: POST
- **URL**: `/api/v1/gaia_interface_robbbot`
- **Cuerpo de la solicitud**:
  ```json
  {
    "datos_sensores": {...}
  }
  ```
- **Respuesta**:
  ```json
  {
    "ajustes": {
      "entalpia": 123.45,
      "entropia": 0.67,
      "configuracion": {
         "modo": "automático",
         "umbral": 42
      }
    }
  }
