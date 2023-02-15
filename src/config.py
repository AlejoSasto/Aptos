from psycopg2 import connect

HOST = 'ec2-3-214-2-141.compute-1.amazonaws.com'
PORT = '5432'
BD = 'd2iu7iktus3s4q'
USUARIO = 'qtjjqqphghckhr'
PASSWORD = '1490eb493a8c2f85ee5292da1f044b44699f025cbccf63763062197f47df702b'

def EstablecerConexion():
    try:
        conexion = connect(host = HOST, port = PORT, dbname = BD, user = USUARIO, password = PASSWORD)
    except ConnectionError:
        print("Error de Conexion")
    return conexion
