import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="test_db"
)

print(conexion)

print("Bienvenido a esta prueba de registro de sesion V2")
nombre = input("Favor de ingresar tu nombre: ")
apellido = input("Favor de ingresar tu apellido: ")
correo = input("Favor de ingresar tu correo: ")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)"
            cursor.execute(sentencia,(nombre,apellido,correo))
            registros = cursor.rowcount
            print(f"Numeros de registros {registros}")
except Exception as e:
    print(f"Error tipo: {e}")
finally:
    conexion.close()