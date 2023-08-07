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
            sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
            valores = (
                ("Carlos", "Lara", "clara@gmail.com"),
                ("Estiven", "Cortina", "ecortina@gmail.com"),
                ("Angel", "Quintana", "aquintana@gmail.com")
            )
            cursor.executemany(sentencia,valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Error tipo {e}")
finally:
    conexion.close()