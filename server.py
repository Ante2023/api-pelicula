from flask import  Flask
from pelicula_controller import route_pelicula

app = Flask(__name__)
app.register_blueprint(route_pelicula)

if __name__== "__main__":
    app.run(debug=True)