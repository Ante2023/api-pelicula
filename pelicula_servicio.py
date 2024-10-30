from db import obtener_conexion

def crear_pelicula(titulo, anio):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pelicula(titulo, anio) VALUES (%s,%s)",(titulo,anio))
        conexion.commit()
        return cursor.lastrowid
    except Exception as e:
        conexion.rollback()
        raise Exception(f"Error al agregar la película: {str(e)}")
    finally:
        conexion.close()
        

def mostrar_peliculas():
    try: 
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM pelicula")
            peliculas_info = cursor.fetchall()
            columnas_info = [desc[0] for desc in cursor.description]#claves,[id,anio,titulo]
            resultado_json = [dict(zip(columnas_info, fila)) for fila in peliculas_info]#{'id': 1, 'anio': '2014'}
            return resultado_json
    except Exception as e:
        raise Exception(f"Error al obtener la película:{str(e)}")
    finally:
        conexion.close()

def mostrar_pelicula(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute( "SELECT * FROM pelicula WHERE id = %s", (id,))
            pelicula_info = cursor.fetchone()
            columnas_info = [desc[0] for desc in cursor.description]
            pelicula_json = dict(zip(columnas_info, pelicula_info))
            return pelicula_json
    except Exception as e:
        raise Exception(f"Error al obtener la película ID {id}:{str(e)}")
    finally:
        conexion.close()
    

def actualizar_pelicula(id,titulo,anio):
    try:
        conexion = obtener_conexion()
        query="UPDATE pelicula SET titulo = %s, anio =%s WHERE id = %s"
        with conexion.cursor() as cursor:
            cursor.execute( query,[titulo,anio,id])
            conexion.commit()
            if cursor.rowcount==0:
                return None
            return id
    except Exception as e:
        conexion.rollback()
        raise Exception(f"Error al actualizar la película: {str(e)}")
    finally:
        conexion.close()
        

def eliminar_pelicula(id):
    try:
        conexion = obtener_conexion()
        query="DELETE FROM pelicula WHERE id = %s"
        with conexion.cursor() as cursor:
            cursor.execute( query,[id])
            conexion.commit()
            return cursor.rowcount > 0  # Retorna True si se eliminó
    except Exception as e:
        conexion.rollback()
        raise Exception(f"Error al eliminar la película: {str(e)}")
    finally:
        conexion.close()
        
