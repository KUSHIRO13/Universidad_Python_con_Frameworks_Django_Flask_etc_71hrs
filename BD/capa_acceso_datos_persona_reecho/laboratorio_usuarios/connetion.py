from logger_base import log
from psycopg2 import pool
import sys

class Connetion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _PORT = "5432"
    _HOST = "127.0.0.1"
    _MAX_CONN = 5
    _MIN_CONN = 1
    _pool = None

    @classmethod
    def obtained_pool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN,cls._MAX_CONN,
                                                       user=cls._USERNAME,
                                                       password=cls._PASSWORD,
                                                       host=cls._HOST,
                                                       port=cls._PORT,
                                                       database=cls._DATABASE)
                # log.info(f"Se creo el pool {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error de tipo '{e}'")
                sys.exit()
        else:
            # log.warning(f"Ya se habia creado la conexion")
            return cls._pool

    @classmethod
    def obtained_connetion(cls):
        try:
            conexion = cls.obtained_pool().getconn()
            # log.info(f"Obteniendo la conexion {conexion}")
            return conexion
        except Exception as e:
            log.error(f"Ocurrio un error '{e}'")

    @classmethod
    def leave_connetion(cls, connetion):
        cls.obtained_pool().putconn(connetion)
        # log.info(f"Se cerro la conexion {connetion}")


    @classmethod
    def closed_connetion(cls):
        cls.obtained_pool().closeall()


if __name__ == "__main__":
    conexion1 = Connetion.obtained_connetion()
    conexion2 = Connetion.obtained_connetion()
    conexion3 = Connetion.obtained_connetion()
    conexion4 = Connetion.obtained_connetion()
    Connetion.leave_connetion(conexion1)
    conexion5 = Connetion.obtained_connetion()
    conexion6 = Connetion.obtained_connetion()