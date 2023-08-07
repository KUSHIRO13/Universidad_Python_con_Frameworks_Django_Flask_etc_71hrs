import psycopg2

conexion = psycopg2.connect(
    user="postgres1",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_db"
)

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM persona WHERE id_persona = %s"
            entrada = input("Proporciona los id a eliminar: ")
            valor = tuple(tuple(entrada.split(",")))
            cursor.executemany(sentencia,valor)
            conteo = cursor.rowcount
            print(f"Registros: {conteo}")
except Exception as e:
    print(f"Error tipo {e}")