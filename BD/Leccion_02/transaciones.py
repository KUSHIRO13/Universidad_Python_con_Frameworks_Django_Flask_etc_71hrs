import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="test_db"
)

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)"
    valor = ("Carlos", "Gomez", "cgomez@gmail.com")
    cursor.execute(sentencia,valor)

    sentencia = "UPDATE persona set nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    valor = ("Juan", "Juares", "jcjuares@gmai.com", 5)
    cursor.execute(sentencia,valor)

    conexion.commit()
    print("Termina la transacion")
except Exception as e:
    conexion.rollback()
    print(f"Error tipo '{e}' ")
finally:
    cursor.close()
    conexion.close()