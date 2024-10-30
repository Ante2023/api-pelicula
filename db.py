import pymysql
def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='user',
        password='pass',
        db='nameDB'
)