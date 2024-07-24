from flask import Flask
from controladores.ControladorCartas import ControladorCartas
from controladores.Controlador import Controlador
from controladores.ControladorFiguras import ControladorFiguras
from modelos.BBDD import BBDD

# Crear una instancia de la aplicación Flask
app = Flask(__name__, template_folder='vista')

if __name__ == "__main__":

    # Crea una instancia de BBDD
    # Lo dejo pero no hace falta psar una instancia, segun pone se puede llamar a la bbdd con las credenciales
    # ademas no devuelve conexion
    BBDD()

    # Llama a rutasCartas y pasa la instancia de la aplicación Flask y de BBDD
    ControladorCartas.rutasCartas(app)
    ControladorFiguras.rutasFiguras(app)
    Controlador.registrar_rutas(app)

    # Iniciar la aplicación Flask
    app.run(debug=True)
