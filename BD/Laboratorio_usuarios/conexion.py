from logger_base import log
from psycopg2 import pool
import sys


class Connetion:
    _DATABASE = "test_db"
    _PORT = "5432"
    _HOST = "127.0.0.1"
    _USER = "postgres"
    _PASSWORD = "admin"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None


    @classmethod
    def obtainedPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      user=cls._USER,
                                                      password=cls._PASSWORD,
                                                      host=cls._HOST,
                                                      port=cls._PORT,
                                                      database=cls._DATABASE)
                log.info(f"Creacion del pool exitosa '{cls._pool}'")
                return cls._pool
            except Exception as e:
                print(f"Hubo un problema al obtener el pool {e}")
                sys.exit()
        else:
            if cls._pool.closed == True:
                cls._pool.closed = False
            return cls._pool

    @classmethod
    def obtainedConnetion(cls):
        try:
            conexion = cls.obtainedPool().getconn()
            log.info(f"Se consiguio la conexion '{conexion}'")
            return conexion
        except Exception as e:
            log.error(f"Ocurrio un error al obtener la conexion {e}")
            sys.exit()

    @classmethod
    def releaseConnetion(cls, conexion):
        cls.obtainedPool().putconn(conexion)
        log.warning(f"Se a cerrado la conexion {conexion}")

    @classmethod
    def closeConnetion(cls):
        cls.obtainedPool().closeall()
        log.warning(f"Se cerraron todas las conexiones")


# Check Connetions
# Comprobacion de las conexiones

if __name__ == "__main__":
    conexion1 = Connetion.obtainedConnetion()
    conexion2 = Connetion.obtainedConnetion()
    conexion3 = Connetion.obtainedConnetion()
    conexion4 = Connetion.obtainedConnetion()
    conexion5 = Connetion.obtainedConnetion()
    Connetion.releaseConnetion(conexion1)
    conexion6 = Connetion.obtainedConnetion()
    Connetion.closeConnetion()
    conexion7 = Connetion.obtainedConnetion()
