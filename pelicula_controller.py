
from flask import Blueprint, jsonify, request
from flask_cors import CORS
import pelicula_servicio

route_pelicula = Blueprint('route_pelicula', __name__)



@route_pelicula.route("/api/v1/peliculas", methods=["GET"])
def get_peliculas():
    try:
        data = pelicula_servicio.mostrar_peliculas()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error":str(e)}),500

@route_pelicula.route("/api/v1/peliculas/<int:id>", methods=["GET"])
def get_pelicula(id):
    try:
        pelicula=pelicula_servicio.mostrar_pelicula(id)
        if pelicula:
            return jsonify(pelicula)
        return jsonify({"error":"Pelicula no encontrada"}),404
    except Exception as e:
        return jsonify({"error":str(e)}),500
        

@route_pelicula.route("/api/v1/peliculas", methods=["POST"])
def crear_pelicula():
    data = request.json
    try:

        pelicula_id=pelicula_servicio.crear_pelicula(data["titulo"],data["anio"])
        return jsonify({"id":pelicula_id}),201

    except Exception as e:
        return jsonify({"error":str(e)}),500

@route_pelicula.route("/api/v1/peliculas/<int:id>", methods=["PUT"])
def actualizar_pelicula(id):
    data = request.json
   
    try:

        pelicula=pelicula_servicio.actualizar_pelicula(id,data["titulo"],data["anio"])
        if pelicula:
            return jsonify({"id":pelicula})
        return jsonify({"error":"Pelicula no encontrada"}),400
    except Exception as e:
        return jsonify({"error":str(e)}),500
    
@route_pelicula.route("/api/v1/peliculas/<int:id>", methods=["DELETE"])
def eliminar_pelicula(id):   
    try:
        if pelicula_servicio.eliminar_pelicula(id):
            return jsonify({"mensaje":"Pelicula eliminada"}),200 #204 no pinta mensaje
        return jsonify({'error': 'Pelicula no encontrada'}), 404
    except Exception as e:
        return jsonify({"error":str(e)}),500