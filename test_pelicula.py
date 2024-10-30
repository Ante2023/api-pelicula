import unittest
from flask import Flask
from pelicula_controller import route_pelicula
from db import obtener_conexion

class TestPeliculaAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(route_pelicula)
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        
    def test_get_peliculas(self):
        response = self.client.get('/api/v1/peliculas')
        self.assertEqual(response.status_code, 200)
        
    def test_get_pelicula(self):
        response = self.client.get('/api/v1/peliculas/2')  # Asegurarse que película id=1 exista
        self.assertEqual(response.status_code, 200)
 
    def test_crear_pelicula(self):
            new_pelicula = {
                "titulo": "Nueva Película",
                "anio": 2024
            }
            response = self.client.post('/api/v1/peliculas', json=new_pelicula)
            self.assertEqual(response.status_code, 201)
    def test_actualizar_pelicula(self):
            updated_pelicula = {
                "titulo": "Pelícudda Actualizada", #Cambiar en cada test
                "anio": 2025
            }
            response = self.client.put('/api/v1/peliculas/2', json=updated_pelicula)  # Asegúrarse de que la película 2 existe
            self.assertEqual(response.status_code, 200)

    def test_eliminar_pelicula(self):
        response = self.client.delete('/api/v1/peliculas/20')  # Asegúrarse de que la película 1 existe
        self.assertEqual(response.status_code, 200)
        
    def test_db_connection(self):
        try:
            connection = obtener_conexion()
            self.assertTrue(connection.open)
        except Exception as e:
            self.fail(f"Error de conexión a la base de datos: {e}")
        finally:
            if connection.open:
                connection.close()
                                
if __name__ == '__main__':
    unittest.main()