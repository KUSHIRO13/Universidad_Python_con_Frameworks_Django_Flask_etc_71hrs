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
            sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
            # llaves_primarias = ((1,2,3),)
            entrada = input("Proporciona los id a buscar: ")
            llaves_primarias = (tuple(entrada.split(",")),)
            # id_persona = input("Proporciona el valor primario: ")
            print(sentencia)
            print(llaves_primarias)
            cursor.execute(sentencia, llaves_primarias)
            registro = cursor.fetchall()
            for r in registro:
                print(r)
except Exception as e:
    print(f"Error tipo: {e}")
finally:
    conexion.close()
