import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_db"
)

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)"
            valor = ("Alex", "Rojas", "arojas@gmail.com")
            cursor.execute(sentencia,valor)

            sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valor = ("Juan", "Perez", "jperez@gmail.com", 5)
            cursor.execute(sentencia,valor)
except Exception as e:
    print(f"Error tipo {e}")
finally:
    conexion.close()
    print("Se termino la conexion")
