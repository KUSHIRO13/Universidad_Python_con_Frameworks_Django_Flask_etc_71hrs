import psycopg2

# TODO: Averiguar donde saco todos estos datos
conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="test_db")

print(conexion) # Se verifica si se logro la conexion

try:
    with conexion:
        with conexion.cursor() as cursor: # Se crea un cursor que parece que es el que ejecuta las sentencias
            sentencia = "SELECT * FROM persona ORDER BY id_persona;" # Sentencia en codigo SQL
            cursor.execute(sentencia) # El cursor utiliza la sentencia proporcionadad
            registros = cursor.fetchall() # Se obtiene todos los datos en registro
            print(registros)
except Exception as e:
    print(f"Tipo: {e}")
finally:
    conexion.close()