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
    "condiciones_climaticas": {...},
    "consumo_combustible": {...},
    "restricciones": {...}
  }
  ```
- **Respuesta**:
  ```json
  {
    "ruta_optimizada": [...]
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
