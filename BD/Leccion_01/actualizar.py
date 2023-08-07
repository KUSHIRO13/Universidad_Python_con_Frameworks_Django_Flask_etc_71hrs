import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="test_db"
)

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valores = (
                ("Juan Carlos", "perez", "jperez@gmail.com", 5),
                ("Kevin", "Carlos", "kcarlos@gmail.com", 12)
            )
            cursor.executemany(sentencia, valores)
            # Contar los registros
            c_registros = cursor.rowcount
            print(f"N° registros: {c_registros}")
except Exception as e:
    print(f"Error tipo '{e}'")
finally:
    conexion.close()