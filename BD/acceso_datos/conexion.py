# Importaciones
import psycopg2

class Conexion:
    DATABASE = "test_db"
    USERNAME = "postgres"
    PASSWORD = "admin"
    DB_PORT = "5432"
    HOST = "127.0.0.1"

    def __init__(self):
        self.conexion = Conexion.obtenerConnexion()
        self.conexion.autocommit = False
        self.cursor = Conexion.obtenerCursor()
    @classmethod
    def obtenerConnexion(cls):
        return psycopg2.connect(
            user=cls.USERNAME,
            password=cls.PASSWORD,
            host=cls.HOST,
            port=cls.DB_PORT,
            database=cls.DATABASE
        )
    @classmethod
    def obtenerCursor(cls):
        with cls.obtenerConnexion() as cursor:
            return cursor

    @classmethod
    def cerrar(cls, conexion, cursor):
        try:
            conexion.commit()
            c_registro = cursor.rowcount
            return c_registro
        except Exception as e:
            conexion.rollback()
            return f"Ocurrio un error de tipo: '{e}'"
        finally:
            if conexion:
                conexion.close()
            if cursor:
                cursor.close()


if __name__ == "__main__":
    conexion = Conexion()
    sentencia = "SELECT * FROM persona"
    conexion.cursor.execute(sentencia)
    registro = conexion.cursor.fetchall()
    print(registro)

    sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)"
    valor = ("Andres", "Cortina", "acortina@gmail.com")
    conexion.cursor.execute(sentencia,valor)

    r_regis = conexion.cerrar(conexion.conexion,conexion.cursor)
    print(f"Registros afectados: {r_regis}")
