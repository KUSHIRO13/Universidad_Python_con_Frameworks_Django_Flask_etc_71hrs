from conexion import Conexion
from logger_base import log
class Cursor:
    def __init__(self,):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del metodo with __enter__ ")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tiop_execepcion, valor_execepcion, datalle_execepcion):
        log.debug("Se ejecuta metodo __exit__")
        if valor_execepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio un error {valor_execepcion} {tiop_execepcion} {datalle_execepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transacion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
    with Cursor() as cursor:
        log.info("Dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())