from logger_base import log
from psycopg2 import pool
import sys


class Connetion:
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _HOST = "127.0.0.1"
    _PORT = "5432"
    _DATABASE = "test_db"
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    @classmethod
    def obtained_pool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      host=cls._HOST,
                                                      port=cls._PORT,
                                                      database=cls._DATABASE)
                log.info(f"Se crea el pool '{cls._pool}'")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error del tipo {e}")
                sys.exit()
        else:
            log.warning("El pool ya existia, se devuelve")
            return cls._pool

    @classmethod
    def obtained_connetion(cls):
        connetion = cls.obtained_pool().getconn()
        log.debug(f"Conexion obtenida del pool {connetion}")
        return connetion

    @classmethod
    def leave_connetion(cls, connetion):
        cls.obtained_pool().putconn(connetion)
        log.warning(f"Se regresa la conexion {connetion}")

    @classmethod
    def closed_connetion(cls):
        cls.obtained_pool().closeall()


if __name__ == "__main__":
    connetion1 = Connetion.obtained_connetion()
    connetion2 = Connetion.obtained_connetion()
    connetion3 = Connetion.obtained_connetion()
    connetion4 = Connetion.obtained_connetion()
    connetion5 = Connetion.obtained_connetion()
    Connetion.leave_connetion(connetion3)
    connetion6 = Connetion.obtained_connetion()
