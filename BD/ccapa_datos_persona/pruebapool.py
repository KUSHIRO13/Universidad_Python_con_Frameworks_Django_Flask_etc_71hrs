import sys

from psycopg2 import pool
from prueba1 import log


# TODO: Empezar a usar el lenguaje ingles para programar y por el momento en comentar solo en español
class Connection:
    _USERNAME = "postgres"
    _HOST = "localhost"
    _PASSWORD = "admin"
    _PORT = "5432"
    _DATABASE = "test_db"
    _MIN_CONNECT = 1
    _MAX_CONNECT = 5
    _pool = None

    @classmethod
    def obtainedPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONNECT, cls._MAX_CONNECT,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      host=cls._HOST,
                                                      port=cls._PORT,
                                                      database=cls._DATABASE)

                log.info(f"Creacion del pool fue exitosa {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error tipo '{e}'")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtainedConnection(cls):
        try:
            conexion = cls.obtainedPool().getconn()
            log.debug(f"Conexion Exitosa {conexion}")
            return conexion
        except Exception as e:
            log.error(f"Ocurrio un error de tipo '{e}'")

    @classmethod
    def releasePool(cls, conexion):
        cls.obtainedPool().putconn(conexion)
        log.info(f"Se a cerrado la conexion {conexion}")

    @classmethod
    def closePool(cls):
        cls.obtainedPool().closeall()

if __name__ == "__main__":
    conexion1 = Connection.obtainedConnection()
    Connection.releasePool(conexion1)
    conexion2 = Connection.obtainedConnection()
    conexion3 = Connection.obtainedConnection()
    conexion4 = Connection.obtainedConnection()
    Connection.releasePool(conexion3)
    conexion5 = Connection.obtainedConnection()
