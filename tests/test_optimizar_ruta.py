import unittest
from src.optimizar_ruta import optimizar_ruta

class TestOptimizarRuta(unittest.TestCase):

    def setUp(self):
        self.origen = (40.7128, -74.0060)  # Nueva York
        self.destino = (34.0522, -118.2437)  # Los Ángeles
        self.condiciones_climaticas = {"viento": "moderado", "precipitaciones": "bajas"}
        self.consumo_combustible = {"modelo": "A320", "consumo_por_km": 2.5}
        self.restricciones = {"altitud_maxima": 35000, "zonas_restringidas": ["Z1", "Z2"]}

    def test_ruta_optimizada(self):
        ruta_optimizada = optimizar_ruta(
            self.origen,
            self.destino,
            self.condiciones_climaticas,
            self.consumo_combustible,
            self.restricciones
        )
        self.assertIsInstance(ruta_optimizada, list)
        self.assertGreater(len(ruta_optimizada), 0)
        for waypoint in ruta_optimizada:
            self.assertIn("waypoint", waypoint)
            self.assertIn("lat", waypoint)
            self.assertIn("lon", waypoint)

    def test_ruta_sin_restricciones(self):
        restricciones = {}
        ruta_optimizada = optimizar_ruta(
            self.origen,
            self.destino,
            self.condiciones_climaticas,
            self.consumo_combustible,
            restricciones
        )
        self.assertIsInstance(ruta_optimizada, list)
        self.assertGreater(len(ruta_optimizada), 0)

    def test_ruta_condiciones_extremas(self):
        condiciones_climaticas = {"viento": "fuerte", "precipitaciones": "altas"}
        ruta_optimizada = optimizar_ruta(
            self.origen,
            self.destino,
            condiciones_climaticas,
            self.consumo_combustible,
            self.restricciones
        )
        self.assertIsInstance(ruta_optimizada, list)
        self.assertGreater(len(ruta_optimizada), 0)

if __name__ == '__main__':
    unittest.main()
